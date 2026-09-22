# Module 5 data

## Songs workshop

`songs_demo.json` contains twelve **fictional** song records, four per artist,
with short original
classroom verses (not full commercial lyrics). Names include intentional spaces
and capitalization differences. Two rows have missing text: one unavailable
and one instrumental. These are different from zero-word songs. `song_id` is the
unique playlist-entry identifier; `source` explicitly marks demo data. Durations
are invented demo metadata, not measurements of those verses.

The homework loader requests public records from https://lrclib.net/docs
using the supplied `lyrics_api.py`. Its lower-level `fetch_songs` function keeps
one row per requested entry, including status/detail for failed requests. The
homework loader stops on retrieval problems instead of returning incomplete
homework data. Live results can change; an exact title/artist match is not verification of
album, recording, duration, or text accuracy. The notebook's added-on dates and
playlist groups are instructor-created, not release dates or API metadata.
No commercial lyrics are bundled in this repository.

Part A uses the offline dataset. Part B instead uses `homework_playlist.json`,
which pins nine records: three each by Taylor Swift, Olivia Dean, and BTS.
It contains only metadata, not lyrics or word-count answers. BTS songs are
English-language selections. Internet is required; the homework loader checks
album and duration as well as title and artist, and stops on failed retrievals.
Do not substitute fictional records. The source is user-contributed and can
change. Describe this small selected sample, not an artist's entire catalog.

Loading, cleaning, dates, and merging are supplied in the notebook. Students
write the word-count function, groupby summary, and two plots. Artist summaries
must distinguish total songs from available texts. Missing counts are not zero.

## Practice files

| File | Grain | Purpose |
|---|---|---|
| `orders_january.csv` | One row per January order | Merge and aggregation examples. |
| `orders_february.csv` | One row per February order | Concatenate compatible rows. |
| `product_catalog.csv` | One row per product | Add a category without changing order grain. |
| `returns_log.csv` | One row per returned order | Preserve all purchases with a left merge. |
| `retail_orders_messy.csv` | One row per order | Clean text, amounts, dates, missing values, and notes. |

## Messy export grain

Each row represents one retail order. `order_id` is the row identifier.

## Messy export columns

| Column | Meaning |
|---|---|
| `order_id` | Order identifier. |
| `channel` | Sales channel as exported by the source system. |
| `amount` | Recorded order revenue before cleaning. |
| `order_date` | Order date before conversion to a pandas datetime. |
| `sku` | Structured product code. |
| `region` | Sales region. |
| `returned` | Return flag as exported. |
| `return_note` | Optional free-text note from the returns process. |

## Intentional data-quality issues

The file includes inconsistent capitalization and whitespace, formatted dollar
amounts, placeholders for unknown values, mixed date formats, and free-text
notes with imperfect order identifiers. These are deliberate practice cases,
not mistakes to repair in the source CSV.

Do not replace missing revenue with zero without a business justification.
Do not use a bare `dropna()` when only particular fields are required; name
those fields with `subset=[...]` and report how many rows remain.
Keep identifiers such as `sku` and `order_id` as text.
