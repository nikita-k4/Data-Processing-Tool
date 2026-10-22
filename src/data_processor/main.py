from pathlib import Path
from src.data_processor.core.cleaning import *
from src.data_processor.core.statistics import *

import pandas as pd

def load_csv(path: Path) -> pd.DataFrame:
    return pd.read_csv(path)

def load_json(path:Path) -> pd.DataFrame:
    return pd.read_json(path)


def save_csv(df: pd.DataFrame, path:Path) -> None:
    df.to_csv(path, index=False)


def save_json(df: pd.DataFrame, path:Path) -> None:
    df.to_json(path, orient='records', indent=2)

def format_stats(stats: dict) -> str:
    lines = []
    lines.append("Summary")
    lines.append("=======")
    lines.append(f"Rows: {stats['rows']}")
    lines.append(f"Columns: {stats['columns']}")
    lines.append("")
    lines.append("Column details:")
    for col_name, details in stats['column_details'].items():
        lines.append(
            f"  {col_name:<6} "
            f"dtype={details['dtype']:<8}"
            f"non_missing={details['non_missing']:<3}"
            f"missing={details['missing']}"
        )

    return "\n".join(lines)


def main() -> None:
    path_csv = Path("data/sample.csv")
    df = load_csv(path_csv)
    print(f'Loaded {path_csv}')
    print(f'Initial shape: {df.shape}')

    df = remove_duplicates(df)
    print(f'Shape removing duplicates: {df.shape}')
    print()

    print("--- Option 1: fill missing with 0 ---")
    df = fill_missing(df, value=0)
    print(f"Shape: {df.shape}")
    print(df)
    print()

    #print("--- Option 2: drop rows with missing ---")
    #df = drop_missing(df)
    #print(f"Shape: {df.shape}")
    #print(df)

    stats = summary_stats(df)
    stats_formatted = format_stats(stats)
    print(stats_formatted)

    output_path = Path("data/cleaned.csv")
    save_csv(df, output_path)
    save_json(df, Path("data/cleaned.json"))
    print(f"Saved cleaned data to {output_path}")

    path_json = Path("data/sample.json")
    df_json = load_json(path_json)
    print(f"Loaded {path_json}")
    print(f"Json initial shape: {df_json.shape}")

    df_json = remove_duplicates(df_json)
    df_json = fill_missing(df_json, value=0)

    save_csv(df_json, Path("data/cleaned_from_json.csv"))
    save_json(df_json, Path("data/cleaned_from_json.json"))

if __name__ == '__main__':
    main()