---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# hermes_cli/dashboard_auth/routes.py

Symbols in `hermes_cli/dashboard_auth/routes.py`.

- L54 `_redirect_uri(request: Request)` (function) — Reconstruct the absolute callback URL the IDP redirects back to.
- L106 `_client_ip(request: Request)` (function)
- L113 `_prefix(request: Request)` (function) — Resolve the X-Forwarded-Prefix header for the active request.
- L131 `login_page(request: Request)` (function)
- L151 `api_auth_providers()` (function)
- L179 `auth_login(request: Request, provider: str, next: str='')` (function)
- L232 `auth_callback(request: Request, code: str='', state: str='', error: str='', error_description: str='')` (function)
- L356 `_validate_post_login_target(raw: str)` (function) — Return ``raw`` if it's a safe same-origin path, else empty string.
- L410 `_password_rate_limited(ip: str)` (function) — True if ``ip`` has exceeded the password-login attempt budget.
- L432 `_reset_password_rate_limit()` (function) — Test-only: clear all rate-limit buckets.
- L438 `_PasswordLoginBody` (class)
- L446 `auth_password_login(request: Request, body: _PasswordLoginBody)` (function) — Authenticate a username/password against a password provider.
- L537 `auth_logout(request: Request)` (function)
- L573 `api_auth_me(request: Request)` (function) — Return the verified session as JSON. Auth-required (gate enforces).
- L594 `api_auth_ws_ticket(request: Request)` (function) — Mint a short-lived single-use ticket for the authenticated session.
