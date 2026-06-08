---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# gateway/stream_consumer.py

Symbols in `gateway/stream_consumer.py`.

- L51 `StreamConsumerConfig` (class) — Runtime config for a single stream consumer instance.
- L79 `GatewayStreamConsumer` (class) — Async consumer that progressively edits a platform message with streamed tokens.
- L115 `__init__(self, adapter: Any, chat_id: str, config: Optional[StreamConsumerConfig]=None, metadata: Optional[dict]=None, on_new_message: Optional[callable]=None, initial_reply_to_id: Optional[str]=None)` (method)
- L187 `already_sent(self)` (method) — True if at least one message was sent or edited during the run.
- L192 `final_response_sent(self)` (method) — True when the stream consumer delivered the final assistant reply.
- L197 `message_id(self)` (method) — The Discord/chat message ID of the last-sent or edited message.
- L202 `final_content_delivered(self)` (method) — True when the final response content reached the user, even if
- L207 `_edit_message(self, *, message_id: str, content: str, finalize: bool=False)` (method) — Edit via the adapter, passing routing metadata when supported.
- L236 `on_segment_break(self)` (method) — Finalize the current stream segment and start a fresh message.
- L240 `on_commentary(self, text: str)` (method) — Queue a completed interim assistant commentary message.
- L245 `_notify_new_message(self)` (method) — Fire the on_new_message callback, swallowing any errors.
- L255 `_reset_segment_state(self, *, preserve_no_edit: bool=False)` (method)
- L281 `on_delta(self, text: str)` (method) — Thread-safe callback — called from the agent's worker thread.
- L293 `finish(self)` (method) — Signal that the stream is complete.
- L305 `_filter_and_accumulate(self, text: str)` (method) — Add a text delta to the accumulated buffer, suppressing think blocks.
- L393 `_flush_think_buffer(self)` (method) — Flush any held-back partial-tag buffer into accumulated text.
- L403 `run(self)` (method) — Async task that drains the queue and edits the platform message.
- L679 `_clean_for_display(text: str)` (method) — Strip MEDIA: directives and internal markers from text before display.
- L698 `_send_new_chunk(self, text: str, reply_to_id: Optional[str])` (method) — Send a new message chunk, optionally threaded to a previous message.
- L729 `_visible_prefix(self)` (method) — Return the visible text already shown in the streamed message.
- L736 `_continuation_text(self, final_text: str)` (method) — Return only the part of final_text the user has not already seen.
- L744 `_split_text_chunks(text: str, limit: int, len_fn: 'Callable[[str], int]'=len)` (method) — Split text into reasonably sized chunks for fallback sends.
- L764 `_send_fallback_final(self, text: str)` (method) — Send the final continuation after streaming edits stop working.
- L892 `_is_flood_error(self, result)` (method) — Check if a SendResult failure is due to flood control / rate limiting.
- L898 `_resolve_draft_streaming(self)` (method) — Decide whether this run should use native draft streaming.
- L941 `_send_draft_frame(self, text: str)` (method) — Emit a single animated draft frame for the current accumulated text.
- L981 `_flush_segment_tail_on_edit_failure(self)` (method) — Deliver un-sent tail content before a segment-break reset.
- L1014 `_try_strip_cursor(self)` (method) — Best-effort edit to remove the cursor from the last visible message.
- L1034 `_send_commentary(self, text: str)` (method) — Send a completed interim assistant commentary message.
- L1060 `_should_send_fresh_final(self)` (method) — Return True when a long-lived preview should be replaced with a
- L1082 `_try_fresh_final(self, text: str, *, is_turn_final: bool=True)` (method) — Send ``text`` as a brand-new message (best-effort delete the old
- L1141 `_send_or_edit(self, text: str, *, finalize: bool=False, is_turn_final: bool=True)` (method) — Send or edit the streaming message.
