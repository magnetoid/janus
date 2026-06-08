---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:44'
updated: '2026-06-08T00:38:44'
---

# tests/tools/test_transcription_command_providers.py

Symbols in `tests/tools/test_transcription_command_providers.py`.

- L51 `_make_silent_wav(path: Path, seconds: float=0.1)` (function) — Write a minimal silent .wav file so _validate_audio_file accepts it.
- L63 `_python_emit_command(transcript_text: str, output_placeholder: str='{output_path}')` (function) — Return a portable shell command that writes ``transcript_text`` to {output_path}.
- L75 `_python_emit_stdout_command(transcript_text: str)` (function) — Return a portable shell command that writes transcript to stdout only.
- L87 `TestResolveCommandSTTProviderConfig` (class)
- L88 `test_builtin_names_are_never_command_providers(self)` (method)
- L102 `test_missing_provider_returns_none(self)` (method)
- L106 `test_empty_provider_returns_none(self)` (method)
- L110 `test_none_provider_short_circuits(self)` (method)
- L119 `test_provider_without_command_field_returns_none(self)` (method)
- L123 `test_provider_with_empty_command_returns_none(self)` (method)
- L127 `test_provider_with_explicit_type_other_than_command_returns_none(self)` (method)
- L131 `test_provider_with_command_string_and_no_type_resolves(self)` (method)
- L137 `test_provider_with_explicit_type_command_resolves(self)` (method)
- L142 `test_resolution_is_case_insensitive(self)` (method)
- L153 `TestGetNamedSTTProviderConfig` (class)
- L154 `test_canonical_stt_providers_lookup(self)` (method)
- L159 `test_legacy_stt_dot_name_fallback(self)` (method)
- L166 `test_builtin_name_is_not_legacy_resolved(self)` (method)
- L173 `test_missing_returns_empty(self)` (method)
- L177 `test_canonical_wins_over_legacy(self)` (method)
- L190 `TestSTTCommandHelpers` (class)
- L191 `test_timeout_uses_default_when_missing(self)` (method)
- L194 `test_timeout_accepts_int_and_float(self)` (method)
- L198 `test_timeout_falls_back_when_invalid(self)` (method)
- L206 `test_timeout_legacy_key(self)` (method)
- L209 `test_output_format_defaults_to_txt(self)` (method)
- L213 `test_output_format_validates_against_allowed_set(self)` (method)
- L217 `test_output_format_rejects_unknown(self)` (method)
- L223 `test_output_format_strips_leading_dot(self)` (method)
- L226 `test_output_format_legacy_key(self)` (method)
- L229 `test_iter_command_providers_yields_only_command_type(self)` (method)
- L241 `test_iter_command_providers_excludes_builtins(self)` (method)
- L254 `test_has_any_command_provider_false_when_none_configured(self)` (method)
- L257 `test_has_any_command_provider_true_when_one_configured(self)` (method)
- L267 `TestRenderCommandSTTTemplate` (class)
- L268 `test_renders_all_placeholders(self)` (method)
- L285 `test_preserves_doubled_braces(self)` (method)
- L295 `test_shell_quote_outside_quotes_uses_shlex(self)` (method)
- L304 `test_shell_quote_inside_single_quotes(self)` (method)
- L312 `test_shell_quote_inside_double_quotes(self)` (method)
- L320 `test_placeholder_not_in_dict_passes_through(self)` (method)
- L334 `TestTranscribeCommandSTT` (class)
- L335 `test_writes_transcript_to_output_path(self, tmp_path)` (method)
- L346 `test_reads_transcript_from_stdout_when_no_file(self, tmp_path)` (method)
- L356 `test_missing_command_returns_error(self, tmp_path)` (method)
- L362 `test_missing_audio_returns_error(self, tmp_path)` (method)
- L370 `test_nonzero_exit_returns_error_with_stderr(self, tmp_path)` (method)
- L384 `test_timeout_returns_clean_error(self, tmp_path)` (method)
- L395 `test_model_override_passed_to_template(self, tmp_path)` (method)
- L410 `test_config_model_used_when_no_override(self, tmp_path)` (method)
- L421 `test_language_from_provider_config_wins(self, tmp_path)` (method)
- L435 `test_language_falls_back_to_stt_section(self, tmp_path)` (method)
- L447 `test_language_defaults_to_en(self, tmp_path)` (method)
- L463 `TestTranscribeAudioDispatchToCommandProvider` (class) — Verify ``transcribe_audio()`` picks command providers correctly.
- L470 `_config_with_command_provider(self, name: str, command: str)` (method)
- L478 `test_command_provider_dispatches_via_transcribe_audio(self, tmp_path)` (method)
- L489 `test_builtin_name_shadow_does_not_route_to_command(self, tmp_path)` (method)
- L507 `test_unknown_provider_no_command_falls_through_to_error(self, tmp_path)` (method)
- L521 `TestCommandWinsOverPlugin` (class) — When a name has BOTH a command provider AND a registered plugin, the
- L527 `test_command_wins_when_both_configured(self, tmp_path)` (method)
- L569 `test_plugin_fires_when_no_command_provider(self, tmp_path)` (method)
