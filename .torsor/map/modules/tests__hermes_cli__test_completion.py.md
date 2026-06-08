---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/hermes_cli/test_completion.py

Symbols in `tests/hermes_cli/test_completion.py`.

- L19 `_make_parser()` (function) — Build a minimal parser that mirrors the real hermes structure.
- L63 `TestWalk` (class)
- L64 `test_top_level_subcommands_extracted(self)` (method)
- L68 `test_nested_subcommands_extracted(self)` (method)
- L73 `test_aliases_not_duplicated(self)` (method) — 'foreground' is an alias of 'run' — must not appear as separate entry.
- L79 `test_flags_extracted(self)` (method)
- L84 `test_help_text_captured(self)` (method)
- L94 `TestGenerateBash` (class)
- L95 `test_contains_completion_function_and_register(self)` (method)
- L100 `test_top_level_commands_present(self)` (method)
- L105 `test_nested_subcommands_in_case(self)` (method)
- L110 `test_valid_bash_syntax(self)` (method) — Script must pass `bash -n` syntax check.
- L127 `TestGenerateZsh` (class)
- L128 `test_contains_compdef_header(self)` (method)
- L132 `test_top_level_commands_present(self)` (method)
- L137 `test_nested_describe_blocks(self)` (method)
- L143 `test_registers_compdef_instead_of_invoking_completion_function(self)` (method)
- L148 `test_preserves_valid_zsh_arguments_alias_syntax(self)` (method)
- L156 `test_valid_zsh_syntax(self)` (method)
- L169 `test_zsh_eval_style_source_registers_after_compinit(self)` (method)
- L196 `TestGenerateFish` (class)
- L197 `test_disables_file_completion(self)` (method)
- L201 `test_top_level_commands_present(self)` (method)
- L206 `test_subcommand_guard_present(self)` (method)
- L210 `test_valid_fish_syntax(self)` (method) — Script must be accepted by fish without errors.
- L229 `TestSubcommandDrift` (class)
- L230 `test_SUBCOMMANDS_covers_required_commands(self)` (method) — _SUBCOMMANDS must include all known top-level commands so that
- L256 `TestProfileCompletion` (class) — Ensure profile name completion is present in all shell outputs.
- L259 `test_bash_has_profiles_helper(self)` (method)
- L264 `test_bash_completes_profiles_after_p_flag(self)` (method)
- L270 `test_bash_profile_subcommand_has_action_completion(self)` (method)
- L274 `test_bash_profile_actions_complete_profile_names(self)` (method) — After 'hermes profile use', complete with profile names.
- L289 `test_zsh_has_profiles_helper(self)` (method)
- L294 `test_zsh_has_profile_flag_completion(self)` (method)
- L299 `test_zsh_profile_actions_complete_names(self)` (method)
- L303 `test_fish_has_profiles_helper(self)` (method)
- L308 `test_fish_has_profile_flag_completion(self)` (method)
- L313 `test_fish_profile_actions_complete_names(self)` (method)
