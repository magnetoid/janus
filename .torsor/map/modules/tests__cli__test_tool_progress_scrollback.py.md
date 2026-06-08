---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/cli/test_tool_progress_scrollback.py

Symbols in `tests/cli/test_tool_progress_scrollback.py`.

- L20 `_make_cli(tool_progress='all', verbose=_UNSET)` (function) — Create a HermesCLI instance with minimal mocking.
- L63 `TestToolProgressScrollback` (class) — Stacked scrollback lines for 'all' and 'new' modes.
- L66 `test_all_mode_prints_scrollback_on_completed(self)` (method) — In 'all' mode, tool.completed prints a stacked line.
- L80 `test_all_mode_prints_every_call(self)` (method) — In 'all' mode, consecutive calls to the same tool each get a line.
- L93 `test_new_mode_skips_consecutive_repeats(self)` (method) — In 'new' mode, consecutive calls to the same tool only print once.
- L104 `test_new_mode_prints_when_tool_changes(self)` (method) — In 'new' mode, a different tool name triggers a new line.
- L118 `test_off_mode_no_scrollback(self)` (method) — In 'off' mode, no stacked lines are printed.
- L127 `test_error_suffix_on_failed_tool(self)` (method) — When a failed tool's result is forwarded, the stacked line surfaces
- L144 `test_spinner_still_updates_on_started(self)` (method) — tool.started still updates the spinner text for live display.
- L150 `test_spinner_timer_clears_on_completed(self)` (method) — tool.completed still clears the tool timer.
- L159 `test_concurrent_tools_produce_stacked_lines(self)` (method) — Multiple tool.started followed by multiple tool.completed all produce lines.
- L172 `test_verbose_mode_no_duplicate_scrollback(self)` (method) — In 'verbose' mode, scrollback lines are NOT printed (run_agent handles verbose output).
- L181 `test_verbose_mode_config_does_not_enable_global_debug_logging(self)` (method) — display.tool_progress=verbose controls TOOL-CALL DISPLAY ONLY.
- L195 `test_explicit_verbose_argument_wins_over_config(self)` (method) — Explicit verbose=True from the CLI flag still enables DEBUG logging
- L203 `test_explicit_non_verbose_argument_keeps_debug_logging_off(self)` (method) — Explicit verbose=False overrides any default to enable DEBUG.
- L210 `test_pending_info_stores_on_started(self)` (method) — tool.started stores args for later use by tool.completed.
- L218 `test_pending_info_consumed_on_completed(self)` (method) — tool.completed consumes stored args (FIFO for concurrent).
