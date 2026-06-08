---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/run_agent/test_primary_runtime_restore.py

Symbols in `tests/run_agent/test_primary_runtime_restore.py`.

- L19 `_make_tool_defs(*names: str)` (function)
- L33 `_make_agent(fallback_model=None, provider='custom', base_url='https://my-llm.example.com/v1')` (function) — Create a minimal AIAgent with optional fallback config.
- L53 `_mock_resolve(base_url='https://openrouter.ai/api/v1', api_key='fallback-key-1234')` (function) — Helper to create a mock client for resolve_provider_client.
- L65 `TestPrimaryRuntimeSnapshot` (class)
- L66 `test_snapshot_created_at_init(self)` (method)
- L77 `test_snapshot_includes_compressor_state(self)` (method)
- L86 `test_snapshot_includes_anthropic_state_when_applicable(self)` (method) — Anthropic-mode agents should snapshot Anthropic-specific state.
- L108 `test_snapshot_omits_anthropic_for_openai_mode(self)` (method)
- L118 `TestRestorePrimaryRuntime` (class)
- L119 `test_noop_when_not_fallback(self)` (method)
- L124 `test_restores_model_and_provider(self)` (method)
- L149 `test_resets_fallback_index(self)` (method) — After restore, the full fallback chain should be available again.
- L169 `test_restores_compressor_state(self)` (method)
- L191 `test_restores_prompt_caching_flag(self)` (method)
- L204 `test_restore_survives_exception(self)` (method) — If client rebuild fails, the method returns False gracefully.
- L219 `_make_transport_error(error_type='ReadTimeout')` (function) — Create an exception whose type().__name__ matches the given name.
- L225 `TestTryRecoverPrimaryTransport` (class)
- L227 `test_recovers_on_read_timeout(self)` (method)
- L239 `test_recovers_on_connect_timeout(self)` (method)
- L251 `test_recovers_on_pool_timeout(self)` (method)
- L263 `test_recovers_on_openai_api_connection_error(self)` (method)
- L275 `test_recovers_on_openai_api_timeout_error(self)` (method)
- L287 `test_skipped_when_already_on_fallback(self)` (method)
- L297 `test_skipped_for_non_transport_error(self)` (method) — Non-transport errors (ValueError, APIError, etc.) skip recovery.
- L307 `test_skipped_for_openrouter(self)` (method)
- L316 `test_skipped_for_nous_provider(self)` (method)
- L325 `test_allowed_for_anthropic_direct(self)` (method) — Direct Anthropic endpoint should get recovery.
- L339 `test_allowed_for_ollama(self)` (method)
- L351 `test_wait_time_scales_with_retry_count(self)` (method)
- L363 `test_wait_time_capped_at_8(self)` (method)
- L375 `test_closes_existing_client_before_rebuild(self)` (method)
- L390 `test_survives_rebuild_failure(self)` (method) — If client rebuild fails, returns False gracefully.
- L408 `TestRestoreInRunConversation` (class) — Verify the hook in run_conversation() calls _restore_primary_runtime.
- L411 `test_restore_called_at_turn_start(self)` (method)
- L422 `test_full_cycle_fallback_then_restore(self)` (method) — Simulate: turn 1 activates fallback, turn 2 restores primary.
- L453 `TestRateLimitCooldown` (class) — Verify _restore_primary_runtime() respects the 60s rate-limit cooldown.
- L456 `test_restore_blocked_during_cooldown(self)` (method) — While _rate_limited_until is in the future, restore returns False.
- L474 `test_restore_allowed_after_cooldown_expires(self)` (method) — Once the cooldown window passes, restore proceeds normally.
- L494 `test_cooldown_set_on_rate_limit_reason(self)` (method) — _try_activate_fallback with rate_limit reason sets _rate_limited_until.
- L508 `test_cooldown_not_set_when_already_on_fallback(self)` (method) — Chain-switching while already on fallback must not reset cooldown.
