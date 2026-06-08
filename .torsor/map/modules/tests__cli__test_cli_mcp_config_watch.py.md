---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/cli/test_cli_mcp_config_watch.py

Symbols in `tests/cli/test_cli_mcp_config_watch.py`.

- L7 `_make_cli(tmp_path, mcp_servers=None)` (function) — Create a minimal HermesCLI instance with mocked config.
- L29 `TestMCPConfigWatch` (class)
- L31 `test_no_change_does_not_reload(self, tmp_path)` (method) — If mtime and mcp_servers unchanged, _reload_mcp is NOT called.
- L40 `test_mtime_change_with_same_mcp_servers_does_not_reload(self, tmp_path)` (method) — If file mtime changes but mcp_servers is identical, no reload.
- L55 `test_new_mcp_server_triggers_reload(self, tmp_path)` (method) — Adding a new MCP server to config triggers auto-reload.
- L69 `test_removed_mcp_server_triggers_reload(self, tmp_path)` (method) — Removing an MCP server from config triggers auto-reload.
- L83 `test_interval_throttle_skips_check(self, tmp_path)` (method) — If called within CONFIG_WATCH_INTERVAL, stat() is skipped.
- L95 `test_missing_config_file_does_not_crash(self, tmp_path)` (method) — If config.yaml doesn't exist, _check_config_mcp_changes is a no-op.
