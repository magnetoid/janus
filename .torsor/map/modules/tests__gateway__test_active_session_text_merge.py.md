---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/gateway/test_active_session_text_merge.py

Symbols in `tests/gateway/test_active_session_text_merge.py`.

- L42 `_make_event(text: str, chat_id: str='12345', *, chat_type: str='dm', user_id: str='u1', user_name: str | None=None, thread_id: str | None=None)` (function)
- L67 `_DummyAdapter` (class)
- L68 `connect(self)` (method)
- L71 `disconnect(self)` (method)
- L74 `get_chat_info(self, chat_id)` (method)
- L77 `send(self, *args, **kwargs)` (method)
- L81 `_make_initialized_adapter()` (function)
- L85 `_make_adapter()` (function) — Build a BasePlatformAdapter without running its heavy __init__.
- L114 `_debounced_event(adapter: BasePlatformAdapter, session_key: str)` (function)
- L119 `test_rapid_text_followups_accumulate_instead_of_replacing()` (function) — Rapid TEXT follow-ups must all survive in the pending event.
- L136 `test_debounce_buffers_rapid_text_then_flushes_to_pending()` (function)
- L159 `test_debounce_resets_timer_on_new_arrival()` (function)
- L191 `test_active_drain_force_flushes_debounce_before_release()` (function)
- L222 `test_force_flush_cancels_timer_without_duplicate_processing()` (function)
- L245 `test_text_debounce_does_not_merge_different_senders()` (function)
- L275 `test_control_and_clarify_messages_bypass_text_debounce()` (function)
- L303 `test_debounce_skipped_when_busy_text_mode_not_queue()` (function)
- L316 `test_debounce_respects_env_var_override(monkeypatch)` (function)
- L323 `test_debounce_cleanup_in_cancel_background_tasks()` (function)
- L340 `test_single_followup_is_stored_as_is()` (function)
- L355 `test_adapter_defaults_to_interrupt_mode(monkeypatch)` (function)
- L362 `test_adapter_is_queue_text_debounce_candidate_when_queue_set()` (function)
- L368 `test_command_messages_bypass_debounce_even_in_queue_mode()` (function)
- L374 `test_busy_text_mode_respects_env_var_override(monkeypatch)` (function)
