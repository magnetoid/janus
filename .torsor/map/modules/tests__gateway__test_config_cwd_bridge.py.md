---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_config_cwd_bridge.py

Symbols in `tests/gateway/test_config_cwd_bridge.py`.

- L16 `_simulate_config_bridge(cfg: dict, initial_env: dict | None=None)` (function) — Simulate the gateway config bridge logic from gateway/run.py.
- L78 `TestTopLevelCwdAlias` (class) — Top-level `cwd:` should be treated as `terminal.cwd`.
- L81 `test_top_level_cwd_sets_terminal_cwd(self)` (method)
- L86 `test_top_level_backend_sets_terminal_env(self)` (method)
- L91 `test_top_level_cwd_and_backend(self)` (method)
- L97 `test_nested_terminal_takes_precedence_over_top_level(self)` (method) — terminal.cwd should win over top-level cwd.
- L106 `test_nested_terminal_backend_takes_precedence(self)` (method)
- L114 `test_no_cwd_falls_back_to_messaging_cwd(self)` (method)
- L119 `test_no_cwd_no_messaging_cwd_falls_back_to_home(self)` (method)
- L124 `test_dot_cwd_triggers_messaging_fallback(self)` (method) — cwd: '.' should trigger MESSAGING_CWD fallback.
- L136 `test_auto_cwd_triggers_messaging_fallback(self)` (method)
- L141 `test_empty_cwd_ignored(self)` (method)
- L146 `test_whitespace_only_cwd_ignored(self)` (method)
- L151 `test_messaging_cwd_env_var_works(self)` (method) — MESSAGING_CWD in initial env should be picked up as fallback.
- L157 `test_top_level_cwd_beats_messaging_cwd(self)` (method) — Explicit top-level cwd should take precedence over MESSAGING_CWD.
- L164 `TestNestedTerminalCwdPlaceholderSkip` (class) — terminal.cwd placeholder values must not clobber TERMINAL_CWD.
- L173 `test_terminal_dot_cwd_does_not_clobber_env(self)` (method) — terminal.cwd: '.' should not overwrite a pre-set TERMINAL_CWD.
- L179 `test_terminal_auto_cwd_does_not_clobber_env(self)` (method)
- L184 `test_terminal_cwd_keyword_does_not_clobber_env(self)` (method)
- L189 `test_terminal_explicit_cwd_does_override(self)` (method) — terminal.cwd: '/explicit/path' SHOULD override TERMINAL_CWD.
- L195 `test_terminal_dot_cwd_falls_back_to_messaging_cwd(self)` (method) — terminal.cwd: '.' with no TERMINAL_CWD should fall to MESSAGING_CWD.
- L201 `test_terminal_dot_cwd_and_messaging_cwd_both_set(self)` (method) — Pre-set TERMINAL_CWD from .env wins over terminal.cwd: '.'.
- L210 `test_non_cwd_terminal_keys_still_bridge(self)` (method) — Other terminal config keys (backend, timeout) should still bridge normally.
- L219 `TestTildeExpansion` (class) — terminal.cwd values containing shell tilde must be expanded.
- L226 `test_terminal_cwd_tilde_expanded(self)` (method) — terminal.cwd: '~/projects' should expand to /home/<user>/projects.
- L232 `test_top_level_cwd_tilde_expanded(self)` (method) — top-level cwd: '~/' should expand to user's home directory.
- L238 `test_tilde_with_nested_precedence(self)` (method) — Nested terminal.cwd should win over top-level, both expanded.
