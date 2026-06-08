---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/hermes_cli/test_dashboard_auth_ws_auth.py

Symbols in `tests/hermes_cli/test_dashboard_auth_ws_auth.py`.

- L45 `gated_app()` (function) — web_server.app configured for gated mode + stub provider registered.
- L66 `loopback_app()` (function) — web_server.app configured for loopback mode (gate OFF).
- L85 `insecure_public_app()` (function) — web_server.app configured for all-interfaces insecure mode.
- L103 `_logged_in(client: TestClient)` (function) — Drive the stub OAuth round trip so the client holds session cookies.
- L119 `TestWsTicketEndpoint` (class)
- L120 `test_authenticated_session_can_mint(self, gated_app)` (method)
- L130 `test_unauthenticated_returns_401_or_redirect(self, gated_app)` (method)
- L136 `test_each_call_returns_a_distinct_ticket(self, gated_app)` (method)
- L142 `test_get_method_is_not_allowed(self, gated_app)` (method)
- L167 `insecure_explicit_host_app()` (function) — web_server.app bound to an explicit non-loopback host (--insecure).
- L190 `_fake_ws(*, query: dict, client_host: str='127.0.0.1', path: str='/api/pty')` (function) — Build a stand-in for starlette.WebSocket good enough for _ws_auth_ok.
- L207 `TestWsAuthOkLoopback` (class) — Gate OFF — legacy token path.
- L210 `test_correct_token_accepted(self, loopback_app)` (method)
- L214 `test_wrong_token_rejected(self, loopback_app)` (method)
- L218 `test_missing_token_rejected(self, loopback_app)` (method)
- L222 `test_ticket_param_ignored_in_loopback(self, loopback_app)` (method)
- L230 `TestWsAuthOkGated` (class) — Gate ON — ticket path only.
- L233 `test_valid_ticket_accepted(self, gated_app)` (method)
- L238 `test_consumed_ticket_rejected(self, gated_app)` (method)
- L246 `test_unknown_ticket_rejected(self, gated_app)` (method)
- L250 `test_missing_ticket_rejected(self, gated_app)` (method)
- L254 `test_legacy_token_rejected_in_gated_mode(self, gated_app)` (method) — Critical: gated mode must NOT honour the legacy token path
- L261 `test_rejection_audit_logs(self, gated_app, tmp_path, monkeypatch)` (method)
- L283 `test_internal_credential_accepted(self, gated_app)` (method) — Server-spawned children present the process-lifetime internal
- L290 `test_internal_credential_is_multi_use(self, gated_app)` (method) — Unlike single-use tickets, the internal credential survives
- L298 `test_wrong_internal_credential_rejected(self, gated_app)` (method)
- L304 `test_internal_credential_not_accepted_in_loopback(self, loopback_app)` (method) — Outside gated mode, ?internal= is meaningless — only ?token= works.
- L312 `TestWsRequestIsAllowedGated` (class) — Bug fix: in gated mode, the WS peer-IP loopback check must be
- L331 `test_non_loopback_peer_allowed_in_gated_mode(self, gated_app)` (method)
- L338 `test_non_loopback_peer_rejected_in_loopback_mode(self, loopback_app)` (method) — Loopback mode still enforces the peer-IP guard — the legacy
- L346 `test_loopback_peer_allowed_in_loopback_mode(self, loopback_app)` (method)
- L351 `test_non_loopback_peer_allowed_in_insecure_public_mode(self, insecure_public_app)` (method) — `--host 0.0.0.0 --insecure` is an explicit LAN/public opt-in.
- L366 `test_peer_allowed_on_explicit_non_loopback_bind(self, insecure_explicit_host_app)` (method) — `--host 100.64.0.10 --insecure` (Tailscale/LAN IP) is an explicit
- L381 `test_rebinding_host_rejected_on_explicit_non_loopback_bind(self, insecure_explicit_host_app)` (method) — Lifting the peer-IP gate for an explicit bind must NOT lift the
- L393 `test_host_origin_guard_still_runs_in_gated_mode(self, gated_app)` (method) — Bypassing the peer-IP check must not bypass the DNS-rebinding
- L402 `TestWsHostOriginGuardOrigins` (class) — The WS Origin guard must let the packaged desktop shell connect.
- L418 `_ws(self, *, origin, host)` (method)
- L423 `test_loopback_file_origin_allowed(self, loopback_app)` (method)
- L427 `test_loopback_null_origin_allowed(self, loopback_app)` (method)
- L431 `test_loopback_app_scheme_origin_allowed(self, loopback_app)` (method)
- L435 `test_loopback_matching_http_origin_allowed(self, loopback_app)` (method)
- L440 `test_loopback_cross_site_http_origin_rejected(self, loopback_app)` (method)
- L446 `test_explicit_non_loopback_file_origin_allowed(self, insecure_explicit_host_app)` (method) — Packaged Hermes Desktop also uses file:// when connecting to a
- L456 `test_explicit_non_loopback_null_origin_allowed(self, insecure_explicit_host_app)` (method)
- L460 `test_explicit_non_loopback_cross_site_http_origin_rejected(self, insecure_explicit_host_app)` (method)
- L466 `test_gated_file_origin_allowed(self, gated_app)` (method)
- L477 `test_gated_null_origin_allowed(self, gated_app)` (method)
- L481 `test_gated_app_scheme_origin_allowed(self, gated_app)` (method)
- L485 `test_gated_cross_site_http_origin_still_host_checked(self, gated_app)` (method)
- L492 `test_gated_same_host_https_origin_allowed(self, gated_app)` (method)
- L497 `TestSidecarUrl` (class)
- L498 `test_loopback_uses_session_token(self, loopback_app)` (method)
- L504 `test_gated_uses_internal_credential(self, gated_app)` (method)
- L519 `test_no_bound_host_returns_none(self, gated_app)` (method)
- L534 `TestGatewayWsUrl` (class)
- L535 `test_loopback_uses_session_token(self, loopback_app)` (method)
- L542 `test_gated_uses_internal_credential(self, gated_app)` (method)
- L554 `test_gated_credential_matches_sidecar(self, gated_app)` (method) — Both server-internal builders share one process credential, so a
- L564 `test_no_bound_host_returns_none(self, gated_app)` (method)
