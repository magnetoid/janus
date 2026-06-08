---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/hermes_cli/test_goals.py

Symbols in `tests/hermes_cli/test_goals.py`.

- L17 `hermes_home(tmp_path, monkeypatch)` (function) — Isolated HERMES_HOME so SessionDB.state_meta writes don't clobber the real one.
- L39 `TestParseJudgeResponse` (class)
- L40 `test_clean_json_done(self)` (method)
- L47 `test_clean_json_continue(self)` (method)
- L54 `test_json_in_markdown_fence(self)` (method)
- L62 `test_json_embedded_in_prose(self)` (method) — Some models prefix reasoning before emitting JSON — we extract it.
- L71 `test_string_done_values(self)` (method)
- L81 `test_malformed_json_fails_open(self)` (method) — Non-JSON → not done, with error-ish reason (so judge_goal can map to continue).
- L89 `test_empty_response(self)` (method)
- L102 `TestJudgeGoal` (class)
- L103 `test_empty_goal_skipped(self)` (method)
- L109 `test_empty_response_continues(self)` (method)
- L115 `test_no_aux_client_continues(self)` (method) — Fail-open: if no aux client, we must return continue, not skipped/done.
- L126 `test_api_error_continues(self)` (method) — Judge exception → fail-open continue (don't wedge progress on judge bugs).
- L140 `test_judge_says_done(self)` (method)
- L159 `test_judge_says_continue(self)` (method)
- L184 `TestGoalManager` (class)
- L185 `test_no_goal_initial(self, hermes_home)` (method)
- L194 `test_set_then_status(self, hermes_home)` (method)
- L207 `test_set_rejects_empty(self, hermes_home)` (method)
- L216 `test_pause_and_resume(self, hermes_home)` (method)
- L230 `test_clear(self, hermes_home)` (method)
- L239 `test_persistence_across_managers(self, hermes_home)` (method) — Key invariant: a second manager on the same session sees the goal.
- L255 `test_evaluate_after_turn_done(self, hermes_home)` (method) — Judge says done → status=done, no continuation.
- L272 `test_evaluate_after_turn_continue_under_budget(self, hermes_home)` (method)
- L289 `test_evaluate_after_turn_budget_exhausted(self, hermes_home)` (method) — When turn budget hits ceiling, auto-pause instead of continuing.
- L310 `test_evaluate_after_turn_inactive(self, hermes_home)` (method) — evaluate_after_turn is a no-op when goal isn't active.
- L325 `test_continuation_prompt_shape(self, hermes_home)` (method) — The continuation prompt must include the goal text verbatim —
- L344 `test_goal_command_in_registry()` (function)
- L352 `test_goal_command_dispatches_in_cli_registry_helpers()` (function) — goal shows up in autocomplete / help categories alongside other Session cmds.
- L366 `TestJudgeParseFailureAutoPause` (class) — Regression: weak judge models (e.g. deepseek-v4-flash) that return
- L371 `test_parse_response_flags_empty_as_parse_failure(self)` (method)
- L379 `test_parse_response_flags_non_json_as_parse_failure(self)` (method)
- L389 `test_parse_response_clean_json_is_not_parse_failure(self)` (method)
- L398 `test_api_error_does_not_count_as_parse_failure(self)` (method) — Transient network/API errors must not trip the auto-pause guard.
- L412 `test_empty_judge_reply_flagged_as_parse_failure(self)` (method) — End-to-end: judge returns empty content → parse_failed=True.
- L428 `test_auto_pause_after_three_consecutive_parse_failures(self, hermes_home)` (method) — N=3 consecutive parse failures → auto-pause with config pointer.
- L457 `test_parse_failure_counter_resets_on_good_reply(self, hermes_home)` (method) — A single good judge reply resets the counter — transient flakes don't pause.
- L481 `test_parse_failure_counter_not_incremented_by_api_errors(self, hermes_home)` (method) — API/transport errors must NOT count toward the auto-pause threshold.
- L498 `test_consecutive_parse_failures_persists_across_goalmanager_reloads(self, hermes_home)` (method) — The counter must be durable so cross-session resumes see it.
- L524 `TestGoalStateSubgoalsBackcompat` (class)
- L525 `test_old_state_meta_row_loads_without_subgoals(self)` (method) — A goal serialized BEFORE the subgoals field existed must
- L543 `test_subgoals_round_trip(self)` (method)
- L550 `TestGoalManagerSubgoals` (class)
- L551 `test_add_subgoal(self, hermes_home)` (method)
- L559 `test_add_subgoal_requires_active_goal(self, hermes_home)` (method)
- L566 `test_add_empty_subgoal_rejected(self, hermes_home)` (method)
- L574 `test_remove_subgoal(self, hermes_home)` (method)
- L585 `test_remove_subgoal_out_of_range(self, hermes_home)` (method)
- L596 `test_clear_subgoals(self, hermes_home)` (method)
- L606 `test_subgoals_persist_across_reloads(self, hermes_home)` (method) — Subgoals stored in SessionDB survive a fresh GoalManager.
- L618 `TestContinuationPromptWithSubgoals` (class)
- L619 `test_empty_subgoals_uses_original_template(self, hermes_home)` (method)
- L628 `test_with_subgoals_includes_them(self, hermes_home)` (method)
- L642 `TestJudgeGoalWithSubgoals` (class)
- L643 `test_judge_uses_subgoals_template_when_provided(self, hermes_home)` (method) — judge_goal switches templates when subgoals is non-empty.
- L691 `test_judge_uses_original_template_when_no_subgoals(self, hermes_home)` (method)
- L723 `TestStatusLineSubgoalCount` (class)
- L724 `test_status_line_no_subgoals(self, hermes_home)` (method)
- L732 `test_status_line_with_subgoals(self, hermes_home)` (method)
