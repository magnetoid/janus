---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/hermes_cli/test_auth_provider_gate.py

Symbols in `tests/hermes_cli/test_auth_provider_gate.py`.

- L7 `_write_config(tmp_path, config: dict)` (function)
- L14 `_write_auth_store(tmp_path, payload: dict)` (function)
- L21 `_clean_anthropic_env(monkeypatch)` (function) — Strip Anthropic env vars so CI secrets don't leak into tests.
- L27 `test_returns_false_when_no_config(tmp_path, monkeypatch)` (function)
- L35 `test_returns_true_when_active_provider_matches(tmp_path, monkeypatch)` (function)
- L47 `test_returns_true_when_config_provider_matches(tmp_path, monkeypatch)` (function)
- L55 `test_returns_false_when_config_provider_is_different(tmp_path, monkeypatch)` (function)
- L68 `test_returns_true_when_anthropic_env_var_set(tmp_path, monkeypatch)` (function)
- L77 `test_claude_code_oauth_token_does_not_count_as_explicit(tmp_path, monkeypatch)` (function) — CLAUDE_CODE_OAUTH_TOKEN is set by Claude Code, not the user — must not gate.
