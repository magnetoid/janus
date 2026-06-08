---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# agent/think_scrubber.py

Symbols in `agent/think_scrubber.py`.

- L64 `StreamingThinkScrubber` (class) — Stateful scrubber for streaming reasoning/thinking blocks.
- L95 `__init__(self)` (method)
- L100 `reset(self)` (method) — Reset all state.  Call at the top of every new turn.
- L106 `feed(self, text: str)` (method) — Feed one delta; return the scrubbed visible portion.
- L204 `flush(self)` (method) — End-of-stream flush.
- L228 `_find_first_tag(buf: str, tags: Tuple[str, ...])` (method) — Return (earliest_index, tag_length) over *tags*, or (-1, 0).
- L245 `_find_earliest_closed_pair(self, buf: str)` (method) — Return (start_idx, end_idx) of the earliest closed pair, else None.
- L273 `_find_open_at_boundary(self, buf: str, already_emitted: list[str])` (method) — Return the earliest block-boundary open-tag (idx, len).
- L298 `_is_block_boundary(self, buf: str, idx: int, already_emitted: list[str])` (method) — True iff position *idx* in *buf* is a block boundary.
- L334 `_max_partial_suffix(cls, buf: str, tags: Tuple[str, ...])` (method) — Return the longest buf-suffix that is a prefix of any tag.
- L356 `_strip_orphan_close_tags(cls, text: str)` (method) — Remove any close tags from *text* (orphan-close handling).
