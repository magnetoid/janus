---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:44'
updated: '2026-06-08T00:38:44'
---

# tests/tools/test_tts_dotenv_fallback.py

Symbols in `tests/tools/test_tts_dotenv_fallback.py`.

- L16 `isolate_env(monkeypatch)` (function) — Strip every TTS-related env var so the test really exercises the
- L35 `TestDotenvFallbackPerProvider` (class) — For each affected provider, when only ``~/.hermes/.env`` carries the
- L45 `test_elevenlabs_reads_dotenv_key(self, tmp_path)` (method)
- L59 `test_xai_reads_dotenv_key(self, tmp_path)` (method) — xAI TTS now resolves credentials through ``tools.xai_http``; the
- L83 `test_minimax_reads_dotenv_key(self, tmp_path)` (method)
- L104 `test_mistral_reads_dotenv_key(self, tmp_path)` (method)
- L127 `test_gemini_reads_dotenv_key(self, tmp_path)` (method)
- L174 `TestRegressionGuard` (class) — Goal-backward proof that the old behaviour ('only check ``os.environ``')
- L182 `test_import_after_config_env_patch_uses_restored_dotenv_loader(self, tmp_path, monkeypatch)` (method) — Importing TTS while hermes_cli.config.get_env_value is patched must
- L221 `test_minimax_missing_when_only_in_dotenv_before_fix(self, tmp_path, monkeypatch)` (method)
- L259 `test_check_tts_requirements_sees_dotenv_minimax(self, monkeypatch)` (method) — ``check_tts_requirements`` is the gate that decides whether
