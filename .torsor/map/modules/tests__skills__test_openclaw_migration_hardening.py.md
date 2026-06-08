---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/skills/test_openclaw_migration_hardening.py

Symbols in `tests/skills/test_openclaw_migration_hardening.py`.

- L29 `_load()` (function)
- L41 `test_redact_replaces_secret_by_key_name()` (function)
- L47 `test_redact_replaces_secret_by_value_pattern()` (function)
- L55 `test_redact_handles_github_token_pattern()` (function)
- L62 `test_redact_handles_slack_token_pattern()` (function)
- L68 `test_redact_handles_google_api_key_pattern()` (function)
- L75 `test_redact_handles_bearer_header()` (function)
- L84 `test_redact_is_recursive()` (function)
- L99 `test_redact_preserves_non_secret_keys_and_values()` (function)
- L106 `test_redact_normalizes_key_case_and_punctuation()` (function)
- L114 `test_redact_leaves_env_secretref_alone()` (function) — SecretRef-like shapes ({source: env, id: ...}) are pointers, not secrets.
- L125 `test_write_report_redacts_api_keys_on_disk(tmp_path)` (function)
- L154 `_make_minimal_migrator(mod, tmp_path, **overrides)` (function)
- L175 `test_dry_run_report_includes_rerun_next_step(tmp_path)` (function)
- L183 `test_conflict_produces_overwrite_warning(tmp_path)` (function)
- L200 `test_error_produces_inspect_warning(tmp_path)` (function)
- L208 `test_provider_keys_skipped_warning_when_secrets_disabled(tmp_path)` (function)
- L225 `test_config_apply_block_flips_on_config_yaml_conflict(tmp_path)` (function)
- L238 `test_config_apply_block_flips_on_config_yaml_error(tmp_path)` (function)
- L251 `test_config_apply_block_does_not_flip_on_non_config_conflict(tmp_path)` (function)
- L263 `test_run_if_selected_skips_config_ops_after_block(tmp_path)` (function)
- L279 `test_run_if_selected_runs_non_config_ops_even_after_block(tmp_path)` (function)
- L290 `test_dry_run_never_blocks_even_after_conflict(tmp_path)` (function) — Dry runs must preview the full plan — blocking mid-preview would hide
- L306 `test_json_mode_emits_structured_report(tmp_path)` (function) — End-to-end: run the CLI with --json and no --execute, parse stdout.
- L337 `test_json_mode_redacts_secrets_in_output(tmp_path)` (function) — Even plan-only JSON output goes through the redactor — the stdout
- L371 `test_item_result_has_sensitive_field()` (function)
- L377 `test_record_honors_sensitive_flag(tmp_path)` (function)
- L384 `test_status_constants_match_historical_strings()` (function) — Downstream consumers (claw.py, tests, docs) depend on these string values.
