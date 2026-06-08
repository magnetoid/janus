---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/run_agent/test_18028_content_policy_blocked.py

Symbols in `tests/run_agent/test_18028_content_policy_blocked.py`.

- L19 `TestContentPolicyBlockedClassification` (class) — Verify classify_api_error returns the right shape so downstream
- L24 `test_openai_codex_cybersecurity_no_status(self)` (method) — The reported #18028 case — SDK raises without a status code.
- L45 `TestContentPolicyTriggersClientErrorAbort` (class) — Mirror the ``is_client_error`` predicate in
- L53 `_mirror_is_client_error(self, *, classified_retryable: bool, classified_reason, classified_should_compress: bool=False, is_local_validation_error: bool=False, is_context_length_error: bool=False)` (method) — Exact shape of conversation_loop.py's is_client_error check.
- L84 `test_content_policy_blocked_triggers_abort(self)` (method) — Safety-filter block must reach is_client_error → fallback/abort.
- L101 `TestContentPolicyPatternsAreNarrow` (class) — Defensive guard: the safety-filter patterns must not collide with
- L108 `test_generic_400_format_error_not_misclassified(self)` (method)
- L120 `test_billing_402_not_misclassified(self)` (method)
- L132 `test_openrouter_account_policy_block_stays_distinct(self)` (method) — ``provider_policy_blocked`` (OpenRouter account-level data
