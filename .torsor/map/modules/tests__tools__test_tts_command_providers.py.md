---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:44'
updated: '2026-06-08T00:38:44'
---

# tests/tools/test_tts_command_providers.py

Symbols in `tests/tools/test_tts_command_providers.py`.

- L50 `_python_copy_command(output_placeholder: str='{output_path}')` (function) — Return a cross-platform shell command that copies {input_path} -> output.
- L64 `TestResolveCommandProviderConfig` (class)
- L65 `test_builtin_names_are_never_command_providers(self)` (method)
- L75 `test_missing_provider_returns_none(self)` (method)
- L79 `test_user_declared_command_provider_resolves(self)` (method)
- L89 `test_type_command_is_implied_when_command_is_set(self)` (method)
- L94 `test_other_type_values_reject(self)` (method)
- L98 `test_empty_command_rejects(self)` (method)
- L102 `test_case_insensitive_lookup(self)` (method)
- L106 `test_native_piper_cannot_be_shadowed_by_command_entry(self)` (method) — Regression guard for PR that added native Piper as a built-in.
- L117 `TestGetNamedProviderConfig` (class)
- L118 `test_providers_block_wins(self)` (method)
- L123 `test_legacy_tts_name_block_still_resolves(self)` (method)
- L129 `test_builtin_names_do_not_leak_through_legacy_path(self)` (method) — ``tts.openai`` must never be mistaken for a command provider.
- L135 `TestIsCommandProviderConfig` (class)
- L136 `test_empty_dict_is_false(self)` (method)
- L139 `test_non_dict_is_false(self)` (method)
- L143 `test_type_mismatch_is_false(self)` (method)
- L151 `TestIterCommandProviders` (class)
- L152 `test_iterates_only_user_command_providers(self)` (method)
- L164 `test_has_any_command_provider_detects_declared(self)` (method)
- L168 `test_has_any_command_provider_when_none(self)` (method)
- L177 `TestConfigGetters` (class)
- L178 `test_timeout_defaults(self)` (method)
- L181 `test_timeout_coerces_string(self)` (method)
- L184 `test_timeout_rejects_non_positive(self)` (method)
- L188 `test_timeout_rejects_garbage(self)` (method)
- L191 `test_timeout_seconds_alias(self)` (method)
- L194 `test_output_format_defaults(self)` (method)
- L197 `test_output_format_path_override(self)` (method)
- L200 `test_output_format_unknown_path_falls_back_to_config(self)` (method)
- L203 `test_output_format_rejects_unknown(self)` (method)
- L206 `test_output_format_supported_set(self)` (method)
- L209 `test_voice_compatible_boolean(self)` (method)
- L213 `test_voice_compatible_string(self)` (method)
- L217 `test_voice_compatible_default_off(self)` (method)
- L225 `TestMaxTextLengthForCommandProviders` (class)
- L226 `test_default_for_command_provider(self)` (method)
- L230 `test_override_under_providers(self)` (method)
- L234 `test_override_under_legacy_tts_name_block(self)` (method)
- L238 `test_non_command_unknown_provider_still_falls_back(self)` (method)
- L246 `TestShellQuoteContext` (class)
- L247 `test_bare_context(self)` (method)
- L252 `test_inside_single_quotes(self)` (method)
- L257 `test_inside_double_quotes(self)` (method)
- L262 `test_escaped_double_quote_inside_double(self)` (method)
- L268 `TestRenderCommandTtsTemplate` (class)
- L269 `test_substitutes_all_placeholders(self)` (method)
- L286 `test_quotes_paths_with_spaces(self)` (method)
- L304 `test_literal_braces_survive(self)` (method)
- L316 `test_injection_is_neutralized(self)` (method) — Embedded shell metacharacters in a placeholder value must be quoted.
- L336 `test_preserves_shell_quoting_style(self)` (method)
- L355 `TestGenerateCommandTts` (class)
- L356 `test_writes_output_file(self, tmp_path)` (method)
- L372 `test_empty_command_raises(self, tmp_path)` (method)
- L382 `test_nonzero_exit_raises_runtime(self, tmp_path)` (method)
- L393 `test_empty_output_raises_runtime(self, tmp_path)` (method)
- L406 `test_timeout_raises_runtime(self, tmp_path)` (method)
- L425 `TestTextToSpeechToolWithCommandProvider` (class)
- L426 `test_command_provider_dispatches_end_to_end(self, tmp_path)` (method)
- L453 `test_voice_compatible_opt_in_toggles_flag(self, tmp_path)` (method) — voice_compatible=true is reflected in the response when the
- L476 `test_missing_command_falls_through_to_builtin(self, tmp_path)` (method) — A provider entry with an empty command is not a command
- L494 `TestCheckTtsRequirements` (class)
- L495 `test_configured_command_provider_satisfies_requirement(self)` (method)
