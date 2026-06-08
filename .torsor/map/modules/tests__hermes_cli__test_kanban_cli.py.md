---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/hermes_cli/test_kanban_cli.py

Symbols in `tests/hermes_cli/test_kanban_cli.py`.

- L18 `kanban_home(tmp_path, monkeypatch)` (function)
- L40 `test_parse_workspace_flag_valid(value, expected)` (function)
- L44 `test_parse_workspace_flag_expands_user()` (function)
- L56 `test_parse_workspace_flag_rejects(bad)` (function)
- L65 `test_parse_branch_flag_rejects_empty_and_option_like()` (function)
- L80 `test_run_slash_no_args_shows_usage(kanban_home)` (function)
- L86 `test_run_slash_create_and_list(kanban_home)` (function)
- L94 `test_run_slash_create_worktree_path_and_branch(kanban_home, tmp_path)` (function)
- L110 `test_run_slash_rejects_branch_without_worktree(kanban_home)` (function)
- L115 `test_run_slash_create_with_parent_and_cascade(kanban_home)` (function)
- L133 `test_run_slash_show_includes_comments(kanban_home)` (function)
- L142 `test_run_slash_comment_max_len_trims_long_body(kanban_home)` (function)
- L152 `test_run_slash_block_unblock_cycle(kanban_home)` (function)
- L162 `test_run_slash_json_output(kanban_home)` (function)
- L170 `test_run_slash_dispatch_dry_run_counts(kanban_home)` (function)
- L177 `test_run_slash_context_output_format(kanban_home)` (function)
- L188 `test_run_slash_tenant_filter(kanban_home)` (function)
- L197 `test_run_slash_session_filter(kanban_home)` (function) — `hermes kanban list --session <id>` filters by the originating
- L222 `test_kanban_list_json_includes_session_id(kanban_home)` (function) — JSON output exposes `session_id` so external clients (Scarf, web
- L239 `test_run_slash_usage_error_returns_message(kanban_home)` (function)
- L245 `test_run_slash_assign_reassigns(kanban_home)` (function)
- L254 `test_run_slash_link_unlink(kanban_home)` (function)
- L267 `test_board_override_is_isolated_per_concurrent_call(kanban_home, monkeypatch)` (function)
- L317 `test_kanban_is_resolvable()` (function)
- L325 `test_kanban_bypasses_active_session_guard()` (function)
- L331 `test_kanban_in_autocomplete_table()` (function)
- L340 `test_kanban_autocomplete_includes_live_subcommands()` (function)
- L358 `test_kanban_not_gateway_only()` (function)
- L371 `test_run_slash_reclaim_running_task(kanban_home)` (function)
- L409 `test_run_slash_reassign_with_reclaim_flag(kanban_home)` (function)
- L449 `test_run_slash_specify_end_to_end(kanban_home, monkeypatch)` (function) — The /kanban specify slash command routes through run_slash, which
- L487 `test_run_slash_specify_help_is_reachable(kanban_home)` (function) — `-h`/`--help` on a subcommand returns the actual help text — see
- L501 `test_run_slash_bare_returns_curated_help(kanban_home)` (function) — Bare `/kanban` returns the curated short-help block — not a 5KB
- L515 `test_run_slash_help_aliases_match_bare(kanban_home, alias)` (function) — Every documented help alias produces the same curated output.
- L522 `test_run_slash_subcommand_help_returns_help_text(kanban_home)` (function) — `/kanban show -h` returns the actual subcommand help, not a
- L531 `test_run_slash_unknown_action_friendly_error(kanban_home)` (function) — Unknown subcommand surfaces a single-line usage error prefixed
- L543 `test_run_slash_missing_required_arg_friendly_error(kanban_home)` (function) — Missing positional argument shows the subcommand-scoped usage
- L551 `test_run_slash_board_override_restores_prior_env(kanban_home, monkeypatch)` (function)
- L561 `test_run_slash_board_override_does_not_change_boards_show_current(kanban_home)` (function)
