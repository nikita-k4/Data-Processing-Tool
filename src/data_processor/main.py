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
    non_missing_counts = df.notna().sum()
    missing_counts = df.isna().sum()
    dtypes = df.dtypes

    column_details = {}
    for col_name in df.columns:
        column_details[col_name] = {
            'dtype': str(dtypes[col_name]),
            'non_missing': int(non_missing_counts[col_name]),
            'missing': int(missing_counts[col_name]),
        }
    return {
        'rows': len(df),
        'columns': len(df.columns),
        'column_details': column_details,
    }


def save_csv(df: pd.DataFrame, path:Path) -> None:
    df.to_csv(path, index=False)

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
    path = Path("data/sample.csv")
    df = load_csv(path)
    print(f'Loaded {path}')
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
    print(f"Saved cleaned data to {output_path}")

if __name__ == '__main__':
    main()