---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/plugins/test_disk_cleanup_plugin.py

Symbols in `tests/plugins/test_disk_cleanup_plugin.py`.

- L24 `_isolate_env(tmp_path, monkeypatch)` (function) — Isolate HERMES_HOME for each test.
- L37 `_load_lib()` (function) — Import the plugin's library module directly from the repo path.
- L49 `_load_plugin_init()` (function) — Import the plugin's __init__.py (which depends on the library).
- L77 `TestIsSafePath` (class)
- L78 `test_accepts_path_under_hermes_home(self, _isolate_env)` (method)
- L85 `test_rejects_outside_hermes_home(self, _isolate_env)` (method)
- L89 `test_accepts_tmp_hermes_prefix(self, _isolate_env, tmp_path)` (method)
- L93 `test_rejects_plain_tmp(self, _isolate_env)` (method)
- L97 `test_rejects_windows_mount(self, _isolate_env)` (method)
- L102 `TestGuessCategory` (class)
- L103 `test_test_prefix(self, _isolate_env)` (method)
- L109 `test_tmp_prefix(self, _isolate_env)` (method)
- L115 `test_dot_test_suffix(self, _isolate_env)` (method)
- L121 `test_skips_protected_top_level(self, _isolate_env)` (method)
- L130 `test_cron_subtree_categorised(self, _isolate_env)` (method)
- L139 `test_cron_jobs_json_not_tracked(self, _isolate_env)` (method) — Regression for #32164: the cron registry must never be tracked.
- L148 `test_cron_tick_lock_not_tracked(self, _isolate_env)` (method) — Regression for #32164: cron tick-lock is control-plane state.
- L157 `test_cronjobs_top_level_not_tracked(self, _isolate_env)` (method) — The legacy ``cronjobs`` alias is also control-plane at the top.
- L166 `test_ordinary_file_returns_none(self, _isolate_env)` (method)
- L173 `TestStaleCronEntryMigration` (class) — Regression tests for #37721 — stale cron-output entries in tracked.json.
- L176 `test_quick_skips_stale_cron_output_for_jobs_json(self, _isolate_env)` (method) — A stale tracked.json entry with category="cron-output" for
- L209 `test_quick_skips_stale_cron_output_for_cron_dir(self, _isolate_env)` (method) — Stale entry for the cron/ directory itself must not be deleted.
- L231 `test_quick_skips_protected_cron_paths_defense_in_depth(self, _isolate_env)` (method) — Defense-in-depth: even if guess_category returned cron-output
- L255 `test_dry_run_omits_stale_cron_output(self, _isolate_env)` (method) — dry_run() should also skip stale cron-output entries.
- L276 `test_legitimate_cron_output_still_deleted(self, _isolate_env)` (method) — A valid cron-output entry under cron/output/ must still be deleted.
- L302 `TestTrackForgetQuick` (class)
- L303 `test_track_then_quick_deletes_test(self, _isolate_env)` (method)
- L312 `test_track_dedup(self, _isolate_env)` (method)
- L320 `test_track_rejects_outside_home(self, _isolate_env)` (method)
- L326 `test_track_skips_missing(self, _isolate_env)` (method)
- L330 `test_forget_removes_entry(self, _isolate_env)` (method)
- L338 `test_quick_preserves_unexpired_temp(self, _isolate_env)` (method)
- L347 `test_quick_preserves_protected_top_level_dirs(self, _isolate_env)` (method)
- L356 `TestStatus` (class)
- L357 `test_empty_status(self, _isolate_env)` (method)
- L363 `test_status_with_entries(self, _isolate_env)` (method)
- L376 `TestDryRun` (class)
- L377 `test_classifies_by_category(self, _isolate_env)` (method)
- L394 `TestPostToolCallHook` (class)
- L395 `test_write_file_test_pattern_tracked(self, _isolate_env)` (method)
- L410 `test_write_file_non_test_not_tracked(self, _isolate_env)` (method)
- L423 `test_terminal_command_picks_up_paths(self, _isolate_env)` (method)
- L437 `test_ignores_unrelated_tool(self, _isolate_env)` (method)
- L450 `TestOnSessionEndHook` (class)
- L451 `test_runs_quick_when_test_files_tracked(self, _isolate_env)` (method)
- L465 `test_noop_when_no_test_tracked(self, _isolate_env)` (method)
- L475 `TestSlashCommand` (class)
- L476 `test_help(self, _isolate_env)` (method)
- L482 `test_status_empty(self, _isolate_env)` (method)
- L487 `test_track_rejects_missing(self, _isolate_env)` (method)
- L494 `test_track_rejects_bad_category(self, _isolate_env)` (method)
- L501 `test_track_and_forget(self, _isolate_env)` (method)
- L510 `test_unknown_subcommand(self, _isolate_env)` (method)
- L515 `test_quick_on_empty(self, _isolate_env)` (method)
- L525 `TestBundledDiscovery` (class)
- L526 `_write_enabled_config(self, hermes_home, names)` (method) — Write plugins.enabled allow-list to config.yaml.
- L532 `test_disk_cleanup_discovered_but_not_loaded_by_default(self, _isolate_env)` (method) — Bundled plugins are discovered but NOT loaded without opt-in.
- L545 `test_disk_cleanup_loads_when_enabled(self, _isolate_env)` (method) — Adding to plugins.enabled activates the bundled plugin.
- L557 `test_disabled_beats_enabled(self, _isolate_env)` (method) — plugins.disabled wins even if the plugin is also in plugins.enabled.
- L574 `test_memory_and_context_engine_subdirs_skipped(self, _isolate_env)` (method) — Bundled scan must NOT pick up plugins/memory or plugins/context_engine
