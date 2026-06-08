---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:44'
updated: '2026-06-08T00:38:44'
---

# tools/transcription_tools.py

Symbols in `tools/transcription_tools.py`.

- L50 `get_env_value(name, default=None)` (function) — Read env values through the live config module.
- L71 `_safe_find_spec(module_name: str)` (function)
- L120 `_load_stt_config()` (function) — Load the ``stt`` section from user config, falling back to defaults.
- L129 `is_stt_enabled(stt_config: Optional[dict]=None)` (function) — Return whether STT is enabled in config.
- L137 `_has_openai_audio_backend()` (function) — Return True when OpenAI audio can use config credentials, env credentials, or the managed gateway.
- L146 `_find_binary(binary_name: str)` (function) — Find a local binary, checking common Homebrew/local prefixes as well as PATH.
- L155 `_find_ffmpeg_binary()` (function)
- L159 `_find_whisper_binary()` (function)
- L163 `_get_local_command_template()` (function)
- L178 `_has_local_command()` (function)
- L182 `_normalize_local_model(model_name: Optional[str])` (function) — Return a valid faster-whisper model size, mapping cloud-only names to the default.
- L203 `_normalize_local_command_model(model_name: Optional[str])` (function)
- L207 `_try_lazy_install_stt()` (function) — Attempt to lazy-install faster-whisper and return True on success.
- L273 `_get_stt_section(stt_config: Dict[str, Any], name: str)` (function) — Return an stt sub-section if it's a dict, else an empty dict.
- L281 `_get_named_stt_provider_config(stt_config: Dict[str, Any], name: str)` (function) — Return the config dict for a user-declared STT command provider.
- L311 `_is_command_stt_provider_config(config: Dict[str, Any])` (function) — Return True when *config* declares a command-type STT provider.
- L322 `_resolve_command_stt_provider_config(provider: str, stt_config: Dict[str, Any])` (function) — Return the provider config if *provider* resolves to a command type.
- L343 `_iter_command_stt_providers(stt_config: Dict[str, Any])` (function) — Yield (name, config) pairs for every declared command-type STT provider.
- L354 `_has_any_command_stt_provider(stt_config: Optional[Dict[str, Any]]=None)` (function) — Return True when any command-type STT provider is configured.
- L363 `_get_command_stt_timeout(config: Dict[str, Any])` (function) — Return timeout in seconds, falling back when invalid.
- L375 `_get_command_stt_output_format(config: Dict[str, Any])` (function) — Return the validated output format (txt/json/srt/vtt).
- L386 `_shell_quote_context_stt(command_template: str, position: int)` (function) — Return the shell quote character active right before *position*.
- L418 `_quote_command_stt_placeholder(value: str, quote_context: Optional[str])` (function) — Quote a placeholder value for its position in a shell command template.
- L438 `_render_command_stt_template(command_template: str, placeholders: Dict[str, str])` (function) — Replace supported placeholders while preserving ``{{`` / ``}}``.
- L478 `_terminate_command_stt_process_tree(proc: subprocess.Popen)` (function) — Best-effort termination of a shell process and all of its children.
- L542 `_run_command_stt(command: str, timeout: float)` (function) — Run a command-provider shell command with process-tree timeout cleanup.
- L585 `_read_command_stt_output(output_path: Path, stdout: str, fmt: str)` (function) — Return the transcript text from a command-provider invocation.
- L615 `_transcribe_command_stt(file_path: str, provider_name: str, config: Dict[str, Any], stt_config: Dict[str, Any], model_override: Optional[str]=None)` (function) — Transcribe via a user-declared ``stt.providers.<name>: type: command``.
- L744 `_get_provider(stt_config: dict)` (function) — Determine which STT provider to use.
- L872 `_dispatch_to_plugin_provider(file_path: str, provider: str, stt_config: Optional[Dict[str, Any]]=None, *, model: Optional[str]=None, language: Optional[str]=None)` (function) — Route the call to a plugin-registered transcription provider, or
- L1020 `_validate_audio_file(file_path: str)` (function) — Validate the audio file.  Returns an error dict or None if OK.
- L1075 `_looks_like_cuda_lib_error(exc: BaseException)` (function) — Heuristic: is this exception a missing/broken CUDA runtime library?
- L1087 `_load_local_whisper_model(model_name: str)` (function) — Load faster-whisper with graceful CUDA → CPU fallback.
- L1114 `_transcribe_local(file_path: str, model_name: str)` (function) — Transcribe using faster-whisper (local, free).
- L1175 `_prepare_local_audio(file_path: str, work_dir: str)` (function) — Normalize audio for local CLI STT when needed.
- L1200 `_transcribe_local_command(file_path: str, model_name: str)` (function) — Run the configured local STT command template and read back a .txt transcript.
- L1276 `_transcribe_groq(file_path: str, model_name: str)` (function) — Transcribe using Groq Whisper API (free tier available).
- L1328 `_transcribe_openai(file_path: str, model_name: str)` (function) — Transcribe using OpenAI Whisper API (paid).
- L1385 `_transcribe_mistral(file_path: str, model_name: str)` (function) — Transcribe using Mistral Voxtral Transcribe API.
- L1429 `_transcribe_xai(file_path: str, model_name: str)` (function) — Transcribe using xAI Grok STT API.
- L1536 `_transcribe_elevenlabs(file_path: str, model_name: str)` (function) — Transcribe using ElevenLabs Scribe STT API.
- L1622 `transcribe_audio(file_path: str, model: Optional[str]=None)` (function) — Transcribe an audio file using the configured STT provider.
- L1752 `_resolve_openai_audio_client_config()` (function) — Return direct OpenAI audio config or a managed gateway fallback.
- L1782 `_extract_transcript_text(transcription: Any)` (function) — Normalize text and JSON transcription responses to a plain string.
