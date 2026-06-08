---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/run_agent/test_notice_spine.py

Symbols in `tests/run_agent/test_notice_spine.py`.

- L24 `_bare_agent()` (function) — Build an AIAgent without running __init__ (no heavy init required).
- L36 `TestEmitNotice` (class)
- L37 `test_emit_notice_calls_callback_with_exact_notice(self)` (method)
- L52 `test_emit_notice_clear_calls_callback_with_exact_key(self)` (method)
- L59 `test_emit_notice_swallows_callback_exception(self)` (method)
- L69 `test_emit_notice_clear_swallows_callback_exception(self)` (method)
- L79 `test_emit_notice_no_op_when_callback_is_none(self)` (method)
- L85 `test_emit_notice_clear_no_op_when_callback_is_none(self)` (method)
- L95 `TestSignatureThreading` (class)
- L96 `test_agent_init_exposes_notice_callback(self)` (method)
- L100 `test_agent_init_exposes_notice_clear_callback(self)` (method)
- L104 `test_init_agent_exposes_notice_callback(self)` (method)
- L109 `test_init_agent_exposes_notice_clear_callback(self)` (method)
- L118 `TestAgentCbsNoticeBinding` (class) — Mirror test_status_callback_emits_kind_and_text from test_tui_gateway_server.py.
- L121 `test_notice_callback_emits_notification_show(self)` (method)
- L149 `test_notice_callback_payload_is_full_snake_case_dict(self)` (method) — All six snake_case fields must be present in the payload — no extras,
- L172 `test_notice_clear_callback_emits_notification_clear(self)` (method)
- L185 `test_notice_callback_event_type_is_notification_show(self)` (method)
- L195 `test_notice_clear_callback_event_type_is_notification_clear(self)` (method)
