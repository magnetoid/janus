---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_bluebubbles.py

Symbols in `tests/gateway/test_bluebubbles.py`.

- L10 `_make_adapter(monkeypatch, **extra)` (function)
- L26 `TestBlueBubblesConfigLoading` (class)
- L27 `test_apply_env_overrides_bluebubbles(self, monkeypatch)` (method)
- L46 `test_home_channel_set_from_env(self, monkeypatch)` (method)
- L58 `test_not_connected_without_password(self, monkeypatch)` (method)
- L68 `TestBlueBubblesHelpers` (class)
- L69 `test_check_requirements(self, monkeypatch)` (method)
- L76 `test_supports_message_editing_is_false(self, monkeypatch)` (method)
- L80 `test_truncate_message_omits_pagination_suffixes(self, monkeypatch)` (method)
- L88 `test_send_splits_paragraphs_into_multiple_bubbles(self, monkeypatch)` (method)
- L107 `test_format_message_strips_markdown(self, monkeypatch)` (method)
- L111 `test_format_message_preserves_underscores_in_identifiers(self, monkeypatch)` (method)
- L116 `test_strip_markdown_headers(self, monkeypatch)` (method)
- L120 `test_strip_markdown_links(self, monkeypatch)` (method)
- L124 `test_init_normalizes_webhook_path(self, monkeypatch)` (method)
- L128 `test_init_preserves_leading_slash(self, monkeypatch)` (method)
- L132 `test_server_url_normalized(self, monkeypatch)` (method)
- L136 `test_server_url_adds_scheme(self, monkeypatch)` (method)
- L140 `test_default_mention_patterns_match_hermes_variants(self, monkeypatch)` (method)
- L149 `test_custom_mention_patterns_override_defaults(self, monkeypatch)` (method)
- L159 `test_clean_mention_text_strips_leading_wake_word(self, monkeypatch)` (method)
- L167 `_FakeBlueBubblesRequest` (class)
- L168 `__init__(self, payload, password='secret')` (method)
- L173 `read(self)` (method)
- L177 `TestBlueBubblesMentionGating` (class)
- L179 `test_group_message_without_mention_is_acknowledged_and_skipped(self, monkeypatch)` (method)
- L208 `test_group_message_with_default_mention_is_dispatched_cleaned(self, monkeypatch)` (method)
- L237 `test_dm_message_does_not_require_mention(self, monkeypatch)` (method)
- L266 `TestBlueBubblesWebhookParsing` (class)
- L267 `test_webhook_prefers_chat_guid_over_message_guid(self, monkeypatch)` (method)
- L284 `test_webhook_can_fall_back_to_sender_when_chat_fields_missing(self, monkeypatch)` (method)
- L324 `test_webhook_extracts_chat_guid_from_chats_array_dm(self, monkeypatch)` (method) — BB v1.9+ webhook payloads omit top-level chatGuid; GUID is in chats[0].guid.
- L353 `test_webhook_extracts_chat_guid_from_chats_array_group(self, monkeypatch)` (method) — Group chat GUIDs contain ;+; and must be extracted from chats array.
- L381 `test_extract_payload_record_accepts_list_data(self, monkeypatch)` (method)
- L396 `test_extract_payload_record_dict_data(self, monkeypatch)` (method)
- L402 `test_extract_payload_record_fallback_to_message(self, monkeypatch)` (method)
- L409 `TestBlueBubblesGuidResolution` (class)
- L410 `test_raw_guid_returned_as_is(self, monkeypatch)` (method) — If target already contains ';' it's a raw GUID — return unchanged.
- L420 `test_empty_target_returns_none(self, monkeypatch)` (method)
- L430 `TestBlueBubblesAttachmentDownload` (class) — Verify _download_attachment routes to the correct cache helper.
- L433 `test_download_image_uses_image_cache(self, monkeypatch)` (method) — Image MIME routes to cache_image_from_bytes.
- L469 `test_download_audio_uses_audio_cache(self, monkeypatch)` (method) — Audio MIME routes to cache_audio_from_bytes.
- L504 `test_download_document_uses_document_cache(self, monkeypatch)` (method) — Non-image/audio MIME routes to cache_document_from_bytes.
- L539 `test_download_returns_none_without_client(self, monkeypatch)` (method) — No client → returns None gracefully.
- L556 `TestBlueBubblesWebhookUrl` (class) — _webhook_url property normalises local hosts to 'localhost'.
- L559 `test_default_host(self, monkeypatch)` (method)
- L567 `test_local_hosts_normalized(self, monkeypatch, host)` (method)
- L571 `test_custom_host_preserved(self, monkeypatch)` (method)
- L575 `test_register_url_embeds_password(self, monkeypatch)` (method) — _webhook_register_url should append ?password=... for inbound auth.
- L581 `test_register_url_url_encodes_password(self, monkeypatch)` (method) — Passwords with special characters must be URL-encoded.
- L586 `test_register_url_for_log_masks_password(self, monkeypatch)` (method) — Log-safe webhook URLs must never expose the webhook password.
- L594 `test_register_url_omits_query_when_no_password(self, monkeypatch)` (method) — If no password is configured, the register URL should be the bare URL.
- L606 `TestBlueBubblesWebhookRegistration` (class) — Tests for _register_webhook, _unregister_webhook, _find_registered_webhooks.
- L610 `_mock_client(get_response=None, post_response=None, delete_ok=True)` (method) — Build a tiny mock httpx.AsyncClient.
- L646 `test_find_registered_webhooks_returns_matches(self, monkeypatch)` (method)
- L662 `test_find_registered_webhooks_empty_when_none(self, monkeypatch)` (method)
- L673 `test_find_registered_webhooks_handles_api_error(self, monkeypatch)` (method)
- L690 `test_register_fresh(self, monkeypatch)` (method) — No existing webhook → POST creates one.
- L703 `test_register_accepts_201(self, monkeypatch)` (method) — BB might return 201 Created — must still succeed.
- L716 `test_register_reuses_existing(self, monkeypatch)` (method) — Crash resilience — existing registration is reused, no POST needed.
- L742 `test_register_returns_false_without_client(self, monkeypatch)` (method)
- L751 `test_register_returns_false_on_server_error(self, monkeypatch)` (method)
- L765 `test_unregister_removes_matching(self, monkeypatch)` (method)
- L779 `test_unregister_removes_all_duplicates(self, monkeypatch)` (method) — Multiple orphaned registrations for same URL — all get removed.
- L811 `test_unregister_returns_false_without_client(self, monkeypatch)` (method)
- L820 `test_unregister_handles_api_failure_gracefully(self, monkeypatch)` (method)
