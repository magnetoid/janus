---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/hermes_cli/test_web_server_host_header.py

Symbols in `tests/hermes_cli/test_web_server_host_header.py`.

- L22 `TestHostHeaderValidator` (class) — Unit test the _is_accepted_host helper directly — cheaper and
- L26 `test_loopback_bind_accepts_loopback_names(self)` (method)
- L39 `test_loopback_bind_rejects_attacker_hostnames(self)` (method) — The core rebinding defence: attacker-controlled hosts that
- L57 `test_zero_zero_bind_accepts_anything(self)` (method) — 0.0.0.0 means operator explicitly opted into all-interfaces
- L67 `test_explicit_non_loopback_bind_requires_exact_match(self)` (method) — If the operator bound to a specific non-loopback hostname,
- L79 `test_case_insensitive_comparison(self)` (method) — Host headers are case-insensitive per RFC — accept variations.
- L87 `TestHostHeaderMiddleware` (class) — End-to-end test via the FastAPI app — verify the middleware
- L91 `test_rebinding_request_rejected(self)` (method)
- L112 `test_legit_loopback_request_accepted(self)` (method)
- L134 `test_no_bound_host_skips_validation(self)` (method) — If app.state.bound_host isn't set (e.g. running under test
- L151 `TestWebSocketHostOriginGuard` (class) — WebSocket upgrades must enforce the same dashboard boundary as HTTP.
- L154 `test_rebinding_websocket_host_is_rejected(self, monkeypatch)` (method)
- L177 `test_rebinding_websocket_origin_is_rejected(self, monkeypatch)` (method)
- L200 `test_loopback_websocket_host_and_origin_are_accepted(self, monkeypatch)` (method)
