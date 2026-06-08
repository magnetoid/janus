---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# scripts/run_tests_parallel.py

Symbols in `scripts/run_tests_parallel.py`.

- L86 `_count_tests(files: List[Path], repo_root: Path, pytest_passthrough: List[str])` (function) — Run ``pytest --co -q`` once to count individual tests per file.
- L144 `_discover_files(roots: List[Path])` (function) — Return every ``test_*.py`` under the given roots (sorted).
- L191 `_kill_tree(proc: 'subprocess.Popen', pgid: int | None=None)` (function) — Kill the pytest subprocess and every descendant it spawned.
- L249 `_run_one_file(file: Path, pytest_args: List[str], repo_root: Path, file_timeout: float)` (function) — Run ``python -m pytest <file> <pytest_args>`` in a fresh subprocess.
- L348 `_parse_pytest_summary(output: str)` (function) — Extract per-file test pass/fail/skip counts from pytest output.
- L383 `_format_file(file: Path, repo_root: Path)` (function) — Render a test-file path for display: strip the repo-root prefix
- L396 `_print_progress(tests_done: int, total_tests: int, file: Path, rc: int, dur: float, repo_root: Path, tests_passed: int, tests_failed: int, test_counts: dict[Path, int], file_summary: dict[str, int] | None=None, subproc_wall: float | None=None)` (function) — Single-line live progress.
- L469 `_print_inline_failure(file: Path, output: str, repo_root: Path, pytest_passthrough: List[str])` (function) — Print a compact failure summary immediately when a file fails.
- L500 `_load_durations(repo_root: Path)` (function) — Read the duration cache from the repo root.
- L516 `_save_durations(file_times: List[Tuple[Path, float]], repo_root: Path)` (function) — Write the duration cache so future ``--slice`` runs can use it.
- L535 `_slice_files(files: List[Path], slice_index: int, slice_count: int, durations: dict[str, float], repo_root: Path)` (function) — Return the subset of *files* belonging to slice *slice_index*.
- L601 `main()` (function)
