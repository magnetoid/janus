---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/agent/test_runtime_cwd.py

Symbols in `tests/agent/test_runtime_cwd.py`.

- L17 `_raise_oserror(*args, **kwargs)` (function)
- L21 `TestResolveAgentCwd` (class)
- L22 `test_prefers_terminal_cwd_over_getcwd(self, monkeypatch, tmp_path)` (method)
- L27 `test_falls_back_to_getcwd_when_unset(self, monkeypatch, tmp_path)` (method)
- L33 `test_skips_nonexistent_terminal_cwd(self, monkeypatch, tmp_path)` (method)
- L38 `test_expands_leading_tilde(self, monkeypatch)` (method)
- L42 `test_whitespace_only_terminal_cwd_falls_back_to_getcwd(self, monkeypatch, tmp_path)` (method)
- L48 `test_propagates_oserror_from_getcwd(self, monkeypatch)` (method)
- L58 `TestResolveContextCwd` (class)
- L59 `test_returns_dir_when_set(self, monkeypatch, tmp_path)` (method)
- L63 `test_returns_none_when_unset(self, monkeypatch)` (method)
- L69 `test_returns_nonexistent_dir_unguarded(self, monkeypatch, tmp_path)` (method)
- L76 `test_expands_leading_tilde(self, monkeypatch)` (method)
- L80 `test_whitespace_only_terminal_cwd_returns_none(self, monkeypatch)` (method)
- L87 `TestSessionCwdOverride` (class) — The #29531 per-session arm: a contextvar cwd wins over TERMINAL_CWD so a
- L91 `test_session_cwd_overrides_terminal_cwd(self, monkeypatch, tmp_path)` (method)
- L102 `test_empty_session_cwd_falls_back_to_terminal_cwd(self, monkeypatch, tmp_path)` (method)
- L111 `test_clear_session_cwd_restores_terminal_cwd(self, monkeypatch, tmp_path)` (method)
- L122 `test_nonexistent_session_cwd_falls_back(self, monkeypatch, tmp_path)` (method)
