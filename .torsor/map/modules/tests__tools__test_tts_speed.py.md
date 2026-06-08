---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:44'
updated: '2026-06-08T00:38:44'
---

# tests/tools/test_tts_speed.py

Symbols in `tests/tools/test_tts_speed.py`.

- L10 `clean_env(monkeypatch)` (function)
- L24 `TestEdgeTtsSpeed` (class)
- L25 `_run(self, tts_config, tmp_path)` (method)
- L36 `test_default_no_rate_kwarg(self, tmp_path)` (method) — No speed config => no rate kwarg passed to Communicate.
- L42 `test_global_speed_applied(self, tmp_path)` (method) — Global tts.speed used as fallback.
- L48 `test_provider_speed_overrides_global(self, tmp_path)` (method) — tts.edge.speed takes precedence over tts.speed.
- L54 `test_speed_below_one(self, tmp_path)` (method) — Speed < 1.0 produces a negative rate string.
- L60 `test_speed_exactly_one_no_rate(self, tmp_path)` (method) — Explicit speed=1.0 should not pass rate kwarg.
- L71 `TestOpenaiTtsSpeed` (class)
- L72 `_run(self, tts_config, tmp_path, monkeypatch)` (method)
- L86 `test_default_no_speed_kwarg(self, tmp_path, monkeypatch)` (method) — No speed config => no speed kwarg in create call.
- L92 `test_global_speed_applied(self, tmp_path, monkeypatch)` (method) — Global tts.speed used as fallback.
- L98 `test_provider_speed_overrides_global(self, tmp_path, monkeypatch)` (method) — tts.openai.speed takes precedence over tts.speed.
- L104 `test_speed_clamped_low(self, tmp_path, monkeypatch)` (method) — Speed below 0.25 is clamped to 0.25.
- L110 `test_speed_clamped_high(self, tmp_path, monkeypatch)` (method) — Speed above 4.0 is clamped to 4.0.
- L124 `_hex_response(payload_audio: bytes=b'\x00\x01\x02\x03')` (function) — Build a mock response shaped like a successful t2a_v2 reply.
- L136 `TestMinimaxTtsT2aV2` (class) — Default path: base_url contains 't2a_v2'.
- L139 `_run(self, tts_config, tmp_path, monkeypatch, response=None)` (method)
- L147 `test_nested_payload(self, tmp_path, monkeypatch)` (method) — Default endpoint uses nested voice_setting / audio_setting.
- L160 `test_decodes_hex_audio(self, tmp_path, monkeypatch)` (method) — t2a_v2 hex-encoded audio is decoded and written verbatim.
- L166 `test_default_url_is_t2a_v2(self, tmp_path, monkeypatch)` (method) — Default base URL points at the live t2a_v2 endpoint.
- L173 `test_group_id_from_config(self, tmp_path, monkeypatch)` (method) — group_id from config attaches as ?GroupId=<id>.
- L179 `test_group_id_from_env(self, tmp_path, monkeypatch)` (method) — MINIMAX_GROUP_ID env var attaches as ?GroupId=<id>.
- L186 `test_group_id_already_in_url_left_alone(self, tmp_path, monkeypatch)` (method) — If user already set GroupId in base_url, don't double-append it.
- L197 `test_api_error_raises(self, tmp_path, monkeypatch)` (method) — Non-zero base_resp.status_code surfaces as RuntimeError.
- L210 `TestMinimaxTtsLegacyTextToSpeech` (class) — Legacy path: caller pins base_url to the old text_to_speech endpoint.
- L215 `_run(self, tts_config, tmp_path, monkeypatch)` (method)
- L228 `test_flat_payload(self, tmp_path, monkeypatch)` (method) — Legacy endpoint keeps the flat {model, text, voice_id} shape.
- L236 `test_writes_raw_audio(self, tmp_path, monkeypatch)` (method) — Legacy endpoint returns raw bytes written directly to file.
