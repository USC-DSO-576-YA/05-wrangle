# Module 5 — Wrangle Data with Pandas

This repository contains the practice data used in the Module 5 **Data
Wrangling with Pandas** handout. The export is intentionally messy so you can practice
cleaning strings, converting numbers and dates, inspecting missing values,
grouping, aggregating, and checking regular-expression results.

## Files

| Path | Purpose |
|---|---|
| `data/retail_orders_messy.csv` | The 120-row retail order export used in the Wednesday activities. |
| `data/README.md` | The grain, column meanings, and cautions for the export. |
| `starter.py` | A minimal loader that preserves the original text for inspection. |
| `pyproject.toml` | The pandas environment for `uv run`. |

## Start

Open a terminal in this repository and run:

```text
uv sync
uv run python starter.py
```

The handout refers to the file with this relative path:

```python
raw = pd.read_csv(
    "data/retail_orders_messy.csv",
    dtype="string",
    keep_default_na=False,
)
```

Keep `raw` unchanged. Create a separate `clean = raw.copy()` before applying
transformations so you can compare the cleaned values with the source export.

Students work locally and commit locally. Do not push work to the shared course
repository.
