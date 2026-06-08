---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/hermes_cli/test_config.py

Symbols in `tests/hermes_cli/test_config.py`.

- L28 `TestGetHermesHome` (class)
- L29 `test_default_path(self)` (method)
- L35 `test_env_override(self)` (method)
- L41 `TestEnsureHermesHome` (class)
- L42 `test_creates_subdirs(self, tmp_path)` (method)
- L50 `test_creates_default_soul_md_if_missing(self, tmp_path)` (method)
- L57 `test_does_not_overwrite_existing_soul_md(self, tmp_path)` (method)
- L65 `TestLoadConfigDefaults` (class)
- L66 `test_returns_defaults_when_no_file(self, tmp_path)` (method)
- L76 `test_legacy_root_level_max_turns_migrates_to_agent_config(self, tmp_path)` (method)
- L86 `TestLoadConfigParseFailure` (class) — A YAML parse failure must NOT silently fall back to defaults.
- L99 `test_logs_and_warns_on_parse_failure(self, tmp_path, caplog, capsys)` (method)
- L128 `test_dedup_on_repeated_load_same_file(self, tmp_path, capsys)` (method)
- L143 `test_rewarns_after_file_edit(self, tmp_path, capsys)` (method)
- L160 `test_corrupt_config_is_backed_up(self, tmp_path, capsys)` (method) — A broken config.yaml is snapshotted to a timestamped .bak so the
- L186 `test_backup_skips_when_same_size_bak_exists(self, tmp_path, capsys)` (method) — Don't churn backups: if a corrupt backup of the same size already
- L205 `test_corrupt_symlink_config_not_backed_up(self, tmp_path)` (method) — Symlinked config.yaml is not copied (mirrors Gemini #21541 lstat
- L225 `TestSaveAndLoadRoundtrip` (class)
- L226 `test_roundtrip(self, tmp_path)` (method)
- L241 `test_save_config_normalizes_legacy_root_level_max_turns(self, tmp_path)` (method)
- L249 `test_nested_values_preserved(self, tmp_path)` (method)
- L259 `TestSaveEnvValueSecure` (class)
- L260 `test_save_env_value_writes_without_stdout(self, tmp_path, capsys)` (method)
- L270 `test_secure_save_returns_metadata_only(self, tmp_path)` (method)
- L280 `test_save_env_value_updates_process_environment(self, tmp_path)` (method)
- L286 `test_save_env_value_hardens_file_permissions_on_posix(self, tmp_path)` (method)
- L296 `TestRemoveEnvValue` (class)
- L297 `test_removes_key_from_env_file(self, tmp_path)` (method)
- L308 `test_clears_os_environ(self, tmp_path)` (method)
- L315 `test_returns_false_when_key_not_found(self, tmp_path)` (method)
- L324 `test_handles_missing_env_file(self, tmp_path)` (method)
- L331 `test_clears_os_environ_even_when_not_in_file(self, tmp_path)` (method)
- L339 `TestSaveConfigAtomicity` (class) — Verify save_config uses atomic writes (tempfile + os.replace).
- L342 `test_no_partial_write_on_crash(self, tmp_path)` (method) — If save_config crashes mid-write, the previous file stays intact.
- L366 `test_no_leftover_temp_files(self, tmp_path)` (method) — Failed writes must clean up their temp files.
- L382 `test_atomic_write_creates_valid_yaml(self, tmp_path)` (method) — The written file must be valid YAML matching the input.
- L398 `TestSanitizeEnvLines` (class) — Tests for .env file corruption repair.
- L401 `test_splits_concatenated_keys(self)` (method) — Two KEY=VALUE pairs jammed on one line get split.
- L410 `test_preserves_clean_file(self)` (method) — A well-formed .env file passes through unchanged (modulo trailing newlines).
- L421 `test_preserves_comments_and_blanks(self)` (method)
- L426 `test_adds_missing_trailing_newline(self)` (method) — Lines missing trailing newline get one added.
- L432 `test_three_concatenated_keys(self)` (method) — Three known keys on one line all get separated.
- L442 `test_value_with_equals_sign_not_split(self)` (method) — A value containing '=' shouldn't be falsely split (lowercase in value).
- L448 `test_unknown_keys_not_split(self)` (method) — Unknown key names on one line are NOT split (avoids false positives).
- L455 `test_value_ending_with_digits_still_splits(self)` (method) — Concatenation is detected even when value ends with digits.
- L463 `test_glm_suffix_collision_not_split(self)` (method) — GLM_API_KEY / GLM_BASE_URL must not be mangled by LM_API_KEY / LM_BASE_URL suffixes (#17138).
- L472 `test_suffix_collision_does_not_break_real_concatenation(self)` (method) — A genuine concatenation that happens to start with a suffix-superset key still splits.
- L480 `test_save_env_value_fixes_corruption_on_write(self, tmp_path)` (method) — save_env_value sanitizes corrupted lines when writing a new key.
- L498 `test_sanitize_env_file_returns_fix_count(self, tmp_path)` (method) — sanitize_env_file reports how many entries were fixed.
- L514 `test_sanitize_env_file_noop_on_clean_file(self, tmp_path)` (method) — No changes when file is already clean.
- L523 `TestOptionalEnvVarsRegistry` (class) — Verify that key env vars are registered in OPTIONAL_ENV_VARS.
- L526 `test_tavily_api_key_registered(self)` (method) — TAVILY_API_KEY is listed in OPTIONAL_ENV_VARS.
- L531 `test_tavily_api_key_is_tool_category(self)` (method) — TAVILY_API_KEY is in the 'tool' category.
- L536 `test_tavily_api_key_is_password(self)` (method) — TAVILY_API_KEY is marked as password.
- L541 `test_tavily_api_key_has_url(self)` (method) — TAVILY_API_KEY has a URL.
- L546 `test_tavily_in_env_vars_by_version(self)` (method) — TAVILY_API_KEY is listed in ENV_VARS_BY_VERSION.
- L554 `test_max_iterations_not_offered_as_env_var(self)` (method) — HERMES_MAX_ITERATIONS must NOT be in OPTIONAL_ENV_VARS (issue #17534).
- L567 `TestConfigMigrationSecretPrompts` (class)
- L568 `test_required_secret_env_prompt_uses_masked_prompt(self, tmp_path, monkeypatch)` (method)
- L610 `TestConfigVersionDetection` (class)
- L611 `test_check_config_version_uses_raw_on_disk_version(self, tmp_path)` (method)
- L619 `test_check_config_version_treats_missing_file_as_current(self, tmp_path)` (method)
- L624 `test_check_config_version_does_not_migrate_invalid_yaml(self, tmp_path)` (method)
- L632 `TestAnthropicTokenMigration` (class) — Test that config version 8→9 clears ANTHROPIC_TOKEN.
- L635 `_write_config_version(self, tmp_path, version)` (method)
- L640 `test_clears_token_on_upgrade_to_v9(self, tmp_path)` (method) — ANTHROPIC_TOKEN is cleared unconditionally when upgrading to v9.
- L651 `test_skips_on_version_9_or_later(self, tmp_path)` (method) — Already at v9 — ANTHROPIC_TOKEN is not touched.
- L663 `TestCustomProviderCompatibility` (class) — Custom provider compatibility across legacy and v12+ config schemas.
- L666 `test_v11_upgrade_moves_custom_providers_into_providers(self, tmp_path)` (method)
- L709 `test_v11_upgrade_preserves_custom_provider_model_metadata(self, tmp_path)` (method)
- L774 `test_providers_dict_resolves_at_runtime(self, tmp_path)` (method) — After migration deleted custom_providers, get_compatible_custom_providers
- L805 `test_compatible_custom_providers_prefers_base_url_then_url_then_api(self, tmp_path)` (method) — URL field precedence is base_url > url > api (PR #9332).
- L836 `test_dedup_across_legacy_and_providers(self, tmp_path)` (method) — Same name+url in both schemas should not produce duplicates.
- L869 `test_dedup_preserves_entries_with_different_models(self, tmp_path)` (method) — Entries with same name+URL but different models must not be collapsed.
- L894 `TestInterimAssistantMessageConfig` (class) — Test the explicit gateway interim-message config gate.
- L897 `test_default_config_enables_interim_assistant_messages(self)` (method)
- L900 `test_migrate_to_v15_adds_interim_assistant_message_gate(self, tmp_path)` (method)
- L917 `TestDiscordChannelPromptsConfig` (class)
- L918 `test_default_config_includes_discord_channel_prompts(self)` (method)
- L921 `test_migrate_adds_discord_channel_prompts_default(self, tmp_path)` (method)
- L938 `TestUserMessagePreviewConfig` (class)
- L939 `test_default_config_preview_line_counts(self)` (method)
- L945 `TestEnvWriteDenylist` (class) — ``save_env_value`` refuses to persist env-var names that
- L963 `_hermes_home(self, tmp_path, monkeypatch)` (method)
- L994 `test_denylisted_keys_rejected(self, denied_key)` (method) — Each denylisted name raises ``ValueError`` and never reaches
- L1014 `test_hermes_integration_keys_still_writable(self, allowed_key)` (method) — ``HERMES_*`` overall is NOT blocked — only the four runtime
- L1024 `test_legitimate_provider_key_still_works(self)` (method) — The denylist must not regress on real provider key writes.
- L1030 `test_arbitrary_user_key_still_works(self)` (method) — Plugin / user-defined env vars (anything outside the
- L1038 `test_save_env_value_secure_inherits_denylist(self)` (method) — The ``_secure`` variant goes through ``save_env_value`` so
- L1044 `test_pre_existing_value_in_env_file_is_left_alone(self, tmp_path)` (method) — The gate is on *write*. If ``.env`` already contains
