---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/run_agent/test_fallback_credential_isolation.py

Symbols in `tests/run_agent/test_fallback_credential_isolation.py`.

- L21 `_make_pool(provider, n_entries=1)` (function) — Create a mock credential pool with N entries.
- L38 `_make_agent(provider='openai-codex', model='gpt-5.5', base_url='https://chatgpt.com/backend-api/codex', api_mode='codex_responses')` (function) — Create a minimal AIAgent-like object with just the fields we need.
- L79 `TestFallbackCredentialIsolation` (class) — Test that _try_activate_fallback isolates the credential pool.
- L82 `test_fallback_clears_primary_pool(self)` (method) — When switching from openai-codex to openrouter, the codex pool is cleared.
- L108 `test_fallback_keeps_matching_pool(self)` (method) — When fallback provider matches pool provider, pool is preserved.
- L128 `TestRecoveryProviderGuard` (class) — Test that _recover_with_credential_pool skips mismatched pools.
- L131 `test_recovery_skips_mismatched_pool(self)` (method) — _recover_with_credential_pool should not mutate a pool belonging
- L149 `test_recovery_allows_matching_pool(self)` (method) — When pool and agent provider match, recovery proceeds normally.
- L164 `test_recovery_429_from_zai_does_not_exhaust_codex_pool(self)` (method) — Regression test for GH #33088: zai 429 should NOT exhaust
- L183 `TestBaseUrlLeak` (class) — Regression tests for GH #33163: base_url leaks from primary.
- L186 `test_client_kwargs_base_url_preserved_after_pool_clear(self)` (method) — After fallback activation clears the pool, _client_kwargs should
- L210 `test_swap_credential_does_not_restore_primary_url(self)` (method) — _swap_credential should not be called when pool is None,
