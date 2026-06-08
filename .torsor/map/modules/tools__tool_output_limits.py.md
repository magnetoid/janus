---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:44'
updated: '2026-06-08T00:38:44'
---

# tools/tool_output_limits.py

Symbols in `tools/tool_output_limits.py`.

- L48 `_coerce_positive_int(value: Any, default: int)` (function) — Return ``value`` as a positive int, or ``default`` on any issue.
- L59 `get_tool_output_limits()` (function) — Return resolved tool-output limits, reading ``tool_output`` from config.
- L92 `_reset_tool_output_limits_cache()` (function) — Reset the cached limits — for tests or after config hot-reload.
- L98 `get_max_bytes()` (function) — Shortcut for terminal-tool callers that only need the byte cap.
- L103 `get_max_lines()` (function) — Shortcut for file-ops callers that only need the line cap.
- L108 `get_max_line_length()` (function) — Shortcut for file-ops callers that only need the per-line cap.
