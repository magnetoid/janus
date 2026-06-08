---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/hermes_cli/test_auth_qwen_provider.py

Symbols in `tests/hermes_cli/test_auth_qwen_provider.py`.

- L34 `_make_qwen_tokens(access_token='test-access-token', refresh_token='test-refresh-token', expiry_date=None, **extra)` (function) — Create a minimal Qwen CLI OAuth credential dict.
- L55 `_write_qwen_creds(tmp_path, tokens=None)` (function) — Write tokens to the Qwen CLI credentials file and return the path.
- L67 `qwen_env(tmp_path, monkeypatch)` (function) — Redirect _qwen_cli_auth_path to tmp_path/.qwen/oauth_creds.json.
- L80 `test_qwen_cli_auth_path_returns_expected_location()` (function)
- L89 `test_read_qwen_cli_tokens_success(qwen_env)` (function)
- L97 `test_read_qwen_cli_tokens_missing_file(qwen_env)` (function)
- L103 `test_read_qwen_cli_tokens_invalid_json(qwen_env)` (function)
- L112 `test_read_qwen_cli_tokens_non_dict(qwen_env)` (function)
- L125 `test_save_qwen_cli_tokens_roundtrip(qwen_env)` (function)
- L133 `test_save_qwen_cli_tokens_creates_parent(qwen_env)` (function)
- L139 `test_save_qwen_cli_tokens_permissions(qwen_env)` (function)
- L153 `test_expiring_token_not_expired()` (function)
- L159 `test_expiring_token_already_expired()` (function)
- L165 `test_expiring_token_within_skew()` (function)
- L171 `test_expiring_token_none_returns_true()` (function)
- L175 `test_expiring_token_non_numeric_returns_true()` (function)
- L183 `test_refresh_qwen_cli_tokens_success(qwen_env)` (function)
- L203 `test_refresh_qwen_cli_tokens_preserves_old_refresh_if_not_in_response(qwen_env)` (function)
- L221 `test_refresh_qwen_cli_tokens_missing_refresh_token()` (function)
- L228 `test_refresh_qwen_cli_tokens_http_error(qwen_env)` (function)
- L242 `test_refresh_qwen_cli_tokens_network_error(qwen_env)` (function)
- L252 `test_refresh_qwen_cli_tokens_invalid_json_response(qwen_env)` (function)
- L266 `test_refresh_qwen_cli_tokens_missing_access_token_in_response(qwen_env)` (function)
- L280 `test_refresh_qwen_cli_tokens_default_expires_in(qwen_env)` (function) — When expires_in is missing, default to 6 hours.
- L297 `test_refresh_qwen_cli_tokens_saves_to_disk(qwen_env)` (function)
- L322 `test_resolve_qwen_runtime_credentials_fresh_token(qwen_env)` (function)
- L333 `test_resolve_qwen_runtime_credentials_triggers_refresh(qwen_env)` (function)
- L349 `test_resolve_qwen_runtime_credentials_force_refresh(qwen_env)` (function)
- L363 `test_resolve_qwen_runtime_credentials_missing_access_token(qwen_env)` (function)
- L372 `test_resolve_qwen_runtime_credentials_base_url_env_override(qwen_env, monkeypatch)` (function)
- L385 `test_get_qwen_auth_status_logged_in(qwen_env)` (function)
- L394 `test_get_qwen_auth_status_refreshes_expired_token(qwen_env)` (function)
- L411 `test_get_qwen_auth_status_expired_unrefreshable_token_is_not_logged_in(qwen_env)` (function)
- L431 `test_get_qwen_auth_status_not_logged_in(qwen_env)` (function)
- L438 `test_model_flow_qwen_oauth_stale_token_shows_reauth_guidance(qwen_env, monkeypatch, capsys)` (function)
