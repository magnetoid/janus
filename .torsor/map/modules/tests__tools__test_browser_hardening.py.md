---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/tools/test_browser_hardening.py

Symbols in `tests/tools/test_browser_hardening.py`.

- L13 `_reset_caches()` (function) — Reset all module-level caches so tests start clean.
- L26 `_clean_caches()` (function)
- L36 `TestDeadCodeRemoval` (class) — Verify dead code was actually removed.
- L39 `test_no_default_session_timeout(self)` (method)
- L43 `test_browser_close_schema_removed(self)` (method)
- L53 `TestFindAgentBrowserCache` (class)
- L55 `test_cached_after_first_call(self)` (method)
- L63 `test_cache_cleared_by_cleanup(self)` (method)
- L70 `test_not_found_cached_raises_on_subsequent(self)` (method) — After FileNotFoundError, subsequent calls should raise from cache.
- L96 `TestCommandTimeoutCache` (class)
- L98 `test_default_is_30(self)` (method)
- L103 `test_reads_from_config(self)` (method)
- L109 `test_cached_after_first_call(self)` (method)
- L122 `TestHomebrewNodeDirsCache` (class)
- L124 `test_lru_cached(self)` (method)
- L134 `TestUrlDecodedSecretCheck` (class) — Verify that URL-encoded API keys are caught by the exfiltration guard.
- L137 `test_encoded_key_blocked_in_navigate(self)` (method) — browser_navigate should block URLs with percent-encoded API keys.
- L156 `TestRecordingSessionsThreadSafety` (class) — Verify _recording_sessions is accessed under _cleanup_lock.
- L159 `test_start_recording_uses_lock(self)` (method)
- L165 `test_stop_recording_uses_lock(self)` (method)
- L171 `test_emergency_cleanup_clears_under_lock(self)` (method) — _recording_sessions.clear() in emergency cleanup should be under _cleanup_lock.
- L187 `TestTruncateSnapshot` (class)
- L189 `test_short_snapshot_unchanged(self)` (method)
- L194 `test_long_snapshot_truncated_at_line_boundary(self)` (method)
- L209 `test_truncation_reports_remaining_count(self)` (method)
- L222 `TestScrollOptimization` (class)
- L224 `test_agent_browser_path_uses_pixel_scroll(self)` (method) — Verify agent-browser path uses single pixel-based scroll, not 5x loop.
- L236 `TestEmptyStdoutFailure` (class)
- L238 `test_empty_stdout_returns_failure(self)` (method) — Verify _run_browser_command returns failure on empty stdout.
- L245 `test_empty_ok_commands_is_module_level_frozenset(self)` (method) — _EMPTY_OK_COMMANDS should be a module-level frozenset, not defined inside a function.
- L258 `TestCamofoxEvalFix` (class)
- L260 `test_uses_correct_ensure_tab_signature(self)` (method) — _camofox_eval should pass task_id string to _ensure_tab, not a session dict.
