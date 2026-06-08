---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/hermes_cli/test_codex_runtime_plugin_migration.py

Symbols in `tests/hermes_cli/test_codex_runtime_plugin_migration.py`.

- L24 `TestTranslateOneServer` (class)
- L25 `test_stdio_basic(self)` (method)
- L38 `test_stdio_with_cwd(self)` (method)
- L45 `test_http_basic(self)` (method)
- L56 `test_sse_falls_under_streamable_http_with_warning(self)` (method)
- L64 `test_timeouts_translate(self)` (method)
- L73 `test_non_numeric_timeout_skipped(self)` (method)
- L81 `test_disabled_server_emits_enabled_false(self)` (method)
- L88 `test_enabled_true_omitted(self)` (method)
- L92 `test_command_and_url_prefers_stdio_warns(self)` (method)
- L100 `test_no_transport_returns_none(self)` (method)
- L105 `test_sampling_dropped_with_warning(self)` (method)
- L113 `test_unknown_keys_warned(self)` (method)
- L121 `test_non_dict_input(self)` (method)
- L128 `TestTomlValueFormatter` (class)
- L129 `test_string_quoted(self)` (method)
- L132 `test_string_with_quotes_escaped(self)` (method)
- L135 `test_bool(self)` (method)
- L139 `test_int(self)` (method)
- L142 `test_float(self)` (method)
- L145 `test_list_of_strings(self)` (method)
- L148 `test_inline_table(self)` (method)
- L152 `test_empty_inline_table(self)` (method)
- L155 `test_string_with_newline_escaped(self)` (method) — TOML basic strings don't allow literal newlines — a path or
- L163 `test_string_with_tab_escaped(self)` (method)
- L168 `test_string_with_other_controls_escaped(self)` (method)
- L178 `test_windows_path_escaped_correctly(self)` (method)
- L183 `test_atomic_write_no_temp_leak_on_success(self, tmp_path)` (method) — The atomic-write path uses tempfile.mkstemp + rename. On
- L198 `test_atomic_write_cleanup_on_rename_failure(self, tmp_path, monkeypatch)` (method) — If rename fails partway through (out of disk, permissions,
- L223 `test_unsupported_type_raises(self)` (method)
- L228 `TestRenderToml` (class)
- L229 `test_starts_with_marker(self)` (method)
- L233 `test_empty_servers_emits_placeholder(self)` (method)
- L237 `test_servers_sorted_alphabetically(self)` (method)
- L249 `test_server_with_args_and_env(self)` (method)
- L266 `TestStripExistingManagedBlock` (class)
- L267 `test_no_managed_block_unchanged(self)` (method)
- L271 `test_strips_managed_block_alone(self)` (method)
- L280 `test_preserves_user_content_above_managed_block(self)` (method)
- L294 `test_preserves_unrelated_section_after_managed_block(self)` (method)
- L311 `TestMigrate` (class)
- L312 `test_no_servers_no_plugins_no_perms_writes_placeholder(self, tmp_path)` (method)
- L321 `test_no_servers_still_writes_permissions_default(self, tmp_path)` (method) — Even with zero MCP servers, enabling the runtime should write the
- L334 `test_explicit_none_permissions_skips_block(self, tmp_path)` (method)
- L344 `test_plugin_discovery_writes_plugin_blocks(self, tmp_path, monkeypatch)` (method) — Discovered curated plugins land as [plugins."<name>@<marketplace>"]
- L366 `test_plugin_discovery_skips_unavailable_plugins(self)` (method) — Plugins where codex reports availability != AVAILABLE should
- L414 `test_plugin_discovery_failure_non_fatal(self, tmp_path, monkeypatch)` (method) — If codex isn't installed or RPC fails, MCP migration still
- L430 `test_discover_plugins_false_skips_query(self, tmp_path, monkeypatch)` (method) — Tests and restricted environments can opt out of the subprocess
- L445 `test_dry_run_skips_plugin_query(self, tmp_path, monkeypatch)` (method) — Dry run should never spawn codex. Even with discover_plugins=True
- L460 `test_re_run_replaces_plugin_block(self, tmp_path, monkeypatch)` (method) — Plugin blocks are managed and re-runs should replace them
- L488 `test_expose_hermes_tools_writes_callback_mcp_entry(self, tmp_path)` (method) — When expose_hermes_tools=True (production default), an
- L508 `test_expose_hermes_tools_disabled_skips_entry(self, tmp_path)` (method) — expose_hermes_tools=False suppresses the callback registration.
- L518 `test_dry_run_doesnt_write(self, tmp_path)` (method)
- L525 `test_full_migration_round_trip(self, tmp_path)` (method)
- L546 `test_idempotent_re_run_replaces_managed_block(self, tmp_path)` (method)
- L557 `test_preserves_user_codex_config_above_marker(self, tmp_path)` (method)
- L576 `test_managed_root_keys_stay_top_level_when_config_ends_in_table(self, tmp_path)` (method) — TOML has no explicit 'leave current table' syntax. If Hermes appends
- L597 `test_preserves_user_mcp_server_outside_managed_block(self, tmp_path)` (method) — Quirk #6: when a user adds their own MCP server entry directly
- L630 `test_skipped_keys_reported(self, tmp_path)` (method)
- L642 `test_invalid_mcp_servers_value(self, tmp_path)` (method)
- L646 `test_server_without_transport_skipped_with_error(self, tmp_path)` (method)
- L653 `test_summary_reports_migration_count(self, tmp_path)` (method)
- L666 `TestStripUnmanagedPluginTables` (class) — Regression tests for issue #26250 Bug B.
- L675 `test_strips_plugin_tables_outside_managed_block(self)` (method)
- L698 `test_preserves_content_when_no_plugin_tables(self)` (method)
- L707 `test_multi_line_array_in_plugin_table_does_not_leak(self)` (method) — A multi-line TOML array inside a [plugins.X] table whose
- L735 `test_migrate_dedups_codex_owned_plugin_tables(self, tmp_path, monkeypatch)` (method) — End-to-end: codex's pre-existing [plugins.X] tables get replaced by
- L772 `test_migrate_preserves_plugin_tables_when_plugin_list_fails(self, tmp_path, monkeypatch)` (method) — If plugin/list RPC fails, we can't re-emit plugins authoritatively,
- L798 `TestHermesHomeLeakGuard` (class) — Regression tests for issue #26250 Bug C.
- L807 `test_tempdir_detector_recognizes_pytest_paths(self)` (method)
- L818 `test_tempdir_detector_accepts_real_hermes_home(self)` (method)
- L824 `test_pytest_tempdir_not_burned_into_mcp_env(self, monkeypatch)` (method) — The headline regression: even when HERMES_HOME points at a pytest
- L838 `test_real_hermes_home_propagates(self, monkeypatch, tmp_path)` (method) — A legitimate HERMES_HOME (not a tempdir path) DOES propagate so the
- L851 `test_unset_hermes_home_omits_env_key(self, monkeypatch)` (method) — When HERMES_HOME is unset in the environment, the MCP entry MUST
