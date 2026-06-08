---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:44'
updated: '2026-06-08T00:38:44'
---

# tools/tts_tool.py

Symbols in `tools/tts_tool.py`.

- L58 `get_env_value(name, default=None)` (function) — Read env values through the live config module.
- L85 `_import_edge_tts()` (function) — Lazy import edge_tts. Returns the module or raises ImportError.
- L97 `_import_elevenlabs()` (function) — Lazy import ElevenLabs client. Returns the class or raises ImportError.
- L118 `_import_openai_client()` (function) — Lazy import OpenAI client. Returns the class or raises ImportError.
- L123 `_import_mistral_client()` (function) — Lazy import Mistral client. Returns the class or raises ImportError.
- L141 `_import_sounddevice()` (function) — Lazy import sounddevice. Returns the module or raises ImportError/OSError.
- L147 `_import_kittentts()` (function) — Lazy import KittenTTS. Returns the class or raises ImportError.
- L153 `_import_piper()` (function) — Lazy import Piper. Returns the PiperVoice class or raises ImportError.
- L198 `_get_default_output_dir()` (function)
- L243 `_resolve_max_text_length(provider: Optional[str], tts_config: Optional[Dict[str, Any]]=None)` (function) — Return the input-character cap for *provider*.
- L302 `_load_tts_config()` (function) — Load TTS configuration from ~/.hermes/config.yaml.
- L321 `_get_provider(tts_config: Dict[str, Any])` (function) — Get the configured TTS provider name.
- L376 `_get_provider_section(tts_config: Dict[str, Any], name: str)` (function) — Return a provider config block if it's a dict, else an empty dict.
- L384 `_get_named_provider_config(tts_config: Dict[str, Any], name: str)` (function) — Return the config dict for a user-declared provider.
- L408 `_is_command_provider_config(config: Dict[str, Any])` (function) — Return True when *config* declares a command-type provider.
- L419 `_resolve_command_provider_config(provider: str, tts_config: Dict[str, Any])` (function) — Return the provider config if *provider* resolves to a command type.
- L440 `_dispatch_to_plugin_provider(text: str, output_path: str, provider: str, tts_config: Dict[str, Any])` (function) — Route the call to a plugin-registered TTS provider, or return None.
- L531 `_plugin_provider_is_voice_compatible(provider: str)` (function) — Return True when the registered plugin provider opts into voice
- L557 `_iter_command_providers(tts_config: Dict[str, Any])` (function) — Yield (name, config) pairs for every declared command-type provider.
- L568 `_get_command_tts_timeout(config: Dict[str, Any])` (function) — Return timeout in seconds, falling back when invalid.
- L580 `_get_command_tts_output_format(config: Dict[str, Any], output_path: Optional[str]=None)` (function) — Return the validated output format (mp3/wav/ogg/flac).
- L598 `_is_command_tts_voice_compatible(config: Dict[str, Any])` (function) — Return True only when the user explicitly opted in to voice delivery.
- L606 `_shell_quote_context(command_template: str, position: int)` (function) — Return the shell quote character active right before *position*.
- L637 `_quote_command_tts_placeholder(value: str, quote_context: Optional[str])` (function) — Quote a placeholder value for its position in a shell command template.
- L654 `_render_command_tts_template(command_template: str, placeholders: Dict[str, str])` (function) — Replace supported placeholders while preserving ``{{`` / ``}}``.
- L684 `_terminate_command_tts_process_tree(proc: subprocess.Popen)` (function) — Best-effort termination of a shell process and all of its children.
- L735 `_run_command_tts(command: str, timeout: float)` (function) — Run a command-provider shell command with process-tree timeout cleanup.
- L775 `_configured_command_tts_output_path(path: Path, config: Dict[str, Any])` (function) — Return an output path whose extension matches the provider's output_format.
- L781 `_generate_command_tts(text: str, output_path: str, provider_name: str, config: Dict[str, Any], tts_config: Dict[str, Any])` (function) — Generate speech by running a user-configured shell command.
- L849 `_has_any_command_tts_provider(tts_config: Optional[Dict[str, Any]]=None)` (function) — Return True when any command-type TTS provider is configured.
- L861 `_has_ffmpeg()` (function) — Check if ffmpeg is available on the system.
- L866 `_convert_to_opus(mp3_path: str)` (function) — Convert an MP3 file to OGG Opus format for Telegram voice bubbles.
- L904 `_generate_edge_tts(text: str, output_path: str, tts_config: Dict[str, Any])` (function) — Generate audio using Edge TTS.
- L934 `_generate_elevenlabs(text: str, output_path: str, tts_config: Dict[str, Any])` (function) — Generate audio using ElevenLabs.
- L980 `_generate_openai_tts(text: str, output_path: str, tts_config: Dict[str, Any])` (function) — Generate audio using OpenAI TTS.
- L1069 `_xai_bool_config(value: Any, default: bool=False)` (function) — Coerce common YAML/env bool spellings without treating random strings as true.
- L1086 `_apply_xai_auto_speech_tags(text: str)` (function) — Add light xAI speech tags for more natural voice-mode replies.
- L1105 `_generate_xai_tts(text: str, output_path: str, tts_config: Dict[str, Any])` (function) — Generate audio using xAI TTS.
- L1180 `_generate_minimax_tts(text: str, output_path: str, tts_config: Dict[str, Any])` (function) — Generate audio using MiniMax TTS API.
- L1312 `_generate_mistral_tts(text: str, output_path: str, tts_config: Dict[str, Any])` (function) — Generate audio using Mistral Voxtral TTS API.
- L1361 `_wrap_pcm_as_wav(pcm_bytes: bytes, sample_rate: int=GEMINI_TTS_SAMPLE_RATE, channels: int=GEMINI_TTS_CHANNELS, sample_width: int=GEMINI_TTS_SAMPLE_WIDTH)` (function) — Wrap raw signed-little-endian PCM with a standard WAV RIFF header.
- L1395 `_generate_gemini_tts(text: str, output_path: str, tts_config: Dict[str, Any])` (function) — Generate audio using Google Gemini TTS.
- L1530 `_check_neutts_available()` (function) — Check if the neutts engine is importable (installed locally).
- L1539 `_check_kittentts_available()` (function) — Check if the kittentts engine is importable (installed locally).
- L1548 `_default_neutts_ref_audio()` (function) — Return path to the bundled default voice reference audio.
- L1553 `_default_neutts_ref_text()` (function) — Return path to the bundled default voice reference transcript.
- L1558 `_generate_neutts(text: str, output_path: str, tts_config: Dict[str, Any])` (function) — Generate speech using the local NeuTTS engine.
- L1621 `_check_piper_available()` (function) — Check whether the piper-tts package is importable.
- L1630 `_get_piper_voices_dir()` (function) — Return the directory where Hermes caches Piper voice models.
- L1642 `_resolve_piper_voice_path(voice: str, download_dir: Path)` (function) — Resolve *voice* (a model name or path) to a concrete .onnx file path.
- L1694 `_generate_piper_tts(text: str, output_path: str, tts_config: Dict[str, Any])` (function) — Generate speech using the local Piper engine.
- L1780 `_generate_kittentts(text: str, output_path: str, tts_config: Dict[str, Any])` (function) — Generate speech using KittenTTS local ONNX model.
- L1838 `text_to_speech_tool(text: str, output_path: Optional[str]=None)` (function) — Convert text to speech audio.
- L2153 `check_tts_requirements()` (function) — Check if at least one TTS provider is available.
- L2210 `_resolve_openai_audio_client_config()` (function) — Return direct OpenAI audio config or a managed gateway fallback.
- L2237 `_has_openai_audio_backend()` (function) — Return True when OpenAI audio can use direct credentials or the managed gateway.
- L2261 `_strip_markdown_for_tts(text: str)` (function) — Remove markdown formatting that shouldn't be spoken aloud.
- L2276 `stream_tts_to_speaker(text_queue: queue.Queue, stop_event: threading.Event, tts_done_event: threading.Event, display_callback: Optional[Callable[[str], None]]=None)` (function) — Consume text deltas from *text_queue*, buffer them into sentences,
