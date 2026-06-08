---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/hermes_cli/test_dashboard_auth_middleware.py

Symbols in `tests/hermes_cli/test_dashboard_auth_middleware.py`.

- L34 `gated_app()` (function) — Configure web_server.app for gated mode + register the stub provider.
- L59 `test_gated_status_is_public(gated_app)` (function) — ``/api/status`` MUST be public under the OAuth gate.
- L93 `test_other_public_api_paths_are_public_under_gate(gated_app, path)` (function) — The remaining ``PUBLIC_API_PATHS`` entries must also bypass the
- L116 `test_gated_html_redirects_to_login(gated_app)` (function)
- L123 `test_gated_auth_providers_is_public(gated_app)` (function)
- L131 `test_gated_login_html_is_public_and_lists_providers(gated_app)` (function)
- L139 `test_gated_static_asset_path_is_public(gated_app)` (function) — ``/assets/*`` is allowlisted so the SPA's CSS/JS loads pre-login.
- L152 `test_full_login_round_trip_unlocks_gated_api(gated_app)` (function)
- L194 `test_login_unknown_provider_returns_404(gated_app)` (function)
- L199 `test_callback_without_pkce_cookie_returns_400(gated_app)` (function)
- L208 `test_callback_state_mismatch_returns_400(gated_app)` (function)
- L219 `test_callback_invalid_code_returns_400(gated_app)` (function)
- L234 `test_invalid_cookie_returns_401_on_api(gated_app)` (function)
- L240 `test_invalid_cookie_redirects_on_html(gated_app)` (function)
- L248 `test_logout_clears_cookies_and_redirects_to_login(gated_app)` (function)
- L276 `test_api_auth_me_returns_session_after_login(gated_app)` (function)
- L294 `test_api_auth_me_requires_auth(gated_app)` (function)
- L305 `test_gated_zero_providers_fails_closed_on_api_auth_providers()` (function) — If gate is on but no providers are registered, /api/auth/providers 503s.
- L322 `test_gated_zero_providers_login_page_renders_help_text()` (function)
- L351 `_UnreachableProvider` (class) — A provider whose IDP is unreachable: verify_session always raises.
- L363 `verify_session(self, *, access_token: str)` (method)
- L368 `refresh_session(self, *, refresh_token: str)` (method)
- L374 `_mint_stub_at(stub: StubAuthProvider)` (function) — Mint a valid access-token cookie value from a StubAuthProvider via its
- L398 `_gated_state()` (function) — Bare gated app-state setup WITHOUT registering any provider, so each
- L420 `test_unreachable_first_provider_does_not_block_second(_gated_state)` (function) — An unreachable provider registered FIRST must not 503 a request whose
- L445 `test_all_providers_unreachable_returns_503(_gated_state)` (function) — If NO provider can verify the token AND at least one was unreachable,
- L457 `test_unverifiable_token_with_reachable_providers_redirects(_gated_state)` (function) — When every provider is REACHABLE but none recognises the token (all
