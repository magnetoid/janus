---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_slash_access_dispatch.py

Symbols in `tests/gateway/test_slash_access_dispatch.py`.

- L32 `_make_source(*, platform: Platform=Platform.DISCORD, user_id: str='user1', chat_type: str='dm', chat_id: str='c1')` (function)
- L48 `_make_event(text: str, source: SessionSource)` (function)
- L52 `_make_runner(*, platform_extra: dict | None=None, platform: Platform=Platform.DISCORD)` (function)
- L121 `test_whoami_unrestricted_when_no_admin_list()` (function)
- L129 `test_whoami_admin_user()` (function)
- L136 `test_whoami_non_admin_lists_runnable_commands()` (function)
- L157 `test_non_admin_denied_for_unlisted_command()` (function)
- L173 `test_non_admin_with_empty_user_commands_gets_floor_only()` (function)
- L195 `test_admin_runs_unlisted_command()` (function)
- L211 `test_user_runs_listed_command()` (function)
- L229 `test_backward_compat_no_admin_list_means_no_gate()` (function)
- L244 `test_dm_admin_is_not_group_admin()` (function)
- L261 `test_group_only_gating_leaves_dm_unrestricted()` (function)
- L278 `test_plugin_registered_command_is_gated(monkeypatch)` (function) — The gate must recognize plugin-registered slash commands, not just
- L330 `test_running_agent_fastpath_blocks_non_admin_command()` (function) — When an agent is running, /restart from a non-admin must be denied.
- L351 `test_running_agent_fastpath_allows_admin_command()` (function) — Admins must still be able to run privileged commands like /restart
- L375 `test_running_agent_fastpath_status_always_works()` (function) — /status is intentionally pre-gate on the fast-path so users can
- L402 `test_gate_uses_canonical_name_not_alias()` (function) — If /hist resolves to canonical 'history' and history is in
- L429 `test_gate_does_not_intercept_unknown_command()` (function) — Random non-command text like /xyzzy is not in the registry. The gate
- L462 `test_dm_admin_blocked_in_group_with_separate_admin_list()` (function)
- L484 `test_gating_isolated_per_platform()` (function) — When Discord is gated and Telegram isn't, the same user_id on
