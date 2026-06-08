---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/hermes_cli/test_plugin_auxiliary_tasks.py

Symbols in `tests/hermes_cli/test_plugin_auxiliary_tasks.py`.

- L27 `_make_ctx(name: str='test_plugin')` (function) — Build a PluginContext + fresh PluginManager wired together.
- L41 `patched_manager(monkeypatch)` (function) — Replace the module-level singleton with a fresh manager for the test.
- L63 `test_register_auxiliary_task_basic()` (function)
- L82 `test_register_auxiliary_task_with_custom_defaults()` (function)
- L97 `test_register_auxiliary_task_rejects_builtin_keys()` (function)
- L117 `test_register_auxiliary_task_rejects_invalid_key_shapes()` (function)
- L128 `test_register_auxiliary_task_allows_same_plugin_re_registration()` (function) — Re-registration by the same plugin updates the entry (idempotent).
- L140 `test_register_auxiliary_task_rejects_cross_plugin_collision()` (function) — Two different plugins cannot register the same task key.
- L162 `test_force_rediscovery_clears_aux_tasks()` (function)
- L180 `test_get_plugin_auxiliary_tasks_returns_sorted_list(patched_manager)` (function)
- L197 `test_get_plugin_auxiliary_tasks_empty_when_none_registered(patched_manager)` (function)
- L204 `test_all_aux_tasks_includes_plugin_registered(patched_manager)` (function)
- L230 `test_all_aux_tasks_swallows_plugin_discovery_failure(monkeypatch)` (function) — Plugin discovery failure must not break the aux config UI.
- L249 `test_reset_aux_to_auto_resets_plugin_tasks(tmp_path, monkeypatch, patched_manager)` (function) — Plugin task with non-auto config gets reset alongside built-ins.
- L284 `test_get_auxiliary_task_config_layers_plugin_defaults(tmp_path, monkeypatch, patched_manager)` (function) — Plugin-declared defaults appear when user has no config entry.
- L311 `test_get_auxiliary_task_config_user_config_wins_over_plugin_defaults(tmp_path, monkeypatch, patched_manager)` (function) — User's config.yaml entry overrides plugin-declared defaults.
- L343 `test_get_auxiliary_task_config_unknown_task_returns_empty(tmp_path, monkeypatch, patched_manager)` (function)
