---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:44'
updated: '2026-06-08T00:38:44'
---

# tests/tools/test_resolve_path.py

Symbols in `tests/tools/test_resolve_path.py`.

- L9 `TestResolvePath` (class) — Verify _resolve_path respects TERMINAL_CWD for worktree isolation.
- L12 `test_relative_path_uses_terminal_cwd(self, monkeypatch, tmp_path)` (method) — Relative paths resolve against TERMINAL_CWD, not process CWD.
- L20 `test_absolute_path_ignores_terminal_cwd(self, monkeypatch, tmp_path)` (method) — Absolute paths are unaffected by TERMINAL_CWD.
- L29 `test_falls_back_to_cwd_without_terminal_cwd(self, monkeypatch)` (method) — Without TERMINAL_CWD, falls back to os.getcwd().
- L37 `test_tilde_expansion(self, monkeypatch, tmp_path)` (method) — ~ is expanded before TERMINAL_CWD join (already absolute).
- L46 `test_result_is_resolved(self, monkeypatch, tmp_path)` (method) — Output path has no '..' components.
- L55 `test_relative_path_prefers_live_file_ops_cwd(self, monkeypatch, tmp_path)` (method) — Live env.cwd must win after the terminal session changes directory.
