---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# agent/transcription_provider.py

Symbols in `agent/transcription_provider.py`.

- L61 `TranscriptionProvider` (class) — Abstract base class for a speech-to-text backend.
- L71 `name(self)` (method) — Stable short identifier used in ``stt.provider`` config.
- L81 `display_name(self)` (method) — Human-readable label shown in ``hermes tools``.
- L88 `is_available(self)` (method) — Return True when this provider can service calls.
- L100 `list_models(self)` (method) — Return model catalog entries.
- L117 `default_model(self)` (method) — Return the default model id, or None if not applicable.
- L124 `get_setup_schema(self)` (method) — Return provider metadata for the ``hermes tools`` picker.
- L152 `transcribe(self, file_path: str, *, model: Optional[str]=None, language: Optional[str]=None, **extra: Any)` (method) — Transcribe the audio file at ``file_path``.
