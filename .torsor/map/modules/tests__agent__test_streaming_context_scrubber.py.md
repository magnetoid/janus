---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/agent/test_streaming_context_scrubber.py

Symbols in `tests/agent/test_streaming_context_scrubber.py`.

- L12 `TestStreamingContextScrubberBasics` (class)
- L13 `test_empty_input_returns_empty(self)` (method)
- L18 `test_plain_text_passes_through(self)` (method)
- L23 `test_complete_block_in_single_delta(self)` (method) — Regression: the one-shot test case from #13672 must still work.
- L36 `test_open_and_close_in_separate_deltas_strips_payload(self)` (method) — The real streaming case: tag pair split across deltas.
- L49 `test_realistic_fragmented_chunks_strip_memory_payload(self)` (method) — Exact leak scenario from the reviewer's comment — 4 realistic chunks.
- L71 `test_open_tag_split_across_two_deltas(self)` (method) — The open tag itself arriving in two fragments.
- L82 `test_open_tag_waits_for_newline_confirmation_across_deltas(self)` (method) — A boundary tag is only a leaked block when the next char is a newline.
- L93 `test_close_tag_split_across_two_deltas(self)` (method) — The close tag arriving in two fragments.
- L105 `TestStreamingContextScrubberPartialTagFalsePositives` (class)
- L106 `test_partial_open_tag_tail_emitted_on_flush(self)` (method) — Bare '<mem' at end of stream is not really a memory-context tag.
- L112 `test_partial_tag_released_when_disambiguated(self)` (method) — A held-back partial tag that turns out to be prose gets released.
- L119 `test_inline_memory_context_tag_mention_is_not_scrubbed(self)` (method) — A prose mention of the fence tag must not swallow the answer.
- L130 `test_mid_sentence_memory_context_mention_is_not_scrubbed(self)` (method) — Only block-like memory-context spans are treated as leaked context.
- L136 `test_line_start_memory_context_mention_without_close_is_not_scrubbed(self)` (method) — A plain-text line that starts with the tag name must be preserved.
- L147 `TestStreamingContextScrubberUnterminatedSpan` (class)
- L148 `test_unterminated_span_drops_payload(self)` (method) — Provider drops close tag — better to lose output than to leak.
- L155 `test_reset_clears_hung_span(self)` (method) — Cross-turn scrubber reset drops a hung span so next turn is clean.
- L164 `TestStreamingContextScrubberCaseInsensitivity` (class)
- L165 `test_uppercase_tags_still_scrubbed(self)` (method)
- L176 `TestSanitizeContextUnchanged` (class) — Smoke test that the one-shot sanitize_context still works for whole strings.
- L179 `test_whole_block_still_sanitized(self)` (method)
- L191 `TestStreamingContextScrubberCrossTurn` (class) — A scrubber instance is reused across turns (per agent).  reset() must
- L196 `test_reset_clears_held_partial_tag(self)` (method)
- L210 `test_reset_clears_in_span_state(self)` (method)
- L220 `TestBuildMemoryContextBlockWarnsOnViolation` (class) — Providers must return raw context — not pre-wrapped.  When they do,
- L224 `test_provider_emitting_wrapper_warns(self, caplog)` (method)
- L241 `test_clean_provider_output_does_not_warn(self, caplog)` (method)
