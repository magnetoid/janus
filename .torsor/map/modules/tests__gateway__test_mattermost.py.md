---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_mattermost.py

Symbols in `tests/gateway/test_mattermost.py`.

- L15 `TestMattermostConfigLoading` (class)
- L16 `test_apply_env_overrides_mattermost(self, monkeypatch)` (method)
- L30 `test_mattermost_not_loaded_without_token(self, monkeypatch)` (method)
- L40 `test_mattermost_home_channel(self, monkeypatch)` (method)
- L55 `test_mattermost_url_warning_without_url(self, monkeypatch)` (method) — MATTERMOST_TOKEN set but MATTERMOST_URL missing should still load.
- L72 `_make_adapter()` (function) — Create a MattermostAdapter with mocked config.
- L84 `TestMattermostFormatMessage` (class)
- L85 `setup_method(self)` (method)
- L88 `test_image_markdown_to_url(self)` (method) — ![alt](url) should be converted to just the URL.
- L93 `test_image_markdown_strips_alt_text(self)` (method)
- L98 `test_regular_markdown_preserved(self)` (method) — Regular markdown (bold, italic, code) should be kept as-is.
- L103 `test_regular_links_preserved(self)` (method) — Non-image links should be preserved.
- L108 `test_plain_text_unchanged(self)` (method)
- L112 `test_multiple_images(self)` (method)
- L120 `TestMattermostTruncateMessage` (class)
- L121 `setup_method(self)` (method)
- L124 `test_short_message_single_chunk(self)` (method)
- L130 `test_long_message_splits(self)` (method)
- L137 `test_custom_max_length(self)` (method)
- L142 `test_exactly_at_limit(self)` (method)
- L152 `TestMattermostSend` (class)
- L153 `setup_method(self)` (method)
- L158 `test_send_calls_api_post(self)` (method) — send() should POST to /api/v4/posts with channel_id and message.
- L183 `test_send_empty_content_succeeds(self)` (method) — Empty content should return success without calling the API.
- L189 `test_send_with_thread_reply(self)` (method) — When reply_mode is 'thread', reply_to should become root_id.
- L221 `test_send_without_thread_no_root_id(self)` (method) — When reply_mode is 'off', reply_to should NOT set root_id.
- L241 `test_send_api_failure(self)` (method) — When API returns error, send should return failure.
- L261 `TestMattermostWebSocketParsing` (class)
- L262 `setup_method(self)` (method)
- L270 `test_parse_posted_event(self)` (method) — 'posted' events should extract message from double-encoded post JSON.
- L295 `test_ignore_own_messages(self)` (method) — Messages from the bot's own user_id should be ignored.
- L315 `test_ignore_non_posted_events(self)` (method) — Non-'posted' events should be ignored.
- L326 `test_ignore_system_posts(self)` (method) — Posts with a 'type' field (system messages) should be ignored.
- L347 `test_channel_type_mapping(self)` (method) — channel_type 'D' should map to 'dm'.
- L370 `test_thread_id_from_root_id(self)` (method) — Post with root_id should have thread_id set.
- L394 `test_invalid_post_json_ignored(self)` (method) — Invalid JSON in data.post should be silently ignored.
- L412 `TestMattermostMentionBehavior` (class)
- L413 `setup_method(self)` (method)
- L419 `_make_event(self, message, channel_type='O', channel_id='chan_456')` (method)
- L436 `test_require_mention_true_skips_without_mention(self)` (method) — Default: messages without @mention in channels are skipped.
- L445 `test_require_mention_false_responds_to_all(self)` (method) — MATTERMOST_REQUIRE_MENTION=false: respond to all channel messages.
- L452 `test_free_response_channel_responds_without_mention(self)` (method) — Messages in free-response channels don't need @mention.
- L460 `test_non_free_channel_still_requires_mention(self)` (method) — Channels NOT in free-response list still require @mention.
- L468 `test_dm_always_responds(self)` (method) — DMs (channel_type=D) always respond regardless of mention settings.
- L476 `test_mention_stripped_from_text(self)` (method) — @mention is stripped from message text.
- L493 `TestMattermostFileUpload` (class)
- L494 `setup_method(self)` (method)
- L500 `test_send_image_downloads_and_uploads(self, _mock_safe)` (method) — send_image should download the URL, upload via /api/v4/files, then post.
- L553 `TestMattermostDedup` (class)
- L554 `setup_method(self)` (method)
- L561 `test_duplicate_post_ignored(self)` (method) — The same post_id within the TTL window should be ignored.
- L587 `test_different_post_ids_both_processed(self)` (method) — Different post IDs should both be processed.
- L608 `test_prune_seen_clears_expired(self)` (method) — Dedup cache should remove entries older than TTL on overflow.
- L626 `test_seen_cache_tracks_post_ids(self)` (method) — Posts are tracked in the dedup cache.
- L636 `TestMattermostRequirements` (class)
- L637 `test_check_requirements_with_token_and_url(self, monkeypatch)` (method)
- L643 `test_check_requirements_without_token(self, monkeypatch)` (method)
- L649 `test_check_requirements_without_url(self, monkeypatch)` (method)
- L660 `TestMattermostMediaTypes` (class) — Verify that media_types contains actual MIME types (e.g. 'image/png')
- L665 `setup_method(self)` (method)
- L670 `_make_event(self, file_ids)` (method)
- L688 `test_image_media_type_is_full_mime(self)` (method) — An image attachment should produce 'image/png', not 'image'.
- L709 `test_audio_media_type_is_full_mime(self)` (method) — An audio attachment should produce 'audio/ogg', not 'audio'.
- L732 `test_document_media_type_is_full_mime(self)` (method) — A document attachment should produce 'application/pdf', not 'document'.
