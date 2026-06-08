---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_stream_consumer_fresh_final.py

Symbols in `tests/gateway/test_stream_consumer_fresh_final.py`.

- L22 `_make_adapter(*, supports_delete: bool=True)` (function) — Build a minimal MagicMock adapter wired for send/edit/delete.
- L42 `TestFreshFinalForLongLivedPreviews` (class) — openclaw#72038 port — send fresh final when preview is old.
- L46 `test_disabled_by_default_still_edits_in_place(self)` (method) — ``fresh_final_after_seconds=0`` preserves the legacy edit path.
- L63 `test_short_lived_preview_edits_in_place(self)` (method) — Finalizing a preview younger than the threshold → normal edit.
- L78 `test_long_lived_preview_sends_fresh_final(self)` (method) — Finalizing a preview older than the threshold → fresh send.
- L104 `test_fresh_final_without_delete_support_is_best_effort(self)` (method) — Adapter lacking ``delete_message`` still gets the fresh send.
- L125 `test_fresh_final_fallback_to_edit_on_send_failure(self)` (method) — If the fresh send fails, fall back to the normal edit path.
- L146 `test_only_finalize_triggers_fresh_final(self)` (method) — Intermediate edits (``finalize=False``) never switch to fresh send.
- L161 `test_no_edit_sentinel_is_not_affected(self)` (method) — Platforms with the ``__no_edit__`` sentinel never go fresh-final.
- L177 `TestSegmentBreakDoesNotMarkFinalSent` (class) — Regression for #29346 — silent response loss after tool calls.
- L194 `_delivered_texts(adapter)` (method) — Every text the adapter actually put on screen (sends + edits).
- L201 `test_preamble_fresh_final_at_tool_boundary_does_not_mark_final(self)` (method) — Real-aging reproduction (exercises the actual _should_send_fresh_final
- L231 `test_final_answer_after_preamble_is_delivered_exactly_once(self)` (method) — P0 user-visible contract: when the real final answer DOES stream in
- L265 `test_genuine_final_answer_without_tools_marks_delivered(self)` (method) — P1 happy path: a single answer streamed straight to completion (no
- L287 `test_no_edit_adapter_delivers_final_after_preamble(self)` (method) — No-edit adapters (Signal/SMS/webhook → __no_edit__) accumulate and
- L316 `test_multi_tool_call_turn_delivers_final_once(self)` (method) — Two tool boundaries before the final answer: flags stay clear across
- L350 `TestStreamConsumerConfigFreshFinalField` (class) — The dataclass field must exist and default to 0 (disabled).
- L353 `test_default_is_disabled(self)` (method)
- L357 `test_field_is_configurable(self)` (method)
- L362 `TestStreamingConfigFreshFinalField` (class) — The gateway-level StreamingConfig carries the setting.
- L365 `test_default_enables_with_60s(self)` (method)
- L370 `test_from_dict_uses_default_when_missing(self)` (method)
- L375 `test_from_dict_respects_explicit_zero(self)` (method)
- L383 `test_to_dict_round_trip(self)` (method)
- L390 `TestTelegramAdapterDeleteMessage` (class) — Contract: Telegram adapter implements ``delete_message``.
- L393 `test_delete_message_method_exists(self)` (method)
- L405 `test_base_adapter_default_returns_false(self)` (method) — BasePlatformAdapter.delete_message default = no-op returning False.
