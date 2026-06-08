---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_feishu_bot_admission.py

Symbols in `tests/gateway/test_feishu_bot_admission.py`.

- L30 `test_feishu_load_settings_populates_allow_bots(monkeypatch, env_value, expected)` (function)
- L41 `test_feishu_load_settings_allow_bots_defaults_to_none(monkeypatch)` (function)
- L52 `test_feishu_load_settings_ignores_extra_allow_bots(monkeypatch)` (function)
- L64 `test_feishu_load_settings_falls_back_to_env_when_extra_missing(monkeypatch)` (function)
- L75 `test_feishu_load_settings_warns_on_unknown_allow_bots(monkeypatch, caplog)` (function)
- L100 `test_feishu_load_settings_require_mention(monkeypatch, env_value, extra, expected)` (function)
- L114 `test_feishu_load_settings_parses_per_group_require_mention(monkeypatch)` (function)
- L135 `test_sender_identity_collects_every_non_empty_id_variant()` (function)
- L144 `test_sender_identity_handles_missing_sender_id()` (function)
- L151 `test_is_bot_sender_treats_bot_and_app_as_bot_origin(sender_type)` (function)
- L158 `test_is_bot_sender_rejects_non_bot_origin(sender_type)` (function)
- L172 `_admit_case(*, adapter: dict | None=None, sender: dict | None=None, message: dict | None=None, mentions_self: bool | None=None, expected: str | None=None)` (function)
- L379 `test_admit_pipeline(case)` (function)
- L391 `test_admit_skips_mention_check_under_all_mode()` (function)
- L408 `test_admit_group_mention_checked_once_per_call()` (function)
- L432 `test_admit_per_group_require_mention_overrides_global()` (function)
- L454 `test_hydrate_bot_identity_populates_self_ids_from_bot_v3_info(monkeypatch)` (function)
- L515 `test_resolve_sender_profile_uses_open_id_for_bot_name_lookup()` (function)
- L550 `_group_case(*, adapter: dict | None=None, admins: set | None=None, group_rules: dict | None=None, sender: dict | None=None, chat_id: str='oc_1', is_bot: bool=False, expected: bool=False)` (function)
- L571 `_group_rule(policy: str, **kwargs)` (function)
- L653 `test_allow_group_message_matrix(case)` (function)
- L666 `test_allow_group_message_channel_locks_apply_to_bots(policy, sender_type, expected)` (function)
- L678 `test_allow_group_message_blacklist_is_human_scope_only(sender_type)` (function)
- L696 `test_admit_accepts_realistic_bot_at_bot_group_event()` (function)
- L727 `test_handle_message_event_data_drops_bot_sender_by_default()` (function)
- L750 `test_handle_message_event_data_forwards_sender_when_admitted()` (function)
