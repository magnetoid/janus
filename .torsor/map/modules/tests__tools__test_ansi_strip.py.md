---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/tools/test_ansi_strip.py

Symbols in `tests/tools/test_ansi_strip.py`.

- L11 `TestStripAnsiBasicSGR` (class) — Select Graphic Rendition — the most common ANSI sequences.
- L14 `test_reset(self)` (method)
- L17 `test_color(self)` (method)
- L20 `test_truecolor_semicolon(self)` (method)
- L23 `test_truecolor_colon_separated(self)` (method) — Modern terminals use colon-separated SGR params.
- L29 `TestStripAnsiCSIPrivateMode` (class) — CSI sequences with ? prefix (DEC private modes).
- L32 `test_cursor_show_hide(self)` (method)
- L36 `test_alt_screen(self)` (method)
- L40 `test_bracketed_paste(self)` (method)
- L44 `TestStripAnsiCSIIntermediate` (class) — CSI sequences with intermediate bytes (space, etc.).
- L47 `test_cursor_shape(self)` (method)
- L53 `TestStripAnsiOSC` (class) — Operating System Command sequences.
- L56 `test_bel_terminator(self)` (method)
- L59 `test_st_terminator(self)` (method)
- L62 `test_hyperlink_preserves_text(self)` (method)
- L68 `TestStripAnsiDECPrivate` (class) — DEC private / Fp escape sequences.
- L71 `test_save_restore_cursor(self)` (method)
- L75 `test_keypad_modes(self)` (method)
- L80 `TestStripAnsiFe` (class) — Fe (C1 as 7-bit) escape sequences.
- L83 `test_reverse_index(self)` (method)
- L86 `test_reset_terminal(self)` (method)
- L89 `test_index_and_newline(self)` (method)
- L94 `TestStripAnsiNF` (class) — nF (character set selection) sequences.
- L97 `test_charset_selection(self)` (method)
- L103 `TestStripAnsiDCS` (class) — Device Control String sequences.
- L106 `test_dcs(self)` (method)
- L110 `TestStripAnsi8BitC1` (class) — 8-bit C1 control characters.
- L113 `test_8bit_csi(self)` (method)
- L117 `test_8bit_standalone(self)` (method)
- L123 `TestStripAnsiRealWorld` (class) — Real-world contamination scenarios from bug reports.
- L126 `test_colored_shebang(self)` (method) — The original reported bug: shebang corrupted by color codes.
- L132 `test_stacked_sgr(self)` (method)
- L137 `test_ansi_mid_code(self)` (method)
- L143 `TestStripAnsiPassthrough` (class) — Clean content must pass through unmodified.
- L146 `test_plain_text(self)` (method)
- L149 `test_empty(self)` (method)
- L152 `test_none(self)` (method)
- L155 `test_whitespace_preserved(self)` (method)
- L158 `test_unicode_safe(self)` (method)
- L161 `test_backslash_in_code(self)` (method)
- L165 `test_square_brackets_in_code(self)` (method) — Array indexing must not be confused with CSI.
