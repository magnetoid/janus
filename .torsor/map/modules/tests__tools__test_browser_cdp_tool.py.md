---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/tools/test_browser_cdp_tool.py

Symbols in `tests/tools/test_browser_cdp_tool.py`.

- L28 `_CDPServer` (class) — A tiny CDP-over-WebSocket mock.
- L36 `__init__(self)` (method)
- L47 `on(self, method: str, handler)` (method) — Register a handler ``handler(params, session_id) -> dict or Exception``.
- L53 `start(self)` (method)
- L114 `stop(self)` (method)
- L123 `received(self)` (method)
- L133 `cdp_server(monkeypatch)` (function) — Start a CDP mock and route tool resolution to it.
- L151 `test_missing_method_returns_error()` (function)
- L158 `test_non_string_method_returns_error()` (function)
- L164 `test_non_dict_params_returns_error(monkeypatch)` (function)
- L180 `test_no_endpoint_returns_helpful_error(monkeypatch)` (function)
- L188 `test_non_ws_endpoint_returns_error(monkeypatch)` (function)
- L197 `test_websockets_missing_returns_error(monkeypatch)` (function)
- L209 `test_browser_level_success(cdp_server)` (function)
- L231 `test_empty_params_sends_empty_object(cdp_server)` (function)
- L242 `test_target_attach_then_call(cdp_server)` (function)
- L278 `test_cdp_method_error_returns_tool_error(cdp_server)` (function)
- L288 `test_attach_failure_returns_tool_error(cdp_server)` (function)
- L306 `test_timeout_when_server_never_replies(cdp_server)` (function)
- L327 `test_timeout_clamped_above_max(cdp_server)` (function)
- L336 `test_invalid_timeout_falls_back_to_default(cdp_server)` (function)
- L349 `test_registered_in_browser_toolset()` (function)
- L364 `test_dispatch_through_registry(cdp_server)` (function)
- L381 `test_check_fn_false_when_no_cdp_url(monkeypatch)` (function) — Gate closes when no CDP URL is set — even if the browser toolset is
- L391 `test_check_fn_true_when_cdp_url_set(monkeypatch)` (function) — Gate opens as soon as a CDP URL is resolvable.
- L402 `test_check_fn_false_when_browser_requirements_fail(monkeypatch)` (function) — Even with a CDP URL, gate closes if the overall browser toolset is
