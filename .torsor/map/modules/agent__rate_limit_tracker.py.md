---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# agent/rate_limit_tracker.py

Symbols in `agent/rate_limit_tracker.py`.

- L31 `RateLimitBucket` (class) — One rate-limit window (e.g. requests per minute).
- L40 `used(self)` (method)
- L44 `usage_pct(self)` (method)
- L50 `remaining_seconds_now(self)` (method) — Estimated seconds remaining until reset, adjusted for elapsed time.
- L57 `RateLimitState` (class) — Full rate-limit state parsed from response headers.
- L68 `has_data(self)` (method)
- L72 `age_seconds(self)` (method)
- L78 `_safe_int(value: Any, default: int=0)` (function)
- L85 `_safe_float(value: Any, default: float=0.0)` (function)
- L92 `parse_rate_limit_headers(headers: Mapping[str, str], provider: str='')` (function) — Parse x-ratelimit-* headers into a RateLimitState.
- L135 `_fmt_count(n: int)` (function) — Human-friendly number: 7999856 -> '8.0M', 33599 -> '33.6K', 799 -> '799'.
- L146 `_fmt_seconds(seconds: float)` (function) — Seconds -> human-friendly duration: '58s', '2m 14s', '58m 57s', '1h 2m'.
- L159 `_bar(pct: float, width: int=20)` (function) — ASCII progress bar: [████████░░░░░░░░░░░░] 40%.
- L167 `_bucket_line(label: str, bucket: RateLimitBucket, label_width: int=14)` (function) — Format one bucket as a single line.
- L182 `format_rate_limit_display(state: RateLimitState)` (function) — Format rate limit state for terminal/chat display.
- L226 `format_rate_limit_compact(state: RateLimitState)` (function) — One-line compact summary for status bars / gateway messages.
