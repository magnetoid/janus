---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/hermes_cli/test_kanban_diagnostics.py

Symbols in `tests/hermes_cli/test_kanban_diagnostics.py`.

- L27 `kanban_home(tmp_path, monkeypatch)` (function)
- L36 `_task(**overrides)` (function)
- L49 `_event(kind, ts=None, **payload)` (function)
- L57 `_run(outcome='completed', run_id=1, error=None)` (function)
- L70 `test_hallucinated_cards_fires_on_blocked_event()` (function)
- L93 `test_hallucinated_cards_clears_on_subsequent_completion()` (function)
- L103 `test_prose_phantom_refs_fires_after_clean_completion()` (function)
- L120 `test_prose_phantom_refs_clears_on_later_clean_edit()` (function)
- L132 `test_repeated_failures_fires_at_threshold_on_spawn()` (function) — A task with multiple spawn_failed runs gets a spawn-flavoured
- L153 `test_repeated_failures_fires_on_timeout_loop()` (function) — The rule surfaces for timeout loops too — that's the point of
- L173 `test_repeated_failures_escalates_to_critical()` (function)
- L179 `test_repeated_failures_below_threshold_silent()` (function)
- L184 `test_repeated_failures_default_matches_dispatcher_failure_limit()` (function) — Default dispatcher auto-blocks at 2 failures, so diagnostics must
- L201 `test_repeated_failures_derives_threshold_from_kanban_failure_limit()` (function)
- L220 `test_repeated_failures_explicit_threshold_overrides_failure_limit()` (function)
- L233 `test_config_from_kanban_config_preserves_explicit_diagnostics_threshold()` (function)
- L242 `test_repeated_crashes_counts_trailing_streak_only()` (function)
- L258 `test_repeated_crashes_breaks_on_recent_success()` (function)
- L268 `test_repeated_crashes_escalates_on_many_crashes()` (function)
- L275 `test_stuck_in_blocked_fires_past_threshold()` (function)
- L291 `test_stuck_in_blocked_silent_with_recent_comment()` (function)
- L301 `test_stuck_in_blocked_silent_when_not_blocked()` (function)
- L307 `test_repeated_crashes_surfaces_actual_error_in_title()` (function) — The title should lead with the actual error text so operators
- L325 `test_repeated_crashes_no_error_fallback_title()` (function)
- L335 `test_repeated_failures_surfaces_actual_error_in_title()` (function)
- L345 `test_repeated_crashes_truncates_huge_tracebacks()` (function) — Full Python tracebacks can be tens of KB. The title stays one
- L369 `test_diagnostics_sorted_critical_first()` (function) — A task with both a critical (many spawn failures) and a warning
- L390 `test_engine_works_on_sqlite_row_objects(kanban_home)` (function) — Regression: the rule functions must handle sqlite3.Row (which
- L430 `test_broken_rule_is_isolated(monkeypatch)` (function)
- L454 `test_stranded_in_ready_fires_when_age_exceeds_threshold()` (function) — Default threshold = 30 min. A ready task promoted 45 min ago
- L469 `test_stranded_in_ready_silent_below_threshold()` (function) — A ready task only 10 min old should NOT fire.
- L478 `test_stranded_in_ready_skips_non_ready_status()` (function) — Tasks not in ready status are out of scope (running tasks have
- L489 `test_stranded_in_ready_skips_unassigned_tasks()` (function) — Empty assignee = `skipped_unassigned` on the dispatcher already.
- L499 `test_stranded_in_ready_skips_claimed_tasks()` (function) — A live claim_lock means a worker is on it — even an old one. Don't
- L511 `test_stranded_in_ready_uses_latest_ready_transition()` (function) — When multiple ready-transition events exist, the rule should
- L525 `test_stranded_in_ready_severity_escalates_with_age()` (function) — warning → error → critical at 2x and 6x threshold.
- L545 `test_stranded_in_ready_respects_config_override()` (function) — Config override changes the threshold.
- L562 `test_stranded_in_ready_falls_back_to_created_at()` (function) — When events have no ready-transition kind, the rule falls back
- L578 `test_stranded_in_ready_works_on_real_db_row(kanban_home)` (function) — Round-trip through real kanban_db.connect() — confirms the rule
- L624 `_triage_task()` (function)
- L628 `test_triage_aux_unavailable_silent_without_config_context()` (function) — Low-level callers passing no config dict should not see this rule.
- L634 `test_triage_aux_unavailable_silent_when_main_model_visible()` (function) — Default `provider: auto` falls back to the main model — no warning.
- L645 `test_triage_aux_unavailable_silent_when_decomposer_explicit()` (function) — User explicitly configured decomposer → no warning, even without main.
- L657 `test_triage_aux_unavailable_fires_auto_decompose_on_no_fallback()` (function) — auto_decompose=True, no decomposer, no main model → warn about decomposer.
- L676 `test_triage_aux_unavailable_fires_auto_decompose_off_points_at_specifier()` (function) — auto_decompose=False → primary is specifier, not decomposer.
- L694 `test_triage_aux_unavailable_skips_non_triage_tasks()` (function)
- L701 `test_triage_aux_status_recognises_auto_default_as_not_explicit()` (function) — Default `provider: auto` with empty fields → not 'explicit'.
- L713 `test_triage_aux_status_recognises_explicit_model_only()` (function) — Even with provider=auto, a non-empty model counts as explicit.
- L725 `test_config_from_runtime_config_carries_aux_and_model()` (function)
- L737 `test_config_from_runtime_config_handles_empty_input()` (function)
- L742 `test_severity_at_or_above_uses_threshold_semantics()` (function)
