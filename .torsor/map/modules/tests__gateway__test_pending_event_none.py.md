---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_pending_event_none.py

Symbols in `tests/gateway/test_pending_event_none.py`.

- L17 `_extract_channel_prompt(pending_event)` (function) — Reproduce the fixed logic from gateway/run.py.
- L29 `_extract_pending_text(interrupted, pending_event, interrupt_message)` (function) — Reproduce the fixed pending-text selection from gateway/run.py.
- L38 `TestPendingEventNoneChannelPrompt` (class) — Guard against AttributeError when pending_event is None.
- L41 `test_none_pending_event_returns_none_channel_prompt(self)` (method) — Path B: pending_event is None — must not raise AttributeError.
- L46 `test_pending_event_with_channel_prompt_passes_through(self)` (method) — Path A: pending_event present — channel_prompt is forwarded.
- L52 `test_pending_event_without_channel_prompt_returns_none(self)` (method) — Path A: pending_event present but has no channel_prompt attribute.
- L59 `TestControlInterruptMessages` (class) — Control interrupt reasons must not become follow-up user input.
- L62 `test_stop_requested_is_not_treated_as_pending_user_message(self)` (method)
- L66 `test_session_reset_requested_is_not_treated_as_pending_user_message(self)` (method)
- L70 `test_real_user_interrupt_message_still_requeues(self)` (method)
