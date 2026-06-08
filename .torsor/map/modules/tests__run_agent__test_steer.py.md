---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/run_agent/test_steer.py

Symbols in `tests/run_agent/test_steer.py`.

- L18 `_bare_agent()` (function) — Build an AIAgent without running __init__, then install the steer
- L29 `TestSteerAcceptance` (class)
- L30 `test_accepts_non_empty_text(self)` (method)
- L35 `test_rejects_empty_string(self)` (method)
- L40 `test_rejects_whitespace_only(self)` (method)
- L45 `test_rejects_none(self)` (method)
- L50 `test_strips_surrounding_whitespace(self)` (method)
- L55 `test_concatenates_multiple_steers_with_newlines(self)` (method)
- L63 `TestSteerDrain` (class)
- L64 `test_drain_returns_and_clears(self)` (method)
- L70 `test_drain_on_empty_returns_none(self)` (method)
- L75 `TestSteerInjection` (class)
- L76 `test_appends_to_last_tool_result(self)` (method)
- L94 `test_no_op_when_no_steer_pending(self)` (method)
- L103 `test_no_op_when_num_tool_msgs_zero(self)` (method)
- L111 `test_marker_labels_text_as_out_of_band_user_message(self)` (method) — The injection marker must attribute the appended text to the user
- L126 `test_multimodal_content_list_preserved(self)` (method) — Anthropic-style list content should be preserved, with the steer
- L143 `test_restashed_when_no_tool_result_in_batch(self)` (method) — If the 'batch' contains no tool-role messages (e.g. all skipped
- L162 `TestSteerThreadSafety` (class)
- L163 `test_concurrent_steer_calls_preserve_all_text(self)` (method)
- L184 `TestSteerClearedOnInterrupt` (class)
- L185 `test_clear_interrupt_drops_pending_steer(self)` (method) — A hard interrupt supersedes any pending steer — the agent's
- L205 `TestPreApiCallSteerDrain` (class) — Test that steers arriving during an API call are drained before the
- L211 `test_pre_api_drain_injects_into_last_tool_result(self)` (method) — If a steer is pending when the main loop starts building
- L238 `test_pre_api_drain_restashes_when_no_tool_message(self)` (method) — If there are no tool results yet (first iteration), the steer
- L259 `test_pre_api_drain_finds_tool_msg_past_assistant(self)` (method) — The pre-API drain should scan backwards past a non-tool message
- L281 `TestSteerMarkerContract` (class)
- L282 `test_system_prompt_note_describes_the_real_marker(self)` (method) — The system-prompt note tells the model which marker to trust; it
- L292 `test_marker_no_longer_uses_the_distrusted_label(self)` (method) — Regression: the bare 'User guidance:' line read as tool content and
- L298 `TestSteerCommandRegistry` (class)
- L299 `test_steer_in_command_registry(self)` (method) — The /steer slash command must be registered so it reaches all
- L311 `test_steer_in_bypass_set(self)` (method) — When the agent is running, /steer MUST bypass the Level-1
