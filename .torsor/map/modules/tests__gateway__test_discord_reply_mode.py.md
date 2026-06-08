---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_discord_reply_mode.py

Symbols in `tests/gateway/test_discord_reply_mode.py`.

- L21 `_ensure_discord_mock()` (function) — Install a mock discord module when discord.py isn't available.
- L60 `adapter_factory()` (function) — Factory to create DiscordAdapter with custom reply_to_mode.
- L68 `TestReplyToModeConfig` (class) — Tests for reply_to_mode configuration loading.
- L71 `test_default_mode_is_first(self, adapter_factory)` (method)
- L75 `test_off_mode(self, adapter_factory)` (method)
- L79 `test_first_mode(self, adapter_factory)` (method)
- L83 `test_all_mode(self, adapter_factory)` (method)
- L87 `test_invalid_mode_stored_as_is(self, adapter_factory)` (method) — Invalid modes are stored but send() handles them gracefully.
- L92 `test_none_mode_defaults_to_first(self)` (method)
- L97 `test_empty_string_mode_defaults_to_first(self)` (method)
- L103 `_make_discord_adapter(reply_to_mode: str='first')` (function) — Create a DiscordAdapter with mocked client and channel for send() tests.
- L131 `TestSendWithReplyToMode` (class) — Tests for send() method respecting reply_to_mode.
- L135 `test_off_mode_no_reply_reference(self)` (method)
- L148 `test_first_mode_only_first_chunk_references(self)` (method)
- L163 `test_all_mode_all_chunks_reference(self)` (method)
- L176 `test_no_reply_to_param_no_reference(self)` (method)
- L187 `test_single_chunk_respects_first_mode(self)` (method)
- L198 `test_single_chunk_off_mode(self)` (method)
- L210 `test_invalid_mode_falls_back_to_first_behavior(self)` (method) — Invalid mode behaves like 'first' — only first chunk gets reference.
- L223 `TestConfigSerialization` (class) — Tests for reply_to_mode serialization (shared with Telegram).
- L226 `test_to_dict_includes_reply_to_mode(self)` (method)
- L231 `test_from_dict_loads_reply_to_mode(self)` (method)
- L236 `test_from_dict_defaults_to_first(self)` (method)
- L242 `TestEnvVarOverride` (class) — Tests for DISCORD_REPLY_TO_MODE environment variable override.
- L245 `_make_config(self)` (method)
- L250 `test_env_var_sets_off_mode(self)` (method)
- L256 `test_env_var_sets_all_mode(self)` (method)
- L262 `test_env_var_case_insensitive(self)` (method)
- L268 `test_env_var_invalid_value_ignored(self)` (method)
- L274 `test_env_var_empty_value_ignored(self)` (method)
- L280 `test_env_var_creates_platform_config_if_missing(self)` (method) — DISCORD_REPLY_TO_MODE creates PlatformConfig even without DISCORD_BOT_TOKEN.
- L304 `FakeDMChannel` (class) — Minimal DM channel stub (skips mention / channel-allow checks).
- L306 `__init__(self, channel_id: int=100, name: str='dm')` (method)
- L312 `_make_message(*, content: str='hi', reference=None)` (function) — Build a mock Discord message for _handle_message tests.
- L328 `reply_text_adapter(monkeypatch)` (function) — DiscordAdapter wired for _handle_message → handle_message capture.
- L338 `TestReplyToText` (class) — Tests for reply_to_text populated by _handle_message.
- L342 `test_no_reference_both_none(self, reply_text_adapter)` (method)
- L352 `test_reference_without_resolved(self, reply_text_adapter)` (method)
- L363 `test_reference_with_resolved_content(self, reply_text_adapter)` (method)
- L375 `test_reference_with_empty_resolved_content(self, reply_text_adapter)` (method) — Empty string content should become None, not leak as empty string.
- L388 `test_reference_with_deleted_message(self, reply_text_adapter)` (method) — Deleted messages lack .content — getattr guard should return None.
- L401 `TestYamlConfigLoading` (class) — Tests for reply_to_mode loaded from config.yaml discord section.
- L404 `_write_config(self, tmp_path, content: str)` (method)
- L410 `test_top_level_reply_to_mode_off(self, tmp_path, monkeypatch)` (method) — YAML 1.1 parses bare 'off' as boolean False — must map back to 'off'.
- L420 `test_top_level_reply_to_mode_all(self, tmp_path, monkeypatch)` (method)
- L429 `test_extra_reply_to_mode_off(self, tmp_path, monkeypatch)` (method) — discord.extra.reply_to_mode is also honoured.
- L441 `test_env_var_takes_precedence_over_yaml(self, tmp_path, monkeypatch)` (method) — Existing DISCORD_REPLY_TO_MODE env var is not overwritten by YAML.
- L451 `test_top_level_takes_precedence_over_extra(self, tmp_path, monkeypatch)` (method) — discord.reply_to_mode wins over discord.extra.reply_to_mode.
