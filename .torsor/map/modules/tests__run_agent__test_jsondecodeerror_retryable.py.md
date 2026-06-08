---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/run_agent/test_jsondecodeerror_retryable.py

Symbols in `tests/run_agent/test_jsondecodeerror_retryable.py`.

- L24 `_mirror_agent_predicate(err: BaseException)` (function) — Exact shape of run_agent.py's is_local_validation_error check.
- L48 `TestJSONDecodeErrorIsRetryable` (class)
- L50 `test_json_decode_error_is_not_local_validation(self)` (method) — Provider returning malformed JSON surfaces as JSONDecodeError —
- L63 `test_unicode_encode_error_is_not_local_validation(self)` (method) — Existing carve-out — surrogate sanitization handles this separately.
- L72 `test_bare_value_error_is_local_validation(self)` (method) — Programming bugs that raise bare ValueError must still be
- L77 `test_bare_type_error_is_local_validation(self)` (method)
- L81 `TestAgentLoopSourceStillHasCarveOut` (class) — Belt-and-suspenders: the production source must actually include
- L86 `test_run_agent_excludes_jsondecodeerror_from_local_validation(self)` (method)
- L107 `TestNoneTypeNotIterableIsRetryable` (class) — Regression for #33136 / closes lingering Telegram "Non-retryable error (HTTP None)".
- L118 `test_nonetype_not_iterable_is_retryable(self)` (method)
- L126 `test_nonetype_not_iterable_uppercase_variants_still_retryable(self)` (method)
- L138 `test_unrelated_type_error_remains_local_validation(self)` (method) — TypeError without the NoneType-not-iterable pattern still aborts (programming bug).
- L144 `TestAgentLoopSourceHasNoneTypeCarveOut` (class) — Belt-and-suspenders: the production source must include the carve-out.
- L147 `test_conversation_loop_excludes_nonetype_not_iterable_from_local_validation(self)` (method)
