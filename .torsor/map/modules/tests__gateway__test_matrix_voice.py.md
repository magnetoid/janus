---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_matrix_voice.py

Symbols in `tests/gateway/test_matrix_voice.py`.

- L28 `_make_adapter()` (function) — Create a MatrixAdapter with mocked config.
- L45 `_make_audio_event(event_id: str='$audio_event', sender: str='@alice:example.org', room_id: str='!test:example.org', body: str='Voice message', url: str='mxc://example.org/abc123', is_voice: bool=False, mimetype: str='audio/ogg', timestamp: int=9999999999000)` (function) — Create a mock mautrix room message event.
- L87 `_make_state_store(member_count: int=2)` (function) — Create a mock state store with get_members/get_member support.
- L104 `TestMatrixVoiceMessageDetection` (class) — Test that MSC3245 voice messages are detected and tagged correctly.
- L107 `setup_method(self)` (method)
- L122 `test_voice_message_has_type_voice(self)` (method) — Voice messages (with MSC3245 field) should be MessageType.VOICE.
- L142 `test_voice_message_has_local_path(self)` (method) — Voice messages should have a local cached path in media_urls.
- L167 `test_audio_without_msc3245_stays_audio_type(self)` (method) — Regular audio uploads (no MSC3245 field) should remain MessageType.AUDIO.
- L186 `test_regular_audio_is_cached_locally(self)` (method) — Regular audio uploads are cached locally for downstream tool access.
- L215 `TestMatrixVoiceCacheFallback` (class) — Test graceful fallback when voice caching fails.
- L218 `setup_method(self)` (method)
- L229 `test_voice_cache_failure_falls_back_to_http_url(self)` (method) — If caching fails (download returns None), voice message should still be delivered with HTTP URL.
- L253 `test_voice_cache_exception_falls_back_to_http_url(self)` (method) — Unexpected download exceptions should also fall back to HTTP URL.
- L279 `TestMatrixSendVoiceMSC3245` (class) — Test that send_voice includes MSC3245 field for native voice rendering.
- L282 `setup_method(self)` (method)
- L297 `test_send_voice_includes_msc3245_field(self, _mock_guess)` (method) — send_voice should include org.matrix.msc3245.voice in message content.
