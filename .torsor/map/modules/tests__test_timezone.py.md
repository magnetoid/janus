---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/test_timezone.py

Symbols in `tests/test_timezone.py`.

- L23 `_reset_hermes_time_cache()` (function) — Reset the hermes_time module cache (replacement for removed reset_cache).
- L34 `TestHermesTimeNow` (class) — Test the timezone-aware now() helper.
- L37 `setup_method(self)` (method)
- L40 `teardown_method(self)` (method)
- L44 `test_valid_timezone_applies(self)` (method) — With a valid IANA timezone, now() returns time in that zone.
- L53 `test_utc_timezone(self)` (method) — UTC timezone works.
- L59 `test_us_eastern(self)` (method) — US/Eastern timezone works (DST-aware zone).
- L68 `test_invalid_timezone_falls_back(self, caplog)` (method) — Invalid timezone logs warning and falls back to server-local.
- L77 `test_empty_timezone_uses_local(self)` (method) — No timezone configured → server-local time (still tz-aware).
- L83 `test_format_unchanged(self)` (method) — Timestamp formatting matches original strftime pattern.
- L93 `test_cache_invalidation(self)` (method) — Changing env var + reset_cache picks up new timezone.
- L106 `TestGetTimezone` (class) — Test get_timezone().
- L109 `setup_method(self)` (method)
- L112 `teardown_method(self)` (method)
- L116 `test_returns_zoneinfo_for_valid(self)` (method)
- L122 `test_returns_none_for_empty(self)` (method)
- L127 `test_returns_none_for_invalid(self)` (method)
- L139 `TestCodeExecutionTZ` (class) — Verify TZ env var is passed to sandboxed child process via real execute_code.
- L143 `_import_execute_code(self, monkeypatch)` (method) — Lazy-import execute_code to avoid pulling in firecrawl at collection time.
- L154 `teardown_method(self)` (method)
- L157 `_mock_handle(self, function_name, function_args, task_id=None, user_task=None)` (method)
- L161 `test_tz_injected_when_configured(self)` (method) — When HERMES_TIMEZONE is set, child process sees TZ env var.
- L191 `test_tz_not_injected_when_empty(self)` (method) — When HERMES_TIMEZONE is not set, child process has no TZ.
- L210 `TestCronTimezone` (class) — Verify cron paths use timezone-aware now().
- L213 `setup_method(self)` (method)
- L216 `teardown_method(self)` (method)
- L220 `test_parse_schedule_duration_uses_tz_aware_now(self)` (method) — parse_schedule('30m') should produce a tz-aware run_at.
- L229 `test_compute_next_run_tz_aware(self)` (method) — compute_next_run returns tz-aware timestamps.
- L238 `test_get_due_jobs_handles_naive_timestamps(self, tmp_path, monkeypatch)` (method) — Backward compat: naive timestamps from before tz support don't crash.
- L261 `test_ensure_aware_naive_preserves_absolute_time(self)` (method) — _ensure_aware must preserve the absolute instant for naive datetimes.
- L290 `test_ensure_aware_normalizes_aware_to_hermes_tz(self)` (method) — Already-aware datetimes should be normalized to Hermes tz.
- L307 `test_ensure_aware_due_job_not_skipped_when_system_ahead(self, tmp_path, monkeypatch)` (method) — Reproduce the actual bug: system tz ahead of Hermes tz caused
- L340 `test_get_due_jobs_naive_cross_timezone(self, tmp_path, monkeypatch)` (method) — Naive past timestamps must be detected as due even when Hermes tz
- L368 `test_create_job_stores_tz_aware_timestamps(self, tmp_path, monkeypatch)` (method) — New jobs store timezone-aware created_at and next_run_at.
