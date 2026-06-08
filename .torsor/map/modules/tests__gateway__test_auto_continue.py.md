---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_auto_continue.py

Symbols in `tests/gateway/test_auto_continue.py`.

- L11 `_simulate_auto_continue(agent_history: list, user_message: str)` (function) — Reproduce the auto-continue injection logic from _run_agent().
- L31 `TestAutoDetection` (class) — Test that trailing tool results are correctly detected.
- L34 `test_trailing_tool_result_triggers_note(self)` (method)
- L47 `test_trailing_assistant_message_no_note(self)` (method)
- L56 `test_empty_history_no_note(self)` (method)
- L60 `test_trailing_user_message_no_note(self)` (method) — Shouldn't happen in practice, but ensure no false positive.
- L68 `test_multiple_tool_results_still_triggers(self)` (method) — Multiple tool calls in a row — last one is still role=tool.
- L82 `test_original_message_preserved_after_note(self)` (method) — The user's actual message must appear after the system note.
