---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/run_agent/test_create_openai_client_proxy_env.py

Symbols in `tests/run_agent/test_create_openai_client_proxy_env.py`.

- L28 `_make_agent()` (function)
- L40 `_extract_http_client(client_kwargs: dict)` (function) — _create_openai_client calls ``OpenAI(**client_kwargs)``; grab the injected client.
- L45 `test_get_proxy_from_env_prefers_https_then_http_then_all(monkeypatch)` (function)
- L61 `test_get_proxy_from_env_ignores_blank_values(monkeypatch)` (function)
- L70 `test_get_proxy_from_env_normalizes_socks_alias(monkeypatch)` (function)
- L79 `test_create_openai_client_routes_via_proxy_when_env_set(mock_openai, monkeypatch)` (function) — With HTTPS_PROXY set, the custom httpx.Client must mount an HTTPProxy pool.
- L119 `test_create_openai_client_no_proxy_when_env_unset(mock_openai, monkeypatch)` (function) — Without proxy env vars, the keepalive transport must still be installed
- L148 `test_get_proxy_for_base_url_returns_none_when_host_bypassed(monkeypatch)` (function) — NO_PROXY must suppress the proxy for matching base_urls.
- L172 `test_get_proxy_for_base_url_returns_proxy_when_no_proxy_unset(monkeypatch)` (function)
- L181 `test_get_proxy_for_base_url_returns_none_when_proxy_unset(monkeypatch)` (function)
- L192 `test_create_openai_client_bypasses_proxy_for_no_proxy_host(mock_openai, monkeypatch)` (function) — E2E: with HTTPS_PROXY + NO_PROXY=localhost, a local base_url gets a
