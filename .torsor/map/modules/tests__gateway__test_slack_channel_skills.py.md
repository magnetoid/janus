---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_slack_channel_skills.py

Symbols in `tests/gateway/test_slack_channel_skills.py`.

- L5 `_make_adapter(extra=None)` (function) — Create a minimal SlackAdapter stub with the given ``config.extra``.
- L14 `_resolve(adapter, channel_id, parent_id=None)` (function)
- L19 `TestSlackResolveChannelSkills` (class)
- L20 `test_no_bindings_returns_none(self)` (method)
- L24 `test_match_by_dm_channel_id(self)` (method) — The primary use case: binding a skill to a Slack DM channel.
- L33 `test_match_by_parent_id_for_thread(self)` (method) — Slack threads inherit the parent channel's binding.
- L42 `test_no_match_returns_none(self)` (method)
- L50 `test_single_skill_string(self)` (method)
- L58 `test_dedup_preserves_order(self)` (method)
- L66 `test_multiple_bindings_pick_correct(self)` (method)
- L76 `test_malformed_entry_skipped(self)` (method) — Non-dict entries should be ignored, not raise.
- L86 `test_empty_skills_list_returns_none(self)` (method)
- L94 `test_empty_skill_string_returns_none(self)` (method)
- L103 `TestSlackMessageEventAutoSkill` (class) — Integration-style test: verify auto_skill propagates to MessageEvent.
- L106 `test_message_event_carries_auto_skill(self)` (method) — Simulate the handler wiring: resolve + attach to MessageEvent.
