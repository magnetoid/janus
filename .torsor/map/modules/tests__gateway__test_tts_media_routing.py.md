---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_tts_media_routing.py

Symbols in `tests/gateway/test_tts_media_routing.py`.

- L21 `_MediaRoutingAdapter` (class)
- L22 `__init__(self)` (method)
- L25 `connect(self)` (method)
- L28 `disconnect(self)` (method)
- L31 `send(self, chat_id, content=None, **kwargs)` (method)
- L34 `get_chat_info(self, chat_id)` (method)
- L38 `_event(thread_id=None)` (function)
- L53 `_allowed_media_path(tmp_path, monkeypatch, name)` (function)
- L66 `test_base_adapter_routes_telegram_flac_media_tag_to_document_sender(tmp_path, monkeypatch)` (function)
- L85 `test_base_adapter_routes_non_voice_telegram_ogg_media_tag_to_document_sender(tmp_path, monkeypatch)` (function)
- L104 `test_base_adapter_routes_voice_tagged_telegram_ogg_media_tag_to_voice_sender(tmp_path, monkeypatch)` (function)
- L124 `_fake_runner(thread_meta)` (function) — Build a fake GatewayRunner-like object with the helper methods needed by
- L135 `test_streaming_delivery_routes_telegram_flac_media_tag_to_document_sender(tmp_path, monkeypatch)` (function)
- L165 `test_streaming_delivery_routes_non_voice_telegram_ogg_media_tag_to_document_sender(tmp_path, monkeypatch)` (function)
- L195 `test_streaming_delivery_routes_telegram_mp3_media_tag_to_voice_sender(tmp_path, monkeypatch)` (function) — MP3 audio on Telegram must go through send_voice (which routes to
- L227 `test_streaming_delivery_blocks_media_path_outside_allowed_roots(tmp_path, monkeypatch)` (function)
