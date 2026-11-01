"""Dataframe cleaning helpers used by the processing pipeline."""

import pandas as pd


def remove_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    """Drop fully duplicated rows.

    Args:
        df: Source dataframe.

    Returns:
        A new dataframe without duplicate rows and a contiguous index.
    """
    return df.drop_duplicates().reset_index(drop=True)


def drop_missing(df: pd.DataFrame) -> pd.DataFrame:
    """Drop every row that contains at least one missing value.

    Args:
        df: Source dataframe.

    Returns:
        A new dataframe with only complete rows and a contiguous index.
    """
    return df.dropna().reset_index(drop=True)


def fill_missing(df: pd.DataFrame, value: object) -> pd.DataFrame:
    """Replace missing values in every column with ``value``.

    Args:
        df: Source dataframe.
        value: Replacement for ``NaN``/``None``/``NaT`` entries.

    Returns:
        A new dataframe with a contiguous index.
    """
    return df.fillna(value).reset_index(drop=True)