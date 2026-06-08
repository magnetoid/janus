---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/tools/test_mcp_preflight_content_type.py

Symbols in `tests/tools/test_mcp_preflight_content_type.py`.

- L25 `_make_task(name: str='probe_srv')` (function) — Minimal MCPServerTask without running the heavy __init__.
- L33 `_serve(handler_cls)` (function) — Run *handler_cls* on a background thread; yield its base URL.
- L47 `_handler(status: int=200, content_type: 'str | None'='text/html; charset=utf-8', body: bytes=b'<html>x</html>', head_status=None, record=None)` (function) — Build a BaseHTTPRequestHandler that replies with the given shape.
- L95 `test_non_mcp_content_type_raises(content_type)` (function)
- L105 `test_non_mcp_error_is_non_retryable_connection_error()` (function) — NonMcpEndpointError must subclass ConnectionError (retry loop skips it
- L121 `test_valid_mcp_content_types_pass(content_type)` (function)
- L128 `test_missing_content_type_passes()` (function)
- L135 `test_non_2xx_responses_pass(status)` (function) — 4xx/5xx are auth challenges or transient errors — let the SDK handle.
- L142 `test_network_error_passes()` (function) — A connection failure (nothing listening) must pass through, not raise.
- L156 `test_cancelled_error_is_not_swallowed()` (function) — The best-effort except must NOT catch CancelledError (BaseException).
- L182 `test_head_405_falls_back_to_get_and_rejects_html()` (function)
- L194 `test_head_501_falls_back_to_get_and_passes_json()` (function)
- L209 `test_ssl_verify_and_cert_forwarded(monkeypatch)` (function)
