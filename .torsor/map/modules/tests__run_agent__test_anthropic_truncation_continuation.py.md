---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/run_agent/test_anthropic_truncation_continuation.py

Symbols in `tests/run_agent/test_anthropic_truncation_continuation.py`.

- L23 `_make_anthropic_text_block(text: str)` (function)
- L27 `_make_anthropic_tool_use_block(name: str='my_tool')` (function)
- L36 `_make_anthropic_response(blocks, stop_reason: str='max_tokens')` (function)
- L49 `TestTruncatedAnthropicResponseNormalization` (class) — AnthropicTransport.normalize_response() gives us the shape _build_assistant_message expects.
- L52 `test_text_only_truncation_produces_text_content_no_tool_calls(self)` (method) — Pure-text Anthropic truncation → continuation path should fire.
- L72 `test_truncated_tool_call_produces_tool_calls(self)` (method) — Tool-use truncation → tool-call retry path should fire.
- L90 `test_empty_content_does_not_crash(self)` (method) — Empty response.content — defensive: treat as a truncation with no text.
- L102 `TestContinuationLogicBranching` (class) — Symbolic check that the api_mode gate now includes anthropic_messages.
- L106 `test_all_three_api_modes_hit_continuation_branch(self, api_mode)` (method)
- L111 `test_codex_responses_still_excluded(self)` (method)
