---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/run_agent/test_provider_fallback.py

Symbols in `tests/run_agent/test_provider_fallback.py`.

- L13 `_make_agent(fallback_model=None)` (function) — Create a minimal AIAgent with optional fallback config.
- L32 `_mock_client(base_url='https://openrouter.ai/api/v1', api_key='fb-key')` (function)
- L42 `TestFallbackChainInit` (class)
- L43 `test_no_fallback(self)` (method)
- L49 `test_single_dict_backwards_compat(self)` (method)
- L55 `test_list_of_providers(self)` (method)
- L64 `test_invalid_entries_filtered(self)` (method)
- L75 `test_empty_list(self)` (method)
- L80 `test_invalid_dict_no_provider(self)` (method)
- L88 `TestFallbackChainAdvancement` (class)
- L89 `test_exhausted_returns_false(self)` (method)
- L93 `test_advances_index(self)` (method)
- L106 `test_second_fallback_works(self)` (method)
- L120 `test_all_exhausted_returns_false(self)` (method)
- L128 `test_skips_unconfigured_provider_to_next(self)` (method) — If resolve_provider_client returns None, skip to next in chain.
- L144 `test_skips_provider_that_raises_to_next(self)` (method) — If resolve_provider_client raises, skip to next in chain.
- L159 `test_resolves_key_env_for_fallback_provider(self)` (method)
- L189 `_pool(n_entries: int, has_available: bool=True)` (function) — Make a minimal credential-pool stand-in for rotation-room checks.
- L197 `TestPoolRotationRoom` (class)
- L198 `test_none_pool_returns_false(self)` (method)
- L201 `test_single_credential_returns_false(self)` (method) — With one credential that just 429'd, rotation has nowhere to go.
- L210 `test_single_credential_in_cooldown_returns_false(self)` (method)
- L213 `test_two_credentials_available_returns_true(self)` (method) — With >1 credentials and at least one available, rotate instead of fallback.
- L217 `test_multiple_credentials_all_in_cooldown_returns_false(self)` (method) — All credentials cooling down — fall back rather than wait.
- L221 `test_many_credentials_available_returns_true(self)` (method)
- L228 `TestFallbackChainDedup` (class) — A fallback chain entry that resolves to the current provider/model
- L234 `test_skips_entry_matching_current_provider_and_model(self)` (method) — Chain has [same-as-current, real-fallback]; activate must skip
- L264 `test_skips_entry_matching_current_base_url_and_model(self)` (method) — Two custom_providers entries pointing at the same shim URL
- L293 `test_returns_false_when_only_self_matching_entries(self)` (method) — A chain with only self-matching entries exhausts to False.
