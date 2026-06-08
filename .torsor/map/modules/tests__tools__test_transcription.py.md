---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:44'
updated: '2026-06-08T00:38:44'
---

# tests/tools/test_transcription.py

Symbols in `tests/tools/test_transcription.py`.

- L15 `_fake_faster_whisper_module(mock_model)` (function)
- L28 `_clear_openai_env(monkeypatch)` (function)
- L32 `TestGetProvider` (class) — _get_provider() picks the right backend based on config + availability.
- L35 `test_local_when_available(self)` (method)
- L40 `test_explicit_local_no_cloud_fallback(self, monkeypatch)` (method) — Explicit local provider must not silently fall back to cloud.
- L50 `test_local_nothing_available(self, monkeypatch)` (method)
- L58 `test_openai_when_key_set(self, monkeypatch)` (method)
- L64 `test_explicit_openai_no_key_returns_none(self, monkeypatch)` (method) — Explicit openai without key returns none — no cross-provider fallback.
- L72 `test_default_provider_is_local(self)` (method)
- L77 `test_disabled_config_returns_none(self)` (method)
- L87 `TestValidateAudioFile` (class)
- L89 `test_missing_file(self, tmp_path)` (method)
- L95 `test_unsupported_format(self, tmp_path)` (method)
- L103 `test_valid_file_returns_none(self, tmp_path)` (method)
- L109 `test_too_large(self, tmp_path)` (method)
- L130 `TestTranscribeLocal` (class)
- L132 `test_successful_transcription(self, tmp_path)` (method)
- L155 `test_not_installed(self)` (method)
- L168 `TestTranscribeOpenAI` (class)
- L170 `test_no_key(self, monkeypatch)` (method)
- L177 `test_successful_transcription(self, monkeypatch, tmp_path)` (method)
- L199 `TestTranscribeAudio` (class)
- L201 `test_dispatches_to_local(self, tmp_path)` (method)
- L214 `test_dispatches_to_openai(self, tmp_path)` (method)
- L227 `test_no_provider_returns_error(self, tmp_path)` (method)
- L239 `test_disabled_config_returns_disabled_error(self, tmp_path)` (method)
- L251 `test_invalid_file_returns_error(self)` (method)
- L263 `TestNormalizeLocalModel` (class) — _normalize_local_model() maps cloud-only names to the local default.
- L266 `test_openai_model_name_maps_to_default(self)` (method)
- L270 `test_groq_model_name_maps_to_default(self)` (method)
- L274 `test_valid_local_model_preserved(self)` (method)
- L279 `test_none_maps_to_default(self)` (method)
- L283 `test_warning_emitted_for_cloud_model(self, caplog)` (method)
- L290 `test_local_transcribe_normalises_model(self)` (method) — transcribe_audio with local provider must not pass 'whisper-1' to WhisperModel.
