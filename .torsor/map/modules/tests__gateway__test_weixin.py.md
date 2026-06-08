---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_weixin.py

Symbols in `tests/gateway/test_weixin.py`.

- L20 `_make_adapter()` (function)
- L30 `TestWeixinFormatting` (class)
- L31 `test_format_message_preserves_markdown(self)` (method)
- L38 `test_format_message_preserves_markdown_tables(self)` (method)
- L50 `test_format_message_preserves_fenced_code_blocks(self)` (method)
- L57 `test_format_message_wraps_long_plain_lines_for_copying(self)` (method)
- L71 `test_format_message_does_not_wrap_long_code_block_lines(self)` (method)
- L79 `test_format_message_returns_empty_string_for_none(self)` (method)
- L85 `TestWeixinChunking` (class)
- L86 `test_split_text_splits_short_chatty_replies_into_separate_bubbles(self)` (method)
- L94 `test_split_text_keeps_structured_table_block_together(self)` (method)
- L104 `test_split_text_keeps_four_line_structured_blocks_together(self)` (method)
- L117 `test_split_text_keeps_heading_with_body_together(self)` (method)
- L125 `test_split_text_keeps_short_reformatted_table_in_single_chunk(self)` (method)
- L138 `test_split_text_keeps_complete_code_block_together_when_possible(self)` (method)
- L154 `test_split_text_safely_splits_long_code_blocks(self)` (method)
- L166 `test_split_text_can_restore_legacy_multiline_splitting_via_config(self)` (method)
- L184 `TestWeixinConfig` (class)
- L185 `test_apply_env_overrides_configures_weixin(self)` (method)
- L216 `test_get_connected_platforms_includes_weixin_with_token(self)` (method)
- L229 `test_get_connected_platforms_requires_account_id(self)` (method)
- L242 `TestWeixinStatePersistence` (class)
- L243 `test_save_weixin_account_preserves_existing_file_on_replace_failure(self, tmp_path, monkeypatch)` (method)
- L269 `test_context_token_persist_preserves_existing_file_on_replace_failure(self, tmp_path, monkeypatch)` (method)
- L286 `test_save_sync_buf_preserves_existing_file_on_replace_failure(self, tmp_path, monkeypatch)` (method)
- L306 `TestWeixinQrLogin` (class)
- L308 `test_qr_login_timeout_uses_monotonic_clock(self, tmp_path)` (method)
- L335 `TestWeixinSendMessageIntegration` (class)
- L336 `test_parse_target_ref_accepts_weixin_ids(self)` (method)
- L342 `test_send_to_platform_routes_weixin_media_to_native_helper(self, send_weixin_mock)` (method)
- L365 `TestWeixinChunkDelivery` (class)
- L366 `_connected_adapter(self)` (method)
- L377 `test_send_waits_between_multiple_chunks(self, send_message_mock, sleep_mock)` (method)
- L390 `test_send_retries_failed_chunk_before_continuing(self, send_message_mock, sleep_mock)` (method)
- L415 `TestWeixinOutboundMedia` (class)
- L416 `test_send_image_file_accepts_keyword_image_path(self)` (method)
- L439 `test_send_document_accepts_keyword_file_path(self)` (method)
- L461 `test_send_file_uses_post_for_upload_full_url_and_hex_encoded_aes_key(self, tmp_path)` (method)
- L526 `TestWeixinRemoteMediaSafety` (class)
- L527 `test_download_remote_media_blocks_unsafe_urls(self)` (method)
- L539 `TestWeixinMarkdownLinks` (class) — Markdown links should be preserved so WeChat can render them natively.
- L542 `test_format_message_preserves_markdown_links(self)` (method)
- L548 `test_format_message_preserves_links_inside_code_blocks(self)` (method)
- L556 `TestWeixinBlankMessagePrevention` (class) — Regression tests for the blank-bubble bugs.
- L569 `test_split_text_returns_empty_list_for_empty_string(self)` (method)
- L573 `test_split_text_returns_empty_list_for_empty_string_split_per_line(self)` (method)
- L587 `test_send_empty_content_does_not_call_send_message(self, send_message_mock)` (method)
- L600 `test_send_message_rejects_empty_text(self)` (method) — _send_message raises ValueError for empty/whitespace text.
- L617 `TestWeixinStreamingCursorSuppression` (class) — WeChat doesn't support message editing — cursor must be suppressed.
- L620 `test_supports_message_editing_is_false(self)` (method)
- L625 `TestWeixinMediaBuilder` (class) — Media builder uses base64(hex_key), not base64(raw_bytes) for aes_key.
- L628 `test_image_builder_aes_key_is_base64_of_hex(self)` (method)
- L646 `test_video_builder_includes_md5(self)` (method)
- L661 `test_voice_builder_for_audio_files_uses_file_attachment_type(self)` (method)
- L677 `test_voice_builder_for_silk_files(self)` (method)
- L683 `TestWeixinSendImageFileParameterName` (class) — Regression test for send_image_file parameter name mismatch.
- L692 `test_send_image_file_uses_image_path_parameter(self, send_document_mock)` (method) — Verify send_image_file accepts image_path and forwards to send_document.
- L720 `test_send_image_file_works_without_optional_params(self, send_document_mock)` (method) — Verify send_image_file works with minimal required params.
- L745 `TestWeixinVoiceSending` (class)
- L746 `_connected_adapter(self)` (method)
- L756 `test_send_voice_downgrades_to_document_attachment(self, send_file_mock, tmp_path)` (method)
- L772 `test_voice_builder_for_silk_files_can_be_forced_to_file_attachment(self)` (method)
- L794 `test_send_file_sets_voice_metadata_for_silk_payload(self, get_upload_url_mock, upload_ciphertext_mock, api_post_mock, tmp_path)` (method)
- L818 `TestIsStaleSessionRet` (class) — Regression test for #17228: distinguish stale-session ret=-2 from rate-limit ret=-2.
- L821 `test_ret_minus_2_with_unknown_error_is_stale(self)` (method)
- L824 `test_errcode_minus_2_with_unknown_error_is_stale(self)` (method)
- L827 `test_unknown_error_case_insensitive(self)` (method)
- L830 `test_ret_minus_2_with_freq_limit_is_not_stale(self)` (method)
- L834 `test_ret_minus_2_with_no_errmsg_is_not_stale(self)` (method)
- L838 `test_errcode_minus_14_is_not_matched_here(self)` (method)
- L843 `test_success_codes_are_not_stale(self)` (method)
- L848 `TestWeixinContentDedup` (class) — Regression tests for Issue #16182 — upstream API sends duplicate content
- L853 `test_duplicate_content_with_different_message_ids_is_dropped(self)` (method)
- L882 `test_content_dedup_not_called_for_messages_without_text(self)` (method)
- L900 `TestWeixinTextDebounce` (class) — Text-debounce batching for rapid multi-message bursts (issue #35301).
- L906 `test_batch_delays_default_from_config(self)` (method)
- L911 `test_batch_delays_overridden_via_config_extra(self)` (method)
- L926 `test_invalid_config_value_falls_back_to_default(self)` (method)
- L941 `test_rapid_texts_collapse_into_single_dispatch(self)` (method)
- L973 `_StubResponse` (class)
- L974 `__init__(self, *, status=200, body='{}', delay=0.0)` (method)
- L980 `__aenter__(self)` (method)
- L983 `__aexit__(self, *_exc)` (method)
- L986 `text(self)` (method)
- L992 `_StubSession` (class) — Records request kwargs and returns a configurable async-CM response.
- L1000 `__init__(self, response)` (method)
- L1005 `post(self, url, **kwargs)` (method)
- L1009 `get(self, url, **kwargs)` (method)
- L1014 `TestWeixinApiTimeout` (class)
- L1015 `test_api_post_does_not_pass_aiohttp_timeout_kwarg(self)` (method)
- L1033 `test_api_get_does_not_pass_aiohttp_timeout_kwarg(self)` (method)
- L1047 `test_api_post_raises_timeout_when_response_is_slow(self)` (method)
- L1062 `test_api_get_raises_timeout_when_response_is_slow(self)` (method)
- L1074 `test_api_post_raises_runtime_error_on_non_ok_status(self)` (method)
- L1090 `test_api_get_raises_runtime_error_on_non_ok_status(self)` (method)
- L1102 `test_get_updates_returns_empty_sentinel_on_timeout(self)` (method)
