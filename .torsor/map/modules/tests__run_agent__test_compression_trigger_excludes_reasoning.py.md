---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/run_agent/test_compression_trigger_excludes_reasoning.py

Symbols in `tests/run_agent/test_compression_trigger_excludes_reasoning.py`.

- L11 `_make_agent_stub(prompt_tokens, completion_tokens, threshold_tokens)` (function) — Create a minimal stub that exercises the compression check path.
- L26 `TestCompressionTriggerExcludesReasoning` (class)
- L27 `test_high_reasoning_tokens_should_not_trigger_compression(self)` (method) — With the old bug, 40k prompt + 80k reasoning = 120k > 100k threshold.
- L40 `test_high_prompt_tokens_should_trigger_compression(self)` (method) — When prompt tokens genuinely exceed the threshold, compress.
- L52 `test_zero_prompt_tokens_falls_back(self)` (method) — When provider returns 0 prompt tokens, real_tokens is 0 (fallback path).
