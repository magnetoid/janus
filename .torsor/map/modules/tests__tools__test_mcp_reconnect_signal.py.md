---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/tools/test_mcp_reconnect_signal.py

Symbols in `tests/tools/test_mcp_reconnect_signal.py`.

- L15 `test_reconnect_event_attribute_exists()` (function) — MCPServerTask has a _reconnect_event alongside _shutdown_event.
- L25 `test_wait_for_lifecycle_event_returns_reconnect()` (function) — When _reconnect_event fires, helper returns 'reconnect' and clears it.
- L38 `test_wait_for_lifecycle_event_returns_shutdown()` (function) — When _shutdown_event fires, helper returns 'shutdown'.
- L49 `test_wait_for_lifecycle_event_shutdown_wins_when_both_set()` (function) — If both events are set simultaneously, shutdown takes precedence.
