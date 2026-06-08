---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# hermes_cli/dashboard_auth/cookies.py

Symbols in `hermes_cli/dashboard_auth/cookies.py`.

- L87 `_resolved_name(bare: str, *, use_https: bool, prefix: str)` (function) — Pick the cookie-prefix variant for the active request shape.
- L102 `_cookie_path(prefix: str)` (function) — Cookie ``Path`` attribute for the active deploy shape.
- L117 `_common_attrs(*, use_https: bool, prefix: str)` (function)
- L128 `set_session_cookies(response: Response, *, access_token: str, refresh_token: str, access_token_expires_in: int, use_https: bool, prefix: str='')` (function) — Set the session cookies on the response.
- L170 `clear_session_cookies(response: Response, *, prefix: str='')` (function) — Emit Max-Age=0 deletions for both session cookies.
- L191 `set_pkce_cookie(response: Response, *, payload: str, use_https: bool, prefix: str='')` (function)
- L202 `clear_pkce_cookie(response: Response, *, prefix: str='')` (function)
- L211 `_read_with_fallback(request: Request, bare_name: str)` (function) — Read a cookie by checking every prefix variant in order.
- L228 `read_session_cookies(request: Request)` (function) — Returns (access_token, refresh_token), either may be None.
- L235 `read_pkce_cookie(request: Request)` (function)
- L239 `detect_https(request: Request)` (function) — Decide whether to set the ``Secure`` cookie flag.
