---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_display_config.py

Symbols in `tests/gateway/test_display_config.py`.

- L8 `TestResolveDisplaySetting` (class) — resolve_display_setting() resolves with correct priority.
- L11 `test_explicit_platform_override_wins(self)` (method) — display.platforms.<plat>.<key> takes top priority.
- L25 `test_global_setting_when_no_platform_override(self)` (method) — Falls back to display.<key> when no platform override exists.
- L37 `test_platform_default_when_no_user_config(self)` (method) — Falls back to built-in platform default.
- L49 `test_global_default_for_unknown_platform(self)` (method) — Unknown platforms get the global defaults.
- L57 `test_fallback_parameter_used_last(self)` (method) — Explicit fallback is used when nothing else matches.
- L66 `test_platform_override_only_affects_that_platform(self)` (method) — Other platforms are unaffected by a specific platform override.
- L86 `TestBackwardCompat` (class) — Legacy tool_progress_overrides is still respected as a fallback.
- L89 `test_legacy_overrides_read(self)` (method) — tool_progress_overrides is read when no platforms entry exists.
- L105 `test_new_platforms_takes_precedence_over_legacy(self)` (method) — display.platforms beats tool_progress_overrides.
- L118 `test_legacy_overrides_only_for_tool_progress(self)` (method) — Legacy overrides don't affect other settings.
- L135 `TestYAMLNormalisation` (class) — YAML 1.1 quirks (bare off → False, on → True) are handled.
- L138 `test_tool_progress_false_normalised_to_off(self)` (method) — YAML's bare `off` parses as False — normalised to 'off' string.
- L145 `test_tool_progress_true_normalised_to_all(self)` (method) — YAML's bare `on` parses as True — normalised to 'all'.
- L152 `test_show_reasoning_string_true(self)` (method) — String 'true' is normalised to bool True.
- L159 `test_tool_preview_length_string(self)` (method) — String numbers are normalised to int.
- L166 `test_platform_override_false_tool_progress(self)` (method) — Per-platform bare off → normalised.
- L178 `TestPlatformDefaults` (class) — Built-in defaults reflect platform capability tiers.
- L181 `test_high_tier_platforms(self)` (method) — Discord defaults to 'all'; Telegram defaults quiet for mobile.
- L190 `test_medium_tier_platforms(self)` (method) — Mattermost, Matrix, Feishu, WhatsApp default to 'new' tool progress.
- L197 `test_slack_defaults_tool_progress_off(self)` (method) — Slack defaults to quiet tool progress (permanent chat noise otherwise).
- L203 `test_low_tier_platforms(self)` (method) — Signal, BlueBubbles, etc. default to 'off' tool progress.
- L210 `test_minimal_tier_platforms(self)` (method) — Email, SMS, webhook default to 'off' tool progress.
- L217 `test_low_tier_streaming_defaults_to_false(self)` (method) — Low-tier platforms default streaming to False.
- L224 `test_high_tier_streaming_defaults_to_none(self)` (method) — High-tier platforms default streaming to None (follow global).
- L230 `test_telegram_mobile_chatter_defaults(self)` (method) — Telegram keeps real mid-turn signal (interim commentary + heartbeats)
- L250 `test_telegram_mobile_chatter_can_opt_in(self)` (method) — Per-platform config can re-enable Telegram busy-ack detail
- L275 `TestConfigMigration` (class) — Version 16 migration moves tool_progress_overrides into display.platforms.
- L278 `test_migration_creates_platforms_entries(self, tmp_path, monkeypatch)` (method) — Old overrides are migrated into display.platforms.<plat>.tool_progress.
- L307 `test_migration_preserves_existing_platforms_entries(self, tmp_path, monkeypatch)` (method) — Existing display.platforms entries are NOT overwritten by migration.
- L336 `TestStreamingPerPlatform` (class) — Streaming per-platform override semantics.
- L339 `test_none_means_follow_global(self)` (method) — When streaming is None, the caller should use global config.
- L348 `test_global_display_streaming_is_cli_only(self)` (method) — display.streaming must not act as a gateway streaming override.
- L357 `test_explicit_false_disables(self)` (method) — Explicit False disables streaming for that platform.
- L368 `test_explicit_true_enables(self)` (method) — Explicit True enables streaming for that platform.
- L384 `TestCleanupProgress` (class) — ``cleanup_progress`` is off by default and resolvable per-platform.
- L387 `test_default_off_for_all_platforms(self)` (method) — No config set → cleanup_progress resolves to False everywhere.
- L394 `test_global_true_applies_to_all_platforms(self)` (method) — display.cleanup_progress=true opts in globally.
- L402 `test_per_platform_override_wins(self)` (method) — display.platforms.<plat>.cleanup_progress beats the global value.
- L417 `test_yaml_off_string_normalises_to_false(self)` (method) — YAML 1.1 bare ``off`` becomes string 'off' — treat as False.
- L428 `test_yaml_true_string_normalises_to_true(self)` (method) — String 'true'/'yes'/'on' all resolve to True.
