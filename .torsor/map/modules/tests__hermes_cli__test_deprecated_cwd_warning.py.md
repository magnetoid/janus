---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/hermes_cli/test_deprecated_cwd_warning.py

Symbols in `tests/hermes_cli/test_deprecated_cwd_warning.py`.

- L5 `TestDeprecatedCwdWarning` (class) — Warn when MESSAGING_CWD or TERMINAL_CWD is set in .env.
- L8 `test_messaging_cwd_triggers_warning(self, monkeypatch, capsys)` (method)
- L20 `test_terminal_cwd_triggers_warning_when_config_placeholder(self, monkeypatch, capsys)` (method)
- L32 `test_no_warning_when_config_has_explicit_cwd(self, monkeypatch, capsys)` (method)
- L43 `test_no_warning_when_env_clean(self, monkeypatch, capsys)` (method)
- L53 `test_both_deprecated_vars_warn(self, monkeypatch, capsys)` (method)
