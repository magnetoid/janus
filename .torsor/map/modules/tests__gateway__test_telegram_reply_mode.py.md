---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_telegram_reply_mode.py

Symbols in `tests/gateway/test_telegram_reply_mode.py`.

- L17 `_ensure_telegram_mock()` (function) — Mock the telegram package if it's not installed.
- L38 `adapter_factory()` (function) — Factory to create TelegramAdapter with custom reply_to_mode.
- L46 `TestReplyToModeConfig` (class) — Tests for reply_to_mode configuration loading.
- L49 `test_default_mode_is_first(self, adapter_factory)` (method)
- L53 `test_off_mode(self, adapter_factory)` (method)
- L57 `test_first_mode(self, adapter_factory)` (method)
- L61 `test_all_mode(self, adapter_factory)` (method)
- L65 `test_invalid_mode_stored_as_is(self, adapter_factory)` (method) — Invalid modes are stored but _should_thread_reply handles them.
- L70 `test_none_mode_defaults_to_first(self)` (method)
- L75 `test_empty_string_mode_defaults_to_first(self)` (method)
- L81 `TestShouldThreadReply` (class) — Tests for _should_thread_reply method.
- L84 `test_no_reply_to_returns_false(self, adapter_factory)` (method)
- L89 `test_off_mode_never_threads(self, adapter_factory)` (method)
- L95 `test_first_mode_only_first_chunk(self, adapter_factory)` (method)
- L102 `test_all_mode_all_chunks(self, adapter_factory)` (method)
- L109 `test_invalid_mode_falls_back_to_first(self, adapter_factory)` (method) — Invalid mode behaves like 'first' - only first chunk threads.
- L116 `TestSendWithReplyToMode` (class) — Tests for send() method respecting reply_to_mode.
- L120 `test_off_mode_no_reply_threading(self, adapter_factory)` (method)
- L132 `test_first_mode_only_first_chunk_threads(self, adapter_factory)` (method)
- L147 `test_all_mode_all_chunks_thread(self, adapter_factory)` (method)
- L161 `test_no_reply_to_param_no_threading(self, adapter_factory)` (method)
- L174 `test_single_chunk_respects_mode(self, adapter_factory)` (method)
- L187 `TestConfigSerialization` (class) — Tests for reply_to_mode serialization.
- L190 `test_to_dict_includes_reply_to_mode(self)` (method)
- L195 `test_from_dict_loads_reply_to_mode(self)` (method)
- L200 `test_from_dict_defaults_to_first(self)` (method)
- L206 `TestEnvVarOverride` (class) — Tests for TELEGRAM_REPLY_TO_MODE environment variable override.
- L209 `_make_config(self)` (method)
- L214 `test_env_var_sets_off_mode(self)` (method)
- L220 `test_env_var_sets_all_mode(self)` (method)
- L226 `test_env_var_case_insensitive(self)` (method)
- L232 `test_env_var_invalid_value_ignored(self)` (method)
- L238 `test_env_var_empty_value_ignored(self)` (method)
- L245 `TestTelegramYamlConfigLoading` (class) — Tests for reply_to_mode loaded from config.yaml telegram section.
- L248 `_write_config(self, tmp_path, content: str)` (method)
- L254 `test_top_level_reply_to_mode_off(self, tmp_path, monkeypatch)` (method) — YAML 1.1 parses bare 'off' as boolean False — must map back to 'off'.
- L264 `test_top_level_reply_to_mode_all(self, tmp_path, monkeypatch)` (method)
- L273 `test_extra_reply_to_mode_off(self, tmp_path, monkeypatch)` (method) — telegram.extra.reply_to_mode is also honoured.
- L285 `test_env_var_takes_precedence_over_yaml(self, tmp_path, monkeypatch)` (method) — Existing TELEGRAM_REPLY_TO_MODE env var is not overwritten by YAML.
- L295 `test_top_level_takes_precedence_over_extra(self, tmp_path, monkeypatch)` (method) — telegram.reply_to_mode wins over telegram.extra.reply_to_mode.
- L309 `TestDMTopicFallbackReplyToMode` (class) — Tests for reply_to_mode enforcement on DM topic fallback paths.
- L326 `test_reply_to_id_suppressed_when_off(self)` (method) — reply_to_mode='off' suppresses reply anchor for DM topic fallback.
- L333 `test_reply_to_id_returned_when_first(self)` (method) — reply_to_mode='first' still returns reply anchor for DM topic fallback.
- L340 `test_reply_to_id_returned_when_all(self)` (method) — reply_to_mode='all' still returns reply anchor for DM topic fallback.
- L347 `test_reply_to_id_returned_when_no_mode(self)` (method) — Without reply_to_mode, behavior is unchanged (backward compat).
- L354 `test_explicit_reply_to_overrides_mode(self)` (method) — Explicit reply_to param always wins, regardless of mode.
- L363 `test_thread_kwargs_suppressed_reply_anchor_when_off(self)` (method) — reply_to_mode='off' returns thread_id without reply anchor.
- L371 `test_thread_kwargs_returns_full_when_first(self)` (method) — reply_to_mode='first' returns thread_id (reply anchor in send kwargs).
- L379 `test_thread_kwargs_no_mode_backward_compat(self)` (method) — Without reply_to_mode, behavior is unchanged.
- L390 `test_send_dm_topic_off_no_quote(self, adapter_factory)` (method) — send() with DM topic fallback and reply_to_mode='off' skips reply.
- L403 `test_send_dm_topic_first_still_quotes(self, adapter_factory)` (method) — send() with DM topic fallback and reply_to_mode='first' still quotes.
