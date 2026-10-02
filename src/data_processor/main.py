from pathlib import Path

import pandas as pd

def load_csv(path: Path) -> pd.DataFrame:
    return pd.read_csv(path)

def remove_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    return df.drop_duplicates().reset_index(drop=True)

def main() -> None:
    path = Path("data/sample.csv")
    df = load_csv(path)
    print(f'Shape before: {df.shape}')

    df = remove_duplicates(df)
    print(f'Loaded {path}')
    print(f'Shape after: {df.shape}')
    
    print(df.head())


if __name__ == '__main__':
    main()