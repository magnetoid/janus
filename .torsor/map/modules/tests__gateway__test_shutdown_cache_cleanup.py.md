---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_shutdown_cache_cleanup.py

Symbols in `tests/gateway/test_shutdown_cache_cleanup.py`.

- L27 `_FakeGateway` (class) — Minimal stand-in with just enough state for ``stop()`` to run.
- L30 `__init__(self)` (method)
- L54 `_running_agent_count(self)` (method)
- L57 `_update_runtime_status(self, *_a, **_kw)` (method)
- L60 `_notify_active_sessions_of_shutdown(self)` (method)
- L63 `_drain_active_agents(self, timeout)` (method)
- L66 `_finalize_shutdown_agents(self, agents)` (method)
- L70 `_cleanup_agent_resources(self, agent)` (method)
- L84 `_evict_cached_agent(self, key)` (method)
- L88 `_make_mock_agent()` (function)
- L99 `TestCachedAgentCleanupOnShutdown` (class) — Verify that ``stop()`` calls ``_cleanup_agent_resources`` on idle
- L105 `test_cached_agent_memory_provider_shut_down(self)` (method) — A cached agent's shutdown_memory_provider is called during gateway stop.
- L117 `test_cache_cleared_after_shutdown(self)` (method) — The _agent_cache dict is cleared after stop.
- L128 `test_no_cached_agents_no_error(self)` (method) — stop() works fine when _agent_cache is empty.
- L137 `test_multiple_cached_agents_all_cleaned(self)` (method) — All cached agents get cleaned up.
- L152 `test_cleanup_survives_agent_exception(self)` (method) — An exception from one agent's shutdown doesn't prevent others.
- L171 `test_plain_agent_not_tuple(self)` (method) — Cache entries that aren't tuples (just bare agents) are also cleaned.
- L183 `test_none_entry_skipped(self)` (method) — A None cache entry doesn't cause errors.
- L193 `TestRunningAgentsNotDoubleCleaned` (class) — Verify behavior when agents appear in both _running_agents and _agent_cache.
- L197 `test_running_and_cached_agent_cleaned_at_least_once(self)` (method) — An agent in both _running_agents and _agent_cache gets
