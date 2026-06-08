---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:44'
updated: '2026-06-08T00:38:44'
---

# tui_gateway/entry.py

Symbols in `tui_gateway/entry.py`.

- L32 `_install_sidecar_publisher()` (function) — Mirror every dispatcher emit to the dashboard sidebar via WS.
- L62 `_shutdown_grace_seconds()` (function)
- L73 `_log_signal(signum: int, frame)` (function) — Capture WHICH thread and WHERE a termination signal hit us.
- L173 `_log_exit(reason: str)` (function) — Record why the gateway subprocess is shutting down.
- L195 `wait_for_mcp_discovery(timeout: float=0.75)` (function) — Briefly block until background MCP discovery finishes, up to ``timeout``.
- L213 `main()` (function)
