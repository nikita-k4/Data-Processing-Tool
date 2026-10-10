from pathlib import Path

import pandas as pd

def load_csv(path: Path) -> pd.DataFrame:
    return pd.read_csv(path)

def remove_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    return df.drop_duplicates().reset_index(drop=True)

def drop_missing(df: pd.DataFrame) -> pd.DataFrame:
    return df.dropna().reset_index(drop=True)

def fill_missing(df: pd.DataFrame, value: object) -> pd.DataFrame:
    return df.fillna(value).reset_index(drop=True)

def summary_stats(df: pd.DataFrame) -> dict:
    return {
        'rows': len(df),
        'columns': len(df.columns),
    }

def main() -> None:
    path = Path("data/sample.csv")
    df = load_csv(path)
    print(f'Loaded {path}')
    print(f'Initial shape: {df.shape}')

    df = remove_duplicates(df)
    print(f'Shape removing duplicates: {df.shape}')
    print()

    print("--- Option 1: fill missing with 0 ---")
    df_filled = fill_missing(df, value=0)
    print(f"Shape: {df_filled.shape}")
    print(df_filled)
    print()

    print("--- Option 2: drop rows with missing ---")
    df_dropped = drop_missing(df)
    print(f"Shape: {df_dropped.shape}")
    print(df_dropped)

    print("--- Summary of the filled data ---")
    stats = summary_stats(df_filled)
    print(stats)


if __name__ == '__main__':
    main()