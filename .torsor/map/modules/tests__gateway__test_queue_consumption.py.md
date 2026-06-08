---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_queue_consumption.py

Symbols in `tests/gateway/test_queue_consumption.py`.

- L26 `_StubAdapter` (class)
- L27 `__init__(self)` (method)
- L30 `connect(self)` (method)
- L33 `disconnect(self)` (method)
- L36 `send(self, chat_id, content, reply_to=None, metadata=None)` (method)
- L40 `get_chat_info(self, chat_id)` (method)
- L48 `TestQueueMessageStorage` (class) — Verify /queue stores messages correctly in adapter._pending_messages.
- L51 `test_queue_stores_message_in_pending(self)` (method)
- L65 `test_get_pending_message_consumes_and_clears(self)` (method)
- L82 `test_dequeue_pending_event_preserves_voice_media_metadata(self)` (method)
- L102 `test_queue_does_not_set_interrupt_event(self)` (method) — The whole point of /queue — no interrupt signal.
- L123 `test_regular_message_sets_interrupt_event(self)` (method) — Contrast: regular messages DO trigger interrupt.
- L143 `TestQueueConsumptionAfterCompletion` (class) — Verify that pending messages are consumed after normal completion.
- L146 `test_pending_message_available_after_normal_completion(self)` (method) — After agent finishes without interrupt, pending message should
- L170 `test_multiple_queues_overflow_fifo(self)` (method) — Multiple /queue commands must stack in FIFO order, no merging.
- L202 `test_promote_advances_queue_fifo(self)` (method) — After the slot drains, the next overflow item is promoted.
- L249 `test_promote_stages_overflow_when_slot_already_populated(self)` (method) — If the slot was re-populated (e.g. by an interrupt follow-up),
- L301 `test_queue_depth_counts_slot_plus_overflow(self)` (method)
- L336 `test_enqueue_preserves_text_no_merging(self)` (method) — Each /queue item keeps its own text — never merged with neighbors.
