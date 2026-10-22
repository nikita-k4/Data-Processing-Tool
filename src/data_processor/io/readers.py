import pandas as pd
from pathlib import Path



def load_csv(path: Path) -> pd.DataFrame:
    return pd.read_csv(path)


def load_json(path:Path) -> pd.DataFrame:
    return pd.read_json(path)