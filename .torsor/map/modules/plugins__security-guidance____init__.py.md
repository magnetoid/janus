---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# plugins/security-guidance/__init__.py

Symbols in `plugins/security-guidance/__init__.py`.

- L66 `_block_mode_enabled()` (function)
- L70 `_plugin_disabled()` (function)
- L104 `_scan_content(path: str, content: str)` (function) — Return [(ruleName, reminder), ...] for every pattern that matches.
- L149 `_extract_path_and_content(tool_name: str, args: Any)` (function) — Return [(path, content), ...] for a tool call.  Empty if nothing to scan.
- L166 `_format_warning_block(findings: List[Tuple[str, str]])` (function) — Render findings into a Markdown block appended to the tool result.
- L191 `_scan_args(tool_name: str, args: Any)` (function) — Common scan path used by both pre_tool_call (block mode) and
- L202 `_on_pre_tool_call(tool_name: str='', args: Any=None, **_: Any)` (function) — In block mode, refuse the write if any pattern matches.
- L227 `_on_transform_tool_result(tool_name: str='', args: Any=None, result: Any=None, **_: Any)` (function) — Warn-mode hook: append a security-warning block to the tool result.
- L257 `register(ctx)` (function)
