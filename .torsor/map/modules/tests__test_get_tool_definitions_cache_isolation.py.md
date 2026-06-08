---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/test_get_tool_definitions_cache_isolation.py

Symbols in `tests/test_get_tool_definitions_cache_isolation.py`.

- L25 `_clear_cache()` (function) — Each test starts with an empty quiet_mode cache.
- L32 `TestQuietModeCacheIsolation` (class)
- L34 `test_first_uncached_call_returns_fresh_list(self)` (method) — The first quiet_mode call must not alias the cached object —
- L47 `test_cache_hit_returns_fresh_list(self)` (method) — The cache-hit path already returned a copy pre-fix; pin it.
- L55 `test_caller_mutation_does_not_poison_cache(self)` (method) — Simulate run_agent appending LCM tool schemas to the returned
- L77 `test_repeated_caller_mutation_does_not_accumulate(self)` (method) — The original Gateway symptom: every agent init in a long-lived
- L90 `test_non_quiet_mode_does_not_use_cache(self)` (method) — Sanity: quiet_mode=False (TUI path) skips the cache entirely —
