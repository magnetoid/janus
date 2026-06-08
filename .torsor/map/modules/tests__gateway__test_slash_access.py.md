---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_slash_access.py

Symbols in `tests/gateway/test_slash_access.py`.

- L21 `TestPolicyFromExtra` (class)
- L22 `test_empty_extra_is_disabled(self)` (method)
- L28 `test_disabled_policy_treats_anyone_as_admin(self)` (method)
- L35 `test_dm_admin_list_only(self)` (method)
- L41 `test_admin_runs_anything(self)` (method)
- L50 `test_non_admin_runs_only_listed_commands(self)` (method)
- L64 `test_always_allowed_floor_for_non_admin(self)` (method)
- L74 `test_unknown_user_id_blocked(self)` (method)
- L85 `test_id_coercion_ints_become_strings(self)` (method)
- L92 `test_id_coercion_csv_string(self)` (method)
- L96 `test_command_coercion_strips_leading_slash_and_lowercases(self)` (method)
- L106 `test_command_coercion_csv_string(self)` (method)
- L116 `test_group_scope_uses_group_keys(self)` (method)
- L132 `test_dm_falls_back_to_group_user_commands_when_dm_unset(self)` (method)
- L142 `test_dm_admin_does_not_imply_group_admin(self)` (method)
- L166 `TestPolicyForSource` (class)
- L167 `test_no_config_returns_disabled(self)` (method)
- L172 `test_no_platform_config_returns_disabled(self)` (method)
- L180 `test_dm_chat_type_resolves_to_dm_scope(self)` (method)
- L203 `test_group_chat_type_resolves_to_group_scope(self)` (method)
- L228 `test_channel_thread_chat_types_treated_as_group_scope(self)` (method)
- L249 `test_no_admin_list_for_dm_means_unrestricted_in_dm(self)` (method)
- L272 `test_per_platform_isolation(self)` (method)
