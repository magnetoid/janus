---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/hermes_cli/test_tui_resume_flow.py

Symbols in `tests/hermes_cli/test_tui_resume_flow.py`.

- L10 `_args(**overrides)` (function)
- L25 `main_mod(monkeypatch)` (function)
- L32 `test_cmd_chat_tui_continue_uses_latest_tui_session(monkeypatch, main_mod)` (function)
- L62 `test_cmd_chat_tui_continue_falls_back_to_latest_cli_session(monkeypatch, main_mod)` (function)
- L96 `test_cmd_chat_tui_resume_resolves_title_before_launch(monkeypatch, main_mod)` (function)
- L121 `test_cmd_chat_tui_passes_model_and_provider(monkeypatch, main_mod)` (function)
- L159 `test_cmd_chat_tui_passes_toolsets(monkeypatch, main_mod)` (function)
- L181 `test_cmd_chat_tui_forwards_chat_flags(monkeypatch, main_mod)` (function)
- L219 `test_main_top_level_tui_accepts_toolsets(monkeypatch, main_mod)` (function)
- L255 `test_termux_fast_tui_launch_uses_light_parser(monkeypatch, main_mod)` (function)
- L272 `test_termux_fast_tui_launch_skips_help(monkeypatch, main_mod)` (function)
- L279 `test_fast_tui_launch_is_termux_only(monkeypatch, main_mod)` (function)
- L287 `test_termux_fast_cli_launch_chat_uses_light_parser(monkeypatch, main_mod)` (function)
- L316 `test_termux_fast_cli_launch_bare_defers_agent_startup(monkeypatch, main_mod)` (function)
- L347 `test_termux_fast_cli_launch_oneshot_uses_light_parser(monkeypatch, main_mod)` (function)
- L385 `test_termux_fast_cli_launch_version_skips_update_check(monkeypatch, main_mod)` (function)
- L399 `test_termux_ultrafast_version_runs_before_heavy_startup(monkeypatch, capsys, main_mod)` (function)
- L415 `test_read_openai_version_fast(monkeypatch, tmp_path, main_mod)` (function)
- L427 `test_termux_fast_cli_launch_skips_help(monkeypatch, main_mod)` (function)
- L435 `test_termux_fast_cli_launch_can_be_disabled(monkeypatch, main_mod)` (function)
- L444 `test_termux_bundled_skills_stamp_controls_sync(monkeypatch, tmp_path, main_mod)` (function)
- L457 `test_termux_skips_bundled_skill_sync_when_stamp_fresh(monkeypatch, tmp_path, main_mod)` (function)
- L474 `test_termux_forced_bundled_skill_sync_runs(monkeypatch, tmp_path, main_mod)` (function)
- L491 `test_read_git_revision_fingerprint_resolves_packed_refs(tmp_path, main_mod)` (function)
- L510 `test_read_git_revision_fingerprint_packed_refs_in_worktree_common_dir(tmp_path, main_mod)` (function)
- L535 `test_read_git_revision_fingerprint_loose_ref_in_worktree_common_dir(tmp_path, main_mod)` (function) — `git worktree add -b NAME` writes the new branch ref to the common dir,
- L562 `test_read_git_revision_fingerprint_unresolved_ref_is_stable(tmp_path, main_mod)` (function)
- L573 `test_main_top_level_oneshot_accepts_toolsets(monkeypatch, main_mod)` (function)
- L623 `_stub_plugin_discovery(monkeypatch)` (function)
- L631 `test_oneshot_rejects_invalid_only_toolsets(monkeypatch, capsys)` (function)
- L641 `test_oneshot_fails_closed_on_empty_final_response(monkeypatch, capsys)` (function)
- L653 `test_oneshot_prints_nonempty_final_response(monkeypatch, capsys)` (function)
- L665 `test_oneshot_fails_closed_on_agent_exception(monkeypatch, capsys)` (function)
- L681 `test_oneshot_reraises_keyboard_interrupt(monkeypatch)` (function)
- L695 `test_oneshot_filters_invalid_toolsets_before_redirect(monkeypatch, capsys)` (function)
- L706 `test_oneshot_all_toolsets_means_all_not_configured_cli()` (function)
- L715 `test_oneshot_all_toolsets_warns_about_ignored_extra_entries(monkeypatch, capsys)` (function)
- L726 `test_oneshot_accepts_plugin_toolset_after_discovery(monkeypatch)` (function)
- L752 `test_oneshot_rejects_disabled_mcp_toolset(monkeypatch, capsys)` (function)
- L773 `test_oneshot_distinguishes_disabled_mcp_from_unknown(monkeypatch, capsys)` (function)
- L795 `test_oneshot_wires_session_db_for_recall(monkeypatch)` (function) — hermes -z bypasses HermesCLI, but recall still needs SessionDB.
- L861 `test_launch_tui_exports_model_provider_and_toolsets(monkeypatch, main_mod)` (function)
- L899 `test_launch_tui_exit_code_42_relaunches_update(monkeypatch, main_mod)` (function)
- L917 `test_launch_tui_drops_stale_resume_env_without_resume_arg(monkeypatch, main_mod)` (function)
- L938 `test_launch_tui_sets_resume_env_from_resume_arg(monkeypatch, main_mod)` (function)
- L959 `test_make_tui_argv_dev_prebuilds_hermes_ink(monkeypatch, main_mod, tmp_path)` (function)
- L987 `test_print_tui_exit_summary_includes_resume_and_token_totals(monkeypatch, capsys)` (function)
- L1021 `test_print_tui_exit_summary_prefers_actual_active_session_file(monkeypatch, capsys, tmp_path)` (function)
