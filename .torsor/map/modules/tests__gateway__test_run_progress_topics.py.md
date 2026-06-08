---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_run_progress_topics.py

Symbols in `tests/gateway/test_run_progress_topics.py`.

- L17 `ProgressCaptureAdapter` (class)
- L18 `__init__(self, platform=Platform.TELEGRAM)` (method)
- L24 `connect(self)` (method)
- L27 `disconnect(self)` (method)
- L30 `send(self, chat_id, content, reply_to=None, metadata=None)` (method)
- L41 `edit_message(self, chat_id, message_id, content)` (method)
- L51 `send_typing(self, chat_id, metadata=None)` (method)
- L54 `stop_typing(self, chat_id)` (method)
- L57 `get_chat_info(self, chat_id: str)` (method)
- L61 `SmallLimitProgressAdapter` (class) — Adapter with a tiny platform limit to exercise progress rollover.
- L66 `__init__(self, platform=Platform.TELEGRAM)` (method)
- L72 `_mint_id(self)` (method)
- L76 `send(self, chat_id, content, reply_to=None, metadata=None)` (method)
- L89 `edit_message(self, chat_id, message_id, content)` (method)
- L102 `MetadataEditProgressCaptureAdapter` (class)
- L103 `edit_message(self, chat_id, message_id, content, *, finalize: bool=False, metadata=None)` (method)
- L117 `NonEditingProgressCaptureAdapter` (class)
- L120 `edit_message(self, chat_id, message_id, content)` (method)
- L124 `FakeAgent` (class)
- L125 `__init__(self, **kwargs)` (method)
- L133 `run_conversation(self, message, conversation_history=None, task_id=None)` (method)
- L147 `LongPreviewAgent` (class) — Agent that emits a tool call with a very long preview string.
- L151 `__init__(self, **kwargs)` (method)
- L155 `run_conversation(self, message, conversation_history=None, task_id=None)` (method)
- L165 `DelayedProgressAgent` (class)
- L166 `__init__(self, **kwargs)` (method)
- L170 `run_conversation(self, message, conversation_history=None, task_id=None)` (method)
- L182 `ManyProgressLinesAgent` (class) — Emits enough tool-progress lines to exceed a single platform bubble.
- L185 `__init__(self, **kwargs)` (method)
- L189 `run_conversation(self, message, conversation_history=None, task_id=None)` (method)
- L207 `DelayedInterimAgent` (class)
- L208 `__init__(self, **kwargs)` (method)
- L212 `run_conversation(self, message, conversation_history=None, task_id=None)` (method)
- L224 `_make_runner(adapter)` (function)
- L249 `test_run_agent_progress_stays_in_originating_topic(monkeypatch, tmp_path)` (function)
- L296 `test_run_agent_progress_edits_keep_originating_topic_metadata(monkeypatch, tmp_path)` (function)
- L334 `test_run_agent_progress_does_not_use_event_message_id_for_telegram_dm(monkeypatch, tmp_path)` (function) — Telegram DM progress must not reuse event message id as thread metadata.
- L376 `test_run_agent_progress_uses_event_message_id_for_slack_dm(monkeypatch, tmp_path)` (function) — Slack DM progress should keep event ts fallback threading.
- L426 `test_run_agent_feishu_progress_replies_inside_existing_thread(monkeypatch, tmp_path)` (function) — Feishu needs reply_to plus reply_in_thread metadata for topic-scoped progress.
- L474 `_run_long_preview_helper(monkeypatch, tmp_path, preview_length=0)` (function) — Shared setup for long-preview truncation tests.
- L524 `test_all_mode_default_truncation_40_chars(monkeypatch, tmp_path)` (function) — When tool_preview_length is 0 (default), all/new mode truncates to 40 chars.
- L540 `test_all_mode_respects_custom_preview_length(monkeypatch, tmp_path)` (function) — When tool_preview_length is explicitly set (e.g. 120), all/new mode uses that.
- L557 `test_all_mode_no_truncation_when_preview_fits(monkeypatch, tmp_path)` (function) — Short previews (under the cap) are not truncated.
- L568 `CommentaryAgent` (class)
- L569 `__init__(self, **kwargs)` (method)
- L575 `run_conversation(self, message, conversation_history=None, task_id=None)` (method)
- L588 `PreviewedResponseAgent` (class)
- L589 `__init__(self, **kwargs)` (method)
- L593 `run_conversation(self, message, conversation_history=None, task_id=None)` (method)
- L604 `StreamingRefineAgent` (class)
- L605 `__init__(self, **kwargs)` (method)
- L609 `run_conversation(self, message, conversation_history=None, task_id=None)` (method)
- L623 `QueuedCommentaryAgent` (class)
- L626 `__init__(self, **kwargs)` (method)
- L630 `run_conversation(self, message, conversation_history=None, task_id=None)` (method)
- L641 `BackgroundReviewAgent` (class)
- L642 `__init__(self, **kwargs)` (method)
- L646 `run_conversation(self, message, conversation_history=None, task_id=None)` (method)
- L656 `VerboseAgent` (class) — Agent that emits a tool call with args whose JSON exceeds 200 chars.
- L660 `__init__(self, **kwargs)` (method)
- L664 `run_conversation(self, message, conversation_history=None, task_id=None)` (method)
- L677 `_run_with_agent(monkeypatch, tmp_path, agent_cls, *, session_id, pending_text=None, config_data=None, platform=Platform.TELEGRAM, chat_id='-1001', chat_type='group', thread_id='17585', adapter_cls=ProgressCaptureAdapter)` (function)
- L740 `test_run_agent_rolls_progress_bubble_before_platform_limit(monkeypatch, tmp_path)` (function) — Tool progress should start a second editable bubble before Telegram's limit.
- L773 `test_run_agent_surfaces_real_interim_commentary(monkeypatch, tmp_path)` (function)
- L787 `test_run_agent_surfaces_interim_commentary_by_default(monkeypatch, tmp_path)` (function)
- L799 `test_run_agent_suppresses_interim_commentary_when_disabled(monkeypatch, tmp_path)` (function)
- L813 `test_run_agent_tool_progress_does_not_control_interim_commentary(monkeypatch, tmp_path)` (function) — tool_progress=all with interim_assistant_messages=false should not surface commentary.
- L828 `test_run_agent_streaming_does_not_enable_completed_interim_commentary(monkeypatch, tmp_path)` (function) — Streaming alone with interim_assistant_messages=false should not surface commentary.
- L848 `test_display_streaming_does_not_enable_gateway_streaming(monkeypatch, tmp_path)` (function)
- L869 `test_run_agent_interim_commentary_works_with_tool_progress_off(monkeypatch, tmp_path)` (function)
- L888 `test_run_agent_bluebubbles_uses_commentary_send_path_for_quick_replies(monkeypatch, tmp_path)` (function)
- L908 `test_run_agent_previewed_final_marks_already_sent(monkeypatch, tmp_path)` (function)
- L922 `test_run_agent_matrix_streaming_omits_cursor(monkeypatch, tmp_path)` (function)
- L945 `TransformedStreamAgent` (class) — Streams a response, then signals the gateway that a plugin hook
- L952 `__init__(self, **kwargs)` (method)
- L956 `run_conversation(self, message, conversation_history=None, task_id=None)` (method)
- L969 `test_transformed_response_edits_streamed_message_in_place(monkeypatch, tmp_path)` (function) — When a transform_llm_output hook modifies the response after streaming,
- L1002 `test_run_agent_queued_message_does_not_treat_commentary_as_final(monkeypatch, tmp_path)` (function)
- L1020 `test_run_agent_defers_background_review_notification_until_release(monkeypatch, tmp_path)` (function)
- L1034 `test_base_processing_releases_post_delivery_callback_after_main_send()` (function) — Post-delivery callbacks on the adapter fire after the main response.
- L1080 `test_run_agent_drops_tool_progress_after_generation_invalidation(monkeypatch, tmp_path)` (function)
- L1142 `test_run_agent_drops_interim_commentary_after_generation_invalidation(monkeypatch, tmp_path)` (function)
- L1202 `test_keep_typing_stops_immediately_when_interrupt_event_is_set()` (function)
- L1228 `test_verbose_mode_does_not_truncate_args_by_default(monkeypatch, tmp_path)` (function) — Verbose mode with default tool_preview_length (0) should NOT truncate args.
- L1250 `test_verbose_mode_respects_explicit_tool_preview_length(monkeypatch, tmp_path)` (function) — When tool_preview_length is set to a positive value, verbose truncates to that.
