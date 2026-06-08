---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_slack_mention.py

Symbols in `tests/gateway/test_slack_mention.py`.

- L17 `_ensure_slack_mock()` (function)
- L58 `_make_adapter(require_mention=None, strict_mention=None, free_response_channels=None, allowed_channels=None)` (function)
- L81 `test_require_mention_defaults_to_true(monkeypatch)` (function)
- L87 `test_require_mention_false()` (function)
- L92 `test_require_mention_true()` (function)
- L97 `test_require_mention_string_true()` (function)
- L102 `test_require_mention_string_false()` (function)
- L107 `test_require_mention_string_no()` (function)
- L112 `test_require_mention_string_yes()` (function)
- L117 `test_require_mention_empty_string_stays_true()` (function) — Empty/malformed strings keep gating ON (explicit-false parser).
- L123 `test_require_mention_malformed_string_stays_true()` (function) — Unrecognised values keep gating ON (fail-closed).
- L129 `test_require_mention_env_var_fallback(monkeypatch)` (function)
- L135 `test_require_mention_env_var_default_true(monkeypatch)` (function)
- L145 `test_strict_mention_defaults_to_false(monkeypatch)` (function)
- L151 `test_strict_mention_true()` (function)
- L156 `test_strict_mention_false()` (function)
- L161 `test_strict_mention_string_true()` (function)
- L166 `test_strict_mention_string_off()` (function)
- L171 `test_strict_mention_malformed_stays_false()` (function) — Unrecognised values keep strict mode OFF (fail-open to legacy behavior).
- L177 `test_strict_mention_env_var_fallback(monkeypatch)` (function)
- L187 `test_free_response_channels_default_empty(monkeypatch)` (function)
- L193 `test_free_response_channels_list()` (function)
- L200 `test_free_response_channels_csv_string()` (function)
- L207 `test_free_response_channels_empty_string()` (function)
- L212 `test_free_response_channels_env_var_fallback(monkeypatch)` (function)
- L220 `test_free_response_channels_bare_int()` (function)
- L230 `test_free_response_channels_int_list()` (function)
- L241 `_would_process(adapter, *, is_dm=False, channel_id=CHANNEL_ID, text='hello', mentioned=False, thread_reply=False, active_session=False)` (function) — Simulate the mention gating logic from _handle_slack_message.
- L272 `test_default_require_mention_channel_without_mention_ignored()` (function)
- L277 `test_require_mention_false_channel_without_mention_processed()` (function)
- L282 `test_channel_in_free_response_processed_without_mention()` (function)
- L290 `test_other_channel_not_in_free_response_still_gated()` (function)
- L298 `test_dm_always_processed_regardless_of_setting()` (function)
- L303 `test_mentioned_message_always_processed()` (function)
- L308 `test_thread_reply_with_active_session_processed()` (function)
- L316 `test_thread_reply_without_active_session_ignored()` (function)
- L324 `test_bot_uid_none_processes_channel_message()` (function) — When bot_uid is None (before auth_test), channel messages pass through.
- L353 `test_config_bridges_slack_free_response_channels(monkeypatch, tmp_path)` (function)
- L383 `test_top_level_slack_settings_do_not_disable_env_token_setup(monkeypatch, tmp_path)` (function)
- L407 `test_explicit_top_level_slack_enabled_false_wins_over_env_token(monkeypatch, tmp_path)` (function)
- L432 `test_explicit_platforms_slack_enabled_false_wins_over_env_token(monkeypatch, tmp_path)` (function)
- L458 `test_config_bridges_slack_reply_in_thread(monkeypatch, tmp_path)` (function)
- L498 `test_config_bridges_slack_strict_mention(monkeypatch, tmp_path)` (function)
- L526 `test_mention_in_strict_mode_does_not_register_thread()` (function)
- L546 `test_mention_outside_strict_mode_still_registers_thread()` (function)
- L568 `test_allowed_channels_default_empty(monkeypatch)` (function)
- L574 `test_allowed_channels_list()` (function)
- L581 `test_allowed_channels_csv_string()` (function)
- L588 `test_allowed_channels_empty_string()` (function)
- L593 `test_allowed_channels_env_var_fallback(monkeypatch)` (function)
- L605 `test_allowed_channels_blocks_non_whitelisted_channel()` (function) — Messages in channels not in allowed_channels are silently ignored.
- L611 `test_allowed_channels_permits_whitelisted_channel()` (function) — Messages in the allowed channel are processed normally.
- L617 `test_allowed_channels_empty_no_restriction()` (function) — Empty allowed_channels imposes no restriction (fully backward compatible).
- L623 `test_allowed_channels_blocks_even_when_mentioned()` (function) — Whitelist takes precedence — @mention in a non-allowed channel is ignored.
- L629 `test_allowed_channels_dm_unaffected()` (function) — DMs bypass the allowed_channels check entirely.
- L636 `test_allowed_channels_env_var_blocks_channel(monkeypatch)` (function) — SLACK_ALLOWED_CHANNELS env var (no config) also gates messages.
- L648 `test_config_bridges_slack_allowed_channels(monkeypatch, tmp_path)` (function)
- L670 `test_config_bridges_slack_allowed_channels_env_takes_precedence(monkeypatch, tmp_path)` (function) — Env var set before load_gateway_config() should not be overwritten.
