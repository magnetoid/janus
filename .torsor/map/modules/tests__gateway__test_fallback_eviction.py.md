---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_fallback_eviction.py

Symbols in `tests/gateway/test_fallback_eviction.py`.

- L15 `TestFallbackEvictionGating` (class) — The fallback-eviction code path should skip eviction on failed runs.
- L18 `test_failed_run_does_not_evict_cached_agent(self)` (method) — When result has failed=True, the cached agent should NOT be evicted.
- L26 `test_successful_run_allows_eviction(self)` (method) — When result is successful, fallback eviction should proceed.
- L32 `test_none_result_treated_as_not_failed(self)` (method) — When result is None (edge case), treat as not-failed.
- L38 `test_missing_failed_key_treated_as_not_failed(self)` (method) — When result dict doesn't have 'failed' key, treat as not-failed.
