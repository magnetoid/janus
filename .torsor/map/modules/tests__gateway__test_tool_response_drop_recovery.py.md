---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_tool_response_drop_recovery.py

Symbols in `tests/gateway/test_tool_response_drop_recovery.py`.

- L36 `_DummyAdapter` (class) — Minimal BasePlatformAdapter for dispatch tests on any platform.
- L39 `__init__(self, platform: Platform)` (method)
- L43 `connect(self)` (method)
- L46 `disconnect(self)` (method)
- L49 `send(self, chat_id, content, reply_to=None, metadata=None)` (method)
- L53 `send_typing(self, chat_id: str, metadata=None)` (method)
- L56 `get_chat_info(self, chat_id: str)` (method)
- L60 `_make_event(platform: Platform, chat_id: str='111', message_id: str='m1')` (function)
- L68 `_hold_typing(_chat_id, interval=2.0, metadata=None, stop_event=None)` (function)
- L75 `_strip_everything(adapter, monkeypatch)` (function) — Force the extract pipeline to reduce text_content to "" with no
- L90 `TestExtractStripRecoveryAllPlatforms` (class) — A non-empty response stripped to empty must be recovered on EVERY
- L95 `test_response_reduced_to_empty_is_recovered_and_sent(self, platform, monkeypatch, caplog)` (method)
- L129 `test_directives_stripped_from_fallback_text(self, platform, monkeypatch)` (method)
- L155 `test_no_fallback_when_attachment_produced(self, platform, monkeypatch)` (method) — When an image attachment IS extracted, the empty text_content is
- L184 `TestRecoveryDoesNotLeakMediaFragments` (class) — The A2 recovery must not leak fragments of a MEDIA: path to the user.
- L195 `test_spaced_media_path_does_not_leak_fragment(self, monkeypatch, caplog)` (method)
- L231 `TestUnrecoverableDropIsLoud` (class) — A non-empty response that produces NOTHING deliverable (sanitizes to
- L237 `test_directive_only_response_logs_dropped(self, monkeypatch, caplog)` (method)
