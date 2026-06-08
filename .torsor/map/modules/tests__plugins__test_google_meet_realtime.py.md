---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/plugins/test_google_meet_realtime.py

Symbols in `tests/plugins/test_google_meet_realtime.py`.

- L17 `_isolate_home(tmp_path, monkeypatch)` (function)
- L29 `_FakeWS` (class) — Scripted WS: send() records frames, recv() pops a queue.
- L32 `__init__(self, recv_frames: list)` (method)
- L37 `send(self, payload)` (method)
- L43 `recv(self, timeout=None)` (method)
- L51 `close(self)` (method)
- L55 `_install_fake_websockets(monkeypatch, fake_ws)` (function) — Install a fake ``websockets.sync.client`` module in sys.modules.
- L86 `test_connect_sends_session_update_with_voice_and_instructions(monkeypatch)` (function)
- L125 `test_speak_sends_create_and_response_and_writes_audio(monkeypatch, tmp_path)` (function)
- L165 `test_speak_raises_on_error_frame(monkeypatch, tmp_path)` (function)
- L180 `test_speak_without_connect_raises(monkeypatch)` (function)
- L188 `test_close_is_idempotent_and_closes_ws(monkeypatch)` (function)
- L207 `test_connect_raises_clean_error_when_websockets_missing(monkeypatch)` (function)
- L225 `_StubSession` (class)
- L226 `__init__(self)` (method)
- L229 `speak(self, text, timeout=30.0)` (method)
- L234 `test_speaker_run_until_stopped_processes_queue(tmp_path)` (function)
- L264 `test_speaker_exits_immediately_when_stop_fn_true(tmp_path)` (function)
- L276 `test_speaker_drops_line_without_processed_path_when_none(tmp_path)` (function)
