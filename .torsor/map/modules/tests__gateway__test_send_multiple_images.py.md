---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_send_multiple_images.py

Symbols in `tests/gateway/test_send_multiple_images.py`.

- L25 `_run(coro)` (function)
- L34 `_StubAdapter` (class) — Minimal adapter that records per-image send calls.
- L39 `__init__(self)` (method)
- L44 `connect(self)` (method)
- L47 `disconnect(self)` (method)
- L50 `send(self, chat_id, content, reply_to=None, **kwargs)` (method)
- L54 `get_chat_info(self, chat_id)` (method)
- L57 `send_image(self, chat_id, image_url, caption=None, **kwargs)` (method)
- L62 `send_animation(self, chat_id, animation_url, caption=None, **kwargs)` (method)
- L67 `send_image_file(self, chat_id, image_path, caption=None, **kwargs)` (method)
- L73 `TestBaseDefaultLoop` (class)
- L74 `test_loops_per_image_by_default(self)` (method)
- L89 `test_empty_batch_is_noop(self)` (method)
- L102 `_ensure_telegram_mock()` (function)
- L121 `TestTelegramMultiImage` (class)
- L123 `adapter(self)` (method)
- L130 `test_single_batch_under_10_calls_send_media_group_once(self, adapter)` (method) — 3 photos → one send_media_group call with 3 items.
- L144 `test_batch_over_10_chunks(self, adapter)` (method) — 15 photos → two send_media_group calls (10 + 5).
- L156 `test_animations_routed_to_send_animation(self, adapter)` (method) — GIFs are peeled off and sent individually via send_animation.
- L174 `test_fallback_to_per_image_on_send_media_group_failure(self, adapter)` (method) — If send_media_group raises, each photo falls back to send_image.
- L189 `test_empty_noop(self, adapter)` (method)
- L199 `_ensure_discord_mock()` (function)
- L215 `TestDiscordMultiImage` (class)
- L217 `adapter(self)` (method)
- L223 `test_single_batch_of_local_files_sends_once(self, adapter, tmp_path)` (method) — 3 local images → one channel.send with files=[...] of length 3.
- L243 `test_batch_over_10_chunks_into_two_messages(self, adapter, tmp_path)` (method) — 15 local images → two channel.send calls (10 + 5).
- L263 `test_empty_noop(self, adapter)` (method)
- L273 `_ensure_slack_mock()` (function)
- L292 `TestSlackMultiImage` (class)
- L294 `adapter(self)` (method)
- L305 `test_single_batch_of_local_files_sends_one_upload(self, adapter, tmp_path)` (method)
- L320 `test_batch_over_10_chunks(self, adapter, tmp_path)` (method)
- L335 `test_empty_noop(self, adapter)` (method)
- L349 `TestMattermostMultiImage` (class)
- L351 `adapter(self)` (method)
- L363 `test_local_files_uploaded_and_single_post(self, adapter, tmp_path)` (method) — 3 local images → 3 uploads + 1 post with 3 file_ids.
- L380 `test_batch_over_5_chunks(self, adapter, tmp_path)` (method) — 7 images → 2 posts (5 + 2).
- L395 `test_empty_noop(self, adapter)` (method)
- L408 `TestEmailMultiImage` (class)
- L410 `adapter(self)` (method)
- L419 `test_local_files_attached_in_single_email(self, adapter, tmp_path)` (method) — 3 local images → one SMTP send with 3 attachments.
- L440 `test_remote_urls_linked_in_body(self, adapter, tmp_path)` (method) — Remote URL images get their URL appended to the body, no attachment.
- L457 `test_empty_noop(self, adapter)` (method)
