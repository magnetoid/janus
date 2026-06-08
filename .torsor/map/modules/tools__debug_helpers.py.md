---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:44'
updated: '2026-06-08T00:38:44'
---

# tools/debug_helpers.py

Symbols in `tools/debug_helpers.py`.

- L36 `DebugSession` (class) — Per-tool debug session that records tool calls to a JSON log file.
- L43 `__init__(self, tool_name: str, *, env_var: str)` (method)
- L57 `active(self)` (method)
- L60 `log_call(self, call_name: str, call_data: Dict[str, Any])` (method) — Append a tool-call entry to the in-memory log.
- L70 `save(self)` (method) — Flush the in-memory log to a JSON file in the logs directory.
- L91 `get_session_info(self)` (method) — Return a summary dict suitable for returning from get_debug_session_info().
