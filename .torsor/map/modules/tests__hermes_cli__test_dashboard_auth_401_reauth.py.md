---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/hermes_cli/test_dashboard_auth_401_reauth.py

Symbols in `tests/hermes_cli/test_dashboard_auth_401_reauth.py`.

- L52 `gated_app()` (function)
- L74 `TestRefreshTokenCookieDeprecation` (class)
- L75 `_build_app(self, *, refresh_token: str)` (method)
- L89 `test_empty_refresh_token_does_not_emit_rt_cookie(self)` (method)
- L99 `test_present_refresh_token_still_emits_rt_cookie(self)` (method)
- L107 `test_clear_session_cookies_still_emits_rt_deletion(self)` (method) — Even when we never wrote the RT cookie, logout/clear should
- L133 `TestApi401Envelope` (class)
- L139 `test_no_cookie_returns_unauthenticated_envelope(self, gated_app)` (method)
- L147 `test_invalid_cookie_returns_session_expired_envelope(self, gated_app)` (method)
- L155 `test_invalid_cookie_clears_dead_cookie(self, gated_app)` (method) — Dead-cookie cleanup — Phase 6 requirement so the browser
- L166 `test_login_url_drops_next_for_deep_api_path(self, gated_app)` (method) — Bug fix: ``/api/*`` paths must NOT round-trip into ``next=``.
- L184 `test_login_url_drops_next_for_analytics_path(self, gated_app)` (method) — Specific repro for the ``/api/analytics/models?days=30``
- L195 `TestTransparentRefreshOnAccessTokenEviction` (class) — Regression: an expired access token whose cookie the browser has
- L216 `_build_rt_only_app(self)` (method) — Gate over the real app with a Stub provider whose RT is live
- L233 `test_at_evicted_rt_present_refreshes_transparently(self, gated_app)` (method)
- L256 `test_no_cookies_at_all_still_bounces(self, gated_app)` (method) — Guard the fix didn't over-reach: a request with NEITHER cookie
- L265 `test_dead_rt_only_bounces_to_login(self, gated_app)` (method) — An RT-only request whose RT is dead/expired must bounce (the
- L284 `TestHtmlRedirectNext` (class)
- L285 `test_deep_html_path_redirects_with_next(self, gated_app)` (method)
- L290 `test_root_path_redirects_with_next(self, gated_app)` (method)
- L294 `test_login_loop_avoided(self, gated_app)` (method) — A request to /login itself must not produce ``?next=/login``
- L302 `test_auth_loop_avoided(self, gated_app)` (method) — A failed cookie on /auth/me (auth-required path) must drop
- L318 `TestNextSameOriginValidation` (class)
- L319 `test_protocol_relative_path_dropped(self, gated_app)` (method)
- L333 `test_safe_next_validator_accepts_same_origin(self)` (method)
- L346 `test_safe_next_validator_rejects_protocol_relative(self)` (method)
- L355 `test_safe_next_validator_rejects_login_loop(self)` (method)
- L366 `test_safe_next_validator_rejects_api_paths(self)` (method) — ``/api/*`` paths must not round-trip through ``next=``.
- L392 `test_safe_next_validator_does_not_reject_api_prefix_lookalikes(self)` (method) — Negative guard: ``/api-docs`` or ``/apis`` aren't ``/api/*``
- L412 `TestAuthCallbackNext` (class) — End-to-end next= propagation through a full OAuth round trip.
- L434 `_drive_oauth_via_login(self, gated_app, *, next_path: str='', expect_next_in_button: bool=True)` (method) — Walk /login → /auth/login → IDP-bounce → /auth/callback like
- L487 `test_callback_without_next_lands_at_root(self, gated_app)` (method)
- L492 `test_callback_with_safe_next_lands_there(self, gated_app)` (method)
- L497 `test_callback_with_query_string_in_next(self, gated_app)` (method)
- L504 `test_callback_rejects_open_redirect(self, gated_app)` (method)
- L517 `test_callback_rejects_login_loop(self, gated_app)` (method)
- L525 `test_attacker_callback_next_param_is_ignored(self, gated_app)` (method) — Hardening: even if an attacker crafts a callback URL with a
- L548 `test_callback_with_api_next_lands_at_root(self, gated_app)` (method) — End-to-end repro of the analytics-redirect bug.
- L583 `TestValidatePostLoginTarget` (class) — Cover ``_validate_post_login_target`` directly — it's the second
- L589 `test_accepts_same_origin_paths(self)` (method)
- L599 `test_rejects_protocol_relative(self)` (method)
- L604 `test_rejects_login_loop(self)` (method)
- L610 `test_rejects_api_paths(self)` (method) — Bug fix: any ``/api/*`` target is dropped at the callback
- L627 `test_does_not_reject_api_prefix_lookalikes(self)` (method)
- L639 `TestRenderLoginHtmlNext` (class) — Cover ``render_login_html`` directly so a regression that drops
- L644 `setup_method(self)` (method)
- L648 `teardown_method(self)` (method)
- L651 `test_no_next_emits_plain_button(self)` (method)
- L657 `test_next_threaded_url_encoded(self)` (method)
- L667 `test_next_with_html_metacharacters_is_escaped(self)` (method) — Defence in depth: even though the caller validates next_path,
- L685 `TestAuthLoginPkceCookieNext` (class) — Cover the ``/auth/login`` route's PKCE cookie payload directly.
- L693 `test_no_next_query_omits_next_segment(self, gated_app)` (method)
- L702 `test_safe_next_query_encoded_into_cookie(self, gated_app)` (method)
- L712 `test_unsafe_next_query_dropped_from_cookie(self, gated_app)` (method) — The validator at /auth/login refuses //evil.com BEFORE
