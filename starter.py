"""Load the supplied retail export without silently cleaning its text."""

from pathlib import Path

import pandas as pd


DATA_PATH = Path(__file__).parent / "data" / "retail_orders_messy.csv"


def load_orders() -> pd.DataFrame:
    """Return the raw 120-row order export with every column kept as text."""
    return pd.read_csv(DATA_PATH, dtype="string", keep_default_na=False)


if __name__ == "__main__":
    raw = load_orders()
    print(f"rows={raw.shape[0]}, columns={raw.shape[1]}")
    print(raw.head())
