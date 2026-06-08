---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/test_model_picker_scroll.py

Symbols in `tests/test_model_picker_scroll.py`.

- L25 `_compute_scroll_offset(cursor: int, scroll_offset: int, visible: int, n_choices: int)` (function) — Mirror of the scroll adjustment block inside _curses_menu.
- L35 `_visible_indices(cursor: int, scroll_offset: int, visible: int, n_choices: int)` (function) — Return the list indices that would be rendered for the given state.
- L45 `TestScrollOffsetLogic` (class)
- L48 `test_cursor_at_zero_no_scroll(self)` (method) — Start position: offset stays 0, first items visible.
- L52 `test_cursor_within_window_unchanged(self)` (method) — Cursor inside the current window: offset unchanged.
- L56 `test_cursor_at_last_item_scrolls_down(self)` (method) — Cursor on Cancel (index 12) with 8-row window: offset = 12 - 8 + 1 = 5.
- L62 `test_cursor_wraps_to_cancel_via_up(self)` (method) — UP from index 0 wraps to last item; last item must be visible.
- L68 `test_cursor_above_window_scrolls_up(self)` (method) — Cursor above current window: offset tracks cursor.
- L75 `test_visible_window_never_exceeds_list(self)` (method) — Offset is clamped so the window never starts past the list end.
- L80 `test_single_item_list(self)` (method) — Edge case: one choice, cursor 0.
- L84 `test_list_fits_in_window_no_scroll_needed(self)` (method) — If all choices fit in the visible window, offset is always 0.
- L90 `test_cursor_always_in_visible_range(self)` (method) — Invariant: cursor is always within the rendered window after adjustment.
- L97 `test_full_navigation_down_cursor_always_visible(self)` (method) — Simulate pressing DOWN through all items; cursor always in view.
- L108 `test_full_navigation_up_cursor_always_visible(self)` (method) — Simulate pressing UP through all items; cursor always in view.
