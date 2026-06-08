---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_telegram_audio_vs_voice.py

Symbols in `tests/gateway/test_telegram_audio_vs_voice.py`.

- L24 `_make_runner(stt_enabled: bool=True)` (function)
- L36 `_voice_event(path: str='/tmp/voice.ogg')` (function)
- L46 `_audio_event(path: str='/tmp/song.mp3')` (function)
- L61 `test_voice_message_still_transcribed()` (function) — MessageType.VOICE must still be sent through _enrich_message_with_transcription.
- L87 `test_audio_attachment_skips_stt()` (function) — MessageType.AUDIO must NOT be routed to STT — transcribe_audio must not be called.
- L113 `test_audio_attachment_context_note_format()` (function) — Context note for audio file attachments should include the file path and guidance.
- L144 `test_audio_attachment_skips_stt_when_stt_disabled()` (function) — Even with STT disabled, AUDIO must NOT produce STT disabled notice — just a file note.
- L174 `test_telegram_media_type_detection_audio_vs_voice()` (function) — The Telegram platform must set MessageType.AUDIO for msg.audio, VOICE for msg.voice.
