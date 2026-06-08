---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/hermes_cli/test_mcp_tools_config.py

Symbols in `tests/hermes_cli/test_mcp_tools_config.py`.

- L13 `test_no_mcp_servers_prints_info(capsys)` (function) — Returns immediately when no MCP servers are configured.
- L21 `test_all_servers_disabled_prints_info(capsys)` (function) — Returns immediately when all configured servers have enabled=false.
- L34 `test_probe_failure_shows_warning(capsys)` (function) — Shows warning when probe returns no tools.
- L43 `test_probe_exception_shows_error(capsys)` (function) — Shows error when probe raises an exception.
- L52 `test_no_changes_when_checklist_cancelled(capsys)` (function) — No config changes when user cancels (ESC) the checklist.
- L70 `test_disabling_tool_writes_include_list(capsys)` (function) — Unchecking a tool produces an include list of the still-chosen tools.
- L100 `test_enabling_all_clears_filters(capsys)` (function) — Checking all tools clears both include and exclude lists.
- L125 `test_pre_selection_respects_existing_exclude(capsys)` (function) — Tools in exclude list start unchecked.
- L151 `test_pre_selection_respects_existing_include(capsys)` (function) — Only tools in include list start checked.
- L177 `test_multiple_servers_each_get_checklist(capsys)` (function) — Each server gets its own checklist.
- L206 `test_failed_server_shows_warning(capsys)` (function) — Servers that fail to connect show warnings.
- L226 `test_description_truncation_in_labels()` (function) — Long descriptions are truncated in checklist labels.
- L251 `test_modifying_include_stays_in_include_mode(capsys)` (function) — Changing the selection updates the include list — never switches
- L275 `test_empty_tools_server_skipped(capsys)` (function) — Server with no tools shows info message and skips checklist.
