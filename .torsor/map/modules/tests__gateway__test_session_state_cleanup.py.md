---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_session_state_cleanup.py

Symbols in `tests/gateway/test_session_state_cleanup.py`.

- L24 `_make_runner()` (function) — Bare GatewayRunner wired with just the state the helper touches.
- L35 `TestReleaseRunningAgentStateUnit` (class)
- L36 `test_pops_all_three_dicts(self)` (method)
- L48 `test_idempotent_on_missing_key(self)` (method) — Calling twice (or on an absent key) must not raise.
- L54 `test_noop_on_empty_session_key(self)` (method) — Empty string / None key is treated as a no-op.
- L62 `test_preserves_other_sessions(self)` (method)
- L75 `test_handles_missing_busy_ack_attribute(self)` (method) — Backward-compatible with older runners lacking _busy_ack_ts.
- L87 `test_concurrent_release_is_safe(self)` (method) — Multiple threads releasing different keys concurrently.
- L115 `TestNoMoreBareDeleteSites` (class) — Regression: all bare `del self._running_agents[key]` sites were
- L122 `test_no_bare_del_of_running_agents_in_gateway_run(self)` (method)
- L160 `TestSessionDbCloseOnShutdown` (class) — _stop_impl should call .close() on both self._session_db and
- L166 `test_stop_impl_closes_both_session_dbs(self)` (method) — Run the exact shutdown block that closes SessionDBs and verify
- L190 `test_shutdown_tolerates_missing_session_store(self)` (method) — Gateway without a session_store attribute must not crash on shutdown.
- L206 `test_shutdown_tolerates_close_raising(self)` (method) — A close() that raises must not prevent subsequent cleanup.
- L233 `TestSessionResetZombieRace` (class) — Regression for #28686 — a session_reset racing the in-flight run's
- L238 `test_generation_guard_blocks_then_unconditional_release_evicts(self)` (method)
- L263 `test_normal_completion_is_not_evicted_by_outer_release(self)` (method) — Guarded release with the current generation succeeds; the outer
