"""Entry point for the sample data-processing pipeline.

Reads the bundled samples from ``data/``, cleans them, prints a summary and
writes the cleaned results back to that directory.

This module only orchestrates: every step lives in ``core/`` (pure DataFrame
operations) or ``io/`` (file reading and writing).
"""

from pathlib import Path

from src.data_processor.core.cleaning import drop_missing, fill_missing, remove_duplicates
from src.data_processor.core.statistics import format_stats, summary_stats
from src.data_processor.io.readers import load_csv, load_json
from src.data_processor.io.writers import save_csv, save_json

__all__ = [
    "main",
    "load_csv",
    "load_json",
    "save_csv",
    "save_json",
    "remove_duplicates",
    "drop_missing",
    "fill_missing",
    "summary_stats",
    "format_stats",
]


def main() -> None:
    """Run the sample CSV and JSON pipelines end to end."""
    csv_path = Path("data/sample.csv")
    df = load_csv(csv_path)
    print(f"Loaded {csv_path}")
    print(f"CSV initial shape: {df.shape}")

    df = remove_duplicates(df)
    df = fill_missing(df, value=0)
    print(f"CSV shape after cleaning: {df.shape}")
    print(df)
    print()
    print(format_stats(summary_stats(df)))

    save_csv(df, Path("data/cleaned.csv"))
    save_json(df, Path("data/cleaned.json"))

    json_path = Path("data/sample.json")
    df_json = load_json(json_path)
    print(f"Loaded {json_path}")
    print(f"JSON initial shape: {df_json.shape}")

    df_json = remove_duplicates(df_json)
    df_json = fill_missing(df_json, value=0)
    print(f"JSON shape after cleaning: {df_json.shape}")

    save_csv(df_json, Path("data/cleaned_from_json.csv"))
    save_json(df_json, Path("data/cleaned_from_json.json"))

    print("Saved cleaned data to data/")


if __name__ == "__main__":
    main()