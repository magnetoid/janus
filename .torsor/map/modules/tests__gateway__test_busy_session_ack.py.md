---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_busy_session_ack.py

Symbols in `tests/gateway/test_busy_session_ack.py`.

- L39 `_make_event(text='hello', chat_id='123', platform_val='telegram')` (function) — Build a minimal MessageEvent.
- L56 `_make_runner()` (function) — Build a minimal GatewayRunner-like object for testing.
- L78 `_make_adapter(platform_val='telegram')` (function) — Build a minimal adapter mock.
- L95 `TestBusySessionAck` (class) — User sends a message while agent is running — should get acknowledgment.
- L99 `test_handle_message_queue_mode_queues_without_interrupt(self)` (method) — Runner queue mode must not interrupt an active agent for text follow-ups.
- L123 `test_sends_ack_when_agent_running(self)` (method) — First message during busy session should get a status ack.
- L163 `test_queue_mode_suppresses_interrupt_and_updates_ack(self)` (method) — When busy_input_mode is 'queue', message is queued WITHOUT interrupt.
- L191 `test_busy_text_mode_queue_delegates_to_adapter_handle_message(self)` (method) — busy_text_mode=queue lets the adapter debounce text silently.
- L217 `test_steer_mode_calls_agent_steer_no_interrupt_no_queue(self)` (method) — busy_input_mode='steer' injects via agent.steer() and skips queueing.
- L249 `test_steer_mode_falls_back_to_queue_when_agent_rejects(self)` (method) — If agent.steer() returns False, fall back to queue behavior.
- L278 `test_steer_mode_falls_back_to_queue_when_agent_pending(self)` (method) — If agent is still starting (sentinel), steer mode falls back to queue.
- L302 `test_debounce_suppresses_rapid_acks(self)` (method) — Second message within 30s should NOT send another ack.
- L345 `test_ack_after_cooldown_expires(self)` (method) — After 30s cooldown, a new message should send a fresh ack.
- L379 `test_includes_status_detail_when_opted_in(self, monkeypatch)` (method) — Ack message should include iteration and tool info when available.
- L417 `test_telegram_omits_status_detail_by_default(self)` (method) — Telegram busy acks stay concise unless busy_ack_detail is enabled.
- L448 `test_draining_still_works(self)` (method) — Draining case should still produce the drain-specific message.
- L471 `test_pending_sentinel_no_interrupt(self)` (method) — When agent is PENDING_SENTINEL, don't call interrupt (it has no method).
- L490 `test_no_adapter_falls_through(self)` (method) — If adapter is missing, return False so default path handles it.
- L504 `TestBusySessionOnboardingHint` (class) — First-touch hint appended to the busy-ack the first time it fires.
- L508 `test_first_busy_ack_appends_interrupt_hint(self, tmp_path, monkeypatch)` (method) — First busy-while-running message gets an extra hint about /busy.
- L551 `test_second_busy_ack_omits_hint(self, tmp_path, monkeypatch)` (method) — Once the flag is marked, the hint never appears again.
- L593 `test_queue_mode_hint_points_to_interrupt(self, tmp_path, monkeypatch)` (method) — In queue mode the hint should suggest /busy interrupt, not /busy queue.
