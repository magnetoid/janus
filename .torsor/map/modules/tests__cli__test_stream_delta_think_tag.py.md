---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/cli/test_stream_delta_think_tag.py

Symbols in `tests/cli/test_stream_delta_think_tag.py`.

- L8 `_make_cli_stub()` (function) — Create a minimal HermesCLI-like object with stream state.
- L42 `TestThinkTagInProse` (class) — <think> mentioned in prose should NOT trigger reasoning suppression.
- L45 `test_think_tag_mid_sentence(self)` (method) — '(/think not producing <think> tags)' should pass through.
- L62 `test_think_tag_after_text_on_same_line(self)` (method) — 'some text <think>' should NOT trigger reasoning.
- L70 `test_think_tag_in_backticks(self)` (method) — '`<think>`' should NOT trigger reasoning.
- L77 `TestRealReasoningBlock` (class) — Real <think> tags at block boundaries should still be caught.
- L80 `test_think_at_start_of_stream(self)` (method) — '<think>reasoning</think>answer' should suppress reasoning.
- L93 `test_think_after_newline(self)` (method) — 'text\n<think>' should trigger reasoning block.
- L101 `test_think_after_newline_with_whitespace(self)` (method) — 'text\n  <think>' should trigger reasoning block.
- L107 `test_think_with_only_whitespace_before(self)` (method) — '   <think>' (whitespace only prefix) should trigger.
- L114 `TestFlushRecovery` (class) — _flush_stream should recover content from false-positive reasoning blocks.
- L117 `test_flush_recovers_buffered_content(self)` (method) — If somehow in reasoning block at flush, content is recovered.
