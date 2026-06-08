---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# agent/nous_rate_guard.py

Symbols in `agent/nous_rate_guard.py`.

- L29 `_state_path()` (function) — Return the path to the Nous rate limit state file.
- L39 `_parse_reset_seconds(headers: Optional[Mapping[str, str]])` (function) — Extract the best available reset-time estimate from response headers.
- L71 `record_nous_rate_limit(*, headers: Optional[Mapping[str, str]]=None, error_context: Optional[dict[str, Any]]=None, default_cooldown: float=300.0)` (function) — Record that Nous Portal is rate-limited.
- L139 `nous_rate_limit_remaining()` (function) — Check if Nous Portal is currently rate-limited.
- L163 `clear_nous_rate_limit()` (function) — Clear the rate limit state (e.g., after a successful Nous request).
- L173 `format_remaining(seconds: float)` (function) — Format seconds remaining into human-readable duration.
- L192 `is_genuine_nous_rate_limit(*, headers: Optional[Mapping[str, str]]=None, last_known_state: Optional[Any]=None)` (function) — Decide whether a 429 from Nous Portal is a real account rate limit.
- L247 `_parse_buckets_from_headers(headers: Optional[Mapping[str, str]])` (function) — Extract (remaining, reset_seconds) per bucket from x-ratelimit-* headers.
- L286 `_has_exhausted_bucket(buckets: Mapping[str, tuple[Optional[int], Optional[float]]])` (function) — Return True when any bucket has remaining == 0 AND a meaningful reset window.
- L300 `_has_exhausted_bucket_in_object(state: Any)` (function) — Check a RateLimitState-like object for an exhausted bucket.
