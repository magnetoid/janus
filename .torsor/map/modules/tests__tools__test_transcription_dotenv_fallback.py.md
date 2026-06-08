---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:44'
updated: '2026-06-08T00:38:44'
---

# tests/tools/test_transcription_dotenv_fallback.py

Symbols in `tests/tools/test_transcription_dotenv_fallback.py`.

- L19 `isolate_env(monkeypatch)` (function) — Strip every STT-related env var so the test really exercises the
- L36 `TestProviderSelectionGate` (class) — ``_get_provider`` picks the STT backend. If it only consulted
- L44 `test_import_after_config_env_patch_uses_restored_dotenv_loader(self)` (method) — Importing STT while hermes_cli.config.get_env_value is patched must
- L66 `test_xai_resolver_import_after_config_env_patch_uses_restored_dotenv_loader(self)` (method) — xAI HTTP auth must not cache a temporarily patched env helper.
- L93 `test_explicit_groq_sees_dotenv(self)` (method)
- L103 `test_explicit_mistral_sees_dotenv(self)` (method)
- L113 `test_explicit_xai_sees_dotenv(self)` (method)
- L122 `test_explicit_elevenlabs_sees_dotenv(self)` (method)
- L131 `test_auto_detect_sees_dotenv_groq(self)` (method) — No local backend, no explicit provider — auto-detect should fall
- L148 `TestTranscribeCallSitesReadDotenv` (class) — The actual transcribe functions must forward the dotenv-resolved
- L153 `test_transcribe_groq_forwards_dotenv_key(self)` (method)
- L181 `test_transcribe_mistral_forwards_dotenv_key(self)` (method)
- L207 `test_transcribe_xai_forwards_dotenv_key(self)` (method) — xAI STT now resolves credentials through ``tools.xai_http`` so the
- L242 `test_transcribe_elevenlabs_forwards_dotenv_key(self)` (method)
- L270 `TestEndToEndRegressionGuard` (class) — End-to-end probe: patch ``hermes_cli.config.load_env`` to simulate
- L276 `test_xai_key_only_in_dotenv_before_fix(self, monkeypatch)` (method)
