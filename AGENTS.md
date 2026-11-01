# AGENTS.md — Rules for Working With This Project

This file contains instructions for AI assistants (DeepSeek, Cursor, etc.)
and new contributors. Read it fully before writing any code.

## About the Project

Data Processing Tool is a learning project with real standards. The goal is
to grow it into a complete CLI tool. The owner is learning, so:

**Main rule: do not write the whole solution for them. Explain, guide, review.**

## Project Philosophy

1. **One function, one job.** No "clever" 50-line functions.
2. **Pure functions where possible.** Cleaning functions take and return a
   DataFrame; they don't touch files. I/O functions are the only place
   where reading/writing happens.
3. **I/O at the edges, logic in the middle.**
   `load_csv` (path → df) → `clean` (df → df) → `save_csv` (df → path).
4. **Type hints everywhere.** Every parameter and return value.
5. **Every function has a test.** Minimum: happy path.
6. **No premature abstraction.** Three similar functions are better than one
   "smart" function with flags. Refactor when it hurts.

## Rules for the AI Assistant

### When the user asks for code

- **First**, propose an approach or pseudocode. Ask if they want to write it
  themselves.
- **If they want full code** — provide it, but with comments explaining *why*,
  not just *what*.
- **If it's a learning task** (new function, new test) — do not write it
  fully. Give hints, point to relevant pandas functions, identify bugs in
  their attempt.
- **If it's routine** (rename, add import, fix typo) — just do it.

### NEVER do

- Change folder structure without an explicit request.
- Add dependencies (pandas and pytest are already installed; anything else —
  ask first).
- Refactor code that wasn't asked about.
- Write code without type hints.
- Leave a function without a docstring and a test.
- Use `import *` in new code.
- Delete existing tests "because they're inconvenient."

### ALWAYS do

- Read existing code before proposing changes.
- Follow project style: `snake_case`, English docstrings, English comments.
- Suggest a test for every new function.
- When fixing a bug — explain the cause first, then the fix.
- Specify which file to edit (not "add a function" but
  "add `save_parquet` in `src/data_processor/io/writers.py`").

### Response Format

- Concise. No filler. The user is learning — they need facts, not essays.
- Code in blocks with the file path.
- If offering multiple approaches — explain the trade-off briefly.
- If unsure — say so plainly ("not sure, check the docs").

## Architectural Boundaries

- **`io/`** — reading and writing files only. `load_*` and `save_*` live here.
  No business logic.
- **`core/`** — DataFrame operations only. They don't touch files, don't know
  about paths. Pure functions.
- **`main.py`** — orchestration only. No function definitions (except `main`).
  Only imports and calls.

If a new function violates these boundaries — suggest a different approach.

## Testing

- Every new function — at least one test in `tests/test_main.py`.
- Tests use `tmp_path` for any file operations.
- I/O tests should verify round-trip (save → load → compare).
- Do not use real files from `data/` in tests.
- Test naming: `test_<function>_<what_it_checks>`.

## Git

- Atomic commits: one feature / one fix / one refactor.
- Message format: `<what was done>` (imperative mood).
  Example: `add save_parquet`, `fix empty dataframe in summary_stats`.
- Before committing: `pytest tests -v` must be green.

## Not in the Project Yet (don't suggest without a request)

- CLI (argparse) — planned.
- Classes (`Pipeline`, `Config`) — planned, but not now.
- Logging (`logging`) — planned.
- Parquet/Excel support — maybe later.
- Async — not needed.