---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:44'
updated: '2026-06-08T00:38:44'
---

# tests/tools/test_tts_path_traversal.py

Symbols in `tests/tools/test_tts_path_traversal.py`.

- L15 `test_output_path_rejects_traversal_escape()` (function) — A path with '..' components must be rejected before any provider work.
- L25 `test_output_path_rejects_bare_dotdot()` (function) — Bare '..' prefix must be rejected.
- L35 `test_output_path_absolute_path_passes_guard(tmp_path, monkeypatch)` (function) — Explicit absolute paths must pass the traversal guard.
- L52 `test_output_path_relative_no_dotdot_passes_guard(tmp_path, monkeypatch)` (function) — Relative paths without '..' components must pass the guard.
