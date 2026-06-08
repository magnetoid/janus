---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/agent/transports/test_hermes_tools_mcp_server.py

Symbols in `tests/agent/transports/test_hermes_tools_mcp_server.py`.

- L14 `TestModuleSurface` (class)
- L15 `test_module_imports_clean(self)` (method)
- L22 `test_exposed_tools_are_safe_subset(self)` (method) — We MUST NOT expose tools codex already has, because codex'
- L38 `test_expected_hermes_specific_tools_listed(self)` (method) — The Hermes-specific tools should be present so users on the
- L52 `test_agent_loop_tools_not_exposed(self)` (method) — delegate_task / memory / session_search / todo require the
- L63 `test_kanban_worker_tools_exposed(self)` (method) — Kanban workers run as `hermes chat -q` subprocesses; if they
- L83 `test_kanban_orchestrator_tools_exposed(self)` (method) — Orchestrator agents need to dispatch new tasks, query the
- L100 `TestMain` (class)
- L101 `test_main_returns_2_when_mcp_unavailable(self, monkeypatch)` (method) — When the mcp package isn't installed, main() should exit
- L113 `test_main_handles_keyboard_interrupt(self, monkeypatch)` (method)
- L124 `test_main_returns_1_on_runtime_error(self, monkeypatch)` (method)
