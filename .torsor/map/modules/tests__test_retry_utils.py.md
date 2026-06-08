---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/test_retry_utils.py

Symbols in `tests/test_retry_utils.py`.

- L9 `test_backoff_is_exponential()` (function) — Base delay should double each attempt (before jitter).
- L18 `test_backoff_respects_max_delay()` (function) — Even with high attempt numbers, delay should not exceed max_delay.
- L25 `test_backoff_adds_jitter()` (function) — With jitter enabled, delays should vary across calls.
- L33 `test_backoff_attempt_1_is_base()` (function) — First attempt delay should equal base_delay (with no jitter).
- L39 `test_backoff_with_zero_base_delay_returns_max()` (function) — base_delay=0 should return max_delay (guard against busy-wait).
- L45 `test_backoff_with_extreme_attempt_returns_max()` (function) — Very large attempt numbers should not overflow and should return max_delay.
- L51 `test_backoff_negative_attempt_treated_as_one()` (function) — Negative attempt should not crash and behaves like attempt=1.
- L57 `test_backoff_thread_safety()` (function) — Concurrent calls should generally produce different delays.
- L77 `test_backoff_uses_locked_tick_for_seed(monkeypatch)` (function) — Seed derivation should use per-call tick captured under lock.
