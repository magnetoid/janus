---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/hermes_cli/test_dashboard_auth_gate.py

Symbols in `tests/hermes_cli/test_dashboard_auth_gate.py`.

- L20 `client_loopback()` (function)
- L35 `test_loopback_status_is_public(client_loopback)` (function) — `/api/status` must remain reachable without a token in loopback mode.
- L43 `test_loopback_protected_route_requires_token(client_loopback)` (function) — Any non-public /api/ route must require the session token.
- L50 `test_loopback_protected_route_accepts_session_token(client_loopback)` (function) — The injected SPA token unlocks protected /api/ routes.
- L63 `test_loopback_index_injects_session_token(client_loopback)` (function) — Loopback mode keeps injecting the SPA token into index.html.
- L75 `test_loopback_host_header_validation_still_enforced(client_loopback)` (function) — DNS-rebinding protection: a foreign Host header is rejected.
- L98 `test_should_require_auth_truth_table(host, allow_public, expected)` (function)
- L108 `_stub_uvicorn_run(monkeypatch)` (function) — Replace uvicorn.run with a no-op recorder so start_server returns
- L123 `test_start_server_loopback_sets_auth_required_false(monkeypatch)` (function) — Loopback bind: app.state.auth_required is False after start_server.
- L135 `test_start_server_insecure_public_sets_auth_required_false(monkeypatch)` (function) — ``--insecure`` (allow_public=True) on a public host: gate stays OFF.
- L146 `test_start_server_public_without_insecure_records_auth_required(monkeypatch)` (function) — Public bind without --insecure: the gate engages and auth_required=True.
- L170 `test_start_server_gate_with_provider_proceeds_and_sets_proxy_headers(monkeypatch)` (function) — With at least one provider, public bind + no --insecure starts the server.
- L197 `test_start_server_gate_without_provider_fails_closed(monkeypatch)` (function) — No providers + gate would activate → SystemExit with a clear message.
- L211 `test_start_server_surfaces_nous_skip_reason_when_unconfigured(monkeypatch)` (function) — When the bundled Nous plugin loaded but skipped registration (no
- L241 `test_start_server_loopback_keeps_proxy_headers_off(monkeypatch)` (function) — Loopback bind: proxy_headers stays False (no TLS terminator in front).
- L251 `test_start_server_insecure_keeps_proxy_headers_off(monkeypatch)` (function) — --insecure: gate stays off, proxy_headers stays off.
