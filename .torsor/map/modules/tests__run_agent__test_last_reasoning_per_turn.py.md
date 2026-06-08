---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/run_agent/test_last_reasoning_per_turn.py

Symbols in `tests/run_agent/test_last_reasoning_per_turn.py`.

- L12 `_extract_last_reasoning(messages)` (function) — Replica of the extraction loop in run_agent.py (~line 13867).
- L28 `test_simple_turn_reasoning_present()` (function)
- L36 `test_simple_turn_no_reasoning()` (function)
- L44 `test_tool_call_turn_reasoning_on_tool_call_step()` (function) — When the model reasons on the tool-call step and the final-answer
- L64 `test_no_stale_reasoning_across_turns()` (function) — The regression the whole change exists for.  Prior turn had
- L81 `test_tool_call_turn_picks_latest_reasoning_within_turn()` (function) — If BOTH the tool-call step and the final step have reasoning
- L102 `test_empty_string_reasoning_treated_as_missing()` (function)
