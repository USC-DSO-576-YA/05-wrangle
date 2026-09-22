"""Provided setup for the songs workshop; HTTP mechanics are not exam material.

No credentials required. Only song/artist search terms or public record IDs go
to LRCLIB. Lyrics are kept in memory, never written into this repository.
API documentation: https://lrclib.net/docs
"""
import json
from pathlib import Path
from functools import lru_cache

import pandas as pd
import requests

BASE_URL = "https://lrclib.net/api"
COLUMNS = ["song_id", "song", "artist", "album", "duration_seconds",
           "lyrics", "status", "source", "lrclib_id", "detail"]


@lru_cache(maxsize=64)
def _request(endpoint, parameters=()):
    # Cache successful responses during this Python session only.
    response = requests.get(
        BASE_URL + endpoint, params=dict(parameters), timeout=15,
        headers={"User-Agent": "DSO576-Songs-Workshop/1.0"},
    )
    response.raise_for_status()
    return response.json()


def _same(left, right):
    return isinstance(left, str) and left.strip().casefold() == right.strip().casefold()


def search_songs(song, artist=None):
    """Show candidates without printing lyrics. Does not pick a match for you.

    Network/HTTP errors are raised here so they cannot look like an empty search.
    Use fetch_songs for a status-preserving classroom table.
    """
    params = {"track_name": song}
    if artist:
        params["artist_name"] = artist
    results = _request("/search", tuple(params.items()))
    if not isinstance(results, list) or any(not isinstance(r, dict) for r in results):
        raise ValueError("Unexpected API search response")
    columns = ["lrclib_id", "song", "artist", "album", "duration_seconds",
               "has_lyrics", "instrumental"]
    return pd.DataFrame([
        {"lrclib_id": r.get("id"), "song": r.get("trackName"),
         "artist": r.get("artistName"), "album": r.get("albumName"),
         "duration_seconds": r.get("duration"),
         "has_lyrics": bool((r.get("plainLyrics") or "").strip()),
         "instrumental": r.get("instrumental", False)}
        for r in results
    ], columns=columns)


def _song_record(song, artist, record_id=None):
    row = dict(song=song, artist=artist, album=None, duration_seconds=None,
               lyrics=None, status="not_found", source="lrclib",
               lrclib_id=record_id, detail="")
    try:
        if record_id is not None:
            record = _request(f"/get/{int(record_id)}")
            if not isinstance(record, dict):
                raise ValueError("Unexpected API record response")
            if not _same(record.get("trackName"), song) or (artist and not _same(record.get("artistName"), artist)):
                row.update(status="match_mismatch", detail="Record title or artist does not match the requested song. Inspect the candidate metadata.")
                return row
        else:
            params = {"track_name": song}
            if artist:
                params["artist_name"] = artist
            candidates = _request("/search", tuple(params.items()))
            if not isinstance(candidates, list) or any(not isinstance(r, dict) for r in candidates):
                raise ValueError("Unexpected API search response")
            matches = [r for r in candidates if _same(r.get("trackName"), song)
                       and (not artist or _same(r.get("artistName"), artist))]
            if not matches:
                row["detail"] = "No exact title/artist match in the returned search candidates. This is not proof that the song is absent from the catalog."
                return row
            if len(matches) > 1:
                row.update(status="ambiguous", detail="Multiple exact matches. Use search_songs to inspect album/duration, then supply a record_id.")
                return row
            record = matches[0]
        lyrics = record.get("plainLyrics")
        if lyrics is not None and not isinstance(lyrics, str):
            raise ValueError("Unexpected lyrics format")
        if not lyrics or not lyrics.strip():
            lyrics = None
        row.update(song=record.get("trackName"), artist=record.get("artistName"),
                   album=record.get("albumName"), duration_seconds=record.get("duration"),
                   lyrics=lyrics, lrclib_id=record.get("id"))
        if record.get("instrumental"):
            row.update(status="instrumental", lyrics=None)
        else:
            row["status"] = "ok" if lyrics is not None else "no_lyrics"
    except requests.HTTPError as error:
        code = error.response.status_code if error.response is not None else None
        row.update(status="not_found" if code == 404 else "request_failed",
                   detail=f"HTTP {code}; no lyrics were substituted.")
    except (requests.RequestException, ValueError, TypeError) as error:
        row.update(status="request_failed", detail=f"{type(error).__name__}: {error}")
    return row


def get_lyrics(song, artist=None, record_id=None):
    """Return plain lyrics or None for unavailable lyrics; flag other problems.

    The notebook uses fetch_songs instead so it can retain status and metadata.
    Search results are never silently resolved to the first candidate.
    """
    row = _song_record(song, artist, record_id)
    if row["status"] in {"request_failed", "ambiguous", "match_mismatch"}:
        raise RuntimeError(row["status"] + ": " + row["detail"])
    return row["lyrics"]


def fetch_songs(playlist):
    """One row per playlist entry, including failed/unavailable requests.

    Each entry needs song_id, song, artist, and optionally record_id.
    Calls are sequential and timeout after 15 seconds each; do not request a
    whole catalog in class. No data-cleaning or assessed analysis is done here.
    """
    ids = [item["song_id"] for item in playlist]
    if len(set(ids)) != len(ids):
        raise ValueError("Each playlist entry needs a unique song_id")
    rows = []
    for item in playlist:
        row = _song_record(item["song"], item["artist"], item.get("record_id"))
        rows.append({"song_id": item["song_id"], **row})
    return pd.DataFrame(rows, columns=COLUMNS)


def load_demo_songs():
    """Load clearly fictional, original classroom text; never an API fallback."""
    path = Path(__file__).resolve().parent / "data" / "songs_demo.json"
    records = json.loads(path.read_text(encoding="utf-8"))
    return pd.DataFrame(records, columns=COLUMNS)


def load_homework_playlist():
    """Fixed homework metadata only; no lyrics or exercise answers are bundled."""
    path = Path(__file__).resolve().parent / "data" / "homework_playlist.json"
    return pd.DataFrame(json.loads(path.read_text(encoding="utf-8"))["songs"])


def load_homework_songs():
    """Fetch the pinned real-artist playlist; stop on retrieval problems.

    Requires internet. Lyrics stay in memory. Never substitutes fictional
    records, chooses a different recording, or computes word counts.
    """
    playlist = load_homework_playlist()
    songs = fetch_songs(playlist.to_dict("records"))
    problems = []
    for expected, actual in zip(playlist.to_dict("records"), songs.to_dict("records")):
        if actual["status"] != "ok":
            problems.append(f'{actual["song_id"]}: {actual["status"]}')
        elif not _same(actual["album"], expected["album"]):
            problems.append(f'{actual["song_id"]}: album metadata changed')
        elif (pd.isna(actual["duration_seconds"]) or
              abs(float(actual["duration_seconds"]) - expected["duration_seconds"]) > 1):
            problems.append(f'{actual["song_id"]}: duration metadata changed')
    if problems:
        raise RuntimeError(
            "Homework data is not ready: " + "; ".join(problems) + ". "
            "Check your internet connection, restart the kernel and retry. "
            "If it still fails, contact your instructor with this message. "
            "Do not substitute songs or use fictional class data for Part B."
        )
    return songs
