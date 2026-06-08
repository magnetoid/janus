---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/tools/test_kanban_tools.py

Symbols in `tests/tools/test_kanban_tools.py`.

- L21 `test_kanban_tools_hidden_without_env_var(monkeypatch, tmp_path)` (function) — Normal `hermes chat` sessions (no HERMES_KANBAN_TASK) must have
- L42 `test_kanban_tools_visible_with_env_var(monkeypatch, tmp_path)` (function) — Worker sessions get task lifecycle tools, not board-routing tools.
- L64 `test_kanban_worker_env_overrides_profile_toolset_filter(monkeypatch, tmp_path)` (function) — Dispatcher-spawned workers must get lifecycle tools even when the
- L90 `test_worker_with_kanban_toolset_still_hides_board_routing(monkeypatch, tmp_path)` (function) — Task scope wins over profile config for board-routing tools.
- L120 `test_kanban_tools_visible_with_toolset_config(monkeypatch, tmp_path)` (function) — Orchestrator profiles with toolsets: [kanban] see all kanban tools.
- L150 `worker_env(monkeypatch, tmp_path)` (function) — Simulate being a worker: HERMES_HOME isolated, HERMES_KANBAN_TASK set
- L174 `test_show_defaults_to_env_task_id(worker_env)` (function)
- L185 `test_show_explicit_task_id(worker_env)` (function) — Peek at a different task than the one in env.
- L199 `test_list_filters_tasks(monkeypatch, worker_env)` (function) — kanban_list gives orchestrators filtered board discovery.
- L230 `test_list_rejects_invalid_status(monkeypatch, worker_env)` (function)
- L237 `test_list_rejects_bad_limit(monkeypatch, worker_env)` (function)
- L244 `test_list_parses_include_archived_string_false(monkeypatch, worker_env)` (function)
- L265 `test_list_parses_include_archived_string_true(monkeypatch, worker_env)` (function)
- L286 `test_list_rejects_bad_include_archived(monkeypatch, worker_env)` (function)
- L293 `test_complete_happy_path(worker_env)` (function)
- L314 `test_complete_metadata_round_trips_through_show(worker_env)` (function) — Structured completion metadata should be visible to downstream agents.
- L340 `test_complete_stamps_worker_session_id_from_env(monkeypatch, worker_env)` (function)
- L365 `test_complete_does_not_stamp_worker_session_id_without_scoped_task(monkeypatch, worker_env)` (function)
- L392 `test_complete_with_result_only(worker_env)` (function) — `result` alone (without summary) is accepted for legacy compat.
- L400 `test_complete_with_artifacts_lands_in_event_payload(worker_env)` (function) — ``artifacts=[...]`` rides into the completed event payload so the
- L434 `test_complete_artifacts_accepts_single_string(worker_env)` (function) — A bare string is auto-promoted to a single-element list for convenience.
- L453 `test_complete_artifacts_merges_with_explicit_metadata_field(worker_env)` (function) — If the worker passes metadata.artifacts AND the top-level artifacts
- L476 `test_complete_rejects_non_list_artifacts(worker_env)` (function) — Non-list, non-string artifacts should be rejected with a clear error.
- L487 `test_complete_rejects_no_handoff(worker_env)` (function)
- L493 `test_complete_rejects_non_dict_metadata(worker_env)` (function)
- L499 `test_complete_phantom_card_message_advertises_retry(worker_env)` (function) — A phantom-card rejection must surface a tool_error that explicitly
- L534 `test_complete_retry_with_empty_created_cards_succeeds(worker_env)` (function) — After a phantom rejection, retrying kanban_complete with
- L562 `test_complete_retry_with_corrected_created_cards_succeeds(worker_env)` (function) — After a phantom rejection, retrying kanban_complete with a
- L599 `test_block_happy_path(worker_env)` (function)
- L612 `test_block_rejects_empty_reason(worker_env)` (function)
- L619 `test_heartbeat_happy_path(worker_env)` (function)
- L626 `test_heartbeat_without_note(worker_env)` (function) — note is optional.
- L634 `test_heartbeat_extends_claim_expires(worker_env)` (function) — The kanban_heartbeat tool MUST extend claim_expires, not just
- L689 `test_comment_happy_path(worker_env)` (function)
- L710 `test_comment_rejects_empty_body(worker_env)` (function)
- L716 `test_comment_ignores_caller_supplied_author(worker_env)` (function) — ``args["author"]`` is no longer honored — the author is always
- L740 `test_comment_schema_omits_author_override()` (function) — The ``author`` property must not appear on KANBAN_COMMENT_SCHEMA;
- L750 `test_create_happy_path(worker_env)` (function)
- L771 `test_create_inherits_worker_dir_workspace(monkeypatch, worker_env)` (function) — A worker scoped to a dir: task that spawns a child without a
- L801 `test_create_explicit_workspace_beats_inheritance(monkeypatch, worker_env)` (function) — An explicit workspace arg overrides worker-task inheritance.
- L830 `test_create_no_worker_task_stays_scratch(monkeypatch, worker_env)` (function) — Orchestrator/CLI callers (no HERMES_KANBAN_TASK) still default to
- L848 `test_create_stamps_session_id_from_env(monkeypatch, worker_env)` (function) — When the agent loop runs under ACP, the server propagates the
- L871 `test_create_session_id_arg_overrides_env(monkeypatch, worker_env)` (function) — An explicit ``session_id`` arg from the model wins over the env
- L895 `test_create_session_id_absent_when_env_unset(monkeypatch, worker_env)` (function) — No env var, no arg → session_id stays NULL. Important for backwards
- L917 `test_create_rejects_no_title(worker_env)` (function)
- L923 `test_create_rejects_no_assignee(worker_env)` (function)
- L928 `test_create_rejects_non_list_parents(worker_env)` (function)
- L934 `test_create_parses_triage_string_false(worker_env)` (function)
- L952 `test_create_parses_triage_string_true(worker_env)` (function)
- L970 `test_create_rejects_bad_triage(worker_env)` (function)
- L980 `test_create_accepts_string_parent(worker_env)` (function) — Convenience: a single parent id as string is coerced to [id].
- L989 `test_create_accepts_skills_list(worker_env)` (function) — Tool writes the per-task skills through to the kernel.
- L1005 `test_create_accepts_skills_string(worker_env)` (function) — Convenience: a single skill name as string is coerced to [name].
- L1021 `test_create_rejects_non_list_skills(worker_env)` (function) — skills: 42 must be rejected, not silently dropped.
- L1030 `test_link_happy_path(worker_env)` (function)
- L1044 `test_link_rejects_self_reference(worker_env)` (function)
- L1050 `test_link_rejects_missing_args(worker_env)` (function)
- L1056 `test_link_rejects_cycle(worker_env)` (function) — A → B, then try to link B → A.
- L1070 `test_unblock_happy_path(monkeypatch, worker_env)` (function)
- L1093 `test_unblock_rejects_non_blocked_task(monkeypatch, worker_env)` (function)
- L1100 `test_worker_lifecycle_through_tools(worker_env)` (function) — Drive the full claim -> heartbeat -> comment -> complete lifecycle
- L1163 `test_kanban_guidance_not_in_normal_prompt(monkeypatch, tmp_path)` (function) — A normal chat session (no HERMES_KANBAN_TASK) must NOT have
- L1191 `test_kanban_guidance_in_worker_prompt(monkeypatch, tmp_path)` (function) — A worker session (HERMES_KANBAN_TASK set) MUST have the full
- L1226 `test_kanban_guidance_prompt_size_bounded(monkeypatch, tmp_path)` (function) — Sanity: the guidance block is under 4 KB so it doesn't blow
- L1259 `test_worker_complete_rejects_foreign_task_id(worker_env)` (function) — A worker cannot complete a task that isn't its own (#19534).
- L1284 `test_worker_block_rejects_foreign_task_id(worker_env)` (function) — A worker cannot block a task that isn't its own (#19534).
- L1307 `test_worker_heartbeat_rejects_foreign_task_id(worker_env)` (function) — A worker cannot heartbeat a task that isn't its own (#19534).
- L1325 `test_worker_can_comment_on_foreign_task(worker_env)` (function) — Cross-task commenting must remain unrestricted (#19713 policy).
- L1361 `test_worker_unblock_rejects_foreign_task_id(worker_env)` (function) — A worker cannot unblock any task — kanban_unblock is orchestrator-only.
- L1392 `test_worker_complete_own_task_still_works(worker_env)` (function) — The ownership check doesn't break the normal own-task happy path.
- L1401 `test_worker_complete_rejects_stale_run_id(worker_env, monkeypatch)` (function) — A retried worker cannot complete the task using an old run token.
- L1448 `test_orchestrator_complete_any_task_allowed(monkeypatch, tmp_path)` (function) — Orchestrator profiles (no HERMES_KANBAN_TASK) can still complete
- L1488 `multi_board_env(monkeypatch, tmp_path)` (function) — Isolated Hermes home with two distinct kanban boards seeded.
- L1534 `test_board_param_routes_create_to_alt_board(multi_board_env)` (function) — kanban_create with ``board="alt"`` must write into the alt board's DB,
- L1557 `test_board_param_routes_list_to_alt_board(multi_board_env)` (function) — kanban_list filters by the board parameter, not env-active.
- L1574 `test_board_param_routes_show_to_alt_board(multi_board_env)` (function) — kanban_show reads from the board parameter, not env-active.
- L1594 `test_board_param_routes_assign_via_create_to_alt(multi_board_env)` (function) — Workflow test for the 'assign' UX — create with assignee on a
- L1614 `test_board_param_routes_comment_to_alt_board(multi_board_env)` (function) — kanban_comment routes the insert to the alt board's DB.
- L1637 `test_board_param_routes_complete_to_alt_board(multi_board_env)` (function) — kanban_complete on the alt board closes the alt task, leaving
- L1664 `test_board_param_routes_block_to_alt_board(multi_board_env)` (function) — kanban_block targets the alt board's DB.
- L1685 `test_board_param_routes_unblock_to_alt_board(multi_board_env)` (function) — kanban_unblock targets the alt board's DB.
- L1704 `test_board_param_routes_heartbeat_to_alt_board(monkeypatch, tmp_path)` (function) — kanban_heartbeat targets the alt board's DB. Worker-scoped, so we
- L1736 `test_board_param_routes_link_to_alt_board(multi_board_env)` (function) — kanban_link operates on the alt board's DB.
- L1757 `test_board_param_none_falls_back_to_env(worker_env)` (function) — When ``board`` is omitted or None, behaviour is unchanged from
- L1778 `test_board_param_rejects_invalid_slug(multi_board_env)` (function) — A board slug that fails ``_normalize_board_slug`` surfaces as a
- L1788 `test_board_param_in_all_schemas()` (function) — All nine kanban_* tool schemas must expose an optional ``board``
