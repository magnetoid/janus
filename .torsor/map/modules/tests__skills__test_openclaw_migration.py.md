---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/skills/test_openclaw_migration.py

Symbols in `tests/skills/test_openclaw_migration.py`.

- L19 `load_module()` (function)
- L28 `load_skills_guard()` (function)
- L40 `test_extract_markdown_entries_promotes_heading_context()` (function)
- L59 `test_merge_entries_respects_limit_and_reports_overflow()` (function)
- L70 `test_resolve_selected_options_supports_include_and_exclude()` (function)
- L76 `test_resolve_selected_options_supports_presets()` (function)
- L85 `test_resolve_selected_options_rejects_unknown_values()` (function)
- L95 `test_resolve_selected_options_rejects_unknown_preset()` (function)
- L105 `test_migrator_copies_skill_and_merges_allowlist(tmp_path: Path)` (function)
- L150 `test_migrator_optionally_imports_supported_secrets_and_messaging_settings(tmp_path: Path)` (function)
- L188 `test_messaging_cwd_skipped_when_inside_source(tmp_path: Path)` (function) — MESSAGING_CWD pointing inside the OpenClaw source dir should be skipped.
- L220 `test_migrator_can_execute_only_selected_categories(tmp_path: Path)` (function)
- L257 `test_migrator_records_preset_in_report(tmp_path: Path)` (function)
- L283 `test_source_candidate_finds_files_in_custom_workspace(tmp_path: Path)` (function) — When agents.defaults.workspace points outside ~/.openclaw, files should
- L341 `test_source_candidate_prefers_standard_workspace_over_custom(tmp_path: Path)` (function) — When files exist in both ~/.openclaw/workspace/ and the custom workspace,
- L379 `test_migrator_exports_full_overflow_entries(tmp_path: Path)` (function)
- L410 `test_migrator_can_rename_conflicting_imported_skill(tmp_path: Path)` (function)
- L449 `test_migrator_can_overwrite_conflicting_imported_skill_with_backup(tmp_path: Path)` (function)
- L486 `test_discord_settings_migrated(tmp_path: Path)` (function) — Discord bot token and allowlist migrate to .env.
- L517 `test_slack_settings_migrated(tmp_path: Path)` (function) — Slack bot/app tokens and allowlist migrate to .env.
- L550 `test_signal_settings_migrated(tmp_path: Path)` (function) — Signal account, HTTP URL, and allowlist migrate to .env.
- L583 `test_model_config_migrated(tmp_path: Path)` (function) — Default model setting migrates to config.yaml.
- L610 `test_model_config_object_format(tmp_path: Path)` (function) — Model config handles {primary: ...} object format.
- L636 `test_tts_config_migrated(tmp_path: Path)` (function) — TTS provider and voice settings migrate to config.yaml.
- L671 `test_shared_skills_migrated(tmp_path: Path)` (function) — Shared skills from ~/.openclaw/skills/ are migrated.
- L695 `test_daily_memory_merged(tmp_path: Path)` (function) — Daily memory notes from workspace/memory/*.md are merged into MEMORY.md.
- L726 `test_provider_keys_require_migrate_secrets_flag(tmp_path: Path)` (function) — Provider keys migration is double-gated: needs option + --migrate-secrets.
- L770 `test_workspace_agents_records_skip_when_missing(tmp_path: Path)` (function) — Bug fix: workspace-agents records 'skipped' when source is missing.
- L789 `test_cron_store_is_archived_without_config_cron_section(tmp_path: Path)` (function) — Bug fix: archive cron store even when openclaw.json has no top-level cron config.
- L830 `test_skill_installs_cleanly_under_skills_guard()` (function)
- L858 `test_rebrand_text_replaces_openclaw_variants()` (function)
- L871 `test_rebrand_text_replaces_legacy_bot_names()` (function)
- L880 `test_rebrand_text_preserves_unrelated_content()` (function)
- L886 `test_rebrand_text_handles_multiple_replacements()` (function)
- L892 `test_rebrand_text_preserves_filesystem_path_casing()` (function) — Lowercase matches — especially ``.openclaw`` filesystem paths — must
- L912 `test_migrate_memory_rebrands_entries(tmp_path)` (function)
- L946 `test_migrate_soul_rebrands_content(tmp_path)` (function)
- L977 `_run_model_migration(tmp_path: Path, openclaw_json: dict)` (function) — Helper: run just migrate_model_config on an openclaw.json and return
- L1006 `_extract_model(parsed: dict)` (function)
- L1013 `test_migrate_model_config_resolves_alias_against_real_openclaw_schema(tmp_path: Path)` (function) — Regression for #16745 — OpenClaw's catalog is keyed by the full
- L1034 `test_migrate_model_config_resolves_alias_with_bare_string_model(tmp_path: Path)` (function)
- L1049 `test_migrate_model_config_passes_through_existing_api_id(tmp_path: Path)` (function) — If the model value is already a provider/model API ID that appears as
- L1068 `test_migrate_model_config_passes_through_unknown_alias(tmp_path: Path)` (function) — If the model value matches no catalog entry, leave it alone and let
- L1087 `test_migrate_model_config_handles_string_valued_catalog_entries(tmp_path: Path)` (function) — Belt-and-suspenders: some catalogs store the alias as a plain string
- L1104 `test_migrate_model_config_no_catalog_leaves_value_alone(tmp_path: Path)` (function)
