---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/hermes_cli/test_setup_openclaw_migration.py

Symbols in `tests/hermes_cli/test_setup_openclaw_migration.py`.

- L15 `TestOfferOpenclawMigration` (class) — Test the _offer_openclaw_migration helper in isolation.
- L18 `test_skips_when_no_openclaw_dir(self, tmp_path)` (method) — Should return False immediately when ~/.openclaw does not exist.
- L23 `test_skips_when_migration_script_missing(self, tmp_path)` (method) — Should return False when the migration script file is absent.
- L33 `test_skips_when_user_declines(self, tmp_path)` (method) — Should return False when user declines the migration prompt.
- L46 `test_runs_migration_when_user_accepts(self, tmp_path)` (method) — Should run dry-run preview first, then execute after confirmation.
- L116 `test_user_declines_after_preview(self, tmp_path)` (method) — Should return False when user sees preview but declines to proceed.
- L166 `test_handles_migration_error_gracefully(self, tmp_path)` (method) — Should catch exceptions and return False.
- L192 `test_creates_config_if_missing(self, tmp_path)` (method) — Should bootstrap config.yaml before running migration.
- L227 `_first_time_args()` (function)
- L235 `TestSetupWizardOpenclawIntegration` (class) — Verify _offer_openclaw_migration is called during first-time setup.
- L238 `test_migration_offered_during_first_time_setup(self, tmp_path)` (method) — On first-time setup, _offer_openclaw_migration should be called.
- L270 `test_migration_reloads_config_on_success(self, tmp_path)` (method) — When migration returns True, config should be reloaded.
- L302 `test_reloaded_config_flows_into_remaining_setup_sections(self, tmp_path)` (method)
- L333 `test_migration_not_offered_for_existing_install(self, tmp_path)` (method) — Returning users should not see the migration prompt.
- L363 `TestGetSectionConfigSummary` (class) — Test the _get_section_config_summary helper.
- L366 `test_model_returns_none_without_api_key(self)` (method)
- L371 `test_model_returns_summary_with_api_key(self)` (method)
- L381 `test_model_returns_dict_default_key(self)` (method)
- L392 `test_terminal_always_returns(self)` (method)
- L399 `test_agent_always_returns(self)` (method)
- L406 `test_gateway_returns_none_without_tokens(self)` (method)
- L418 `test_gateway_lists_platforms(self)` (method)
- L436 `test_tools_returns_none_without_keys(self)` (method)
- L441 `test_tools_lists_configured(self)` (method)
- L455 `test_model_recognises_zai_glm_api_key(self)` (method) — GLM_API_KEY (zai provider) should count as configured.
- L466 `test_model_recognises_minimax_api_key(self)` (method) — MINIMAX_API_KEY should count as configured.
- L478 `test_gateway_recognises_whatsapp_enabled(self)` (method) — WhatsApp uses WHATSAPP_ENABLED (not WHATSAPP_PHONE_NUMBER_ID).
- L490 `test_gateway_recognises_signal_http_url(self)` (method) — Signal uses SIGNAL_HTTP_URL (not SIGNAL_ACCOUNT).
- L502 `test_model_ignores_bare_gh_token(self)` (method) — GH_TOKEN is commonly set for `gh` / git and must NOT count as a
- L513 `test_model_ignores_bare_github_token(self)` (method) — GITHUB_TOKEN is commonly set in CI and must not trigger skip.
- L522 `test_model_ignores_claude_code_oauth_token(self)` (method) — CLAUDE_CODE_OAUTH_TOKEN is set by Claude Code itself and must not
- L533 `test_model_copilot_recognised_when_explicitly_chosen(self)` (method) — If the user picked copilot in config, GH_TOKEN *does* count —
- L544 `test_gateway_matches_platform_registry(self)` (method) — Every built-in platform should be recognised by its primary
- L575 `TestSkipConfiguredSection` (class) — Test the _skip_configured_section helper.
- L578 `test_returns_false_when_not_configured(self)` (method)
- L583 `test_returns_true_when_user_skips(self)` (method)
- L596 `test_returns_false_when_user_wants_reconfig(self)` (method)
- L610 `TestSetupWizardSkipsConfiguredSections` (class) — After migration, already-configured sections should offer skip.
- L613 `test_sections_skipped_when_migration_imported_settings(self, tmp_path)` (method) — When migration ran and API key exists, model section should be skippable.
