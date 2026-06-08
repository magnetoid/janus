---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/fakes/fake_ha_server.py

Symbols in `tests/fakes/fake_ha_server.py`.

- L77 `FakeHAServer` (class) — In-process fake Home Assistant for integration tests.
- L86 `__init__(self, token: str='test-token-123')` (method)
- L110 `url(self)` (method) — Base URL of the running server, e.g. ``http://127.0.0.1:12345``.
- L117 `push_event(self, event_data: Dict[str, Any])` (method) — Enqueue a state_changed event for delivery over WebSocket.
- L123 `start(self)` (method)
- L128 `stop(self)` (method)
- L137 `__aenter__(self)` (method)
- L141 `__aexit__(self, *exc)` (method)
- L146 `_build_app(self)` (method)
- L165 `_check_rest_auth(self, request: web.Request)` (method) — Return a 401 response if the Bearer token is wrong, else None.
- L176 `_handle_ws(self, request: web.Request)` (method)
- L236 `_handle_get_states(self, request: web.Request)` (method)
- L242 `_handle_get_state(self, request: web.Request)` (method)
- L252 `_handle_notification(self, request: web.Request)` (method)
- L260 `_handle_call_service(self, request: web.Request)` (method)
