---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# hermes_cli/mcp_picker.py

Symbols in `hermes_cli/mcp_picker.py`.

- L55 `_Row` (class) — A row in the picker. ``entry`` is set for catalog rows; for custom
- L65 `is_custom(self)` (method)
- L69 `_build_rows()` (function) — Return catalog rows + any custom (non-catalog) MCPs found in config.
- L106 `_format_row(row: _Row)` (function)
- L113 `_enable_disable(name: str, *, enable: bool)` (function)
- L130 `_configure_tools(name: str)` (function) — Open the tool selection checklist for an already-installed MCP.
- L142 `_remove_custom(name: str)` (function) — Remove a non-catalog MCP entry from config.yaml.
- L160 `_handle_row(row: _Row)` (function) — Act on the picked row based on its current status.
- L231 `_print_rows_text(rows: List[_Row])` (function) — Plain-text catalog dump used as a fallback when curses can't run, and
- L269 `show_catalog()` (function) — `hermes mcp catalog` — print the curated list + custom servers, no interaction.
- L274 `run_picker()` (function) — `hermes mcp picker` (and default `hermes mcp`) — interactive selector.
- L301 `install_by_name(identifier: str)` (function) — `hermes mcp install <name>` — non-interactive entry-point.
