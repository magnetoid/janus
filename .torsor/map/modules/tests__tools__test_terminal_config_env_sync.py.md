---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:44'
updated: '2026-06-08T00:38:44'
---

# tests/tools/test_terminal_config_env_sync.py

Symbols in `tests/tools/test_terminal_config_env_sync.py`.

- L30 `_extract_dict_values(source: str, dict_name: str)` (function) — Return the set of *value* strings in `dict_name = { "k": "VALUE", ... }`.
- L54 `_extract_dict_keys(source: str, dict_name: str)` (function) — Return the set of *key* strings in `dict_name = { "KEY": "v", ... }`.
- L73 `_cli_env_map_keys()` (function) — terminal config keys bridged by cli.load_cli_config().
- L80 `_gateway_env_map_keys()` (function) — terminal config keys bridged by gateway/run.py at module load.
- L89 `_save_config_env_sync_keys()` (function) — terminal config keys bridged by ``hermes config set foo bar``.
- L115 `_terminal_tool_env_var_names()` (function) — All TERMINAL_* env vars actually consumed by terminal_tool.
- L125 `test_cli_and_gateway_env_maps_agree()` (function) — cli.py and gateway/run.py must bridge the same set of terminal keys.
- L157 `test_save_config_set_supports_critical_bridged_keys()` (function) — ``hermes config set terminal.X true`` must propagate to .env for
- L188 `test_docker_run_as_host_user_is_bridged_everywhere()` (function) — Explicit pin for the bug we just fixed.
- L203 `test_docker_mount_cwd_to_workspace_is_bridged_everywhere()` (function) — Same regression class — docker_mount_cwd_to_workspace was missing from
- L214 `test_docker_env_is_bridged_everywhere()` (function) — Regression pin for docker_env config key being silently ignored.
- L230 `test_docker_persist_across_processes_is_bridged_everywhere()` (function) — Regression pin for the cross-process container reuse toggle.
- L250 `test_docker_orphan_reaper_is_bridged_everywhere()` (function) — Regression pin for the startup orphan reaper toggle (issue #20561).
- L266 `test_docker_volumes_is_bridged_everywhere()` (function) — Regression pin for ``terminal.docker_volumes`` being silently dropped by
- L284 `test_docker_forward_env_is_bridged_everywhere()` (function) — Regression pin for ``terminal.docker_forward_env`` — the sibling gap to
