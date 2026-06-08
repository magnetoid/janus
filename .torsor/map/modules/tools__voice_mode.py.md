---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:44'
updated: '2026-06-08T00:38:44'
---

# tools/voice_mode.py

Symbols in `tools/voice_mode.py`.

- L32 `_import_audio()` (function) — Lazy-import sounddevice and numpy.  Returns (sd, np).
- L43 `_audio_available()` (function) — Return True if audio libraries can be imported.
- L55 `_voice_capture_install_hint()` (function)
- L61 `_termux_microphone_command()` (function)
- L68 `_termux_api_app_installed()` (function)
- L84 `_termux_voice_capture_available()` (function)
- L88 `_pulse_socket_reachable()` (function) — Return True if a PulseAudio/PipeWire socket is reachable on disk.
- L141 `detect_audio_environment()` (function) — Detect if the current environment supports audio I/O.
- L290 `play_beep(frequency: int=880, duration: float=0.12, count: int=1)` (function) — Play a short beep tone using numpy + sounddevice.
- L334 `TermuxAudioRecorder` (class) — Recorder backend that uses Termux:API microphone capture commands.
- L339 `__init__(self)` (method)
- L347 `is_recording(self)` (method)
- L351 `elapsed_seconds(self)` (method)
- L357 `current_rms(self)` (method)
- L360 `start(self, on_silence_stop=None)` (method)
- L404 `_stop_termux_recording(self)` (method)
- L410 `stop(self)` (method)
- L438 `cancel(self)` (method)
- L455 `shutdown(self)` (method)
- L462 `AudioRecorder` (class) — Thread-safe audio recorder using sounddevice.InputStream.
- L480 `__init__(self)` (method)
- L507 `elapsed_seconds(self)` (method)
- L513 `current_rms(self)` (method) — Current audio input RMS level (0-32767). Updated each audio chunk.
- L518 `is_recording(self)` (method) — Whether audio recording is currently active.
- L524 `_ensure_stream(self)` (method) — Create the audio InputStream once and keep it alive.
- L654 `start(self, on_silence_stop=None)` (method) — Start capturing audio from the default input device.
- L700 `_close_stream_with_timeout(self, timeout: float=3.0)` (method) — Close the audio stream with a timeout to prevent CoreAudio hangs.
- L724 `stop(self)` (method) — Stop recording and write captured audio to a WAV file.
- L767 `cancel(self)` (method) — Stop recording and discard all captured audio.
- L779 `shutdown(self)` (method) — Release the audio stream.  Call when voice mode is disabled.
- L792 `_write_wav(audio_data)` (method) — Write numpy int16 audio data to a WAV file.
- L812 `create_audio_recorder()` (function) — Return the best recorder backend for the current environment.
- L860 `is_whisper_hallucination(transcript: str)` (function) — Check if a transcript is a known Whisper hallucination on silence.
- L877 `transcribe_recording(wav_path: str, model: Optional[str]=None)` (function) — Transcribe a WAV recording using the existing Whisper pipeline.
- L905 `_should_chunk_for_transcription(file_path: str, max_file_size: int)` (function) — Return whether a CLI WAV recording needs to be split before STT.
- L915 `_transcribe_wav_in_chunks(wav_path: str, *, model: Optional[str], max_file_size: int)` (function) — Split an oversized WAV into provider-sized chunks and join transcripts.
- L965 `_split_wav_for_transcription(wav_path: str, *, max_file_size: int)` (function) — Write WAV chunks small enough to pass the shared STT file-size gate.
- L1022 `stop_playback()` (function) — Interrupt the currently playing audio (if any).
- L1042 `play_audio_file(file_path: str)` (function) — Play an audio file through the default output device.
- L1123 `check_voice_requirements()` (function) — Check if all voice mode requirements are met.
- L1190 `cleanup_temp_recordings(max_age_seconds: int=3600)` (function) — Remove old temporary voice recording files.
