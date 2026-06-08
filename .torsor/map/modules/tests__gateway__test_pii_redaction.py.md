---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_pii_redaction.py

Symbols in `tests/gateway/test_pii_redaction.py`.

- L18 `TestHashHelpers` (class)
- L19 `test_hash_id_deterministic(self)` (method)
- L22 `test_hash_id_12_hex_chars(self)` (method)
- L27 `test_hash_sender_id_prefix(self)` (method)
- L31 `test_hash_chat_id_preserves_prefix(self)` (method)
- L36 `test_hash_chat_id_no_prefix(self)` (method)
- L46 `_make_context(user_id='user-123', user_name=None, chat_id='telegram:99999', platform=Platform.TELEGRAM, home_channels=None)` (function)
- L67 `TestBuildSessionContextPromptRedaction` (class)
- L68 `test_no_redaction_by_default(self)` (method)
- L73 `test_user_id_hashed_when_redact_pii(self)` (method)
- L79 `test_user_name_not_redacted(self)` (method)
- L86 `test_home_channel_id_hashed(self)` (method)
- L100 `test_home_channel_id_preserved_without_redaction(self)` (method)
- L112 `test_redaction_is_deterministic(self)` (method)
- L118 `test_different_ids_produce_different_hashes(self)` (method)
- L125 `test_discord_ids_not_redacted_even_with_flag(self)` (method) — Discord needs real IDs for <@user_id> mentions.
- L131 `test_whatsapp_ids_redacted(self)` (method)
- L137 `test_signal_ids_redacted(self)` (method)
- L143 `test_slack_ids_not_redacted(self)` (method) — Slack may need IDs for mentions too.
