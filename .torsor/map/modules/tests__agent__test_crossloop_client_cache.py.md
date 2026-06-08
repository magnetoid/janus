---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/agent/test_crossloop_client_cache.py

Symbols in `tests/agent/test_crossloop_client_cache.py`.

- L22 `_stub_resolve_provider_client(provider, model, async_mode, **kw)` (function) — Return a unique mock client each time, simulating AsyncOpenAI creation.
- L31 `_clean_client_cache()` (function) — Clear the client cache before each test.
- L43 `TestCrossLoopCacheIsolation` (class) — Verify async clients are cached per-event-loop, not globally.
- L46 `test_same_loop_reuses_client(self)` (method) — Within a single event loop, the same client should be returned.
- L65 `test_different_loops_get_different_clients(self)` (method) — Different event loops must get separate client instances.
- L95 `test_sync_clients_not_affected(self)` (method) — Sync clients (async_mode=False) should still be cached globally,
- L120 `test_gateway_simulation_no_deadlock(self)` (method) — Simulate gateway mode: _run_async spawns a thread with asyncio.run(),
- L157 `test_closed_loop_client_discarded(self)` (method) — A cached client whose loop has closed should be replaced.
