---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# hermes_cli/mcp_startup.py

Symbols in `hermes_cli/mcp_startup.py`.

- L13 `_has_configured_mcp_servers()` (function) — Cheap config probe so non-MCP users avoid importing the MCP stack.
- L26 `start_background_mcp_discovery(*, logger, thread_name: str)` (function) — Spawn one shared background MCP discovery thread for this process.
- L54 `wait_for_mcp_discovery(timeout: float=0.75)` (function) — Briefly wait for background MCP discovery before the first tool snapshot.
