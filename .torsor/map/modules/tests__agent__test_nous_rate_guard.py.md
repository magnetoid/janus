---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/agent/test_nous_rate_guard.py

Symbols in `tests/agent/test_nous_rate_guard.py`.

- L11 `rate_guard_env(tmp_path, monkeypatch)` (function) — Isolate rate guard state to a temp directory.
- L20 `TestRecordNousRateLimit` (class) — Test recording rate limit state.
- L23 `test_records_with_header_reset(self, rate_guard_env)` (method)
- L36 `test_records_with_per_minute_header(self, rate_guard_env)` (method)
- L46 `test_records_with_retry_after_header(self, rate_guard_env)` (method)
- L56 `test_prefers_hourly_over_per_minute(self, rate_guard_env)` (method)
- L70 `test_falls_back_to_error_context_reset_at(self, rate_guard_env)` (method)
- L83 `test_falls_back_to_default_cooldown(self, rate_guard_env)` (method)
- L93 `test_custom_default_cooldown(self, rate_guard_env)` (method)
- L102 `test_creates_directory_if_missing(self, rate_guard_env)` (method)
- L109 `TestNousRateLimitRemaining` (class) — Test checking remaining rate limit time.
- L112 `test_returns_none_when_no_file(self, rate_guard_env)` (method)
- L117 `test_returns_remaining_seconds_when_active(self, rate_guard_env)` (method)
- L125 `test_returns_none_when_expired(self, rate_guard_env)` (method)
- L138 `test_handles_corrupt_file(self, rate_guard_env)` (method)
- L149 `TestClearNousRateLimit` (class) — Test clearing rate limit state.
- L152 `test_clears_existing_file(self, rate_guard_env)` (method)
- L167 `test_clear_when_no_file(self, rate_guard_env)` (method)
- L174 `TestFormatRemaining` (class) — Test human-readable duration formatting.
- L177 `test_seconds(self)` (method)
- L182 `test_minutes(self)` (method)
- L187 `test_exact_minutes(self)` (method)
- L192 `test_hours(self)` (method)
- L198 `TestParseResetSeconds` (class) — Test header parsing for reset times.
- L201 `test_case_insensitive_headers(self, rate_guard_env)` (method)
- L207 `test_returns_none_for_empty_headers(self)` (method)
- L213 `test_ignores_zero_values(self)` (method)
- L219 `test_ignores_invalid_values(self)` (method)
- L226 `TestAuxiliaryClientIntegration` (class) — Test that the auxiliary client respects the rate guard.
- L229 `test_try_nous_skips_when_rate_limited(self, rate_guard_env, monkeypatch)` (method)
- L245 `test_try_nous_works_when_not_rate_limited(self, rate_guard_env, monkeypatch)` (method)
- L256 `TestIsGenuineNousRateLimit` (class) — Tell a real account-level 429 apart from an upstream-capacity 429.
- L264 `test_exhausted_hourly_bucket_in_429_headers_is_genuine(self)` (method)
- L277 `test_exhausted_tokens_bucket_is_genuine(self)` (method)
- L290 `test_healthy_headers_on_429_are_upstream_capacity(self)` (method)
- L312 `test_bare_429_with_no_headers_is_upstream(self)` (method)
- L321 `test_exhausted_bucket_with_short_reset_is_not_genuine(self)` (method)
- L334 `test_last_known_state_with_exhausted_bucket_triggers_genuine(self)` (method)
- L361 `test_last_known_state_all_healthy_stays_upstream(self)` (method)
- L386 `test_none_last_state_and_no_headers_is_upstream(self)` (method)
