---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/run_agent/test_long_context_tier_429.py

Symbols in `tests/run_agent/test_long_context_tier_429.py`.

- L19 `TestLongContextTierDetection` (class) — Verify the detection heuristic matches the Anthropic error.
- L23 `_is_long_context_tier_error(status_code, error_msg, model='claude-sonnet-4.6')` (method)
- L32 `test_matches_anthropic_error(self)` (method)
- L38 `test_matches_lowercase(self)` (method)
- L44 `test_matches_openrouter_model_id(self)` (method)
- L51 `test_matches_nous_model_id(self)` (method)
- L58 `test_rejects_opus(self)` (method) — Opus 1M is general access — should NOT trigger reduction.
- L66 `test_rejects_opus_openrouter(self)` (method)
- L73 `test_rejects_normal_429(self)` (method)
- L79 `test_rejects_wrong_status(self)` (method)
- L85 `test_rejects_partial_match(self)` (method) — Both 'extra usage' AND 'long context' must be present.
- L100 `TestContextReduction` (class) — When the long-context tier error fires, context_length should
- L104 `_make_compressor(self, context_length=1000000, threshold_percent=0.5)` (method)
- L114 `test_reduces_1m_to_200k(self)` (method)
- L130 `test_no_reduction_when_already_200k(self)` (method)
- L140 `test_no_reduction_when_below_200k(self)` (method)
- L156 `TestAgentErrorPath` (class) — Verify the long-context 429 doesn't hit the generic rate-limit
- L160 `test_long_context_429_not_treated_as_rate_limit(self)` (method) — The error should be intercepted before the generic
- L175 `test_opus_429_falls_through_to_rate_limit(self)` (method) — Opus should NOT match — falls through to generic rate-limit.
- L189 `test_normal_429_still_treated_as_rate_limit(self)` (method) — A normal 429 should NOT match the long-context check.
