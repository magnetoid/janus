---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_restart_resume_pending.py

Symbols in `tests/gateway/test_restart_resume_pending.py`.

- L56 `test_resume_pending_is_cleared_only_after_successful_turn()` (function) — Interrupted/failed drain results must keep the restart recovery marker.
- L73 `_make_source(platform=Platform.TELEGRAM, chat_id='123', user_id='u1')` (function)
- L77 `_make_store(tmp_path)` (function)
- L81 `_build_agent_history(history: list)` (function) — Mirror gateway/run.py's ``history → agent_history`` conversion.
- L106 `_simulate_note_injection(history: list, user_message: str, resume_entry: SessionEntry | None, *, agent_history: list | None=None, window_secs: float | None=None)` (function) — Mirror the note-injection logic in gateway/run.py _run_agent().
- L180 `TestSessionEntryResumeFields` (class)
- L181 `test_defaults(self)` (method)
- L193 `test_roundtrip_with_resume_fields(self)` (method)
- L209 `test_from_dict_legacy_without_resume_fields(self)` (method) — Old sessions.json without the new fields deserialize cleanly.
- L224 `test_malformed_timestamp_is_tolerated(self)` (method)
- L247 `TestMarkResumePending` (class)
- L248 `test_marks_existing_session(self, tmp_path)` (method)
- L259 `test_custom_reason_persists(self, tmp_path)` (method)
- L267 `test_returns_false_for_unknown_key(self, tmp_path)` (method)
- L271 `test_does_not_override_suspended(self, tmp_path)` (method) — suspended wins — mark_resume_pending is a no-op on a suspended entry.
- L283 `test_survives_roundtrip_through_json(self, tmp_path)` (method)
- L297 `TestClearResumePending` (class)
- L298 `test_clears_flag(self, tmp_path)` (method)
- L310 `test_returns_false_when_not_pending(self, tmp_path)` (method)
- L317 `test_returns_false_for_unknown_key(self, tmp_path)` (method)
- L327 `TestGetOrCreateResumePending` (class)
- L328 `test_resume_pending_preserves_session_id(self, tmp_path)` (method) — This is THE core behavioural fix — resume_pending ≠ new session.
- L343 `test_suspended_still_creates_new_session(self, tmp_path)` (method) — Regression guard — suspended must still force a clean slate.
- L356 `test_suspended_overrides_resume_pending(self, tmp_path)` (method) — Terminal escalation: a session that somehow has BOTH flags must
- L385 `TestSuspendRecentlyActiveSkipsResumePending` (class)
- L386 `test_resume_pending_entries_not_suspended(self, tmp_path)` (method)
- L398 `test_non_resume_pending_gets_resume_pending(self, tmp_path)` (method) — Non-resume sessions are now marked resume_pending (not suspended).
- L420 `TestResumePendingSystemNote` (class)
- L421 `_pending_entry(self, reason='restart_timeout')` (method)
- L433 `test_resume_pending_restart_note_mentions_restart(self)` (method)
- L446 `test_resume_pending_shutdown_note_mentions_shutdown(self)` (method)
- L457 `test_resume_pending_fires_without_tool_tail(self)` (method) — Key improvement over PR #9934: the restart-resume note fires
- L469 `test_resume_pending_subsumes_tool_tail_note(self)` (method) — When BOTH conditions are true, the restart-resume note wins —
- L486 `test_no_resume_pending_preserves_tool_tail_note(self)` (method) — Regression: the old PR #9934 tool-tail behaviour is unchanged.
- L499 `test_stale_resume_pending_does_not_inject_restart_note(self)` (method) — Old restart markers must not revive an unrelated stale task.
- L521 `test_fresh_tool_tail_preserves_auto_continue_note(self)` (method)
- L537 `test_stale_tool_tail_does_not_inject_auto_continue_note(self)` (method) — The core bug fix: stale tool-tail must not revive a dead task.
- L562 `test_stale_tool_tail_with_production_data_shape(self)` (method) — Regression guard for #16802: exercise the REAL production path
- L609 `test_freshness_gate_disabled_via_zero_window(self)` (method) — window_secs=0 restores pre-fix behaviour (always inject).
- L628 `test_legacy_history_without_timestamps_still_injects(self)` (method) — Transcripts predating timestamp persistence must keep the old
- L641 `test_no_note_when_nothing_to_resume(self)` (method)
- L655 `TestFreshnessHelpers` (class)
- L656 `test_coerce_datetime(self)` (method)
- L660 `test_coerce_epoch_seconds(self)` (method)
- L664 `test_coerce_epoch_milliseconds(self)` (method)
- L668 `test_coerce_iso_string(self)` (method)
- L673 `test_coerce_iso_string_with_z_suffix(self)` (method)
- L678 `test_coerce_numeric_string(self)` (method)
- L681 `test_coerce_rejects_garbage(self)` (method)
- L689 `test_is_fresh_unknown_is_fresh(self)` (method) — Legacy-compat: unknown timestamp → fresh.
- L694 `test_is_fresh_window_bounds(self)` (method)
- L709 `test_is_fresh_zero_window_always_fresh(self)` (method) — Opt-out: window_secs=0 disables the gate entirely.
- L718 `test_last_transcript_timestamp_skips_meta(self)` (method)
- L727 `test_last_transcript_timestamp_empty(self)` (method)
- L731 `test_last_transcript_timestamp_row_without_timestamp(self)` (method) — Legacy transcript row (no timestamp) returns None → caller
- L740 `test_auto_continue_freshness_window_reads_env(self, monkeypatch)` (method)
- L744 `test_auto_continue_freshness_window_default_when_unset(self, monkeypatch)` (method)
- L749 `test_auto_continue_freshness_window_malformed_falls_back(self, monkeypatch)` (method)
- L753 `test_auto_continue_freshness_window_empty_falls_back(self, monkeypatch)` (method)
- L764 `test_drain_timeout_marks_resume_pending()` (function) — End-to-end: a drain timeout during gateway stop should flag every
- L799 `test_drain_timeout_uses_restart_reason_when_restarting()` (function)
- L824 `test_drain_timeout_skips_pending_sentinel_sessions()` (function) — Pending sentinels — sessions whose AIAgent construction hasn't
- L863 `test_startup_auto_resume_schedules_fresh_pending_sessions()` (function) — Fresh resume_pending sessions should continue automatically after startup.
- L903 `test_startup_auto_resume_includes_crash_recovery()` (function) — Crash-recovered sessions (reason=restart_interrupted) are also auto-resumed.
- L936 `test_startup_auto_resume_skips_stale_entries()` (function) — Entries older than the freshness window must not be auto-resumed.
- L965 `test_startup_auto_resume_skips_suspended_and_originless()` (function) — suspended entries and entries with no origin are excluded.
- L1007 `test_startup_auto_resume_skips_disallowed_reasons()` (function) — Reasons outside the auto-resume set (e.g. a future custom reason) are skipped.
- L1038 `test_startup_auto_resume_skips_when_adapter_unavailable()` (function)
- L1064 `test_reconnect_reschedules_pending_after_late_platform_connect()` (function) — A platform offline at startup gets its pending sessions auto-resumed
- L1112 `test_reconnect_reschedule_is_platform_scoped()` (function) — The platform filter limits the pass to that platform's sessions, so
- L1163 `test_auto_resume_skips_sessions_with_running_agent()` (function) — A session already being resumed (agent in-flight) is not scheduled
- L1197 `test_restart_banner_uses_try_to_resume_wording()` (function) — The notification sent before drain should hedge the resume promise
- L1214 `test_restart_notifies_home_channel_even_without_active_sessions()` (function)
- L1232 `test_restart_home_channel_notification_dedupes_active_chat()` (function)
- L1248 `test_restart_home_channel_notification_not_deduped_across_threads()` (function)
- L1276 `test_restart_home_channel_notification_ignores_false_send_result()` (function)
- L1296 `TestStuckLoopEscalation` (class) — The existing .restart_failure_counts counter (PR #7536) remains the
- L1302 `test_escalation_via_stuck_loop_counter_overrides_resume_pending(self, tmp_path, monkeypatch)` (method) — Simulate a session that keeps getting restart-interrupted and
- L1335 `test_successful_turn_flow_clears_both_counter_and_resume_pending(self, tmp_path, monkeypatch)` (method) — The gateway's post-turn cleanup should clear both signals so a
- L1362 `test_increment_restart_failure_counts_uses_atomic_json_write(self, tmp_path, monkeypatch)` (method)
- L1389 `test_clear_restart_failure_count_uses_atomic_json_write_when_entries_remain(self, tmp_path, monkeypatch)` (method)
