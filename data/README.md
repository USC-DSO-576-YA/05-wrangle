# Module 5 data

## Songs workshop

`songs_demo.json` contains twelve **fictional** song records, four per artist,
with short original
classroom verses (not full commercial lyrics). Names include intentional spaces
and capitalization differences. Two rows have missing text: one unavailable
and one instrumental. These are different from zero-word songs. `song_id` is the
unique playlist-entry identifier; `source` explicitly marks demo data. Durations
are invented demo metadata, not measurements of those verses.

The optional live mode requests public records from https://lrclib.net/docs
using the supplied `lyrics_api.py`. It returns one row per requested playlist
entry, even when the request fails. Keep status/detail and the selected source
ID. Live results can change; an exact title/artist match is not verification of
album, recording, duration, or text accuracy. The notebook's added-on dates and
playlist groups are instructor-created, not release dates or API metadata.
No commercial lyrics are bundled in this repository.

The required songs homework uses this offline dataset. Students continue from
their in-class cleaning in `module05_songs.ipynb`, then group and plot the
cleaned data. Artist summaries must distinguish total songs from available
texts. A missing word count must not be replaced with zero. Use the chart to
describe these classroom records, not real music trends.

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

## Earlier Ralphs exercise data

`11-ralphs_sales.csv.gz` is the original instructor-supplied Ralphs grocery
sales export, included unchanged. It is separate from the fictional practice
files above. The `11-` is part of its original filename; the homework is for
Module 5.

The source columns are `Geography`, `Time`, `Product`, `Dollar Sales`, and
`Unit Sales`. They contain the reported geography, reporting period, raw
product description, dollar revenue, and packages sold. Keep the source file
unchanged and consult the homework handout for the cleaning requirements.

From a notebook saved in the top-level `05-wrangle` folder, load it with:

```python
import pandas as pd

raw = pd.read_csv("data/11-ralphs_sales.csv.gz", dtype="string")
```

Pandas reads the gzip archive directly. No manual extraction is needed.
The Ralphs notebook is retained as optional practice; its old submission
instructions no longer apply. The current assignment is `module05_songs.ipynb`
as described in `HOMEWORK.md`. Do not push student work to this shared repository.
