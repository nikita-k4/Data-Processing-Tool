"""Writers that serialize dataframes to CSV and JSON files."""

from pathlib import Path

import pandas as pd


def save_csv(df: pd.DataFrame, path: Path) -> None:
    """Write ``df`` to CSV, omitting the index column.

    Args:
        df: Dataframe to write.
        path: Destination CSV file.
    """
    df.to_csv(path, index=False)


def save_json(df: pd.DataFrame, path: Path) -> None:
    """Write ``df`` to JSON as an indented ``records`` array.

    Args:
        df: Dataframe to write.
        path: Destination JSON file.
    """
    df.to_json(path, orient='records', indent=2)