---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_config.py

Symbols in `tests/gateway/test_config.py`.

- L18 `TestHomeChannelRoundtrip` (class)
- L19 `test_to_dict_from_dict(self)` (method)
- L29 `TestPlatformConfigRoundtrip` (class)
- L30 `test_to_dict_from_dict(self)` (method)
- L49 `test_disabled_no_token(self)` (method)
- L56 `test_from_dict_coerces_quoted_false_enabled(self)` (method)
- L60 `test_gateway_restart_notification_defaults_true(self)` (method)
- L64 `test_gateway_restart_notification_roundtrip_false(self)` (method)
- L69 `test_gateway_restart_notification_coerces_quoted_false(self)` (method)
- L74 `TestGetConnectedPlatforms` (class)
- L75 `test_returns_enabled_with_token(self)` (method)
- L88 `test_empty_platforms(self)` (method)
- L92 `test_dingtalk_recognised_via_extras(self)` (method)
- L103 `test_dingtalk_recognised_via_env_vars(self, monkeypatch)` (method) — DingTalk configured via env vars (no extras) should still be
- L116 `test_dingtalk_missing_creds_not_connected(self, monkeypatch)` (method)
- L126 `test_dingtalk_disabled_not_connected(self)` (method)
- L138 `TestSessionResetPolicy` (class)
- L139 `test_roundtrip(self)` (method)
- L147 `test_defaults(self)` (method)
- L153 `test_from_dict_treats_null_values_as_defaults(self)` (method)
- L161 `test_from_dict_coerces_quoted_false_notify(self)` (method)
- L166 `TestStreamingConfig` (class)
- L167 `test_defaults_to_auto_transport(self)` (method)
- L174 `test_from_dict_coerces_quoted_false_enabled(self)` (method)
- L178 `test_from_dict_malformed_numeric_values_fall_back_to_defaults(self)` (method)
- L191 `TestGatewayConfigRoundtrip` (class)
- L192 `test_full_roundtrip(self)` (method)
- L216 `test_roundtrip_preserves_unauthorized_dm_behavior(self)` (method)
- L232 `test_from_dict_coerces_quoted_false_always_log_local(self)` (method)
- L236 `test_get_notice_delivery_defaults_to_public(self)` (method)
- L243 `test_get_notice_delivery_honors_platform_override(self)` (method)
- L257 `TestLoadGatewayConfig` (class)
- L258 `test_bridges_quick_commands_from_config_yaml(self, tmp_path, monkeypatch)` (method)
- L276 `test_bridges_group_sessions_per_user_from_config_yaml(self, tmp_path, monkeypatch)` (method)
- L288 `test_bridges_thread_sessions_per_user_from_config_yaml(self, tmp_path, monkeypatch)` (method)
- L300 `test_thread_sessions_per_user_defaults_to_false(self, tmp_path, monkeypatch)` (method)
- L312 `test_bridges_discord_thread_require_mention_from_config_yaml(self, tmp_path, monkeypatch)` (method) — discord.thread_require_mention in config.yaml should reach the runtime env var.
- L330 `test_thread_require_mention_yaml_does_not_overwrite_env(self, tmp_path, monkeypatch)` (method) — Explicit env var should win over config.yaml (env > yaml precedence).
- L349 `test_bridges_discord_allow_from_from_config_yaml(self, tmp_path, monkeypatch)` (method) — discord.allow_from should populate DISCORD_ALLOWED_USERS for auth.
- L375 `test_bridges_discord_platform_extra_allow_from_to_env(self, tmp_path, monkeypatch)` (method) — platforms.discord.extra.allow_from should reach DISCORD_ALLOWED_USERS too.
- L399 `test_bridges_quoted_false_platform_enabled_from_config_yaml(self, tmp_path, monkeypatch)` (method)
- L417 `test_bridges_nested_gateway_platforms_from_config_yaml(self, tmp_path, monkeypatch)` (method)
- L450 `test_top_level_platforms_override_nested_gateway_platforms(self, tmp_path, monkeypatch)` (method)
- L480 `test_shared_key_loop_bridges_allow_from_from_nested_platforms(self, tmp_path, monkeypatch)` (method) — Regression: shared-key loop must bridge allow_from / require_mention
- L517 `test_shared_key_loop_bridges_allow_from_from_nested_gateway_platforms(self, tmp_path, monkeypatch)` (method) — Same regression check for ``gateway.platforms:`` path.
- L543 `test_bridges_quoted_false_session_notify_from_config_yaml(self, tmp_path, monkeypatch)` (method)
- L559 `test_bridges_quoted_false_always_log_local_from_config_yaml(self, tmp_path, monkeypatch)` (method)
- L574 `test_bridges_discord_channel_prompts_from_config_yaml(self, tmp_path, monkeypatch)` (method)
- L595 `test_bridges_discord_history_backfill_settings_from_config_yaml(self, tmp_path, monkeypatch)` (method)
- L615 `test_bridges_telegram_channel_prompts_from_config_yaml(self, tmp_path, monkeypatch)` (method)
- L636 `test_bridges_slack_channel_prompts_from_config_yaml(self, tmp_path, monkeypatch)` (method)
- L655 `test_bridges_feishu_allow_bots_from_config_yaml_to_env(self, tmp_path, monkeypatch)` (method)
- L671 `test_feishu_allow_bots_env_takes_precedence_over_config_yaml(self, tmp_path, monkeypatch)` (method)
- L687 `test_invalid_quick_commands_in_config_yaml_are_ignored(self, tmp_path, monkeypatch)` (method)
- L699 `test_bridges_unauthorized_dm_behavior_from_config_yaml(self, tmp_path, monkeypatch)` (method)
- L717 `test_bridges_telegram_disable_link_previews_from_config_yaml(self, tmp_path, monkeypatch)` (method)
- L733 `test_bridges_telegram_extra_base_url_from_config_yaml(self, tmp_path, monkeypatch)` (method)
- L753 `test_bridges_notice_delivery_from_config_yaml(self, tmp_path, monkeypatch)` (method)
- L769 `test_bridges_telegram_proxy_url_from_config_yaml(self, tmp_path, monkeypatch)` (method)
- L787 `test_telegram_proxy_env_takes_precedence_over_config(self, tmp_path, monkeypatch)` (method)
- L806 `TestHomeChannelEnvOverrides` (class) — Home channel env vars should apply even when the platform was already
- L810 `test_existing_platform_configs_accept_home_channel_env_overrides(self)` (method)
