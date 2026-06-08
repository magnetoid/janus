---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# agent/transports/codex_event_projector.py

Symbols in `agent/transports/codex_event_projector.py`.

- L37 `_deterministic_call_id(item_type: str, item_id: str)` (function) — Stable id for tool_call message correlation.
- L50 `_format_tool_args(d: dict)` (function) — Format a dict as JSON the way Hermes' existing tool_calls path does.
- L56 `ProjectionResult` (class) — Output of projecting one Codex item.
- L69 `CodexEventProjector` (class) — Stateful projector consuming Codex notifications in arrival order.
- L75 `__init__(self)` (method)
- L78 `project(self, notification: dict)` (method) — Project a single notification. Idempotent for non-completion events;
- L119 `_project_agent_message(self, item: dict)` (method)
- L127 `_project_user_message(self, item: dict)` (method)
- L142 `_project_command(self, item: dict, item_id: str)` (method)
- L178 `_project_file_change(self, item: dict, item_id: str)` (method)
- L217 `_project_mcp_tool_call(self, item: dict, item_id: str)` (method)
- L258 `_project_dynamic_tool_call(self, item: dict, item_id: str)` (method)
- L298 `_project_opaque(self, item: dict, item_type: str)` (method)
