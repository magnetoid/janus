---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/gateway/test_allowed_channels_widening.py

Symbols in `tests/gateway/test_allowed_channels_widening.py`.

- L26 `_make_telegram_adapter(*, allowed_chats=None, require_mention=None, guest_mode=False)` (function)
- L48 `_tg_group_message(chat_id=-100, text='hello')` (function)
- L61 `_tg_dm_message(text='hello')` (function)
- L74 `TestTelegramAllowedChats` (class)
- L75 `test_empty_is_no_restriction(self, monkeypatch)` (method)
- L81 `test_list_form(self)` (method)
- L85 `test_csv_form(self)` (method)
- L89 `test_env_var_fallback(self, monkeypatch)` (method)
- L94 `test_blocks_non_whitelisted_group(self)` (method)
- L98 `test_permits_whitelisted_group(self)` (method)
- L104 `test_mention_cannot_bypass_whitelist(self)` (method) — @mention in a non-allowed chat is still ignored.
- L113 `test_dms_unaffected(self)` (method) — DMs bypass the allowed_chats whitelist entirely.
- L118 `test_config_bridge(self, monkeypatch, tmp_path)` (method) — slack-style config.yaml → env var bridge works.
- L140 `test_config_bridge_env_takes_precedence(self, monkeypatch, tmp_path)` (method)
- L163 `_make_dingtalk_adapter(*, allowed_chats=None, require_mention=None)` (function)
- L180 `TestDingTalkAllowedChats` (class)
- L181 `test_empty_is_no_restriction(self, monkeypatch)` (method)
- L186 `test_list_form(self)` (method)
- L190 `test_csv_form(self)` (method)
- L194 `test_env_var_fallback(self, monkeypatch)` (method)
- L199 `test_blocks_non_whitelisted_group(self)` (method)
- L205 `test_dm_unaffected(self)` (method) — DMs (is_group=False) bypass the whitelist.
- L212 `test_config_bridge(self, monkeypatch, tmp_path)` (method)
- L238 `TestMattermostAllowedChannels` (class) — Mattermost whitelist logic — replicated since the adapter reads config
- L244 `_would_process(channel_id, channel_type='O', allowed_cfg=None, allowed_env='')` (method) — Replicate the whitelist gate from gateway/platforms/mattermost.py.
- L260 `test_empty_config_is_no_restriction(self)` (method)
- L263 `test_config_list_blocks_non_whitelisted_channel(self)` (method)
- L268 `test_config_list_permits_whitelisted_channel(self)` (method)
- L273 `test_env_var_fallback_when_no_config(self)` (method)
- L278 `test_dm_unaffected(self)` (method)
- L283 `test_config_bridge(self, monkeypatch, tmp_path)` (method)
- L313 `TestMatrixAllowedRooms` (class) — Matrix whitelist behavior — tested via the env-var-initialized
- L317 `test_empty_env_empty_set(self, monkeypatch)` (method)
- L324 `test_env_var_parsed_to_set(self, monkeypatch)` (method)
- L331 `test_block_logic(self)` (method) — Replicates the matrix.py gate: if allowed non-empty and room not in it, drop.
- L348 `test_config_bridge(self, monkeypatch, tmp_path)` (method)
