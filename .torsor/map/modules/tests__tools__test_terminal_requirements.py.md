---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:44'
updated: '2026-06-08T00:38:44'
---

# tests/tools/test_terminal_requirements.py

Symbols in `tests/tools/test_terminal_requirements.py`.

- L8 `_clear_terminal_env(monkeypatch)` (function) — Remove terminal env vars that could affect requirements checks.
- L37 `test_local_terminal_requirements(monkeypatch, caplog)` (function) — Local backend uses Hermes' own LocalEnvironment wrapper.
- L49 `test_unknown_terminal_env_logs_error_and_returns_false(monkeypatch, caplog)` (function)
- L63 `test_ssh_backend_without_host_or_user_logs_and_returns_false(monkeypatch, caplog)` (function)
- L77 `test_modal_backend_without_token_or_config_logs_specific_error(monkeypatch, caplog, tmp_path)` (function)
- L95 `test_modal_backend_with_managed_gateway_does_not_require_direct_creds_or_minisweagent(monkeypatch, tmp_path)` (function)
- L114 `test_modal_backend_auto_mode_prefers_managed_gateway_over_direct_creds(monkeypatch, tmp_path)` (function)
- L134 `test_modal_backend_direct_mode_does_not_fall_back_to_managed(monkeypatch, caplog, tmp_path)` (function)
- L152 `test_modal_backend_managed_mode_does_not_fall_back_to_direct(monkeypatch, caplog, tmp_path)` (function)
- L172 `test_modal_backend_managed_mode_without_feature_flag_logs_clear_error(monkeypatch, caplog, tmp_path)` (function)
