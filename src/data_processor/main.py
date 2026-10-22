from pathlib import Path

from src.data_processor.core.cleaning import remove_duplicates, drop_missing, fill_missing
from src.data_processor.core.statistics import summary_stats, format_stats
from src.data_processor.io.readers import load_csv, load_json
from src.data_processor.io.writers import save_csv, save_json



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