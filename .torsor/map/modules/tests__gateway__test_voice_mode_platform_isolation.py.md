---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_voice_mode_platform_isolation.py

Symbols in `tests/gateway/test_voice_mode_platform_isolation.py`.

- L19 `TestVoiceKeyHelper` (class) — Test the _voice_key helper method.
- L22 `test_voice_key_format(self)` (method) — _voice_key returns 'platform:chat_id' format.
- L29 `test_voice_key_different_platforms_same_chat_id(self)` (method) — Same chat_id on different platforms yields different keys.
- L42 `TestVoiceModePlatformIsolation` (class) — Test that voice mode state is isolated by platform.
- L45 `test_telegram_and_slack_voice_mode_independent(self)` (method) — Setting voice mode for Telegram chat '123' does not affect Slack chat '123'.
- L64 `TestLegacyKeyMigration` (class) — Test migration of legacy unprefixed keys in _load_voice_modes.
- L67 `test_load_voice_modes_skips_legacy_keys(self)` (method) — _load_voice_modes skips keys without ':' prefix and logs a warning.
- L97 `test_load_voice_modes_preserves_prefixed_keys(self)` (method) — _load_voice_modes correctly loads platform-prefixed keys.
- L118 `test_load_voice_modes_invalid_modes_filtered(self)` (method) — _load_voice_modes filters out invalid mode values.
- L140 `TestSyncVoiceModeStateToAdapter` (class) — Test _sync_voice_mode_state_to_adapter filters by platform.
- L143 `test_sync_only_includes_platform_chats(self)` (method) — Only chats matching the adapter's platform are synced.
- L165 `test_sync_clears_existing_state(self)` (method) — _sync_voice_mode_state_to_adapter clears existing disabled_chats first.
- L182 `test_sync_returns_early_without_platform(self)` (method) — _sync_voice_mode_state_to_adapter returns early if adapter has no platform.
- L196 `test_sync_returns_early_without_auto_tts_disabled_chats(self)` (method) — _sync_voice_mode_state_to_adapter returns early if adapter lacks _auto_tts_disabled_chats.
- L211 `_make_runner()` (function) — Create a minimal GatewayRunner for testing.
