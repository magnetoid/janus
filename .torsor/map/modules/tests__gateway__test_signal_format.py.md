---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_signal_format.py

Symbols in `tests/gateway/test_signal_format.py`.

- L18 `_m2s(text: str)` (function) — Shorthand: call the static method and return (plain_text, styles).
- L23 `_style_types(styles: list[str])` (function) — Extract just the STYLE part from '0:4:BOLD' strings.
- L28 `_find_style(styles: list[str], style_type: str)` (function) — Return only styles matching a given type.
- L37 `TestMarkdownToSignalBasic` (class) — Core formatting: bold, italic, strikethrough, monospace.
- L40 `test_bold_double_asterisk(self)` (method)
- L46 `test_bold_double_underscore(self)` (method)
- L52 `test_italic_single_asterisk(self)` (method)
- L58 `test_italic_single_underscore(self)` (method)
- L64 `test_strikethrough(self)` (method)
- L70 `test_inline_monospace(self)` (method)
- L76 `test_fenced_code_block(self)` (method)
- L82 `test_heading_becomes_bold(self)` (method)
- L88 `test_multiple_styles(self)` (method)
- L95 `test_plain_text_no_styles(self)` (method)
- L100 `test_empty_string(self)` (method)
- L110 `TestItalicFalsePositives` (class) — Regressions from signal-italic-false-positive-fix.md and
- L116 `test_snake_case_not_italic(self)` (method) — snake_case identifiers must NOT be italicized.
- L122 `test_multiple_snake_case(self)` (method)
- L126 `test_snake_case_path(self)` (method)
- L130 `test_snake_case_between_words(self)` (method) — file_path and error_code — underscores between words.
- L137 `test_bullet_list_not_italic(self)` (method) — * item lines must NOT be treated as italic delimiters.
- L143 `test_bullet_list_with_content_before(self)` (method)
- L148 `test_bullet_list_file_paths(self)` (method) — Real-world case that triggered the bug.
- L158 `test_bullet_with_italic_inside(self)` (method) — Italic *inside* a bullet item should still work.
- L169 `test_star_italic_no_cross_line(self)` (method) — *foo\nbar* must NOT match as italic (no DOTALL).
- L174 `test_underscore_italic_no_cross_line(self)` (method) — _foo\nbar_ must NOT match as italic (no DOTALL).
- L179 `test_star_italic_multiline_response(self)` (method) — Multi-paragraph response with * should not false-positive.
- L193 `test_star_italic_still_works(self)` (method)
- L198 `test_underscore_italic_still_works(self)` (method)
- L203 `test_multiple_italic_same_line(self)` (method)
- L208 `test_italic_single_word(self)` (method)
- L213 `test_italic_multi_word(self)` (method)
- L223 `TestStylePositions` (class) — Verify that start:length positions map to the correct text.
- L226 `_extract(self, text: str, style_str: str)` (method) — Given 'start:length:STYLE', extract the substring from text.
- L236 `test_bold_position(self)` (method)
- L241 `test_italic_position(self)` (method)
- L246 `test_multiple_styles_positions(self)` (method)
- L252 `test_emoji_utf16_offset(self)` (method) — Emoji (multi-byte UTF-16) before a styled span.
- L264 `TestEdgeCases` (class) — Tricky inputs that have caused issues or could regress.
- L267 `test_bold_inside_bullet(self)` (method) — Bold inside a bullet list item.
- L274 `test_code_span_with_underscores(self)` (method) — `snake_case_var` — backtick takes priority over underscore.
- L282 `test_bold_and_italic_nested(self)` (method) — ***bold+italic*** — bold captured, not italic (bold pattern first).
- L289 `test_lone_asterisk(self)` (method) — A single * with no pair should not cause issues.
- L295 `test_lone_underscore(self)` (method) — A single _ with no pair.
- L300 `test_consecutive_underscored_words(self)` (method) — _foo and _bar (leading underscores, no closers).
- L305 `test_mixed_formatting_no_bleed(self)` (method) — Multiple format types don't bleed into each other.
- L318 `TestMarkdownStripPatch` (class) — Tests for the original signal-markdown-strip-patch.
- L326 `test_fenced_code_block_with_language_tag(self)` (method) — ```python\ncode\n``` — language tag is stripped, content is MONOSPACE.
- L334 `test_fenced_code_block_multiline(self)` (method) — Multi-line code blocks preserve all lines.
- L343 `test_links_preserved(self)` (method) — [text](url) links are kept as-is — Signal auto-linkifies.
- L350 `test_heading_h1(self)` (method) — # H1 becomes bold text.
- L357 `test_heading_h3(self)` (method) — ### H3 becomes bold text.
- L364 `test_multiple_headings(self)` (method) — Multiple headings each become separate bold spans.
- L374 `test_no_raw_markdown_markers_in_output(self)` (method) — All markdown syntax is stripped from plain text output.
- L384 `test_utf16_surrogate_pair_emoji(self)` (method) — Emoji requiring UTF-16 surrogate pairs don't corrupt offsets.
- L397 `test_consecutive_newlines_collapsed(self)` (method) — 3+ consecutive newlines are collapsed to 2.
- L404 `test_empty_bold_not_crash(self)` (method) — **** (empty bold) should not crash.
- L415 `TestSignalStreamingPatch` (class) — Tests for signal-streaming-patch: cursor suppression and edit support.
- L422 `test_signal_does_not_support_editing(self, monkeypatch)` (method) — SignalAdapter.SUPPORTS_MESSAGE_EDITING must be False.
- L429 `test_send_returns_no_message_id(self, monkeypatch)` (method) — send() returns message_id=None so stream consumer uses no-edit path.
