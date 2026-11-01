"""Readers that turn files on disk into dataframes."""

from pathlib import Path

import pandas as pd


def load_csv(path: Path) -> pd.DataFrame:
    """Read a CSV file into a dataframe using the first row as header.

    Args:
        path: CSV file to read.

    Returns:
        The parsed dataframe.
    """
    return pd.read_csv(path)


def load_json(path: Path) -> pd.DataFrame:
    """Read a records-style JSON file into a dataframe.

    Args:
        path: JSON file to read.

    Returns:
        The parsed dataframe.
    """
    return pd.read_json(path)