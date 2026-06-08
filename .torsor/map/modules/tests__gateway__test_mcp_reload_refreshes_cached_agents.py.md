---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_mcp_reload_refreshes_cached_agents.py

Symbols in `tests/gateway/test_mcp_reload_refreshes_cached_agents.py`.

- L27 `_make_source()` (function)
- L37 `_make_event()` (function)
- L41 `_make_runner_with_cached_agents(num_agents: int=2)` (function) — Build a bare GatewayRunner with `num_agents` fake cached agents.
- L86 `test_reload_mcp_refreshes_cached_agent_tools()` (function) — After /reload-mcp succeeds, every cached agent gets its tool list
- L133 `test_reload_mcp_handles_empty_agent_cache()` (function) — Reload with no cached agents (e.g. fresh gateway) must not raise.
- L150 `test_reload_mcp_preserves_per_agent_toolset_overrides()` (function) — If a cached agent was built with enabled_toolsets=["safe"], the
