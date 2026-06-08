---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# hermes_cli/dashboard_auth/middleware.py

Symbols in `hermes_cli/dashboard_auth/middleware.py`.

- L53 `_path_is_public(path: str)` (function) — True if ``path`` bypasses the OAuth auth gate.
- L74 `_client_ip(request: Request)` (function)
- L81 `_unauth_response(request: Request, *, reason: str)` (function) — API routes → 401 JSON with ``login_url``; HTML routes → 302 → /login.
- L135 `_safe_next_target(request: Request)` (function) — Build the URL-encoded ``next`` query value, or empty string.
- L172 `gated_auth_middleware(request: Request, call_next: Callable[[Request], Awaitable[Response]])` (function) — Engaged only when ``app.state.auth_required is True``.
- L313 `_expires_in_seconds(session)` (function) — Seconds until the access token's ``exp``, floored at 60.
- L326 `_attempt_refresh(request: Request, *, refresh_token)` (function) — Try to rotate an expired session via the refresh token.
