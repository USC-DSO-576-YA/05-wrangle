# Module 5 — Wrangle Data with Pandas

**Current YA assignment:** open [`module05_songs.ipynb`](module05_songs.ipynb).
Complete **Part A in class** (cleaning and preparing the songs table), then
**Part B at home** (groupby, aggregation, two plots, and interpretation).
Submit that one completed notebook on Gradescope. See [HOMEWORK.md](HOMEWORK.md)
for the assignment or download the [Word handout with reference plots](Module_05_Songs_Homework.docx).
The earlier Ralphs homework is retained for reference,
not an additional required submission.

This repository also contains the earlier retail practice data used in the
Module 5 **Data Wrangling with Pandas** handout.

## AI help

AI help in this repo is **hints-only**: short context reminders, one hint at a time,
and feedback on your attempt—not completed code or answers. See [tutor.md](tutor.md).
[AGENTS.md](AGENTS.md) tells the coding assistant to follow this approach.
After updating your clone, start a new Codex session from this repo to load it.

## Files

| Path | Purpose |
|---|---|
| `data/orders_january.csv` | Five January orders used for merge, grouping, and reshaping examples. |
| `data/orders_february.csv` | Two February orders with the same schema, used for concatenation. |
| `data/product_catalog.csv` | Product categories used in the safe-merge example. |
| `data/returns_log.csv` | The complete return log at the reporting cutoff. |
| `data/retail_orders_messy.csv` | The 120-row retail order export used in the full wrangling activities. |
| `data/11-ralphs_sales.csv.gz` | Original Ralphs export, preserved for optional reference. |
| [`module05_ralphs.ipynb`](module05_ralphs.ipynb) | Earlier homework starter, superseded by songs; no additional submission. |
| `data/README.md` | The grain, column meanings, and cautions for the export. |
| `starter.py` | A minimal loader that preserves the original text for inspection. |
| [`module05_songs.ipynb`](module05_songs.ipynb) | Current in-class cleaning and homework notebook; complete and submit on Gradescope. |
| [`HOMEWORK.md`](HOMEWORK.md) | Current songs homework instructions, matching the Word handout. |
| [`Module_05_Songs_Homework.docx`](Module_05_Songs_Homework.docx) | Student homework handout including both reference plots. |
| `lyrics_api.py` | Supplied LRCLIB requests, match checks, status handling, and DataFrame loader. |
| `data/songs_demo.json` | Twelve fictional records with original classroom text; offline practice, not real lyrics. |
| `pyproject.toml` | pandas, Matplotlib, requests, and the notebook kernel for `uv run`. |

## Start

Open a terminal in this repository and run:

```text
uv sync
uv run python starter.py
```

The longer cleaning activities use this relative path:

```python
raw = pd.read_csv(
    "data/retail_orders_messy.csv",
    dtype="string",
    keep_default_na=False,
)
```

Keep `raw` unchanged. Create a separate `clean = raw.copy()` before applying
transformations so you can compare the cleaned values with the source export.

## Earlier Ralphs exercise

The earlier Ralphs exercise uses `data/11-ralphs_sales.csv.gz`. It is no longer
the current homework; the file contents are preserved for reference. Open the
[`module05_ralphs.ipynb`](module05_ralphs.ipynb) starter in this repository's
top-level folder, beside `data/`, if you want extra practice. Only the
data-loading code is provided. If you already started your own notebook, keep
your work and use the starter instructions as a reference rather than replacing it.
Pandas can read the compressed CSV directly; no manual extraction is needed.
The `11-` belongs to the original dataset filename, not this module number.
See `data/README.md` for the source columns. Any submission instructions inside
that older notebook are superseded by [HOMEWORK.md](HOMEWORK.md). Do not upload
both notebooks. The hints-only AI policy also applies to this optional practice.

## Wednesday songs workshop

Open `module05_songs.ipynb`, run `uv sync`, and select this repo's `.venv` Python
as the notebook kernel. If needed, register it with:

```text
uv run python -m ipykernel install --user --name dso576-module5 --display-name "DSO576 Module 5"
```

The required work uses twelve explicitly fictional records, four per artist,
so it does not depend on API availability. Change `USE_LIVE_API` to `True` only for the
three-song live demonstration. Failed requests remain visible as status values;
the helper does not silently substitute demo data or select the first search
match. Inspect metadata before using a source record. Requests are cached in
memory for the current session; restart the kernel to fetch fresh data.

The HTTP code is provided setup, outside the exam scope. In class, write the
inspection and name-cleaning steps, then convert the playlist dates early in
class. Next handle missing lyrics, write the scalar function, apply map, and
merge the tables in small cells.
At home, continue with that same table for the artist summary, bar chart,
scatter plot, and written interpretation. Return to `USE_LIVE_API = False` and
run all cells before submitting. The three-song live demo is not the required
homework dataset. Do not mix demo and live rows.

Do not commit downloaded lyrics or notebook outputs containing them. The
hints-only policy still applies to the analysis. This songs assignment
replaces the earlier Ralphs homework.

## Concept checkpoints

### From orders to a comparison table

The business question is: **How does revenue compare between Online and Store
across January and February?**

`groupby` calculates the four month-channel totals. `pivot` rearranges those
totals into two month rows and two channel columns.

```python
jan = pd.read_csv("data/orders_january.csv")
feb = pd.read_csv("data/orders_february.csv")
orders = pd.concat([jan, feb], ignore_index=True)

summary = orders.groupby(
    ["month", "channel"], as_index=False
).agg(revenue=("amount", "sum"))

wide = summary.pivot(
    index="month", columns="channel", values="revenue"
)
```

### How to handle missing data

Use this order:

1. **Detect:** use `isna()` and count the affected rows.
2. **Decide:** keep and flag, `fillna`, or targeted `dropna(subset=[...])`.
3. **Calculate:** report non-missing coverage beside the result.

Only fill when a business rule supplies the replacement. Only drop when the
field is required for the current task. For calculations, remember that `sum`
and `mean` skip missing values; `sum(min_count=1)` prevents an all-missing total
from appearing as zero. Use `groupby(..., dropna=False)` when a missing group
key should remain visible in the report.

Students work locally and commit locally. Do not push work to the shared course
repository.
