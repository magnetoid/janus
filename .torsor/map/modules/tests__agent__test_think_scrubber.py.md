---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/agent/test_think_scrubber.py

Symbols in `tests/agent/test_think_scrubber.py`.

- L17 `_drive(scrubber: StreamingThinkScrubber, deltas: list[str])` (function) — Feed a sequence of deltas and return the concatenated visible output.
- L24 `TestClosedPairs` (class) — Closed <tag>...</tag> pairs are always stripped, regardless of boundary.
- L27 `test_closed_pair_single_delta(self)` (method)
- L31 `test_closed_pair_surrounded_by_content(self)` (method)
- L39 `test_all_tag_variants(self, tag: str)` (method)
- L44 `test_case_insensitive_pair(self)` (method)
- L49 `TestUnterminatedOpen` (class) — Unterminated open tag discards all subsequent content to end of stream.
- L52 `test_open_at_stream_start(self)` (method)
- L56 `test_open_after_newline(self)` (method)
- L61 `test_open_after_newline_then_whitespace(self)` (method)
- L65 `test_prose_mentioning_tag_not_stripped(self)` (method) — Mid-line '<think>' in prose is preserved (no boundary).
- L72 `TestOrphanClose` (class) — Orphan close tags (no prior open) are stripped without boundary check.
- L75 `test_orphan_close_alone(self)` (method)
- L79 `test_orphan_close_with_trailing_space_consumed(self)` (method) — Matches _strip_think_blocks case 3 \s* behaviour.
- L84 `test_multiple_orphan_closes(self)` (method)
- L89 `TestPartialTagsAcrossDeltas` (class) — Partial tags at delta boundaries must be held back, not emitted raw.
- L92 `test_split_open_tag_held_back(self)` (method) — '<' arrives alone, 'think>' completes it on next delta.
- L101 `test_split_open_tag_not_at_boundary(self)` (method) — Mid-line split '<' + 'think>X</think>' is a closed pair.
- L112 `test_split_close_tag_held_back(self)` (method) — Close tag split across deltas still closes the block.
- L120 `test_split_close_tag_deep(self)` (method) — Close tag can be split anywhere.
- L129 `TestTheMiniMaxScenario` (class) — The exact pattern run_agent per-delta regex strip breaks.
- L132 `test_minimax_split_open(self)` (method) — delta1='<think>', delta2='Let me check', delta3='</think>done'.
- L138 `test_minimax_split_open_with_trailing_content(self)` (method) — Reasoning then closes and hands off to final content.
- L152 `test_minimax_unterminated_reasoning_at_end(self)` (method) — Unclosed reasoning at stream end is dropped entirely.
- L159 `TestResetAndReentry` (class)
- L160 `test_reset_clears_in_block_state(self)` (method)
- L169 `test_reset_clears_buffered_partial_tag(self)` (method)
- L178 `TestFlushBehaviour` (class)
- L179 `test_flush_drops_unterminated_block(self)` (method)
- L184 `test_flush_emits_innocent_partial_tag_tail(self)` (method) — If held-back tail turned out not to be a real tag, emit it.
- L191 `test_flush_on_empty_scrubber(self)` (method)
- L196 `TestRealisticStreaming` (class) — Character-by-character streaming must work as well as larger chunks.
- L199 `test_char_by_char_closed_pair(self)` (method)
- L204 `test_char_by_char_orphan_close(self)` (method)
- L209 `test_reasoning_then_real_response_first_word_preserved(self)` (method) — Regression: the first word of the final response must NOT be eaten.
- L225 `test_no_tag_passthrough_is_identical(self)` (method) — Streams without any reasoning tags pass through byte-for-byte.
