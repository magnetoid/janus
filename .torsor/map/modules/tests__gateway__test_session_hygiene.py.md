---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_session_hygiene.py

Symbols in `tests/gateway/test_session_hygiene.py`.

- L30 `_make_history(n_messages: int, content_size: int=100)` (function) — Build a fake transcript with n_messages user/assistant pairs.
- L40 `_make_large_history_tokens(target_tokens: int)` (function) — Build a history that estimates to roughly target_tokens tokens.
- L54 `HygieneCaptureAdapter` (class)
- L55 `__init__(self)` (method)
- L59 `connect(self)` (method)
- L62 `disconnect(self)` (method)
- L65 `send(self, chat_id, content, reply_to=None, metadata=None)` (method)
- L76 `get_chat_info(self, chat_id: str)` (method)
- L84 `TestSessionHygieneThresholds` (class) — Test that the threshold logic correctly identifies large sessions.
- L91 `test_small_session_below_thresholds(self)` (method) — A 10-message session should not trigger compression.
- L104 `test_large_token_count_triggers(self)` (method) — High token count should trigger compression when exceeding model threshold.
- L117 `test_under_threshold_no_trigger(self)` (method) — Session under threshold should not trigger, even with many messages.
- L134 `test_message_count_alone_does_not_trigger(self)` (method) — Message count alone should NOT trigger — only token count matters.
- L153 `test_threshold_scales_with_model(self)` (method) — Different models should have different compression thresholds.
- L173 `test_custom_threshold_percentage(self)` (method) — Custom threshold percentage from config should be respected.
- L189 `test_minimum_message_guard(self)` (method) — Sessions with fewer than 4 messages should never trigger.
- L197 `TestSessionHygieneWarnThreshold` (class) — Test the post-compression warning threshold (95% of context).
- L200 `test_warn_when_still_large(self)` (method) — If compressed result is still above 95% of context, should warn.
- L207 `test_no_warn_when_under(self)` (method) — If compressed result is under 95% of context, no warning.
- L218 `TestEstimatedTokenThreshold` (class) — Verify that hygiene thresholds are always below the model's context
- L229 `test_threshold_below_context_for_200k_model(self)` (method) — Hygiene threshold must always be below model context.
- L235 `test_threshold_below_context_for_128k_model(self)` (method)
- L240 `test_no_multiplier_means_same_threshold_for_estimated_and_actual(self)` (method) — Without the 1.4x, estimated and actual token paths use the same threshold.
- L248 `test_warn_threshold_below_context(self)` (method) — Warn threshold (95%) must be below context length.
- L254 `test_overestimate_fires_early_but_safely(self)` (method) — If rough estimate is 50% inflated, hygiene fires at ~57% actual usage.
- L273 `TestTokenEstimation` (class) — Verify rough token estimation works as expected for hygiene checks.
- L276 `test_empty_history(self)` (method)
- L279 `test_proportional_to_content(self)` (method)
- L284 `test_proportional_to_count(self)` (method)
- L289 `test_pathological_session_detected(self)` (method) — The reported pathological case: 648 messages, ~299K tokens.
- L302 `test_session_hygiene_messages_stay_in_originating_topic(monkeypatch, tmp_path)` (function)
- L399 `test_session_hygiene_warns_user_when_compression_aborts(monkeypatch, tmp_path)` (function) — When auxiliary compression's summary LLM call fails, the compressor
- L518 `test_session_hygiene_informs_user_when_aux_model_fails_but_recovers(monkeypatch, tmp_path)` (function) — When the user's configured ``auxiliary.compression.model`` errors out
- L642 `test_session_hygiene_honors_configurable_hard_message_limit(monkeypatch, tmp_path)` (function) — compression.hygiene_hard_message_limit overrides the 400-message default.
- L760 `test_session_hygiene_default_hard_message_limit_does_not_fire_at_12_messages(monkeypatch, tmp_path)` (function) — Sanity check for the companion test above: without config override,
