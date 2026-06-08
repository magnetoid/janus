---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:44'
updated: '2026-06-08T00:38:44'
---

# tests/tools/test_watch_patterns.py

Symbols in `tests/tools/test_watch_patterns.py`.

- L27 `registry()` (function) — Create a fresh ProcessRegistry.
- L32 `_make_session(sid='proc_test_watch', command='tail -f app.log', task_id='t1', watch_patterns=None)` (function)
- L52 `TestProcessSessionField` (class)
- L53 `test_default_empty(self)` (method)
- L60 `test_can_set_patterns(self)` (method)
- L69 `TestCheckWatchPatterns` (class)
- L70 `test_no_patterns_no_notification(self, registry)` (method) — No watch_patterns → no notifications.
- L76 `test_no_match_no_notification(self, registry)` (method) — Output that doesn't match any pattern → no notification.
- L82 `test_basic_match(self, registry)` (method) — Single matching line triggers a notification.
- L93 `test_match_carries_session_key_and_watcher_routing_metadata(self, registry)` (method)
- L112 `test_multiple_patterns(self, registry)` (method) — First matching pattern is reported.
- L122 `test_disabled_skips(self, registry)` (method) — Disabled watch produces no notifications.
- L129 `test_hit_counter_increments(self, registry)` (method) — Each delivered notification increments _watch_hits.
- L142 `test_output_truncation(self, registry)` (method) — Very long matched output is truncated.
- L157 `TestPerSessionRateLimit` (class)
- L158 `test_first_match_delivers(self, registry)` (method) — A fresh session with no prior cooldown delivers the first match.
- L169 `test_second_match_within_cooldown_is_suppressed(self, registry)` (method) — A second match inside the 15s cooldown is dropped and counted.
- L181 `test_many_drops_inside_window_count_as_ONE_strike(self, registry)` (method) — Multiple suppressions inside the same cooldown window = 1 strike.
- L190 `test_three_strikes_disables_watch_and_promotes_to_notify(self, registry)` (method) — Three consecutive strike windows → watch_disabled + notify_on_complete.
- L223 `test_clean_window_resets_strike_counter(self, registry)` (method) — A cooldown that expires with zero drops resets the consecutive counter.
- L243 `test_suppressed_count_in_next_delivery(self, registry)` (method) — Suppressed count from a strike window is reported in the next emit.
- L268 `TestCheckpointPersistence` (class)
- L269 `test_watch_patterns_in_checkpoint(self, registry)` (method) — watch_patterns is included in checkpoint data.
- L282 `test_watch_patterns_recovery(self, registry, tmp_path, monkeypatch)` (method) — watch_patterns survives checkpoint recovery.
- L312 `TestTerminalToolSchema` (class)
- L313 `test_schema_includes_watch_patterns(self)` (method)
- L320 `test_handler_passes_watch_patterns(self)` (method) — _handle_terminal passes watch_patterns to terminal_tool.
- L337 `TestCodeExecutionBlocked` (class)
- L338 `test_watch_patterns_blocked(self)` (method)
- L347 `TestSuppressAfterExit` (class)
- L348 `test_match_dropped_once_session_exited(self, registry)` (method) — watch_patterns notifications stop the moment session.exited is set.
- L357 `test_match_still_delivered_while_session_running(self, registry)` (method) — Sanity: while the process is still running, matches still deliver.
- L371 `TestMutualExclusion` (class)
- L372 `test_resolver_drops_watch_when_notify_set(self)` (method) — Both flags set → watch_patterns dropped with a note.
- L385 `test_resolver_keeps_watch_when_notify_off(self)` (method) — notify_on_complete=False → watch_patterns kept intact.
- L397 `test_resolver_keeps_notify_when_no_watch(self)` (method) — Only notify_on_complete set → no conflict.
- L409 `test_resolver_inert_when_not_background(self)` (method) — Without background=True, the whole thing is a no-op.
- L426 `TestGlobalCircuitBreaker` (class)
- L427 `test_trips_after_global_threshold(self, registry)` (method) — When >N matches fire across sessions in the window, breaker trips.
- L451 `test_cooldown_suppresses_and_then_releases(self, registry)` (method) — After trip, further events are suppressed; cooldown expiry emits release.
