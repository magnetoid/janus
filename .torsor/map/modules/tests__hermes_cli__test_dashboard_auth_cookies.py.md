---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/hermes_cli/test_dashboard_auth_cookies.py

Symbols in `tests/hermes_cli/test_dashboard_auth_cookies.py`.

- L22 `_build_app(use_https: bool=True, prefix: str='')` (function)
- L58 `test_session_cookies_use_host_prefix_on_https_direct()` (function) — HTTPS + no proxy prefix → __Host- prefix (strongest spec
- L73 `test_session_cookies_use_secure_prefix_when_proxied()` (function) — HTTPS + /hermes prefix → __Secure- prefix (__Host- forbids
- L88 `test_session_cookies_use_bare_name_on_http()` (function) — Loopback HTTP dev: __Host- / __Secure- both require Secure, which
- L106 `test_session_cookies_have_30day_rt_and_token_ttl_at()` (function)
- L116 `test_clear_session_cookies_emits_expired_at_and_rt()` (function) — ``clear_session_cookies`` emits Max-Age=0 deletions for every
- L133 `test_pkce_cookie_short_ttl_and_path_root()` (function)
- L146 `test_read_session_cookies_from_request_bare_name()` (function) — Reader accepts the bare name (loopback) by default.
- L163 `test_read_session_cookies_from_request_host_prefix()` (function) — Reader also finds cookies set with the __Host- variant
- L182 `test_read_session_cookies_from_request_secure_prefix()` (function) — Reader also finds cookies set with the __Secure- variant
- L201 `test_read_session_cookies_missing_returns_none()` (function)
- L206 `test_read_pkce_cookie_round_trip()` (function)
- L217 `test_detect_https_via_scheme()` (function) — ``detect_https`` reads from request.url.scheme.
