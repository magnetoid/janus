---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# plugins/dashboard_auth/self_hosted/__init__.py

Symbols in `plugins/dashboard_auth/self_hosted/__init__.py`.

- L131 `_b64url_no_pad(raw: bytes)` (function) — Base64url-encode without ``=`` padding (RFC 7636 §4).
- L136 `_require_https_or_loopback(url: str, *, field: str)` (function) — Reject an endpoint URL that isn't HTTPS (loopback http is allowed).
- L163 `SelfHostedOIDCProvider` (class) — Generic self-hosted OpenID Connect provider (authorization-code + PKCE).
- L169 `__init__(self, *, issuer: str, client_id: str, scopes: str=_DEFAULT_SCOPES)` (method)
- L200 `start_login(self, *, redirect_uri: str)` (method)
- L229 `complete_login(self, *, code: str, state: str, code_verifier: str, redirect_uri: str)` (method)
- L255 `refresh_session(self, *, refresh_token: str)` (method)
- L276 `verify_session(self, *, access_token: str)` (method)
- L295 `revoke_session(self, *, refresh_token: str)` (method)
- L324 `_exchange(self, token_endpoint: str, data: Dict[str, str], *, bad_request_exc: type[Exception], previous_refresh_token: str='')` (method) — POST the token endpoint and turn the response into a Session.
- L392 `_get_discovery(self)` (method) — Return the cached OIDC discovery document, fetching if stale.
- L415 `_discovery_url(self)` (method)
- L419 `_fetch_discovery(self)` (method)
- L480 `_get_jwks_client(self)` (method)
- L492 `_verify_id_token(self, id_token: str)` (method)
- L545 `_session_from_tokens(self, *, id_token: str, refresh_token: str, claims: Dict[str, Any])` (method) — Map verified OIDC claims onto a Session.
- L593 `_validate_redirect_uri(self, redirect_uri: str)` (method) — Fast-fail obviously-broken redirect_uris before bouncing to the IDP.
- L618 `_parse_json_body(self, response: httpx.Response)` (method)
- L634 `_load_config_oauth_section()` (function) — Return the ``dashboard.oauth`` block from config.yaml, or ``{}``.
- L656 `_oidc_subsection(oauth_section: dict)` (function) — Return the ``dashboard.oauth.self_hosted`` sub-block, or ``{}``.
- L662 `_resolve_setting(env_var: str, cfg_value: Any)` (function) — env-wins-config with empty-is-unset precedence.
- L676 `register(ctx)` (function) — Plugin entry — called by the plugin loader at startup.
