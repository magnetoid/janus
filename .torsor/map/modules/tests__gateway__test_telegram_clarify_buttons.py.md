---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_telegram_clarify_buttons.py

Symbols in `tests/gateway/test_telegram_clarify_buttons.py`.

- L26 `_ensure_telegram_mock()` (function)
- L54 `_make_adapter(extra=None)` (function)
- L62 `_clear_clarify_state()` (function)
- L74 `TestTelegramSendClarify` (class) — Verify the rendered prompt has buttons or none, and stores state.
- L77 `setup_method(self)` (method)
- L81 `test_multi_choice_renders_buttons_and_other(self)` (method)
- L114 `test_open_ended_no_keyboard(self)` (method)
- L136 `test_not_connected(self)` (method)
- L149 `test_long_choice_rendered_in_body_not_truncated(self)` (method) — Long choice text appears in full in the message body;
- L174 `test_html_escapes_question(self)` (method)
- L197 `TestTelegramClarifyCallback` (class) — Verify clicking a button resolves the clarify primitive.
- L200 `setup_method(self)` (method)
- L204 `test_numeric_choice_resolves_with_choice_text(self)` (method)
- L246 `test_other_button_flips_to_text_mode(self)` (method)
- L285 `test_already_resolved(self)` (method)
- L310 `test_unauthorized_user_rejected(self)` (method)
- L355 `test_invalid_choice_token(self)` (method)
- L391 `TestBaseAdapterClarifyFallback` (class) — Adapters without button overrides should render numbered text.
- L395 `test_numbered_text_fallback(self)` (method)
- L432 `test_open_ended_fallback_renders_question_only(self)` (method)
