# Module 5 Homework
## Compare Taylor Swift Olivia Dean and BTS

Use nine real songs, three per artist, to compare artists with `groupby` and
`.agg`, create two plots, and explain your findings. Submit your individual
`module05_songs.ipynb` on Gradescope.

### Open your notebook

Open `module05_songs.ipynb` in your YA `05-wrangle` folder. Run `uv sync` to
install pandas, Matplotlib, requests, and ipykernel, then select its `.venv`
Python as the notebook kernel. Keep the notebook beside `lyrics_api.py` and
the `data` folder. Complete Part A in class and Part B at home.

Part A uses fictional songs for the class demonstration. Part B loads the
fixed real-artist playlist using the supplied helper. Internet is required;
do not combine these records with the class demo. API mechanics are not exam
material. The selected BTS songs are in English.

### Provided code and your work

The notebook provides data loading, artist-name cleaning, numeric conversion,
mixed-format playlist-date conversion, and merging. Run those cells in order.
Dates such as `2026-09-03` and `Sep 3, 2026` describe the same day. They are
instructor-created playlist dates, not song release dates.

Write `count_words(lyrics)` in Part A and reuse it with the supplied `map`
line in Part B to create `word_count`. Test the function with
separate calls; no loop is required. Count whitespace-separated tokens, with
punctuation attached. Missing or whitespace-only lyrics get a missing count,
not zero. Keep the original `lyrics` column.

Use the Part B `enriched` table for all five tasks below. You write the groupby
summary, both plots, and your explanations. Only selected non-lyrics columns
should appear in notebook output. The API source can change; report retrieval
problems rather than silently dropping or replacing songs.

### Using Codex

Predict first, then ask for hints or feedback on one step at a time. Write
your own analysis code and explanations; do not ask for a completed notebook.

### 1 Check your starting table

Use `enriched` from Part B, prepared by the supplied cleaning cells for
Taylor Swift, Olivia Dean, and BTS. First run the provided `map` line with your
own `count_words` function from Part A. Display song ID,
song, `artist_clean`, `duration_seconds`, `word_count`, `status`, and
`playlist_group`. Confirm nine rows, one per song ID, and the same row count as
`homework_raw`. Do not use the fictional `class_enriched` table.
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
mean and the number of available texts supporting it. Describe the selected
songs, not the artist's entire catalog or lyrical quality.

### 4 Plot individual songs

Create a scatter plot from the song-level `enriched` table, not the
artist summary. Put `duration_seconds` on the horizontal axis and `word_count`
on the vertical axis. Use only rows where both values are known; report the
number of included and excluded songs. Label both axes and title the plot.

Describe whether longer durations consistently go with larger word counts in
these records. Cite two songs that support or complicate your observation.
Do not claim a causal relationship. Durations and lyrics come from a
user-contributed source, and nine selected songs cannot establish a general
music trend. Repetition contributes to the word count.

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
assignment on Gradescope**. Include the supplied cleaning cells, your function, homework
code, displayed summary, both plots, explanations, and assistance note.
Restart the kernel, run all cells in order, and save with outputs visible.
Part B requires internet to retrieve the pinned real-song records. If loading
fails repeatedly, contact the instructor; do not substitute the class demo.
Remove any outputs containing full downloaded lyrics before submitting; keep
the summaries, plots, and non-lyrics tables visible. No separate CSV, image,
or PDF upload is required.
Use the posted course calendar for the deadline. Do not push student work to
the shared repository.
