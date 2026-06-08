---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/run_agent/test_31273_402_not_retried.py

Symbols in `tests/run_agent/test_31273_402_not_retried.py`.

- L27 `TestBillingTriggersClientErrorAbort` (class) — Mirror the ``is_client_error`` predicate shape used in
- L33 `_mirror_is_client_error(self, *, classified_retryable: bool, classified_reason, classified_should_compress: bool=False, is_local_validation_error: bool=False, is_context_length_error: bool=False)` (method) — Exact shape of conversation_loop.py's is_client_error check.
- L66 `test_billing_now_aborts_the_loop(self)` (method) — 402 with no fallback / no pool entry → ``is_client_error`` True.
- L80 `test_rate_limit_still_retries(self)` (method) — Sanity check: rate_limit must still fall through to backoff retry.
- L92 `test_local_validation_error_still_aborts(self)` (method) — Sanity check: bare ValueError/TypeError still abort.
- L102 `test_context_overflow_still_falls_through_to_compression(self)` (method) — Sanity check: context-overflow must NOT be classified as
- L114 `TestSourceStillHasBillingExclusionRemoved` (class) — Belt-and-suspenders: the production source must actually omit
- L120 `test_conversation_loop_omits_billing_from_client_error_exclusion(self)` (method)
