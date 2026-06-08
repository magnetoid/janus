---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_unauthorized_dm_behavior.py

Symbols in `tests/gateway/test_unauthorized_dm_behavior.py`.

- L11 `_clear_auth_env(monkeypatch)` (function)
- L44 `_make_event(platform: Platform, user_id: str, chat_id: str)` (function)
- L58 `_make_runner(platform: Platform, config: GatewayConfig)` (function)
- L77 `test_whatsapp_lid_user_matches_phone_allowlist_via_session_mapping(monkeypatch, tmp_path)` (function)
- L103 `test_simplex_allowlist_accepts_display_name(monkeypatch)` (function) — SIMPLEX_ALLOWED_USERS should match the contact's display name as well
- L141 `test_simplex_allowlist_accepts_numeric_contact_id(monkeypatch)` (function) — The numeric contactId form must still work — the new display-name
- L174 `test_simplex_allowlist_denies_unlisted(monkeypatch)` (function) — Sanity check: an unrelated SimpleX user is still rejected.
- L206 `test_star_wildcard_in_allowlist_authorizes_any_user(monkeypatch)` (function) — WHATSAPP_ALLOWED_USERS=* should act as allow-all wildcard.
- L226 `test_star_wildcard_works_for_any_platform(monkeypatch)` (function) — The * wildcard should work generically, not just for WhatsApp.
- L246 `test_qq_group_allowlist_authorizes_group_chat_without_user_allowlist(monkeypatch)` (function)
- L266 `test_qq_group_allowlist_does_not_authorize_other_groups(monkeypatch)` (function)
- L286 `test_telegram_group_user_allowlist_authorizes_forum_sender_without_dm_allowlist(monkeypatch)` (function)
- L305 `test_telegram_group_user_allowlist_rejects_other_senders(monkeypatch)` (function)
- L324 `test_telegram_group_user_allowlist_wildcard_authorizes_any_sender(monkeypatch)` (function)
- L343 `test_telegram_group_user_allowlist_does_not_authorize_dms(monkeypatch)` (function)
- L362 `test_telegram_group_chat_allowlist_authorizes_group_chat_without_user_allowlist(monkeypatch)` (function)
- L382 `test_telegram_group_chat_allowlist_authorizes_anonymous_sender(monkeypatch)` (function) — TELEGRAM_GROUP_ALLOWED_CHATS must authorize chat traffic with no
- L408 `test_telegram_group_chat_allowlist_rejects_anonymous_sender_in_other_chat(monkeypatch)` (function) — Anonymous senders in a chat *not* on the allowlist must still be
- L432 `test_handle_message_does_not_drop_anonymous_sender_in_allowlisted_chat(monkeypatch)` (function) — End-to-end: a group message with from_user=None in an allowlisted
- L474 `test_handle_message_drops_anonymous_sender_outside_allowlist(monkeypatch)` (function) — Anonymous senders in a chat *not* on the allowlist remain silently
- L509 `test_telegram_group_users_legacy_chat_ids_still_authorize(monkeypatch)` (function) — Backward-compat: PR #15027 shipped TELEGRAM_GROUP_ALLOWED_USERS as a
- L535 `test_telegram_group_users_legacy_does_not_cross_chats(monkeypatch)` (function) — Legacy chat-ID value only authorizes the listed chat, not any group.
- L556 `test_telegram_group_users_mixed_sender_and_legacy_chat(monkeypatch)` (function) — Mixed values: positive user ID gates senders; negative chat ID gates chat.
- L588 `test_unauthorized_dm_pairs_by_default(monkeypatch)` (function)
- L615 `test_unauthorized_whatsapp_dm_can_be_ignored(monkeypatch)` (function)
- L641 `test_rate_limited_user_gets_no_response(monkeypatch)` (function) — When a user is already rate-limited, pairing messages are silently ignored.
- L664 `test_rejection_message_records_rate_limit(monkeypatch)` (function) — After sending a 'too many requests' rejection, rate limit is recorded
- L691 `test_global_ignore_suppresses_pairing_reply(monkeypatch)` (function)
- L718 `test_signal_with_allowlist_ignores_unauthorized_dm(monkeypatch)` (function) — When SIGNAL_ALLOWED_USERS is set, unauthorized DMs are silently dropped.
- L743 `test_telegram_with_allowlist_ignores_unauthorized_dm(monkeypatch)` (function) — Same behavior for Telegram: allowlist ⟹ ignore unauthorized DMs.
- L763 `test_global_allowlist_ignores_unauthorized_dm(monkeypatch)` (function) — GATEWAY_ALLOWED_USERS also triggers the 'ignore' behavior.
- L783 `test_no_allowlist_still_pairs_by_default(monkeypatch)` (function) — Without any allowlist, pairing behavior is preserved (open gateway).
- L804 `test_explicit_pair_config_overrides_allowlist_default(monkeypatch)` (function) — Explicit unauthorized_dm_behavior='pair' overrides the allowlist default.
- L830 `test_allowlist_authorized_user_returns_ignore_for_unauthorized(monkeypatch)` (function) — _get_unauthorized_dm_behavior returns 'ignore' when allowlist is set.
- L848 `test_get_unauthorized_dm_behavior_no_allowlist_returns_pair(monkeypatch)` (function) — Without any allowlist, 'pair' is still the default.
- L861 `test_qqbot_with_allowlist_ignores_unauthorized_dm(monkeypatch)` (function) — QQBOT is included in the allowlist-aware default (QQ_ALLOWED_USERS).
