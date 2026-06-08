---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# hermes_cli/voice.py

Symbols in `hermes_cli/voice.py`.

- L86 `voice_record_key_from_config(cfg: Any)` (function) — Shape-safe ``cfg.voice.record_key`` lookup.
- L108 `normalize_voice_record_key_for_prompt_toolkit(raw: Any)` (function) — Coerce ``voice.record_key`` into prompt_toolkit's ``c-x`` / ``a-x`` format.
- L185 `format_voice_record_key_for_status(raw: Any)` (function) — Render ``voice.record_key`` for ``/voice status`` in CLI-friendly form.
- L226 `_debug(msg: str)` (function) — Emit a debug breadcrumb when HERMES_VOICE_DEBUG=1.
- L247 `_beeps_enabled()` (function) — CLI parity: voice.beep_enabled in config.yaml (default True).
- L260 `_play_beep(frequency: int, count: int=1)` (function) — Audible cue matching cli.py's record/stop beeps.
- L309 `start_recording()` (function) — Begin capturing from the default input device (push-to-talk).
- L324 `stop_and_transcribe()` (function) — Stop the active push-to-talk recording, transcribe, return text.
- L369 `start_continuous(on_transcript: Callable[[str], None], on_status: Optional[Callable[[str], None]]=None, on_silent_limit: Optional[Callable[[], None]]=None, silence_threshold: int=200, silence_duration: float=3.0, auto_restart: bool=True)` (function) — Start a VAD-driven continuous recording loop.
- L447 `stop_continuous(force_transcribe: bool=False)` (function) — Stop the active continuous loop and release the microphone.
- L569 `is_continuous_active()` (function) — Whether a continuous voice loop is currently running.
- L575 `_continuous_on_silence()` (function) — AudioRecorder silence callback — runs in a daemon thread.
- L740 `speak_text(text: str)` (function) — Synthesize ``text`` with the configured TTS provider and play it.
