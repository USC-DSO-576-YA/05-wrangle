# Module 5 data

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
Keep identifiers such as `sku` and `order_id` as text.
