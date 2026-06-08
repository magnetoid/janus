---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/hermes_cli/test_dashboard_auth_password_login.py

Symbols in `tests/hermes_cli/test_dashboard_auth_password_login.py`.

- L47 `_sign(secret: bytes, sub: str, kind: str, ttl: int)` (function)
- L61 `_unsign(secret: bytes, token: str)` (function)
- L79 `PasswordProvider` (class) — In-test username/password provider (admin / hunter2).
- L86 `__init__(self, *, ttl: int=3600, secret: bytes=b'test-secret-1234567890')` (method)
- L91 `start_login(self, *, redirect_uri: str)` (method)
- L94 `complete_login(self, **kwargs)` (method)
- L97 `complete_password_login(self, *, username: str, password: str)` (method)
- L114 `verify_session(self, *, access_token: str)` (method)
- L124 `refresh_session(self, *, refresh_token: str)` (method)
- L138 `revoke_session(self, *, refresh_token: str)` (method)
- L148 `pw_provider()` (function)
- L153 `gated_app(pw_provider)` (function)
- L177 `TestProtocolExtension` (class)
- L178 `test_password_provider_is_protocol_compliant(self)` (method)
- L181 `test_default_supports_password_is_false(self)` (method)
- L185 `test_default_complete_password_login_raises_not_implemented(self)` (method)
- L199 `TestProviderListFlag` (class)
- L200 `test_providers_endpoint_reports_supports_password(self, gated_app)` (method)
- L206 `test_oauth_provider_reports_false(self)` (method)
- L228 `TestPasswordLoginRoute` (class)
- L229 `test_valid_credentials_set_session_cookies_and_return_next(self, gated_app)` (method)
- L248 `test_session_cookie_then_grants_authenticated_access(self, gated_app)` (method)
- L262 `test_wrong_password_returns_generic_401(self, gated_app)` (method)
- L272 `test_unknown_user_returns_same_generic_401(self, gated_app)` (method)
- L280 `test_unknown_provider_returns_404(self, gated_app)` (method)
- L287 `test_oauth_provider_rejects_password_login_with_404(self)` (method)
- L310 `test_provider_unreachable_returns_503(self, gated_app, pw_provider)` (method)
- L318 `test_open_redirect_next_is_dropped(self, gated_app)` (method)
- L332 `test_route_is_public_unauthenticated(self, gated_app)` (method)
- L347 `TestPasswordSessionRefresh` (class)
- L348 `test_expired_access_token_refreshes_via_rt_cookie(self)` (method)
- L383 `TestRateLimit` (class)
- L384 `test_repeated_failures_eventually_429(self, gated_app)` (method)
- L407 `TestLoginPageRender` (class)
- L408 `test_password_provider_renders_credential_form_and_script(self)` (method)
- L422 `test_oauth_only_page_stays_script_free(self)` (method)
- L437 `test_mixed_providers_render_both(self)` (method)
