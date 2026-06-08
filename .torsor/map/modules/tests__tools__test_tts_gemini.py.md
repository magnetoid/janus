---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:44'
updated: '2026-06-08T00:38:44'
---

# tests/tools/test_tts_gemini.py

Symbols in `tests/tools/test_tts_gemini.py`.

- L11 `clean_env(monkeypatch)` (function)
- L22 `fake_pcm_bytes()` (function)
- L28 `mock_gemini_response(fake_pcm_bytes)` (function) — A successful Gemini generateContent response.
- L51 `TestWrapPcmAsWav` (class)
- L52 `test_riff_header_structure(self)` (method)
- L72 `test_header_size_is_44(self)` (method)
- L80 `TestGenerateGeminiTts` (class)
- L81 `test_missing_api_key_raises_value_error(self, tmp_path)` (method)
- L88 `test_google_api_key_fallback(self, tmp_path, monkeypatch, mock_gemini_response)` (method)
- L101 `test_wav_output_fast_path(self, tmp_path, monkeypatch, mock_gemini_response, fake_pcm_bytes)` (method)
- L117 `test_default_voice_and_model(self, tmp_path, monkeypatch, mock_gemini_response)` (method)
- L138 `test_custom_voice(self, tmp_path, monkeypatch, mock_gemini_response)` (method)
- L154 `test_custom_model(self, tmp_path, monkeypatch, mock_gemini_response)` (method)
- L166 `test_response_modality_is_audio(self, tmp_path, monkeypatch, mock_gemini_response)` (method)
- L177 `test_http_error_raises_runtime_error(self, tmp_path, monkeypatch)` (method)
- L189 `test_empty_audio_raises(self, tmp_path, monkeypatch)` (method)
- L205 `test_malformed_response_raises(self, tmp_path, monkeypatch)` (method)
- L217 `test_snake_case_inline_data_accepted(self, tmp_path, monkeypatch, fake_pcm_bytes)` (method) — Some Gemini SDK versions return inline_data instead of inlineData.
- L247 `test_custom_base_url_env(self, tmp_path, monkeypatch, mock_gemini_response)` (method)
- L259 `TestGeminiInCheckRequirements` (class)
- L260 `test_gemini_api_key_satisfies_requirements(self, monkeypatch)` (method)
