import pandas as pd



def remove_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    return df.drop_duplicates().reset_index(drop=True)


def drop_missing(df: pd.DataFrame) -> pd.DataFrame:
    return df.dropna().reset_index(drop=True)


def fill_missing(df: pd.DataFrame, value: object) -> pd.DataFrame:
    return df.fillna(value).reset_index(drop=True)