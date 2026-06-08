---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# plugins/platforms/discord/voice_mixer.py

Symbols in `plugins/platforms/discord/voice_mixer.py`.

- L55 `_require_numpy()` (function) — Import numpy lazily.
- L77 `MixerChild` (class) — A single audio stream feeding into :class:`VoiceMixer`.
- L89 `__init__(self, name: str, pcm: bytes, *, loop: bool=False, gain: float=1.0, is_speech: bool=False, fade_in_ms: int=0)` (method)
- L116 `finished(self)` (method)
- L119 `read_frame(self)` (method) — Return the next 20 ms frame as an int16 ndarray, or None if done.
- L148 `VoiceMixer` (class) — A continuous ``discord.AudioSource`` that mixes N child streams.
- L158 `is_opus(self)` (method)
- L161 `__init__(self, *, ambient_gain: float=0.18, duck_gain: float=0.06, speech_gain: float=1.0, duck_release_ms: int=400)` (method)
- L188 `set_ambient(self, pcm: Optional[bytes], *, gain: Optional[float]=None)` (method) — Install (or clear, with ``pcm=None``) the looping ambient bed.
- L201 `_effective_ambient_gain(self)` (method)
- L208 `play_speech(self, pcm: bytes, *, gain: Optional[float]=None, fade_in_ms: int=40)` (method) — Layer a one-shot speech clip over the ambient bed (ducks ambient).
- L226 `speech_active(self)` (method)
- L230 `stop_speech(self)` (method) — Drop any in-flight speech immediately and release the duck.
- L236 `_begin_duck_release_locked(self)` (method)
- L244 `read(self)` (method) — Return one 20 ms mixed PCM frame (always FRAME_SIZE bytes).
- L292 `cleanup(self)` (method)
- L303 `decode_to_pcm(path: str, *, timeout: float=30.0)` (function) — Decode any audio file to 48 kHz / stereo / s16le PCM via ffmpeg.
- L336 `synth_ambient_pcm(seconds: float=4.0)` (function) — Synthesise a subtle looping ambient bed (no asset file required).
