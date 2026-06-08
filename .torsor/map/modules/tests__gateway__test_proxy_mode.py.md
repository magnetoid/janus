---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_proxy_mode.py

Symbols in `tests/gateway/test_proxy_mode.py`.

- L13 `_make_runner(proxy_url=None)` (function) — Create a minimal GatewayRunner for proxy tests.
- L27 `_make_source(platform=Platform.MATRIX)` (function)
- L39 `_FakeSSEResponse` (class) — Simulates an aiohttp response with SSE streaming.
- L42 `__init__(self, status=200, sse_chunks=None, error_text='')` (method)
- L48 `text(self)` (method)
- L51 `iter_any(self)` (method)
- L57 `__aenter__(self)` (method)
- L60 `__aexit__(self, *args)` (method)
- L64 `_FakeSession` (class) — Simulates an aiohttp.ClientSession with captured request args.
- L67 `__init__(self, response)` (method)
- L73 `post(self, url, json=None, headers=None, **kwargs)` (method)
- L79 `__aenter__(self)` (method)
- L82 `__aexit__(self, *args)` (method)
- L86 `_patch_aiohttp(session)` (function) — Patch aiohttp.ClientSession to return our fake session.
- L94 `TestGetProxyUrl` (class) — Test _get_proxy_url() config resolution.
- L97 `test_returns_none_when_not_configured(self, monkeypatch)` (method)
- L103 `test_reads_from_env_var(self, monkeypatch)` (method)
- L108 `test_strips_trailing_slash(self, monkeypatch)` (method)
- L113 `test_reads_from_config_yaml(self, monkeypatch)` (method)
- L120 `test_env_var_overrides_config(self, monkeypatch)` (method)
- L127 `test_empty_string_treated_as_unset(self, monkeypatch)` (method)
- L134 `TestResolveProxyUrl` (class)
- L135 `test_normalizes_socks_alias_from_all_proxy(self, monkeypatch)` (method)
- L142 `test_no_proxy_bypasses_matching_host(self, monkeypatch)` (method)
- L151 `test_no_proxy_bypasses_cidr_target(self, monkeypatch)` (method)
- L160 `test_no_proxy_ignored_without_target(self, monkeypatch)` (method)
- L170 `TestRunAgentProxyDispatch` (class) — Test that _run_agent() delegates to proxy when configured.
- L174 `test_run_agent_delegates_to_proxy(self, monkeypatch)` (method)
- L206 `test_run_agent_skips_proxy_when_not_configured(self, monkeypatch)` (method)
- L227 `TestRunAgentViaProxy` (class) — Test the actual proxy HTTP forwarding logic.
- L231 `test_builds_correct_request(self, monkeypatch)` (method)
- L284 `test_handles_http_error(self, monkeypatch)` (method)
- L308 `test_handles_connection_error(self, monkeypatch)` (method)
- L338 `test_skips_tool_messages_in_history(self, monkeypatch)` (method)
- L376 `test_result_shape_matches_run_agent(self, monkeypatch)` (method)
- L411 `test_proxy_stale_generation_returns_empty_result(self, monkeypatch)` (method)
- L445 `test_no_auth_header_without_key(self, monkeypatch)` (method)
- L471 `test_no_system_message_when_context_empty(self, monkeypatch)` (method)
- L501 `TestEnvVarRegistration` (class) — Verify GATEWAY_PROXY_URL and GATEWAY_PROXY_KEY are registered.
- L504 `test_proxy_url_in_optional_env_vars(self)` (method)
- L511 `test_proxy_key_in_optional_env_vars(self)` (method)
