---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/run_agent/test_stream_interrupt_retry.py

Symbols in `tests/run_agent/test_stream_interrupt_retry.py`.

- L19 `_make_agent(**kwargs)` (function) — Create a minimal AIAgent for streaming tests.
- L37 `TestStreamInterruptBeforeRetry` (class) — Verify _interrupt_requested is checked before each streaming retry.
- L45 `test_interrupt_prevents_stream_retry(self, mock_close, mock_create)` (method) — When _interrupt_requested is set during a transient stream error,
- L84 `test_interrupt_before_first_attempt(self, mock_close, mock_create)` (method) — If _interrupt_requested is already set when the streaming call
- L101 `test_normal_retry_still_works_without_interrupt(self, mock_close, mock_create)` (method) — Without an interrupt, transient errors should still retry normally.
