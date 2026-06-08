---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_whatsapp_group_gating.py

Symbols in `tests/gateway/test_whatsapp_group_gating.py`.

- L7 `_make_adapter(require_mention=None, mention_patterns=None, free_response_chats=None, dm_policy=None, allow_from=None, group_policy=None, group_allow_from=None)` (function)
- L40 `_group_message(body='hello', **overrides)` (function)
- L53 `_dm_message(body='hello', **overrides)` (function)
- L68 `test_group_messages_can_be_opened_via_config()` (function)
- L74 `test_group_messages_can_require_direct_trigger_via_config()` (function)
- L93 `test_regex_mention_patterns_allow_custom_wake_words()` (function)
- L101 `test_invalid_regex_patterns_are_ignored()` (function)
- L108 `test_config_bridges_whatsapp_group_settings(monkeypatch, tmp_path)` (function)
- L132 `test_free_response_chats_bypass_mention_gating()` (function)
- L141 `test_free_response_chats_does_not_bypass_other_groups()` (function)
- L150 `test_dm_passes_with_default_open_policy()` (function)
- L157 `test_mention_stripping_removes_bot_phone_from_body()` (function)
- L166 `test_mention_stripping_preserves_body_when_no_mention()` (function)
- L176 `test_dm_policy_disabled_blocks_all_dms()` (function)
- L182 `test_dm_policy_disabled_still_allows_groups()` (function)
- L188 `test_dm_policy_allowlist_blocks_unlisted_sender()` (function)
- L194 `test_dm_policy_allowlist_allows_listed_sender()` (function)
- L200 `test_dm_policy_open_allows_all_dms()` (function)
- L208 `test_group_policy_disabled_blocks_all_groups()` (function)
- L214 `test_group_policy_disabled_still_allows_dms()` (function)
- L220 `test_group_policy_allowlist_blocks_unlisted_group()` (function)
- L226 `test_group_policy_allowlist_allows_listed_group()` (function)
- L239 `test_group_policy_open_allows_all_groups()` (function)
- L249 `test_config_bridges_whatsapp_dm_and_group_policy(monkeypatch, tmp_path)` (function)
- L277 `test_config_bridges_whatsapp_allow_from(monkeypatch, tmp_path)` (function)
- L304 `test_status_broadcast_chats_are_always_dropped()` (function) — Felipe's gateway.log showed the agent replying to status@broadcast
- L331 `test_broadcast_filter_runs_before_allowlist()` (function) — A status@broadcast message from an allowlisted sender still drops —
- L348 `test_real_dm_still_processed_after_broadcast_filter()` (function) — Sanity check: the broadcast filter doesn't accidentally drop real DMs.
- L360 `test_is_broadcast_chat_helper_recognizes_common_jids()` (function)
