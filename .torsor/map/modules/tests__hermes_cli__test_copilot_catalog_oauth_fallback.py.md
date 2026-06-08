---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/hermes_cli/test_copilot_catalog_oauth_fallback.py

Symbols in `tests/hermes_cli/test_copilot_catalog_oauth_fallback.py`.

- L18 `TestCopilotCatalogApiKeyResolution` (class)
- L19 `test_env_var_token_wins_over_pool(self)` (method) — Env-resolved token still short-circuits the pool fallback.
- L30 `test_falls_back_to_pool_oauth_token(self)` (method) — Empty env → walk credential_pool.copilot[] for an OAuth access_token.
- L44 `test_falls_back_when_env_resolution_raises(self)` (method) — Env path raising an exception still falls through to the pool.
- L58 `test_skips_classic_pat_in_pool(self)` (method) — Classic PATs (``ghp_…``) are unsupported by the Copilot API — skip them.
- L72 `test_skips_invalid_pool_entries_until_first_exchangeable(self)` (method) — Non-dict entries and entries without an ``access_token`` are skipped.
- L93 `test_skips_pool_entry_that_fails_to_exchange(self)` (method) — If the first entry won't exchange, try the next — an unsupported pool[0]
- L120 `test_all_pool_entries_fail_exchange_returns_empty(self)` (method) — All exchanges fail → return "" so the caller falls back to curated.
- L137 `test_returns_empty_string_when_no_credentials_anywhere(self)` (method) — No env, no pool → empty string (caller falls back to curated list).
- L148 `test_pool_failure_returns_empty_string(self)` (method) — If the pool read itself raises, swallow and return "".
