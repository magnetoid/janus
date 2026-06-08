---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/integration/test_ha_integration.py

Symbols in `tests/integration/test_ha_integration.py`.

- L33 `_adapter_for(server: FakeHAServer, **extra)` (function) — Create an adapter pointed at the fake server.
- L48 `TestGatewayWebSocket` (class)
- L50 `test_connect_auth_subscribe(self)` (method) — Full WS handshake succeeds: auth_required -> auth -> auth_ok -> subscribe -> ACK.
- L62 `test_connect_auth_rejected(self)` (method) — connect() returns False when the server rejects auth.
- L71 `test_event_received_and_forwarded(self)` (method) — Server pushes event -> adapter calls handle_message with correct MessageEvent.
- L106 `test_event_filtering_ignores_unwatched(self)` (method) — Events outside watch_domains are silently dropped.
- L132 `test_disconnect_closes_cleanly(self)` (method) — disconnect() cancels listener and closes WebSocket.
- L153 `TestToolRest` (class) — Call the async tool functions directly against the fake server.
- L164 `test_list_entities_returns_all(self, monkeypatch)` (method) — _async_list_entities returns all entities from the fake server.
- L182 `test_list_entities_domain_filter(self, monkeypatch)` (method) — Domain filter is applied after fetching from server.
- L199 `test_get_state_single_entity(self, monkeypatch)` (method) — _async_get_state returns full entity details.
- L217 `test_get_state_not_found(self, monkeypatch)` (method) — Non-existent entity raises an aiohttp error (404).
- L234 `test_call_service_turn_on(self, monkeypatch)` (method) — _async_call_service sends correct payload and server records it.
- L270 `TestSendNotification` (class)
- L272 `test_send_notification_delivered(self)` (method) — Adapter send() delivers notification to fake server REST endpoint.
- L286 `test_send_auth_failure(self)` (method) — send() returns failure when token is wrong.
- L307 `TestAuthAndErrors` (class)
- L309 `test_rest_unauthorized(self, monkeypatch)` (method) — Async function raises on 401 when token is wrong.
- L326 `test_rest_server_error(self, monkeypatch)` (method) — Async function raises on 500 response.
