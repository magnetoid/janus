---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_telegram_documents.py

Symbols in `tests/gateway/test_telegram_documents.py`.

- L32 `_ensure_telegram_mock()` (function) — Install mock telegram modules so TelegramAdapter can be imported.
- L61 `_make_file_obj(data: bytes=b'hello')` (function) — Create a mock Telegram File with download_as_bytearray.
- L69 `_make_document(file_name='report.pdf', mime_type='application/pdf', file_size=1024, file_obj=None)` (function) — Create a mock Telegram Document object.
- L84 `_make_message(document=None, caption=None, media_group_id=None, photo=None)` (function) — Build a mock Telegram Message with the given document/photo.
- L112 `_make_update(msg)` (function) — Wrap a message in a mock Update.
- L119 `_make_video(file_obj=None)` (function)
- L130 `adapter()` (function)
- L144 `_redirect_cache(tmp_path, monkeypatch)` (function) — Point document/video cache to tmp_path so tests don't touch ~/.hermes.
- L158 `TestDocumentTypeDetection` (class)
- L160 `test_document_detected_explicitly(self, adapter)` (method)
- L169 `test_fallback_is_document(self, adapter)` (method) — When no specific media attr is set, message_type defaults to DOCUMENT.
- L183 `_make_photo(file_obj=None)` (function)
- L189 `TestDocumentDownloadBlock` (class)
- L191 `test_supported_pdf_is_cached(self, adapter)` (method)
- L205 `test_supported_txt_injects_content(self, adapter)` (method)
- L221 `test_supported_md_injects_content(self, adapter)` (method)
- L236 `test_caption_preserved_with_injection(self, adapter)` (method)
- L252 `test_zip_document_cached(self, adapter)` (method) — A .zip upload should be cached as a supported document.
- L264 `test_png_document_is_routed_as_image(self, adapter)` (method) — Telegram documents that are really PNGs should use the image path.
- L284 `test_spoofed_png_document_falls_back_with_error(self, adapter)` (method) — A .png filename with non-image bytes should fail clearly, not disappear.
- L301 `test_oversized_file_rejected(self, adapter)` (method)
- L311 `test_none_file_size_rejected(self, adapter)` (method) — Security fix: file_size=None must be rejected (not silently allowed).
- L322 `test_missing_filename_uses_mime_lookup(self, adapter)` (method) — No file_name but valid mime_type should resolve to extension.
- L339 `test_missing_filename_and_mime_rejected(self, adapter)` (method)
- L349 `test_unicode_decode_error_handled(self, adapter)` (method) — Binary bytes that aren't valid UTF-8 in a .txt — content not injected but file still cached.
- L369 `test_text_injection_capped(self, adapter)` (method) — A .txt file over 100 KB should NOT have its content injected.
- L388 `test_download_exception_handled(self, adapter)` (method) — If get_file() raises, the handler logs the error without crashing.
- L401 `TestVideoDownloadBlock` (class)
- L403 `test_native_video_is_cached(self, adapter)` (method)
- L418 `test_mp4_document_is_treated_as_video(self, adapter)` (method)
- L436 `TestMediaGroups` (class)
- L438 `test_non_album_photo_burst_is_buffered_and_combined(self, adapter)` (method)
- L458 `test_photo_album_is_buffered_and_combined(self, adapter)` (method)
- L478 `test_disconnect_cancels_pending_media_group_flush(self, adapter)` (method)
- L500 `TestSendVoice` (class) — Tests for TelegramAdapter.send_voice() routing across audio formats.
- L504 `connected_adapter(self, adapter)` (method) — Adapter with a mock bot attached.
- L511 `test_flac_falls_back_to_document(self, connected_adapter, tmp_path)` (method) — Telegram sendAudio does not accept FLAC — must fall back to sendDocument.
- L535 `test_wav_falls_back_to_document(self, connected_adapter, tmp_path)` (method) — Telegram sendAudio does not accept WAV — must fall back to sendDocument.
- L556 `test_mp3_routes_to_send_audio(self, connected_adapter, tmp_path)` (method) — MP3 is Telegram-sendAudio-compatible.
- L581 `TestSendDocument` (class) — Tests for TelegramAdapter.send_document() — sending files to users.
- L585 `connected_adapter(self, adapter)` (method) — Adapter with a mock bot attached.
- L592 `test_send_document_success(self, connected_adapter, tmp_path)` (method) — A local file is sent via bot.send_document and returns success.
- L617 `test_send_document_custom_filename(self, connected_adapter, tmp_path)` (method) — The file_name parameter overrides the basename for display.
- L637 `test_send_document_file_not_found(self, connected_adapter)` (method) — Missing file returns error without calling Telegram API.
- L649 `test_send_document_workspace_path_has_docker_hint(self, connected_adapter)` (method) — Container-local-looking paths get a more actionable Docker hint.
- L662 `test_send_document_outputs_path_has_docker_hint(self, connected_adapter)` (method) — Legacy /outputs paths also get the Docker hint.
- L675 `test_send_document_not_connected(self, adapter)` (method) — If bot is None, returns not connected error.
- L686 `test_send_document_caption_truncated(self, connected_adapter, tmp_path)` (method) — Captions longer than 1024 chars are truncated.
- L706 `test_send_document_api_error_falls_back(self, connected_adapter, tmp_path)` (method) — If Telegram API raises, falls back to base class text message.
- L731 `test_send_document_reply_to(self, connected_adapter, tmp_path)` (method) — reply_to parameter is forwarded as reply_to_message_id.
- L750 `test_send_document_thread_id(self, connected_adapter, tmp_path)` (method) — metadata thread_id is forwarded as message_thread_id (required for Telegram forum groups).
- L769 `TestTelegramPhotoBatching` (class)
- L771 `test_flush_photo_batch_does_not_drop_newer_scheduled_task(self, adapter)` (method)
- L793 `test_disconnect_cancels_pending_photo_batch_tasks(self, adapter)` (method)
- L818 `TestSendVideo` (class) — Tests for TelegramAdapter.send_video() — sending videos to users.
- L822 `connected_adapter(self, adapter)` (method)
- L828 `test_send_video_success(self, connected_adapter, tmp_path)` (method)
- L847 `test_send_video_file_not_found(self, connected_adapter)` (method)
- L857 `test_send_video_workspace_path_has_docker_hint(self, connected_adapter)` (method)
- L868 `test_send_video_not_connected(self, adapter)` (method)
- L878 `test_send_video_thread_id(self, connected_adapter, tmp_path)` (method) — metadata thread_id is forwarded as message_thread_id (required for Telegram forum groups).
