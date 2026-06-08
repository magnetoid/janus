---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/run_agent/test_background_review_summary.py

Symbols in `tests/run_agent/test_background_review_summary.py`.

- L16 `_tool_msg(tool_call_id, payload)` (function)
- L24 `test_skips_prior_tool_messages_by_tool_call_id()` (function) — Stale 'created' tool result from prior history must not be re-surfaced.
- L49 `test_includes_genuinely_new_actions()` (function)
- L61 `test_falls_back_to_content_equality_when_tool_call_id_missing()` (function) — If a tool message has no tool_call_id, match prior entries by content.
- L77 `test_ignores_failed_tool_results()` (function)
- L86 `test_handles_non_json_tool_content_gracefully()` (function)
- L97 `test_empty_inputs()` (function)
- L102 `test_added_message_relabels_by_target()` (function)
- L115 `test_removed_or_replaced_relabels_by_target()` (function)
