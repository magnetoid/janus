---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/hermes_cli/test_at_context_completion_filter.py

Symbols in `tests/hermes_cli/test_at_context_completion_filter.py`.

- L20 `_run(tmp_path: Path, word: str)` (function)
- L32 `test_at_folder_only_yields_directories(tmp_path, monkeypatch)` (function)
- L44 `test_at_file_only_yields_files(tmp_path, monkeypatch)` (function)
- L56 `test_at_folder_preserves_prefix_on_empty_match(tmp_path, monkeypatch)` (function) — User typed `@folder:` (no partial) — completion text must keep the
- L70 `test_at_folder_bare_without_colon_lists_directories(tmp_path, monkeypatch)` (function) — Typing `@folder` alone (no colon yet) should surface directories so
- L84 `test_at_file_bare_without_colon_lists_files(tmp_path, monkeypatch)` (function)
