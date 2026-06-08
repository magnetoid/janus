---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_discord_send.py

Symbols in `tests/gateway/test_discord_send.py`.

- L11 `_ensure_discord_mock()` (function)
- L49 `test_send_retries_without_reference_when_reply_target_is_system_message()` (function)
- L87 `test_send_retries_without_reference_when_reply_target_is_deleted()` (function)
- L126 `test_send_does_not_retry_on_unrelated_errors()` (function) — Regression guard: errors unrelated to the reply reference (e.g. 50013
- L170 `TestIsForumParent` (class)
- L171 `test_none_returns_false(self)` (method)
- L175 `test_forum_channel_class_instance(self)` (method)
- L185 `test_type_value_15(self)` (method)
- L190 `test_regular_channel_returns_false(self)` (method)
- L195 `test_thread_returns_false(self)` (method)
- L202 `test_send_to_forum_creates_thread_post()` (function)
- L229 `test_send_to_forum_sends_remaining_chunks()` (function)
- L264 `test_send_to_forum_create_thread_failure()` (function)
- L289 `test_send_to_forum_follow_up_chunk_failures_collected_as_warnings()` (function) — Partial-send chunk failures surface in raw_response['warnings'].
- L323 `test_forum_post_file_creates_thread_with_attachment()` (function) — _forum_post_file routes file-bearing sends to create_thread with file kwarg.
- L354 `test_forum_post_file_uses_filename_when_no_content()` (function) — Thread name falls back to file.filename when no content is provided.
- L374 `test_forum_post_file_creation_failure()` (function) — _forum_post_file returns a failed SendResult when create_thread raises.
- L398 `test_typing_task_removed_after_api_error()` (function) — When typing API call fails, stale task must be removed so typing can restart.
- L414 `test_typing_restartable_after_error()` (function) — After a typing error, send_typing should start a new task (not blocked by stale entry).
- L435 `test_typing_stop_cleans_up()` (function) — stop_typing should remove the task from _typing_tasks.
