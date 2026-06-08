---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# hermes_cli/curses_ui.py

Symbols in `hermes_cli/curses_ui.py`.

- L14 `_query_matches(label: str, query: str)` (function) — Return True when every query token is a case-insensitive subsequence.
- L39 `_is_boundary(target: str, index: int)` (function) — True if position ``index`` in ``target`` starts a word.
- L59 `_token_score(orig: str, lower: str, token: str)` (function) — Score one token against a target. None if the token isn't a subsequence.
- L113 `_fuzzy_score(label: str, query: str)` (function) — Aggregate score for a multi-token query (AND). None if any token fails.
- L138 `_filter_indices(items: List[str], query: str)` (function) — Return item indices matching *query*, ranked best-first.
- L164 `_SearchState` (class) — Mutable search state shared by curses picker loops.
- L171 `_reconcile_cursor(filtered: List[int], cursor: int)` (function) — Return ``(cursor, cursor_pos)`` inside the filtered index list.
- L182 `_move_filtered_cursor(filtered: List[int], cursor: int, cursor_pos: int, delta: int)` (function) — Move through the filtered index list, wrapping like the legacy menus.
- L192 `_scroll_for_cursor(scroll_offset: int, cursor_pos: int, visible_rows: int, total_rows: int)` (function) — Clamp scroll offset so the cursor remains visible.
- L206 `_handle_active_search_key(curses_mod, key: int, search: _SearchState)` (function) — Handle a key while the search prompt is active.
- L244 `flush_stdin()` (function) — Flush any stray bytes from the stdin input buffer.
- L276 `read_menu_key(stdscr)` (function) — Read one keypress and normalize it to a menu action.
- L295 `_decode_menu_key(stdscr, key: int)` (function) — Normalize an already-read keypress to a menu action.
- L350 `_run_curses_menu(*, initial_cursor, item_count, draw_header, draw_row, on_action, reserve_bottom=1, draw_footer=None, extra_color_pairs=False, fallback, cancel_value, searchable=False, search_labels=None)` (function) — Shared curses single-/multi-select event loop.
- L531 `curses_checklist(title: str, items: List[str], selected: Set[int], *, cancel_returns: Set[int] | None=None, status_fn: Optional[Callable[[Set[int]], str]]=None)` (function) — Curses multi-select checklist. Returns set of selected indices.
- L622 `curses_radiolist(title: str, items: List[str], selected: int=0, *, cancel_returns: int | None=None, description: str | None=None, searchable: bool=False)` (function) — Curses single-select radio list. Returns the selected index.
- L716 `_radio_numbered_fallback(title: str, items: List[str], selected: int, cancel_returns: int)` (function) — Text-based numbered fallback for radio selection.
- L742 `curses_single_select(title: str, items: List[str], default_index: int=0, *, cancel_label: str='Cancel', searchable: bool=False)` (function) — Curses single-select menu. Returns selected index or None on cancel.
- L816 `_numbered_single_fallback(title: str, items: List[str], cancel_idx: int)` (function) — Text-based numbered fallback for single-select.
- L840 `_numbered_fallback(title: str, items: List[str], selected: Set[int], cancel_returns: Set[int], status_fn: Optional[Callable[[Set[int]], str]]=None)` (function) — Text-based toggle fallback for terminals without curses.
