import pandas as pd
from pathlib import Path



def save_csv(df: pd.DataFrame, path:Path) -> None:
    df.to_csv(path, index=False)


def save_json(df: pd.DataFrame, path:Path) -> None:
    df.to_json(path, orient='records', indent=2)