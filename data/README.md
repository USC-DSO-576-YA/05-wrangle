# Retail orders data

## Grain

Each row represents one retail order. `order_id` is the row identifier.

## Columns

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
