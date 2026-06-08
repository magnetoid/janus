---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_transcript_offset.py

Symbols in `tests/gateway/test_transcript_offset.py`.

- L23 `_filter_history(history: list)` (function) — Replicate the agent_history filtering from GatewayRunner._run_agent.
- L56 `TestTranscriptHistoryOffset` (class) — Verify the transcript extraction uses the filtered history length.
- L59 `test_session_meta_causes_offset_mismatch(self)` (method) — Turn 2: session_meta makes len(history) > len(agent_history).
- L102 `test_no_session_meta_same_result(self)` (method) — First turn has no session_meta, so both approaches agree.
- L123 `test_multiple_session_meta_larger_drift(self)` (method) — Two session_meta entries double the offset error.
- L168 `test_system_messages_also_filtered(self)` (method) — system messages in history are also stripped from agent_history.
- L201 `test_else_branch_returns_empty_list(self)` (method) — When agent has fewer messages than offset, return [] not all.
- L228 `test_tool_call_messages_preserved_in_filter(self)` (method) — Tool call messages pass through the filter, keeping offset correct.
- L270 `test_recursive_queued_followup_keeps_outer_history_offset(self)` (method) — Queued drain persistence must include every turn in the chain.
- L315 `test_recursive_queued_followup_preserves_smaller_existing_offset(self)` (method) — Do not widen the slice if the nested result is already conservative.
