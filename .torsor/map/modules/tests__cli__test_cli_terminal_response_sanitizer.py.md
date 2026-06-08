---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/cli/test_cli_terminal_response_sanitizer.py

Symbols in `tests/cli/test_cli_terminal_response_sanitizer.py`.

- L11 `TestStripLeakedTerminalResponses` (class)
- L12 `test_plain_text_unchanged(self)` (method)
- L16 `test_empty_text(self)` (method)
- L19 `test_strips_canonical_dsr_response(self)` (method)
- L24 `test_strips_dsr_response_in_middle_of_text(self)` (method)
- L28 `test_strips_multiple_dsr_responses(self)` (method)
- L32 `test_strips_visible_form_dsr(self)` (method)
- L38 `test_strips_visible_form_dsr_in_middle_of_text(self)` (method)
- L42 `test_does_not_strip_user_text_with_R(self)` (method)
- L49 `test_does_not_strip_sgr_sequences(self)` (method)
- L55 `test_preserves_multiline_content(self)` (method)
- L59 `test_strips_sgr_mouse_report_esc_form(self)` (method)
- L63 `test_strips_sgr_mouse_report_visible_form(self)` (method)
- L67 `test_strips_sgr_mouse_report_bare_form(self)` (method)
- L71 `test_strips_sgr_mouse_report_with_large_coordinates(self)` (method)
- L75 `test_strips_multiple_concatenated_sgr_mouse_reports(self)` (method)
- L79 `test_does_not_strip_regular_angle_bracket_text(self)` (method)
