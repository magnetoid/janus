---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/run_agent/test_message_sequence_repair.py

Symbols in `tests/run_agent/test_message_sequence_repair.py`.

- L15 `_bare_agent()` (function)
- L21 `test_drop_scaffolding_rewinds_orphan_tool_tail()` (function) — When scaffolding is stripped, also rewind the orphan assistant+tool pair.
- L39 `test_drop_scaffolding_keeps_tail_when_no_scaffolding()` (function) — Mid-iteration tool results must NOT be rewound — only if scaffolding fires.
- L56 `test_drop_scaffolding_handles_multiple_parallel_tool_results()` (function) — Parallel tool calls (one assistant → many tool results) all rewound together.
- L81 `test_repair_merges_consecutive_user_messages()` (function)
- L96 `test_repair_preserves_user_content_when_one_side_empty()` (function)
- L108 `test_repair_does_not_rewind_ongoing_dialog_tool_pair()` (function) — assistant(tool_calls) + tool + user is a VALID pattern (user redirect
- L131 `test_repair_drops_stray_tool_with_unknown_tool_call_id()` (function)
- L146 `test_repair_leaves_valid_conversation_unchanged()` (function)
- L165 `test_repair_preserves_multimodal_user_content()` (function) — Multimodal (list) content must NOT be merged — risks mangling attachments.
- L181 `test_repair_empty_messages_returns_zero()` (function)
- L191 `test_repair_preserves_system_messages()` (function)
