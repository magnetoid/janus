---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_discord_attachment_download.py

Symbols in `tests/gateway/test_discord_attachment_download.py`.

- L26 `_ensure_discord_mock()` (function) — Install a mock discord module when discord.py isn't available.
- L73 `_make_adapter()` (function)
- L77 `_make_attachment_with_read(payload: bytes)` (function) — Attachment stub that exposes .read() — the happy-path primary.
- L87 `_make_attachment_without_read()` (function) — Attachment stub that has no .read() — exercises the URL fallback.
- L100 `TestReadAttachmentBytes` (class) — Unit tests for the low-level att.read() wrapper.
- L104 `test_returns_bytes_on_successful_read(self)` (method)
- L114 `test_returns_none_when_read_missing(self)` (method)
- L123 `test_returns_none_when_read_raises(self)` (method) — Bot-session fetch failures are swallowed so callers fall back.
- L141 `TestCacheDiscordImage` (class)
- L143 `test_prefers_att_read_over_url(self)` (method) — Primary path: att.read() bytes → cache_image_from_bytes, no URL fetch.
- L162 `test_falls_back_to_url_when_no_read(self)` (method) — No .read() → URL path is used (existing SSRF-gated behavior).
- L181 `test_falls_back_to_url_when_bytes_validator_rejects(self)` (method) — If att.read() returns garbage that cache_image_from_bytes rejects
- L206 `TestCacheDiscordAudio` (class)
- L208 `test_prefers_att_read_over_url(self)` (method)
- L226 `test_falls_back_to_url_when_no_read(self)` (method)
- L245 `TestCacheDiscordDocument` (class)
- L247 `test_prefers_att_read_returns_bytes_directly(self)` (method) — Primary path: att.read() → raw bytes, no aiohttp involvement.
- L259 `test_fallback_blocked_by_ssrf_guard(self)` (method) — Document fallback path now honors is_safe_url — was missing before.
- L280 `test_fallback_aiohttp_when_safe_url(self)` (method) — Safe URL + no att.read() → aiohttp fallback executes.
- L309 `TestHandleMessageUsesAuthenticatedRead` (class) — E2E: verify _handle_message routes image/audio downloads through
- L316 `test_image_downloads_via_att_read_not_url(self, monkeypatch)` (method) — Image attachments with .read() never call cache_image_from_url.
- L364 `test_native_voice_note_is_classified_as_voice(self, monkeypatch)` (method) — Discord native voice notes must enter the auto-STT voice path.
- L408 `test_plain_audio_attachment_stays_audio(self, monkeypatch)` (method) — Plain audio uploads should stay out of automatic voice-note STT.
