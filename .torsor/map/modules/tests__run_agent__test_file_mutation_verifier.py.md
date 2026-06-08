---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/run_agent/test_file_mutation_verifier.py

Symbols in `tests/run_agent/test_file_mutation_verifier.py`.

- L39 `TestExtractFileMutationTargets` (class)
- L40 `test_non_mutating_tool_returns_empty(self)` (method)
- L44 `test_write_file_returns_single_path(self)` (method)
- L48 `test_write_file_missing_path_returns_empty(self)` (method)
- L51 `test_patch_replace_mode_returns_path(self)` (method)
- L55 `test_patch_default_mode_is_replace(self)` (method)
- L60 `test_patch_v4a_single_file(self)` (method)
- L73 `test_patch_v4a_multi_file(self)` (method)
- L87 `test_patch_v4a_missing_body_returns_empty(self)` (method)
- L97 `TestExtractErrorPreview` (class)
- L98 `test_json_error_field_preferred(self)` (method)
- L102 `test_plain_string_falls_through(self)` (method)
- L105 `test_long_preview_truncated(self)` (method)
- L111 `test_none_returns_empty(self)` (method)
- L120 `_bare_agent()` (function) — Skip __init__ and only attach the per-turn state dict.
- L134 `TestRecordFileMutationResult` (class)
- L135 `test_non_mutating_tool_ignored(self)` (method)
- L142 `test_failure_recorded(self)` (method)
- L154 `test_success_removes_prior_failure(self)` (method)
- L169 `test_write_file_with_lint_error_counts_as_landed(self)` (method)
- L193 `test_patch_with_lsp_diagnostics_counts_as_landed(self)` (method)
- L219 `test_repeated_failure_keeps_first_error(self)` (method)
- L233 `test_v4a_multi_file_all_tracked(self)` (method)
- L247 `test_no_state_dict_silent_noop(self)` (method) — When called outside run_conversation the state dict is absent.
- L261 `test_missing_path_arg_recorded_nowhere(self)` (method)
- L277 `TestFormatFooter` (class)
- L278 `test_empty_returns_empty_string(self)` (method)
- L281 `test_single_failure(self)` (method)
- L290 `test_truncation_at_10_entries(self)` (method)
- L303 `test_paths_are_backtick_wrapped(self)` (method) — Footer paths must be inline-code wrapped so the gateway's bare-path
- L326 `test_footer_path_not_extracted_by_gateway(self)` (method) — End-to-end: the gateway's extract_local_files must NOT pull a
- L360 `TestVerifierEnabled` (class)
- L361 `test_default_is_enabled(self, monkeypatch)` (method)
- L371 `test_env_disables(self, monkeypatch, value)` (method)
- L376 `test_env_enables_over_config(self, monkeypatch)` (method)
- L386 `test_config_disables_when_no_env(self, monkeypatch)` (method)
- L402 `test_file_mutating_tools_set_shape()` (function) — write_file + patch are the only tools the verifier tracks.
