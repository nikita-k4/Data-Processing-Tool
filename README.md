# Data Processing Tool

A CLI tool for processing data: read CSV/JSON, clean, compute statistics,
export to multiple formats.

## What It Does

- Reads CSV and JSON into pandas DataFrames
- Removes duplicates, handles missing values
- Computes summary statistics per column
- Formats a readable report
- Saves results to CSV and JSON

## Project Structure

```text
src/
└── data_processor/
    ├── __init__.py
    ├── main.py             # orchestration: read → clean → stats → write
    ├── cli.py              # argparse front end (see TASKS.md)
    ├── __main__.py         # entry point for `python -m data_processor`
    ├── io/
    │   ├── readers.py      # load_csv, load_json
    │   └── writers.py      # save_csv, save_json
    └── core/
        ├── cleaning.py     # remove_duplicates, drop_missing, fill_missing
        └── statistics.py   # summary_stats, format_stats
tests/
├── test_main.py            # unit tests (pytest)
└── test_cli.py             # CLI tests (see TASKS.md)
data/
├── sample.csv
├── sample.json
└── cleaned.*               # generated output files
```

## Setup

```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# Mac/Linux:
source .venv/bin/activate

pip install pandas pytest
```

## Run

```bash
py -m src.data_processor.main
```

The script reads `data/sample.csv` and `data/sample.json`, cleans them,
computes statistics, and writes `data/cleaned.*` and `data/cleaned_from_json.*`.

## Tests

```bash
pytest tests -v
```

## Stack

- Python 3.11+
- pandas
- pytest

## Current Status

- [x] Read CSV / JSON
- [x] Cleaning: duplicates, missing values (drop / fill)
- [x] Summary statistics per column
- [x] Formatted report output
- [x] Save to CSV / JSON
- [x] Modular structure (io / core)
- [ ] CLI with arguments (argparse)
- [ ] Extended statistics (mean, median, std)
- [ ] Friendly error handling