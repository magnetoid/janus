---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/run_agent/test_1630_context_overflow_loop.py

Symbols in `tests/run_agent/test_1630_context_overflow_loop.py`.

- L19 `TestGeneric400Heuristic` (class) — The agent should treat a generic 400 with a large session as a
- L23 `_make_agent(self)` (method) — Create a minimal AIAgent for testing error handling.
- L45 `test_generic_400_with_small_session_is_client_error(self)` (method) — A generic 400 with a small session should still be treated
- L69 `test_generic_400_with_large_token_count_triggers_heuristic(self)` (method) — A generic 400 with high token count should be treated as
- L90 `test_generic_400_with_many_messages_triggers_heuristic(self)` (method) — A generic 400 with >80 messages should trigger the heuristic
- L104 `test_specific_error_message_bypasses_heuristic(self)` (method) — A 400 with a specific, long error message should NOT trigger
- L115 `test_descriptive_context_error_caught_by_phrases(self)` (method) — Descriptive context-length errors should still be caught by
- L133 `TestGatewaySkipsPersistenceOnFailure` (class) — When the agent returns failed=True with no final_response,
- L137 `test_agent_failed_early_detected(self)` (method) — The agent_failed_early flag is True when failed=True,
- L149 `test_agent_failed_with_error_response_still_detected(self)` (method) — When _run_agent_blocking converts an error to final_response,
- L162 `test_successful_agent_not_failed_early(self)` (method) — A successful agent result should not trigger skip.
- L172 `TestCompressionExhaustedFlag` (class) — When compression is exhausted, the agent should set both
- L177 `test_compression_exhausted_returns_carry_flag(self)` (method) — Simulate the return dict from a compression-exhausted agent.
- L191 `test_normal_failure_not_compression_exhausted(self)` (method) — Non-compression failures should not have compression_exhausted.
- L207 `TestContextOverflowErrorMessages` (class) — The gateway should produce helpful error messages when the failure
- L211 `test_detects_context_keywords(self)` (method) — Error messages containing context-related keywords should be
- L228 `test_detects_generic_400_with_large_history(self)` (method) — A generic 400 error code in the string with a large history
- L243 `test_unrelated_error_not_flagged(self)` (method) — Unrelated errors should not be flagged as context failures.
- L262 `TestAgentSkipsPersistenceForLargeFailedSessions` (class) — When a 400 error occurs and the session is large, the agent
- L266 `test_large_session_400_skips_persistence(self)` (method) — Status 400 + high token count should skip persistence.
- L275 `test_small_session_400_persists_normally(self)` (method) — Status 400 + small session should still persist.
- L284 `test_non_400_error_persists_normally(self)` (method) — Non-400 errors should always persist normally.
