---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:44'
updated: '2026-06-08T00:38:44'
---

# tests/tools/test_tts_kittentts.py

Symbols in `tests/tools/test_tts_kittentts.py`.

- L10 `clean_env(monkeypatch)` (function)
- L16 `clear_kittentts_cache()` (function) — Reset the module-level model cache between tests.
- L25 `mock_kittentts_module()` (function) — Inject a fake kittentts + soundfile module that return stub objects.
- L50 `TestGenerateKittenTts` (class)
- L51 `test_successful_wav_generation(self, tmp_path, mock_kittentts_module)` (method)
- L63 `test_config_passes_voice_speed_cleantext(self, tmp_path, mock_kittentts_module)` (method)
- L82 `test_default_model_and_voice(self, tmp_path, mock_kittentts_module)` (method)
- L95 `test_model_is_cached_across_calls(self, tmp_path, mock_kittentts_module)` (method)
- L105 `test_different_models_are_cached_separately(self, tmp_path, mock_kittentts_module)` (method)
- L120 `test_non_wav_extension_triggers_ffmpeg_conversion(self, tmp_path, mock_kittentts_module, monkeypatch)` (method) — Non-.wav output path causes WAV → target ffmpeg conversion.
- L149 `test_missing_kittentts_raises_import_error(self, tmp_path, monkeypatch)` (method) — When kittentts package is not installed, _import_kittentts raises.
- L159 `TestCheckKittenttsAvailable` (class)
- L160 `test_reports_available_when_package_present(self, monkeypatch)` (method)
- L171 `test_reports_unavailable_when_package_missing(self, monkeypatch)` (method)
- L179 `TestDispatcherBranch` (class)
- L180 `test_kittentts_not_installed_returns_helpful_error(self, monkeypatch, tmp_path)` (method) — When provider=kittentts but package missing, return JSON error with setup hint.
