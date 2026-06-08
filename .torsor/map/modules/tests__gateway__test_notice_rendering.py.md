---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_notice_rendering.py

Symbols in `tests/gateway/test_notice_rendering.py`.

- L11 `TestRenderNoticeLine` (class) — render_notice_line emits the notice text VERBATIM.
- L20 `test_returns_text_verbatim_with_its_baked_glyph(self)` (method)
- L36 `test_does_not_prepend_a_second_glyph(self)` (method)
- L43 `test_text_is_stripped(self)` (method)
- L46 `test_empty_text_returns_empty_string(self)` (method)
- L51 `test_malformed_notice_does_not_raise(self)` (method)
- L59 `test_real_policy_notices_render_without_doubling()` (function) — End-to-end regression: every notice evaluate_credits_notices emits already
- L103 `_make_source(platform_value='telegram', chat_id='555', user_id='u1')` (function)
- L113 `_make_runner_with_adapter(source, adapter)` (function)
- L124 `TestDeliverNoticeLine` (class) — The seam between render_notice_line and the platform adapter.
- L133 `test_public_delivery_sends_rendered_line(self)` (method)
- L151 `test_private_delivery_prefers_private_notice(self)` (method)
- L168 `test_no_adapter_is_a_noop(self)` (method)
