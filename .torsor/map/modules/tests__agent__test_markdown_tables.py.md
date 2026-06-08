---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/agent/test_markdown_tables.py

Symbols in `tests/agent/test_markdown_tables.py`.

- L21 `_column_offsets(line: str)` (function) — Return the display-cell index of every ``|`` in ``line``.
- L40 `test_split_strips_outer_pipes_and_trims()` (function)
- L46 `test_is_table_divider_handles_alignment_colons()` (function)
- L54 `test_looks_like_table_row()` (function)
- L67 `test_no_op_on_text_without_tables()` (function)
- L72 `test_no_op_when_pipes_but_no_divider()` (function)
- L77 `test_cjk_table_pipes_align_across_rows()` (function)
- L102 `test_emoji_with_cjk_table_aligns()` (function)
- L123 `test_already_aligned_ascii_table_remains_aligned()` (function)
- L137 `test_passes_non_table_lines_through_around_a_table()` (function)
- L164 `test_overflow_falls_back_to_vertical_when_table_wider_than_terminal()` (function) — A horizontal table that would exceed the available width must
- L195 `test_horizontal_kept_when_table_fits()` (function) — A table that fits the terminal must keep the horizontal
- L218 `test_vertical_fallback_wraps_long_cell_text_with_indent()` (function)
- L239 `test_overflow_falls_back_to_vertical_for_cjk_too()` (function) — CJK content can also push a table over the terminal budget;
- L261 `test_handles_ragged_rows_by_padding_short_rows()` (function)
- L278 `test_multiple_tables_in_one_text()` (function)
