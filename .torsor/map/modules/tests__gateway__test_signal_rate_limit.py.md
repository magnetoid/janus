---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_signal_rate_limit.py

Symbols in `tests/gateway/test_signal_rate_limit.py`.

- L16 `_reset_signal_scheduler()` (function) — Drop the process-wide scheduler so each test gets a clean bucket.
- L23 `_patch_sleep_and_time(monkeypatch, capture: list)` (function) — Replace asyncio.sleep inside the scheduler module so tests don't
- L41 `TestSchedulerInitialState` (class)
- L42 `test_default_capacity_matches_signal_cap(self)` (method)
- L46 `test_default_refill_rate_from_default_retry_after(self)` (method)
- L50 `test_starts_full(self)` (method)
- L55 `TestEstimateWait` (class)
- L56 `test_zero_when_bucket_has_enough(self)` (method)
- L61 `test_proportional_to_deficit_when_empty(self, monkeypatch)` (method) — Freeze monotonic so estimate_wait doesn't see fractional refill.
- L74 `TestAcquire` (class)
- L76 `test_acquire_zero_is_noop(self, monkeypatch)` (method)
- L87 `test_acquire_within_capacity_no_sleep(self, monkeypatch)` (method)
- L100 `test_acquire_when_empty_sleeps_for_deficit(self, monkeypatch)` (method)
- L117 `test_back_to_back_acquires_drain_then_wait(self, monkeypatch)` (method) — Two sequential acquires of capacity each: first immediate,
- L136 `test_acquire_more_tokens_than_capacity(self, monkeypatch)` (method)
- L142 `TestFeedback` (class)
- L143 `test_calibrates_refill_rate_from_retry_after(self)` (method)
- L150 `test_none_retry_after_leaves_rate(self)` (method)
- L156 `test_zeros_tokens(self)` (method)
- L163 `test_acquire_after_feedback_uses_calibrated_rate(self, monkeypatch)` (method) — signal-cli ≥v0.14.3: server says 'retry_after=42 for one
- L181 `TestRefillClamping` (class)
- L182 `test_refill_does_not_exceed_capacity(self, monkeypatch)` (method) — Even after a long elapsed window, refill clamps at capacity.
- L195 `TestFifoAcquire` (class)
- L197 `test_concurrent_acquires_serialize(self, monkeypatch)` (method) — Two coroutines acquiring full capacity each: the second waits
- L221 `TestSingleton` (class)
- L222 `test_get_scheduler_returns_same_instance(self)` (method)
- L227 `test_reset_scheduler_yields_new_instance(self)` (method)
