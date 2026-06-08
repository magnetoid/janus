---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:44'
updated: '2026-06-08T00:38:44'
---

# tests/tools/test_tts_piper.py

Symbols in `tests/tools/test_tts_piper.py`.

- L32 `TestPiperRegistration` (class)
- L33 `test_piper_is_a_builtin_provider(self)` (method)
- L36 `test_piper_has_a_text_length_cap(self)` (method)
- L44 `TestCheckPiperAvailable` (class)
- L45 `test_returns_bool_without_raising(self)` (method)
- L55 `TestResolvePiperVoicePath` (class)
- L56 `test_direct_onnx_path_returned_as_is(self, tmp_path)` (method)
- L62 `test_cached_voice_name_not_redownloaded(self, tmp_path)` (method) — If both <voice>.onnx and <voice>.onnx.json exist in the
- L75 `test_missing_voice_triggers_download(self, tmp_path)` (method)
- L96 `test_download_failure_raises_runtime(self, tmp_path)` (method)
- L103 `test_download_success_but_missing_file_raises(self, tmp_path)` (method)
- L111 `test_empty_voice_falls_back_to_default_name(self, tmp_path)` (method)
- L122 `_StubPiperVoice` (class) — Stand-in for piper.PiperVoice used by the synthesis tests.
- L129 `load(cls, model_path, use_cuda=False)` (method)
- L136 `synthesize_wav(self, text, wav_file, syn_config=None)` (method)
- L148 `_reset_piper_cache()` (function) — Clear the module-level voice cache between tests.
- L157 `TestGeneratePiperTts` (class)
- L158 `_prepare_voice_files(self, tmp_path, voice=DEFAULT_PIPER_VOICE)` (method)
- L164 `test_loads_voice_and_writes_wav(self, tmp_path, monkeypatch)` (method)
- L179 `test_voice_cache_reused_across_calls(self, tmp_path, monkeypatch)` (method)
- L192 `test_voice_name_triggers_download(self, tmp_path, monkeypatch)` (method) — A config voice of ``en_US-lessac-medium`` should be resolved via
- L210 `test_advanced_knobs_passed_as_synconfig(self, tmp_path, monkeypatch)` (method)
- L247 `TestTextToSpeechToolWithPiper` (class)
- L248 `test_dispatches_to_piper(self, tmp_path, monkeypatch)` (method)
- L265 `test_missing_package_surfaces_error(self, tmp_path, monkeypatch)` (method)
- L285 `TestCheckTtsRequirementsPiper` (class)
- L286 `test_piper_install_satisfies_requirements(self, monkeypatch)` (method)
