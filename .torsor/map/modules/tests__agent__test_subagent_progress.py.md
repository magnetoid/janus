---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/agent/test_subagent_progress.py

Symbols in `tests/agent/test_subagent_progress.py`.

- L24 `TestPrintAbove` (class) — Tests for KawaiiSpinner.print_above method.
- L27 `test_print_above_without_spinner_running(self)` (method) — print_above should write to stdout even when spinner is not running.
- L37 `test_print_above_with_spinner_running(self)` (method) — print_above should clear spinner line and print text.
- L49 `test_print_above_uses_captured_stdout(self)` (method) — print_above should use self._out, not sys.stdout.
- L71 `TestBuildChildProgressCallback` (class) — Tests for child progress callback builder.
- L74 `test_returns_none_when_no_display(self)` (method) — Should return None when parent has no spinner or callback.
- L83 `test_cli_spinner_tool_event(self)` (method) — Should print tool line above spinner for CLI path.
- L103 `test_cli_spinner_thinking_event(self)` (method) — Should print thinking line above spinner for CLI path.
- L121 `test_gateway_batched_progress(self)` (method) — Gateway path: each tool.started relays a subagent.tool event, and a
- L147 `test_thinking_relayed_to_gateway(self)` (method) — Thinking events are relayed as subagent.thinking events.
- L161 `test_parallel_callbacks_independent(self)` (method) — Each child's callback batches tool names independently.
- L181 `test_task_index_prefix_in_batch_mode(self)` (method) — Batch mode (task_count > 1) should show 1-indexed prefix for all tasks.
- L206 `test_single_task_no_prefix(self)` (method) — Single task (task_count=1) should not show index prefix.
- L228 `TestThinkingCallback` (class) — Tests for the _thinking callback in AIAgent conversation loop.
- L231 `_simulate_thinking_callback(self, content, callback, delegate_depth=1)` (method) — Simulate the exact code path from run_agent.py for the thinking callback.
- L250 `test_thinking_callback_fires_on_content(self)` (method) — tool_progress_callback should receive _thinking event
- L262 `test_thinking_callback_skipped_when_no_content(self)` (method) — Should not fire when assistant has no content.
- L271 `test_thinking_callback_truncates_long_content(self)` (method) — Should truncate long content to 80 chars.
- L281 `test_thinking_callback_skipped_for_main_agent(self)` (method) — Main agent (delegate_depth=0) should NOT fire thinking events.
- L292 `test_thinking_callback_strips_reasoning_scratchpad(self)` (method) — REASONING_SCRATCHPAD tags should be stripped before display.
- L303 `test_thinking_callback_strips_think_tags(self)` (method) — <think> tags should be stripped before display.
- L314 `test_thinking_callback_empty_after_strip(self)` (method) — Should not fire when content is only XML tags.
- L328 `TestBatchFlush` (class) — Tests for gateway batch flush on subagent completion.
- L331 `test_flush_sends_remaining_batch(self)` (method) — _flush should send a final subagent.progress summary of any unsent
- L358 `test_flush_noop_when_batch_empty(self)` (method) — _flush should not send anything when batch is empty.
- L369 `test_flush_noop_when_no_parent_callback(self)` (method) — _flush should not crash when there's no parent callback.
