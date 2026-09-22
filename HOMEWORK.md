# Module 5 Homework
## Analyze the songs we cleaned in class

Use the songs table prepared in class to compare artists with `groupby` and
`.agg`, create two plots, and explain your findings. Submit your individual
`module05_songs.ipynb` on Gradescope.

### Open your notebook

Open `module05_songs.ipynb` in your YA `05-wrangle` folder. Run `uv sync` to
install pandas, Matplotlib, requests, and ipykernel, then select its `.venv`
Python as the notebook kernel. Keep the notebook beside `lyrics_api.py` and
the `data` folder. Complete Part A in class and Part B at home.

Use the twelve fictional songs with original classroom verses and invented
durations. Keep `USE_LIVE_API = False`. The optional live API demonstration
is separate; its supplied helper is not exam material.

### What we prepare in class

Keep `raw` unchanged. Clean artist names into `artist_clean`. Early in class,
convert `playlist_info["added_on"]` with `pd.to_datetime` and `format="mixed"`.
Dates include `2026-09-03` and `Sep 3, 2026`; these mean the same day.
They are playlist dates, not release dates. Check the data type and missing values.

Create `word_count` with a scalar function and `map`. Test the function with
separate calls; no loop is required. Count whitespace-separated tokens, with
punctuation attached. Missing or whitespace-only lyrics get a missing count,
not zero. Keep the original `lyrics` column.

Merge the prepared tables by `song_id` into `enriched`, keeping every song
and the converted dates.

### Using Codex

Predict first, then ask for hints or feedback on one step at a time. Write
your own analysis code and explanations; do not ask for a completed notebook.

### 1 Check your starting table

Continue with `enriched`, the table you cleaned in class. Display song ID,
song, `artist_clean`, `duration_seconds`, `word_count`, `status`, and
`playlist_group`. Confirm one row per song ID and the same row count as `raw`.
Report how many word counts are missing. Keep those songs in the starting table;
missing word counts are not zero.

### 2 Summarize by artist

Use `groupby` and `.agg` to create `artist_summary`, with one row per
`artist_clean` and these four columns:

- `total_songs`: number of songs, including songs without lyrics.
- `songs_with_text`: number of non-missing `word_count` values.
- `mean_words`: mean of the available word counts.
- `mean_duration_seconds`: mean duration of all songs with known duration.

Display the summary sorted from highest to lowest `mean_words`. Explain why
`total_songs` and `songs_with_text` can differ and which count is the denominator
for `mean_words`. Do not fill missing word counts before computing the mean.

### 3 Plot the artist comparison

Create a bar chart from `artist_summary` showing `mean_words` for each
artist, ordered from highest to lowest. Label the artist axis and the mean word
count axis, and give the chart an informative title. Show `songs_with_text`
beside the chart in a small displayed table or in the chart labels.

Below it, identify the artist with the largest mean in this dataset. Cite the
mean and the number of available texts supporting it. Demo texts are short
classroom verses, not full-song lyrics.

### 4 Plot individual songs

Create a scatter plot from the song-level `enriched` table, not the
artist summary. Put `duration_seconds` on the horizontal axis and `word_count`
on the vertical axis. Use only rows where both values are known; report the
number of included and excluded songs. Label both axes and title the plot.

Describe whether longer durations consistently go with larger word counts in
these records. Cite two songs that support or complicate your observation.
Do not claim a causal relationship. Demo durations are invented metadata and
the texts are short verses, so this plot cannot establish a real music trend.

### 5 Explain and check your findings

Choose one artist. Display its song-level word counts and independently
check its mean using only the available values. Show the numerator and
denominator, then compare with your summary.

Write three to five sentences answering: What did the two plots help you see?
How could missing lyrics affect the comparison? Why does this small playlist
not represent an artist's entire catalog?

End with an assistance note: whether you used Codex, one hint you received,
and how you checked your work. If you did not use it, say so.

### Finish and submit

Submit one file, `module05_songs.ipynb`, to the **Module 5 homework
assignment on Gradescope**. Include your in-class cleaning cells, homework
code, displayed summary, both plots, explanations, and assistance note.
Restart the kernel, run all cells in order, and save with outputs visible.
Keep `USE_LIVE_API = False` for the required assignment so it can run without
network access. Remove any optional outputs containing downloaded commercial
lyrics before submitting. No separate CSV, image, or PDF upload is required.
Use the posted course calendar for the deadline. Do not push student work to
the shared repository.
