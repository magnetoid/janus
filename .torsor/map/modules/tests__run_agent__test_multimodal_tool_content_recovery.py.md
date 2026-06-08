---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/run_agent/test_multimodal_tool_content_recovery.py

Symbols in `tests/run_agent/test_multimodal_tool_content_recovery.py`.

- L32 `_FakeApiError` (class) — Stand-in for an openai.BadRequestError with status_code + body.
- L35 `__init__(self, status_code: int, message: str, body: dict | None=None)` (method)
- L42 `_make_agent(provider: str='xiaomi', model: str='mimo-v2.5')` (function) — Build a bare AIAgent for method-level testing, no provider setup.
- L54 `TestStripImagePartsHelper` (class)
- L55 `test_no_messages_returns_false(self)` (method)
- L60 `test_no_tool_messages_returns_false(self)` (method)
- L68 `test_tool_message_with_string_content_unchanged(self)` (method)
- L76 `test_tool_message_list_without_image_unchanged(self)` (method) — List content with only text parts is left alone — caller surfaces
- L87 `test_tool_message_list_with_image_downgrades(self)` (method)
- L102 `test_tool_message_image_only_gets_placeholder(self)` (method) — If the list had nothing but image parts, leave a placeholder so
- L115 `test_records_provider_model_in_session_cache(self)` (method)
- L126 `test_only_tool_messages_get_downgraded(self)` (method) — User / assistant messages with list-type content are out of
- L148 `test_skips_recording_when_no_model_id(self)` (method) — Don't poison the cache with empty keys when provider/model is
- L165 `TestToolResultContentShortCircuit` (class) — Once the session has learned that (provider, model) rejects list
- L171 `_multimodal_result(self, png_b64: str='iVBORw0KGgoAAAA')` (method)
- L184 `test_returns_list_when_cache_empty_and_vision_supported(self, monkeypatch)` (method)
- L195 `test_returns_text_summary_when_model_in_cache(self, monkeypatch)` (method)
- L207 `test_cache_miss_on_different_model(self, monkeypatch)` (method) — Cache is per (provider, model). A cached entry for mimo-v2.5
- L219 `test_missing_cache_attribute_falls_through(self, monkeypatch)` (method) — Tests that build agents via ``object.__new__`` without calling
- L235 `TestRecoveryEndToEndClassification` (class) — Lock in that the patterns used by the recovery path classify to
- L241 `test_xiaomi_mimo_classifies(self)` (method)
- L253 `test_alibaba_variant_classifies(self)` (method)
