---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:44'
updated: '2026-06-08T00:38:44'
---

# tests/tools/test_tts_mistral.py

Symbols in `tests/tools/test_tts_mistral.py`.

- L10 `clean_env(monkeypatch)` (function)
- L16 `mock_mistral_module()` (function)
- L27 `TestGenerateMistralTts` (class)
- L28 `test_missing_api_key_raises_value_error(self, tmp_path, mock_mistral_module)` (method)
- L35 `test_successful_generation(self, tmp_path, mock_mistral_module, monkeypatch)` (method)
- L59 `test_response_format_from_extension(self, tmp_path, mock_mistral_module, monkeypatch, extension, expected_format)` (method)
- L75 `test_voice_id_passed_when_configured(self, tmp_path, mock_mistral_module, monkeypatch)` (method)
- L91 `test_default_voice_id_when_absent(self, tmp_path, mock_mistral_module, monkeypatch)` (method)
- L106 `test_default_voice_id_when_empty_string(self, tmp_path, mock_mistral_module, monkeypatch)` (method)
- L122 `test_api_error_sanitized(self, tmp_path, mock_mistral_module, monkeypatch)` (method)
- L134 `test_default_model_used(self, tmp_path, mock_mistral_module, monkeypatch)` (method)
- L147 `test_model_from_config_overrides_default(self, tmp_path, mock_mistral_module, monkeypatch)` (method)
- L164 `TestTtsDispatcherMistral` (class)
- L165 `test_dispatcher_routes_to_mistral(self, tmp_path, mock_mistral_module, monkeypatch)` (method)
- L185 `test_dispatcher_returns_error_when_sdk_not_installed(self, tmp_path, monkeypatch)` (method)
- L202 `TestCheckTtsRequirementsMistral` (class)
- L203 `test_mistral_sdk_and_key_returns_true(self, mock_mistral_module, monkeypatch)` (method)
- L213 `test_mistral_key_missing_returns_false(self, mock_mistral_module)` (method)
