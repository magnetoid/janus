---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# plugins/dashboard_auth/nous/__init__.py

Symbols in `plugins/dashboard_auth/nous/__init__.py`.

- L143 `_b64url_no_pad(raw: bytes)` (function) — Base64url-encode without ``=`` padding (RFC 7636 §4).
- L153 `NousDashboardAuthProvider` (class) — Nous Portal OAuth via authorization-code + PKCE (S256).
- L159 `__init__(self, *, client_id: str, portal_url: str)` (method)
- L179 `start_login(self, *, redirect_uri: str)` (method)
- L207 `complete_login(self, *, code: str, state: str, code_verifier: str, redirect_uri: str)` (method)
- L244 `refresh_session(self, *, refresh_token: str)` (method) — Rotate the access token using the refresh token.
- L304 `_token_response_to_session(self, response: httpx.Response, *, bad_request_exc: type[Exception])` (method) — Translate a Portal ``/api/oauth/token`` response into a Session.
- L350 `verify_session(self, *, access_token: str)` (method)
- L368 `revoke_session(self, *, refresh_token: str)` (method)
- L384 `_validate_redirect_uri(self, redirect_uri: str)` (method) — Surface obviously-broken redirect_uris before bouncing to Portal.
- L405 `_parse_json_body(self, response: httpx.Response)` (method)
- L415 `_get_jwks_client(self)` (method)
- L426 `_verify_jwt(self, access_token: str)` (method)
- L483 `_check_agent_instance_id(self, claims: Dict[str, Any])` (method) — Contract C9: cross-check agent_instance_id against our config.
- L497 `_check_contract_version(self, claims: Dict[str, Any])` (method) — Contract C11 — tolerant treatment per OQ-C2.
- L513 `_session_from_claims(self, access_token: str, refresh_token: str, claims: Dict[str, Any])` (method)
- L541 `_load_config_oauth_section()` (function) — Return the ``dashboard.oauth`` block from ``config.yaml`` if it
- L566 `_resolve_client_id()` (function) — Resolve the OAuth client_id with env-overrides-config precedence.
- L584 `_resolve_portal_url()` (function) — Resolve the Portal URL with env-overrides-config precedence.
- L601 `register(ctx)` (function) — Plugin entry — called by the plugin loader at startup.
