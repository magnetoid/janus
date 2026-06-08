---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:44'
updated: '2026-06-08T00:38:44'
---

# tools/microsoft_graph_auth.py

Symbols in `tools/microsoft_graph_auth.py`.

- L19 `MicrosoftGraphAuthError` (class) — Base class for Microsoft Graph auth failures.
- L23 `MicrosoftGraphConfigError` (class) — Raised when Graph credentials are missing or invalid.
- L27 `MicrosoftGraphTokenError` (class) — Raised when token acquisition fails.
- L32 `GraphCredentials` (class) — Normalized Microsoft Graph app-only credentials.
- L42 `token_url(self)` (method)
- L48 `from_env(cls, environ: dict[str, str] | None=None, *, required: bool=True)` (method)
- L89 `CachedAccessToken` (class) — Cached app-only Graph access token.
- L96 `is_expired(self, *, skew_seconds: int=DEFAULT_TOKEN_SKEW_SECONDS)` (method)
- L100 `expires_in_seconds(self)` (method)
- L104 `MicrosoftGraphTokenProvider` (class) — Acquire and cache Microsoft Graph app-only access tokens.
- L107 `__init__(self, credentials: GraphCredentials, *, timeout: float=20.0, skew_seconds: int=DEFAULT_TOKEN_SKEW_SECONDS, transport: httpx.AsyncBaseTransport | None=None)` (method)
- L123 `from_env(cls, environ: dict[str, str] | None=None, **kwargs: Any)` (method)
- L131 `clear_cache(self)` (method)
- L134 `inspect_token_health(self)` (method)
- L149 `get_access_token(self, *, force_refresh: bool=False)` (method)
- L167 `_fetch_access_token(self)` (method)
- L223 `_extract_error_detail(response: httpx.Response)` (function)
