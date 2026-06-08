---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_send_image_file.py

Symbols in `tests/gateway/test_send_image_file.py`.

- L20 `_run(coro)` (function) — Run a coroutine in a fresh event loop for sync-style tests.
- L30 `TestExtractMediaImages` (class) — Test that MEDIA: tags with image extensions are correctly extracted.
- L33 `test_png_image_extracted(self)` (method)
- L41 `test_jpg_image_extracted(self)` (method)
- L47 `test_webp_image_extracted(self)` (method)
- L52 `test_mixed_audio_and_image(self)` (method)
- L66 `_ensure_telegram_mock()` (function) — Install mock telegram modules so TelegramAdapter can be imported.
- L88 `TestTelegramSendImageFile` (class)
- L90 `adapter(self)` (method)
- L96 `test_sends_local_image_as_photo(self, adapter, tmp_path)` (method) — send_image_file should call bot.send_photo with the opened file.
- L116 `test_returns_error_when_file_missing(self, adapter)` (method) — send_image_file should return error for nonexistent file.
- L124 `test_returns_error_when_not_connected(self, adapter)` (method) — send_image_file should return error when bot is None.
- L133 `test_caption_truncated_to_1024(self, adapter, tmp_path)` (method) — Telegram captions have a 1024 char limit.
- L150 `test_thread_id_forwarded(self, adapter, tmp_path)` (method) — metadata thread_id is forwarded as message_thread_id (required for Telegram forum groups).
- L176 `_ensure_discord_mock()` (function) — Install mock discord module so DiscordAdapter can be imported.
- L196 `TestDiscordSendImageFile` (class)
- L198 `adapter(self)` (method)
- L204 `test_sends_local_image_as_attachment(self, adapter, tmp_path)` (method) — send_image_file should create discord.File and send to channel.
- L222 `test_send_document_uploads_file_attachment(self, adapter, tmp_path)` (method) — send_document should upload a native Discord attachment.
- L248 `test_send_video_uploads_file_attachment(self, adapter, tmp_path)` (method) — send_video should upload a native Discord attachment.
- L273 `test_returns_error_when_file_missing(self, adapter)` (method)
- L280 `test_returns_error_when_not_connected(self, adapter)` (method)
- L288 `test_handles_missing_channel(self, adapter)` (method)
- L304 `_ensure_slack_mock()` (function) — Install mock slack_bolt module so SlackAdapter can be imported.
- L319 `TestSlackSendImageFile` (class)
- L321 `adapter(self)` (method)
- L327 `test_sends_local_image_via_upload(self, adapter, tmp_path)` (method) — send_image_file should call files_upload_v2 with the local path.
- L346 `test_returns_error_when_file_missing(self, adapter)` (method)
- L353 `test_returns_error_when_not_connected(self, adapter)` (method)
- L367 `TestScreenshotCleanup` (class)
- L368 `test_cleanup_removes_old_screenshots(self, tmp_path)` (method) — _cleanup_old_screenshots should remove files older than max_age_hours.
- L390 `test_cleanup_is_throttled_per_directory(self, tmp_path)` (method)
- L410 `test_cleanup_ignores_non_screenshot_files(self, tmp_path)` (method) — Only files matching browser_screenshot_*.png should be cleaned.
- L426 `test_cleanup_handles_empty_dir(self, tmp_path)` (method) — Cleanup should not fail on empty directory.
- L432 `test_cleanup_handles_nonexistent_dir(self)` (method) — Cleanup should not fail if directory doesn't exist.
