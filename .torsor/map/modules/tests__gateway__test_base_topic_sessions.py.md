---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_base_topic_sessions.py

Symbols in `tests/gateway/test_base_topic_sessions.py`.

- L15 `DummyTelegramAdapter` (class)
- L16 `__init__(self)` (method)
- L23 `connect(self)` (method)
- L26 `disconnect(self)` (method)
- L29 `send(self, chat_id, content, reply_to=None, metadata=None)` (method)
- L40 `send_typing(self, chat_id: str, metadata=None)` (method)
- L44 `get_chat_info(self, chat_id: str)` (method)
- L47 `on_processing_start(self, event: MessageEvent)` (method)
- L50 `on_processing_complete(self, event: MessageEvent, outcome: ProcessingOutcome)` (method)
- L54 `_make_event(chat_id: str, thread_id: str, message_id: str='1')` (function)
- L67 `TestBasePlatformTopicSessions` (class)
- L69 `test_handle_message_does_not_interrupt_different_topic(self, monkeypatch)` (method)
- L91 `test_handle_message_interrupts_same_topic(self, monkeypatch)` (method)
- L114 `test_process_message_background_replies_in_same_topic(self)` (method)
- L152 `test_process_message_background_marks_total_send_failure_unsuccessful(self)` (method)
- L178 `test_process_message_background_marks_exception_unsuccessful(self)` (method)
- L200 `test_process_message_background_marks_cancellation_unsuccessful(self)` (method)
- L228 `test_cancel_background_tasks_marks_expected_cancellation_cancelled(self)` (method)
- L254 `TestTelegramAutoTtsCaptionDelivery` (class)
- L256 `_make_voice_event(chat_id: str='-1001', thread_id: str='17585')` (method)
- L270 `_hold_typing()` (method)
- L277 `test_short_telegram_auto_tts_uses_caption_without_followup_text(self, tmp_path)` (method)
- L299 `test_long_telegram_auto_tts_keeps_followup_text_when_caption_would_truncate(self, tmp_path)` (method)
- L329 `test_telegram_auto_tts_send_failure_keeps_followup_text(self, tmp_path)` (method)
