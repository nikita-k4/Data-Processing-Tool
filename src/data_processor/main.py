from pathlib import Path

import pandas as pd

def load_csv(path: Path) -> pd.DataFrame:
    return pd.read_csv(path)

def remove_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    return df.drop_duplicates().reset_index(drop=True)

def drop_missing(df: pd.DataFrame) -> pd.DataFrame:
    return df.dropna().reset_index(drop=True)

def main() -> None:
    path = Path("data/sample.csv")
    df = load_csv(path)
    print(f'Loaded {path}')
    print(f'Initial shape: {df.shape}')

    df = remove_duplicates(df)
    print(f'Shape removing duplicates: {df.shape}')

    df = drop_missing(df)
    print(f'Shape dropping missing: {df.shape}')
    
    print(df.head())


if __name__ == '__main__':
    main()