---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_replay_entry_fields.py

Symbols in `tests/gateway/test_replay_entry_fields.py`.

- L23 `TestBuildReplayEntry` (class)
- L24 `test_user_message_has_only_role_and_content(self)` (method)
- L32 `test_tool_message_has_only_role_and_content(self)` (method)
- L44 `test_assistant_minimal_has_only_role_and_content(self)` (method)
- L52 `test_assistant_preserves_reasoning(self)` (method)
- L61 `test_assistant_preserves_reasoning_content(self)` (method) — reasoning_content was silently dropped before this fix.
- L75 `test_assistant_preserves_reasoning_details(self)` (method)
- L96 `test_assistant_preserves_codex_reasoning_items(self)` (method)
- L106 `test_assistant_preserves_codex_message_items(self)` (method) — codex_message_items was silently dropped before this fix.
- L130 `test_assistant_preserves_finish_reason(self)` (method) — finish_reason was silently dropped before this fix.
- L144 `test_assistant_drops_falsy_reasoning(self)` (method) — Empty/None reasoning fields stay dropped (matching PR #2974
- L159 `test_assistant_preserves_empty_reasoning_content(self)` (method) — Empty reasoning_content is a meaningful sentinel.
- L177 `test_assistant_drops_none_reasoning_content(self)` (method) — None reasoning_content is just an absent field; drop it.
- L187 `test_assistant_preserves_all_six_fields_together(self)` (method)
- L216 `test_assistant_does_not_invent_keys(self)` (method) — The helper only copies over fields that are explicitly present.
- L230 `test_replay_fields_constant_is_stable(self)` (method) — Pin the whitelist explicitly so accidental renames are caught.
- L241 `test_unrelated_keys_are_ignored(self)` (method) — Random keys on the message must not leak into the replay entry.
