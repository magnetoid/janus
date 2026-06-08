---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/run_agent/test_anthropic_third_party_oauth_guard.py

Symbols in `tests/run_agent/test_anthropic_third_party_oauth_guard.py`.

- L34 `agent()` (function) — Minimal AIAgent construction, skipping tool discovery.
- L52 `TestOAuthFlagOnRefresh` (class) — Site 3 — _try_refresh_anthropic_client_credentials.
- L55 `test_third_party_provider_refresh_is_noop(self, agent)` (method) — Refresh path returns False immediately when provider != anthropic — the
- L79 `test_native_anthropic_preserves_existing_oauth_behaviour(self, agent)` (method) — Regression: native anthropic with OAuth token still flips flag to True.
- L99 `TestOAuthFlagOnCredentialSwap` (class) — Site 4 — _swap_credential (credential pool rotation).
- L102 `test_pool_swap_on_third_party_never_flips_oauth(self, agent)` (method)
- L121 `TestOAuthFlagOnConstruction` (class) — Site 1 — AIAgent.__init__ on a third-party anthropic_messages provider.
- L124 `test_minimax_init_does_not_flip_oauth(self)` (method)
- L152 `TestOAuthFlagOnFallbackActivation` (class) — Site 5 — _try_activate_fallback targeting a third-party Anthropic endpoint.
- L155 `test_fallback_to_third_party_does_not_flip_oauth(self, agent)` (method) — Directly mimic the post-fallback assignment at line ~6537.
- L170 `TestApiKeyTokensAlwaysSafe` (class) — Regression: plain API-key shapes must always resolve to non-OAuth, any provider.
- L173 `test_native_anthropic_with_api_key_token(self)` (method)
- L177 `test_third_party_key_shape(self)` (method)
