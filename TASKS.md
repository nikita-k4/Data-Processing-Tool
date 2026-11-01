# TASKS.md — Project Tasks

Format: `- [ ]` — to do, `- [x]` — done.

## Done

- [x] Read CSV (`load_csv`)
- [x] Read JSON (`load_json`)
- [x] Remove duplicates (`remove_duplicates`)
- [x] Drop rows with NaN (`drop_missing`)
- [x] Fill NaN with a value (`fill_missing`)
- [x] Summary statistics (`summary_stats`)
- [x] Format report (`format_stats`)
- [x] Save to CSV (`save_csv`)
- [x] Save to JSON (`save_json`)
- [x] Modular structure (`io/`, `core/`)
- [x] Tests for all functions

## Current Task

### CLI with argparse

Goal: turn `main.py` into a CLI tool with arguments.

**Requirements:**

- `python -m data_processor --input <path> --output <path>`
- Flags:
  - `--input PATH` (required)
  - `--output PATH` (optional; if omitted — print to console only)
  - `--fill VALUE` (default: don't fill)
  - `--drop-missing` (flag)
  - `--drop-duplicates` (flag)
  - `--stats` (show statistics)
  - `--format {csv,json}` (default: same as input)
- Errors with clear messages (file not found, unknown format).
- `--help` with descriptions of all flags.

**Files:**

- `src/data_processor/cli.py` — argument parsing and pipeline call
- `src/data_processor/__main__.py` — entry point for `python -m data_processor`
- `tests/test_cli.py` — tests via `argparse` or `subprocess`

**Definition of Done:**

- `python -m data_processor --input data/sample.csv --fill 0 --stats` works
- All existing tests pass
- New CLI tests pass

## Next Tasks (after CLI)

- [ ] Extended statistics: mean, median, min, max, std for numeric columns
- [ ] Parquet support (`load_parquet`, `save_parquet`)
- [ ] Friendly error messages (custom exceptions)
- [ ] Logging via `logging`
- [ ] Format registry: `load_file(path)` auto-detects by extension

## Not Doing Soon

- `Pipeline` class — too early, CLI first
- Full config file (YAML/TOML)
- Async
- Web interface

## How to Add Tasks

1. Add under "Current Task" with a clear definition of done.
2. Describe: goal, requirements, files, definition of done.
3. When finished — move to "Done" (or delete).