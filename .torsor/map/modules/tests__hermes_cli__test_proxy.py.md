---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/hermes_cli/test_proxy.py

Symbols in `tests/hermes_cli/test_proxy.py`.

- L25 `test_registry_lists_nous()` (function)
- L29 `test_registry_lists_xai()` (function)
- L33 `test_get_adapter_returns_instance()` (function)
- L39 `test_get_adapter_returns_xai_instance()` (function)
- L45 `test_get_adapter_case_insensitive()` (function)
- L51 `test_get_adapter_unknown_provider_raises()` (function)
- L61 `_write_auth_store(hermes_home: Path, nous_state: Dict[str, Any])` (function) — Write an auth.json with the given nous state into a hermetic HERMES_HOME.
- L71 `test_nous_adapter_metadata()` (function)
- L81 `test_nous_adapter_not_authenticated_when_no_auth_file(tmp_path, monkeypatch)` (function)
- L88 `test_nous_adapter_not_authenticated_when_provider_missing(tmp_path, monkeypatch)` (function)
- L97 `test_nous_adapter_authenticated_with_agent_key(tmp_path, monkeypatch)` (function)
- L107 `test_nous_adapter_authenticated_with_refresh_token_only(tmp_path, monkeypatch)` (function) — If access_token+refresh_token exist but no agent_key yet, we can still refresh.
- L117 `test_nous_adapter_get_credential_uses_runtime_resolver(tmp_path, monkeypatch)` (function)
- L147 `test_nous_adapter_retry_credential_force_refreshes_on_jwt_401(tmp_path, monkeypatch)` (function)
- L181 `test_nous_adapter_retry_credential_skips_non_401(tmp_path, monkeypatch)` (function)
- L205 `test_nous_adapter_get_credential_raises_when_not_logged_in(tmp_path, monkeypatch)` (function)
- L212 `test_nous_adapter_get_credential_raises_on_refresh_failure(tmp_path, monkeypatch)` (function)
- L228 `test_nous_adapter_quarantines_terminal_refresh_failure(tmp_path, monkeypatch)` (function)
- L262 `test_nous_adapter_get_credential_raises_when_no_jwt_returned(tmp_path, monkeypatch)` (function) — If the refresh helper succeeds but produces no JWT, we surface a clear error.
- L279 `test_nous_adapter_concurrent_refresh_serialized(tmp_path, monkeypatch)` (function) — Two parallel get_credential() calls must serialize through the lock.
- L345 `_write_xai_pool_entry(hermes_home: Path, *, access_token: str='xai-access-token', refresh_token: str='xai-refresh-token', base_url: str='https://api.x.ai/v1', source: str='manual:xai_pkce')` (function) — Write an xai-oauth pool entry into a hermetic HERMES_HOME.
- L376 `test_xai_adapter_metadata()` (function)
- L385 `test_xai_adapter_not_authenticated_when_no_pool_entry(tmp_path, monkeypatch)` (function)
- L395 `test_xai_adapter_authenticated_with_pool_entry(tmp_path, monkeypatch)` (function)
- L401 `test_xai_adapter_get_credential_uses_oauth_pool(tmp_path, monkeypatch)` (function)
- L416 `test_xai_adapter_get_credential_defaults_base_url(tmp_path, monkeypatch)` (function)
- L425 `test_xai_adapter_retry_refreshes_current_pool_entry(tmp_path, monkeypatch)` (function)
- L451 `test_xai_adapter_retry_rotates_pool_entry_on_429(tmp_path, monkeypatch)` (function) — 429 from xAI must rotate to the next pool entry, not attempt refresh.
- L519 `test_xai_adapter_retry_returns_none_on_429_when_pool_exhausted(tmp_path, monkeypatch)` (function) — Single-entry pool: 429 has nowhere to rotate to → return None
- L544 `test_xai_adapter_retry_returns_none_for_unrelated_status(tmp_path, monkeypatch)` (function) — Non-{401, 429} statuses must NOT trigger any retry — pool
- L580 `FakeAdapter` (class) — A test adapter that returns a fixed credential without touching disk.
- L583 `__init__(self, base_url: str, bearer: str='test-bearer', allowed=None, raise_on_credential=False, retry_bearer: str | None=None)` (method)
- L595 `name(self)` (method)
- L598 `display_name(self)` (method)
- L601 `allowed_paths(self)` (method)
- L603 `is_authenticated(self)` (method)
- L605 `get_credential(self)` (method)
- L614 `get_retry_credential(self, *, failed_credential, status_code)` (method)
- L626 `_start_runner(app: 'web.Application')` (function) — Spin up an aiohttp app on an ephemeral localhost port. Returns (runner, base_url).
- L637 `_build_fake_upstream(captured: Dict[str, Any])` (function)
- L665 `_build_retrying_fake_upstream(captured: Dict[str, Any])` (function)
- L684 `test_server_forwards_chat_completions()` (function)
- L714 `test_server_retries_once_with_adapter_retry_credential_on_401()` (function)
- L749 `test_server_rejects_disallowed_path()` (function)
- L766 `test_server_returns_401_when_adapter_fails()` (function)
- L783 `test_server_health_endpoint()` (function)
- L801 `test_server_streams_sse()` (function)
- L824 `test_server_strips_client_auth_header()` (function) — The client's Authorization header MUST NOT reach the upstream.
- L853 `test_cmd_proxy_status_runs(capsys, tmp_path, monkeypatch)` (function)
- L866 `test_cmd_proxy_providers_runs(capsys)` (function)
- L877 `test_cmd_proxy_start_refuses_unknown_provider(capsys)` (function)
- L890 `test_cmd_proxy_start_refuses_when_unauthenticated(capsys, tmp_path, monkeypatch)` (function)
