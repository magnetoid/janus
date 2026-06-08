---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/run_agent/test_async_httpx_del_neuter.py

Symbols in `tests/run_agent/test_async_httpx_del_neuter.py`.

- L25 `TestNeuterAsyncHttpxDel` (class) — Verify neuter_async_httpx_del replaces __del__ on the SDK class.
- L28 `test_del_becomes_noop(self)` (method) — After neuter, __del__ should do nothing (no RuntimeError).
- L50 `test_neuter_idempotent(self)` (method) — Calling neuter twice doesn't break anything.
- L71 `test_neuter_graceful_without_sdk(self)` (method) — neuter_async_httpx_del doesn't raise if the openai SDK isn't installed.
- L84 `TestCleanupStaleAsyncClients` (class) — Verify stale cache entries are evicted and force-closed.
- L87 `test_removes_stale_entries(self)` (method) — Entries with a closed loop should be evicted.
- L117 `test_keeps_live_entries(self)` (method) — Entries with an open loop should be preserved.
- L141 `test_keeps_entries_without_loop(self)` (method) — Sync entries (cached_loop=None) should be preserved.
- L167 `TestClientCacheBoundedGrowth` (class) — Verify the cache stays bounded when loops change (fix for #10200).
- L175 `test_same_key_replaces_stale_loop_entry(self)` (method) — When the loop changes, the old entry should be replaced, not duplicated.
- L211 `test_different_loops_do_not_grow_cache(self)` (method) — Multiple event loops for the same provider should NOT create multiple entries.
- L251 `test_max_cache_size_eviction(self)` (method) — Cache should not exceed _CLIENT_CACHE_MAX_SIZE.
