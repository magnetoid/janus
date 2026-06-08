---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# agent/tts_provider.py

Symbols in `agent/tts_provider.py`.

- L64 `TTSProvider` (class) — Abstract base class for a text-to-speech backend.
- L74 `name(self)` (method) — Stable short identifier used in ``tts.provider`` config.
- L85 `display_name(self)` (method) — Human-readable label shown in ``hermes tools``.
- L92 `is_available(self)` (method) — Return True when this provider can service calls.
- L104 `list_voices(self)` (method) — Return voice catalog entries.
- L122 `list_models(self)` (method) — Return model catalog entries.
- L139 `get_setup_schema(self)` (method) — Return provider metadata for the ``hermes tools`` picker.
- L166 `default_model(self)` (method) — Return the default model id, or None if not applicable.
- L173 `default_voice(self)` (method) — Return the default voice id, or None if not applicable.
- L181 `synthesize(self, text: str, output_path: str, *, voice: Optional[str]=None, model: Optional[str]=None, speed: Optional[float]=None, format: str=DEFAULT_OUTPUT_FORMAT, **extra: Any)` (method) — Synthesize ``text`` and write audio bytes to ``output_path``.
- L219 `stream(self, text: str, *, voice: Optional[str]=None, model: Optional[str]=None, format: str='opus', **extra: Any)` (method) — Stream synthesized audio bytes.
- L245 `voice_compatible(self)` (method) — Whether output is suitable for voice-bubble delivery.
- L263 `resolve_output_format(value: Optional[str])` (function) — Clamp an output_format value to the valid set.
