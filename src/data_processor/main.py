from pathlib import Path

import pandas as pd

def load_csv(path:Path) -> pd.DataFrame:
    return pd.read_csv(path)

def main() -> None:
    path = Path("data/sample.csv")
    df = load_csv(path)
    print(f'Loaded {path}')
    print(f'Shape {df.shape}')
    print(df.head())


if __name__ == '__main__':
    main()