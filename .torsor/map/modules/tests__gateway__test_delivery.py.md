---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_delivery.py

Symbols in `tests/gateway/test_delivery.py`.

- L11 `TestParseTargetPlatformChat` (class)
- L12 `test_explicit_telegram_chat(self)` (method)
- L18 `test_platform_only_no_chat_id(self)` (method)
- L24 `test_local_target(self)` (method)
- L29 `test_origin_with_source(self)` (method)
- L37 `test_origin_without_source(self)` (method)
- L42 `test_unknown_platform(self)` (method)
- L47 `TestTargetToStringRoundtrip` (class)
- L48 `test_origin_roundtrip(self)` (method)
- L53 `test_local_roundtrip(self)` (method)
- L57 `test_platform_only_roundtrip(self)` (method)
- L61 `test_explicit_chat_roundtrip(self)` (method)
- L71 `TestCaseSensitiveChatIdParsing` (class) — Test that chat IDs preserve their original case (issue #11768).
- L74 `test_slack_uppercase_chat_id_preserved(self)` (method) — Slack channel IDs like C123ABC should preserve case.
- L81 `test_slack_chat_id_with_thread_preserved(self)` (method) — Slack channel:thread IDs should preserve case.
- L88 `test_matrix_room_id_preserved(self)` (method) — Matrix room IDs like !RoomABC:example.org should preserve case.
- L104 `test_mixed_case_chat_id_roundtrip(self)` (method) — Mixed-case chat IDs should survive parse-to_string roundtrip.
- L113 `TestPlatformNameCaseInsensitivity` (class) — Test that platform names are case-insensitive.
- L116 `test_uppercase_platform_name(self)` (method) — Platform names should be case-insensitive.
- L122 `test_mixed_case_platform_name(self)` (method) — Mixed-case platform names should work.
- L128 `RecordingAdapter` (class)
- L129 `__init__(self)` (method)
- L133 `send(self, chat_id, content, metadata=None)` (method)
- L137 `ensure_dm_topic(self, chat_id, topic_name, force_create=False)` (method)
- L144 `StaleTopicAdapter` (class)
- L145 `__init__(self)` (method)
- L149 `send(self, chat_id, content, metadata=None)` (method)
- L155 `ensure_dm_topic(self, chat_id, topic_name, force_create=False)` (method)
- L163 `test_explicit_telegram_private_thread_requires_reply_anchor(tmp_path, monkeypatch)` (function)
- L176 `test_named_telegram_private_topic_is_created_before_delivery(tmp_path, monkeypatch)` (function)
- L200 `test_named_telegram_private_topic_refreshes_stale_thread_id(tmp_path, monkeypatch)` (function)
- L218 `test_explicit_telegram_private_thread_uses_reply_fallback_with_anchor(tmp_path, monkeypatch)` (function)
- L244 `test_explicit_telegram_direct_messages_topic_metadata_is_respected(tmp_path, monkeypatch)` (function)
- L260 `test_explicit_telegram_group_thread_does_not_mark_dm_fallback(tmp_path, monkeypatch)` (function)
- L271 `FailingAdapter` (class)
- L272 `send(self, chat_id, content, metadata=None)` (method)
- L277 `test_platform_send_failure_raises_for_delivery_result(tmp_path, monkeypatch)` (function)
