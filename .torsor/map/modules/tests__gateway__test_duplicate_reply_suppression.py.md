---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_duplicate_reply_suppression.py

Symbols in `tests/gateway/test_duplicate_reply_suppression.py`.

- L33 `StubAdapter` (class) — Minimal concrete adapter for testing.
- L36 `__init__(self)` (method)
- L40 `connect(self)` (method)
- L43 `disconnect(self)` (method)
- L46 `send(self, chat_id, content, reply_to=None, metadata=None)` (method)
- L50 `send_typing(self, chat_id, metadata=None)` (method)
- L53 `get_chat_info(self, chat_id)` (method)
- L57 `_make_event(text='hello', chat_id='c1', user_id='u1')` (function)
- L74 `TestBaseInterruptSuppression` (class)
- L76 `test_stale_response_suppressed_when_interrupted(self)` (method) — When interrupt_event is set AND a pending message exists,
- L127 `test_response_not_suppressed_without_interrupt(self)` (method) — Normal case: no interrupt, response should be sent.
- L143 `test_response_not_suppressed_with_interrupt_but_no_pending(self)` (method) — Interrupt event set but no pending message (race already resolved) —
- L168 `TestOnlyFinalStreamDeliverySuppressesFinalSend` (class) — The gateway should suppress the fallback final send only when the
- L176 `_make_mock_stream_consumer(self, already_sent=False, final_response_sent=False)` (method)
- L183 `test_partial_stream_output_does_not_set_already_sent(self)` (method) — already_sent=True alone must NOT suppress final delivery.
- L198 `test_already_sent_not_set_when_nothing_sent(self)` (method) — When stream consumer hasn't sent anything, already_sent should
- L214 `test_already_sent_set_on_final_response_sent(self)` (method) — final_response_sent=True should suppress duplicate final sends.
- L229 `test_already_sent_not_set_on_failed_response(self)` (method) — Failed responses should never be suppressed — user needs to see
- L250 `TestEmptyResponseNotSuppressed` (class) — When the model returns '(empty)' after tool calls (e.g. mimo-v2-pro
- L259 `_make_mock_stream_consumer(self, already_sent=False, final_response_sent=False)` (method)
- L265 `_apply_suppression_logic(self, response, sc)` (method) — Reproduce the fixed logic from gateway/run.py return path.
- L275 `test_empty_sentinel_not_suppressed_with_already_sent(self)` (method) — '(empty)' final_response should NOT be suppressed even when
- L283 `test_empty_string_not_suppressed_with_already_sent(self)` (method) — Empty string final_response should NOT be suppressed.
- L290 `test_none_response_not_suppressed_with_already_sent(self)` (method) — None final_response should NOT be suppressed.
- L297 `test_real_response_still_suppressed_only_when_final_delivery_confirmed(self)` (method) — Normal non-empty response should be suppressed only when the final
- L305 `test_failed_empty_response_never_suppressed(self)` (method) — Failed responses are never suppressed regardless of content.
- L312 `TestQueuedMessageAlreadyStreamed` (class) — The queued-message path should skip the first response only when the
- L316 `_make_mock_sc(self, already_sent=False, final_response_sent=False)` (method)
- L322 `test_queued_path_only_skips_send_when_final_response_was_streamed(self)` (method) — Partial streamed output alone must not suppress the first response
- L333 `test_queued_path_detects_confirmed_final_stream_delivery(self)` (method) — Confirmed final streamed delivery should skip the resend.
- L345 `test_queued_path_detects_previewed_response_delivery(self)` (method) — A response already previewed via the adapter should not be resent
- L358 `test_queued_path_sends_when_not_streamed(self)` (method) — Nothing was streamed — first response should be sent before
- L369 `test_queued_path_with_no_stream_consumer(self)` (method) — No stream consumer at all (streaming disabled) — not streamed.
- L384 `TestCancellationHandlerDeliveryConfirmation` (class) — The stream consumer's cancellation handler should only set
- L391 `test_partial_only_no_accumulated_stays_false(self)` (method) — Cancelled after sending intermediate text, nothing accumulated.
- L407 `test_best_effort_succeeds_sets_true(self)` (method) — When accumulated content exists and best-effort send succeeds,
- L423 `test_best_effort_fails_stays_false(self)` (method) — When best-effort send fails (flood control, network), the
- L439 `test_preserves_existing_true(self)` (method) — If final_response_sent was already True before cancellation,
- L455 `test_old_behavior_would_have_promoted_partial(self)` (method) — Verify the old code would have incorrectly promoted
- L469 `TestFinalContentDeliveredSuppression` (class) — When stream consumer delivered the final content but the cosmetic
- L480 `test_content_delivered_but_final_edit_failed_suppresses(self)` (method) — final_content_delivered=True + final_response_sent=False
- L502 `test_intermediate_text_only_does_not_suppress(self)` (method) — already_sent=True from intermediate text + final_content_delivered=False
