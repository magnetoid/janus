---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_wecom.py

Symbols in `tests/gateway/test_wecom.py`.

- L16 `TestWeComRequirements` (class)
- L17 `test_returns_false_without_aiohttp(self, monkeypatch)` (method)
- L24 `test_returns_false_without_httpx(self, monkeypatch)` (method)
- L31 `test_returns_true_when_available(self, monkeypatch)` (method)
- L39 `TestWeComAdapterInit` (class)
- L40 `test_declares_non_editable_message_capability(self)` (method)
- L45 `test_reads_config_from_extra(self)` (method)
- L66 `test_falls_back_to_env_vars(self, monkeypatch)` (method)
- L78 `TestWeComConnect` (class)
- L80 `test_connect_records_missing_credentials(self, monkeypatch)` (method)
- L97 `test_connect_records_handshake_failure_details(self, monkeypatch)` (method)
- L126 `TestWeComQrScan` (class)
- L132 `test_qr_scan_timeout_uses_monotonic_clock(self, mock_request, mock_urlopen, _mock_logger, mock_json_loads, mock_time)` (method)
- L168 `TestWeComReplyMode` (class)
- L170 `test_send_uses_passive_reply_markdown_when_reply_context_exists(self)` (method)
- L191 `test_send_image_file_uses_passive_reply_media_when_reply_context_exists(self)` (method)
- L223 `TestExtractText` (class)
- L224 `test_extracts_plain_text(self)` (method)
- L235 `test_extracts_mixed_text(self)` (method)
- L251 `test_extracts_voice_and_quote(self)` (method)
- L264 `TestCallbackDispatch` (class)
- L267 `test_dispatch_accepts_new_and_legacy_callback_cmds(self, cmd)` (method)
- L278 `TestPolicyHelpers` (class)
- L279 `test_dm_allowlist(self)` (method)
- L288 `test_dm_allowlist_honors_env_only_allowed_users(self, monkeypatch)` (method) — Env-only setup (WECOM_DM_POLICY + WECOM_ALLOWED_USERS, no config
- L306 `test_dm_allowlist_extra_takes_precedence_over_env(self, monkeypatch)` (method) — Config ``extra`` wins over the env fallback, so an explicit
- L321 `test_group_allowlist_and_per_group_sender_allowlist(self)` (method)
- L340 `TestMediaHelpers` (class)
- L341 `test_detect_wecom_media_type(self)` (method)
- L349 `test_voice_non_amr_downgrades_to_file(self)` (method)
- L358 `test_oversized_file_is_rejected(self)` (method)
- L366 `test_decrypt_file_bytes_round_trip(self)` (method)
- L382 `test_load_outbound_media_rejects_placeholder_path(self)` (method)
- L391 `TestMediaUpload` (class)
- L393 `test_upload_media_bytes_uses_sdk_sequence(self, monkeypatch)` (method)
- L441 `test_download_remote_bytes_rejects_large_content_length(self, _mock_safe)` (method)
- L470 `test_cache_media_decrypts_url_payload_before_writing(self)` (method)
- L507 `TestSend` (class)
- L509 `test_send_uses_proactive_payload(self)` (method)
- L528 `test_send_reports_wecom_errors(self)` (method)
- L540 `test_send_image_falls_back_to_text_for_remote_url(self)` (method)
- L553 `test_send_voice_sends_caption_and_downgrade_note(self)` (method)
- L587 `TestInboundMessages` (class)
- L589 `test_on_message_builds_event(self)` (method)
- L621 `test_on_message_preserves_quote_context(self)` (method)
- L650 `test_on_message_respects_group_policy(self)` (method)
- L679 `TestWeComZombieSessionFix` (class) — Tests for PR #11572 — device_id, markdown reply, group req_id fallback.
- L682 `test_adapter_generates_stable_device_id_per_instance(self)` (method)
- L693 `test_different_adapter_instances_get_distinct_device_ids(self)` (method)
- L701 `test_open_connection_includes_device_id_in_subscribe(self)` (method)
- L749 `test_on_message_caches_last_req_id_per_chat(self)` (method)
- L774 `test_on_message_does_not_cache_blocked_sender_req_id(self)` (method) — Blocked chats shouldn't populate the proactive-send fallback cache.
- L804 `test_remember_chat_req_id_is_bounded(self)` (method)
- L815 `test_remember_chat_req_id_ignores_empty_values(self)` (method)
- L825 `test_proactive_group_send_falls_back_to_cached_req_id(self)` (method) — Sending into a group without reply_to should use the last cached
- L852 `test_proactive_send_without_cached_req_id_uses_app_cmd_send(self)` (method) — When we have no prior req_id (fresh DM target), APP_CMD_SEND is used.
- L870 `TestTextBatchFlushRace` (class) — Regression tests for the cancel-delivery race in _flush_text_batch.
- L883 `test_superseded_task_does_not_pop_or_process_event(self)` (method) — A flush task that has been superseded must leave the event in the
- L927 `test_active_task_processes_event_normally(self)` (method) — When the task is not superseded it must still process the event.
