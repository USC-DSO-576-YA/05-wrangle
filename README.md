# Module 5 — Wrangle Data with Pandas

This repository contains the practice data used in the Module 5 **Data
Wrangling with Pandas** handout. The export is intentionally messy so you can practice
cleaning strings, converting numbers and dates, inspecting missing values,
grouping, aggregating, and checking regular-expression results.

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
| `data/11-ralphs_sales.csv.gz` | The original Ralphs sales export for Module 5 homework; separate from the fictional practice files. |
| [`module05_ralphs.ipynb`](module05_ralphs.ipynb) | Homework starter with Markdown instructions, empty code cells, and explanation spaces; complete and submit on Gradescope. |
| `data/README.md` | The grain, column meanings, and cautions for the export. |
| `starter.py` | A minimal loader that preserves the original text for inspection. |
| `pyproject.toml` | The pandas environment for `uv run`. |

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

## Ralphs homework

The Ralphs homework uses `data/11-ralphs_sales.csv.gz`. Open the supplied
[`module05_ralphs.ipynb`](module05_ralphs.ipynb) starter in this repository's
top-level folder, beside `data/`. Complete the code cells and Markdown responses
in the same notebook. Only the data-loading code is provided; the cleaning tasks
are left for you to complete. If you already started your own notebook, keep
your work and use the starter instructions as a reference rather than replacing it.
Pandas can read the compressed CSV directly; no manual extraction is needed.
The `11-` belongs to the original dataset filename, not this module number.
See `data/README.md` for the source columns. Submit your completed notebook
on Gradescope, not to this shared GitHub repository. The hints-only AI policy
above also applies to the homework.

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
