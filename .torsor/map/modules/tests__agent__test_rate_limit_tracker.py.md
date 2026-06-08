---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/agent/test_rate_limit_tracker.py

Symbols in `tests/agent/test_rate_limit_tracker.py`.

- L35 `TestParseHeaders` (class)
- L36 `test_basic_parsing(self)` (method)
- L56 `test_no_headers(self)` (method)
- L60 `test_partial_headers(self)` (method)
- L72 `test_non_rate_limit_headers_ignored(self)` (method)
- L80 `test_malformed_values(self)` (method)
- L93 `TestBucket` (class)
- L94 `test_used(self)` (method)
- L98 `test_usage_pct(self)` (method)
- L102 `test_usage_pct_zero_limit(self)` (method)
- L106 `test_remaining_seconds_now(self)` (method)
- L112 `test_remaining_seconds_expired(self)` (method)
- L117 `TestFormatting` (class)
- L118 `test_fmt_count_millions(self)` (method)
- L122 `test_fmt_count_thousands(self)` (method)
- L126 `test_fmt_count_small(self)` (method)
- L130 `test_fmt_seconds_short(self)` (method)
- L134 `test_fmt_seconds_minutes(self)` (method)
- L138 `test_fmt_seconds_hours(self)` (method)
- L142 `test_bar(self)` (method)
- L148 `test_format_display_no_data(self)` (method)
- L153 `test_format_display_with_data(self)` (method)
- L163 `test_format_display_warning_on_high_usage(self)` (method)
- L172 `test_format_compact(self)` (method)
- L181 `test_format_compact_no_data(self)` (method)
- L187 `TestAgentIntegration` (class) — Test that AIAgent captures rate limit state correctly.
- L190 `test_capture_rate_limits_from_headers(self)` (method) — Simulate the header capture path without a real API call.
- L204 `test_capture_rate_limits_none_response(self)` (method) — _capture_rate_limits should handle None gracefully.
