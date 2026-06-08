---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/run_agent/test_413_compression.py

Symbols in `tests/run_agent/test_413_compression.py`.

- L29 `_no_compression_sleep(monkeypatch)` (function) — Short-circuit the 2s time.sleep between compression retries.
- L44 `_make_tool_defs(*names: str)` (function)
- L58 `_mock_response(content='Hello', finish_reason='stop', tool_calls=None, usage=None)` (function)
- L71 `_make_413_error(*, use_status_code=True, message='Request entity too large')` (function) — Create an exception that mimics a 413 HTTP error.
- L80 `agent()` (function)
- L111 `test_current_user_turn_is_persisted_before_provider_call(agent)` (function) — The inbound user turn is flushed before provider/tool work can crash.
- L144 `TestHTTP413Compression` (class) — 413 errors should trigger compression, not abort as generic 4xx.
- L147 `test_413_triggers_compression(self, agent)` (method) — A 413 error should call _compress_context and retry, not abort.
- L177 `test_413_not_treated_as_generic_4xx(self, agent)` (method) — 413 must NOT hit the generic 4xx abort path; it should attempt compression.
- L204 `test_413_error_message_detection(self, agent)` (method) — 413 detected via error message string (no status_code attr).
- L230 `test_413_clears_conversation_history_on_persist(self, agent)` (method) — After 413-triggered compression, _persist_session must receive None history.
- L270 `test_context_overflow_clears_conversation_history_on_persist(self, agent)` (method) — After context-overflow compression, _persist_session must receive None history.
- L304 `test_400_context_length_triggers_compression(self, agent)` (method) — A 400 with 'maximum context length' should trigger compression, not abort as generic 4xx.
- L343 `test_400_reduce_length_triggers_compression(self, agent)` (method) — A 400 with 'reduce the length' should trigger compression.
- L372 `test_context_length_retry_rebuilds_request_after_compression(self, agent)` (method) — Retry must send the compressed transcript, not the stale oversized payload.
- L421 `test_413_cannot_compress_further(self, agent)` (method) — When compression can't reduce messages, return partial result.
- L444 `TestPreflightCompression` (class) — Preflight compression should compress history before the first API call.
- L447 `test_compress_context_emits_lifecycle_status_before_work(self, agent)` (method) — Direct context compression should tell gateway users why the turn paused.
- L480 `test_preflight_compresses_oversized_history(self, agent)` (method) — When loaded history exceeds the model's context threshold, compress before API call.
- L532 `test_preflight_defers_when_recent_real_usage_fit(self, agent)` (method) — A noisy rough estimate should not re-compact a recently fitting request.
- L572 `test_preflight_compresses_when_rough_growth_after_fit_is_large(self, agent)` (method) — Large rough growth after a fitting request still triggers preflight.
- L622 `test_no_preflight_when_under_threshold(self, agent)` (method) — When history fits within context, no preflight compression needed.
- L648 `test_no_preflight_when_compression_disabled(self, agent)` (method) — Preflight should not run when compression is disabled.
- L672 `test_preflight_respects_anti_thrash(self, agent)` (method) — Preflight must call ``should_compress()`` so anti-thrash applies.
- L706 `test_preflight_seeds_display_tokens_when_compression_aborts(self, agent)` (method) — Display must reflect the real context size even when compression no-ops.
- L746 `test_preflight_seed_only_revises_upward(self, agent)` (method) — A larger tracked value must not be clobbered by a smaller estimate.
- L775 `TestToolResultPreflightCompression` (class) — Compression should trigger when tool results push context past the threshold.
- L778 `test_large_tool_results_trigger_compression(self, agent)` (method) — When tool results push estimated tokens past threshold, compress before next call.
- L816 `test_anthropic_prompt_too_long_safety_net(self, agent)` (method) — Anthropic 'prompt is too long' error triggers compression as safety net.
- L849 `TestOverflowWithCompactionDisabled` (class) — When ``compression.enabled`` is False, NO automatic compaction may
- L861 `_prefill()` (method)
- L867 `test_413_does_not_compress_when_disabled(self, agent)` (method) — 413 must NOT call _compress_context when compaction is disabled.
- L888 `test_context_overflow_does_not_compress_when_disabled(self, agent)` (method) — 400 'prompt is too long' must NOT compress when compaction disabled.
- L910 `test_413_still_compresses_when_enabled(self, agent)` (method) — Control: with compaction enabled, 413 still triggers compression.
