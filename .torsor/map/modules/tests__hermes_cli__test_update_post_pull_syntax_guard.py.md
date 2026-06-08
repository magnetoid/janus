---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/hermes_cli/test_update_post_pull_syntax_guard.py

Symbols in `tests/hermes_cli/test_update_post_pull_syntax_guard.py`.

- L27 `test_capture_head_sha_returns_stripped_sha(monkeypatch, tmp_path)` (function)
- L37 `test_capture_head_sha_returns_none_on_git_failure(monkeypatch, tmp_path)` (function)
- L48 `test_capture_head_sha_returns_none_on_empty_output(monkeypatch, tmp_path)` (function)
- L61 `_populate_critical_tree(root: Path, *, broken_file: str | None=None)` (function) — Create stub files for every entry in ``_UPDATE_CRITICAL_FILES``.
- L86 `test_validate_critical_files_syntax_ok_when_all_files_parse(tmp_path)` (function)
- L96 `test_validate_critical_files_syntax_detects_conflict_markers(tmp_path)` (function) — The exact PR #28452 failure mode: orphan ``<<<<<<<`` in config.py.
- L110 `test_validate_critical_files_syntax_detects_break_in_main_py(tmp_path)` (function)
- L119 `test_validate_critical_files_syntax_tolerates_missing_files(tmp_path)` (function) — A refactor may legitimately remove one of the critical files — the
- L144 `test_production_tree_passes_syntax_guard()` (function) — The repo itself must always satisfy the guard the update command runs.
