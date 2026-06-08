---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_send_voice_reply_notify.py

Symbols in `tests/gateway/test_send_voice_reply_notify.py`.

- L24 `_make_event(thread_id=None)` (function)
- L40 `_runner_with_adapter(send_voice_mock)` (function)
- L50 `_fake_tts_call(monkeypatch, audio_bytes=b'\x00' * 32)` (function) — Patch the TTS tool so it writes a real file at the requested path.
- L70 `test_voice_reply_marks_metadata_notify_true_for_dm(monkeypatch, tmp_path)` (function) — Final voice reply with no thread metadata gets a fresh notify=True dict.
- L88 `test_voice_reply_marks_existing_thread_metadata_without_mutation(monkeypatch, tmp_path)` (function) — When thread metadata exists (Telegram DM-topic), notify=True is added without mutating the source dict.
