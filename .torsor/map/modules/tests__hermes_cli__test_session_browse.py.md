---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/hermes_cli/test_session_browse.py

Symbols in `tests/hermes_cli/test_session_browse.py`.

- L18 `_make_sessions(n=5)` (function) — Generate a list of fake rich-session dicts.
- L41 `TestSessionBrowsePicker` (class) — Tests for the _session_browse_picker function.
- L44 `test_empty_sessions_returns_none(self, capsys)` (method)
- L49 `test_returns_none_when_no_sessions(self, capsys)` (method)
- L53 `test_fallback_mode_valid_selection(self)` (method) — When curses is unavailable, fallback numbered list should work.
- L72 `test_fallback_mode_cancel_q(self)` (method) — Entering 'q' in fallback mode cancels.
- L90 `test_fallback_mode_cancel_empty(self)` (method) — Entering empty string in fallback mode cancels.
- L108 `test_fallback_mode_invalid_then_valid(self)` (method) — Invalid selection followed by valid one works.
- L126 `test_fallback_mode_keyboard_interrupt(self)` (method) — KeyboardInterrupt in fallback mode returns None.
- L144 `test_fallback_displays_all_sessions(self, capsys)` (method) — Fallback mode should display all session entries.
- L167 `test_fallback_shows_title_over_preview(self, capsys)` (method) — When a session has a title, show it instead of the preview.
- L192 `test_fallback_shows_preview_when_no_title(self, capsys)` (method) — When no title, show preview.
- L217 `test_fallback_shows_id_when_no_title_or_preview(self, capsys)` (method) — When neither title nor preview, show session ID.
- L245 `TestCursesBrowse` (class) — Tests for the curses-based interactive picker via simulated key sequences.
- L248 `_run_with_keys(self, sessions, key_sequence)` (method) — Simulate running the curses picker with a given key sequence.
- L270 `test_enter_selects_first_session(self)` (method)
- L275 `test_down_then_enter_selects_second(self)` (method)
- L281 `test_down_down_enter_selects_third(self)` (method)
- L287 `test_up_wraps_to_last(self)` (method)
- L293 `test_escape_cancels(self)` (method)
- L298 `test_q_cancels(self)` (method)
- L303 `test_type_to_filter_then_enter(self)` (method) — Typing characters filters the list, Enter selects from filtered.
- L315 `test_filter_no_match_enter_does_nothing(self)` (method) — When filter produces no results, Enter shouldn't select.
- L322 `test_backspace_removes_filter_char(self)` (method) — Backspace removes the last character from the filter.
- L333 `test_escape_clears_filter_first(self)` (method) — First Esc clears the search text, second Esc exits.
- L341 `test_filter_matches_preview(self)` (method) — Typing should match against session preview text.
- L351 `test_filter_matches_source(self)` (method) — Typing a source name should filter by source.
- L361 `test_q_quits_when_no_filter_active(self)` (method) — When no search text is active, 'q' should quit (not filter).
- L367 `test_q_types_into_filter_when_filter_active(self)` (method) — When search text is already active, 'q' should add to filter, not quit.
- L383 `TestSessionBrowseArgparse` (class) — Verify the 'browse' subcommand is properly registered.
- L386 `test_browse_subcommand_exists(self)` (method) — hermes sessions browse should be parseable.
- L396 `test_browse_default_limit_is_500(self)` (method) — The default --limit for browse should be 500.
- L415 `TestCmdSessionsBrowse` (class) — Integration tests for the 'browse' action in cmd_sessions.
- L418 `test_browse_no_sessions_prints_message(self, capsys)` (method) — When no sessions exist, _session_browse_picker returns None and prints message.
- L425 `test_browse_with_source_filter(self)` (method) — The --source flag should be passed to list_sessions_rich.
- L448 `TestEdgeCases` (class) — Edge case handling for the session browser.
- L451 `test_sessions_with_missing_fields(self)` (method) — Sessions with missing optional fields should not crash.
- L471 `test_single_session(self)` (method) — A single session in the list should work fine.
- L491 `test_long_title_truncated_in_fallback(self, capsys)` (method) — Very long titles should be truncated in fallback mode.
- L517 `test_relative_time_formatting(self, capsys)` (method) — Verify various time deltas format correctly.
