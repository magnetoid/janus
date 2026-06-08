---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# hermes_cli/partial_compress.py

Symbols in `hermes_cli/partial_compress.py`.

- L55 `parse_partial_compress_args(raw_args: str)` (function) — Parse the argument string after ``/compress``.
- L111 `_coerce_keep(value: str)` (function) — Parse a keep-count token, clamping to [1, MAX_KEEP_LAST].
- L124 `split_history_for_partial_compress(history: List[Dict[str, Any]], keep_last: int)` (function) — Split ``history`` into ``(head, tail)`` for partial compression.
- L180 `rejoin_compressed_head_and_tail(compressed_head: List[Dict[str, Any]], tail: List[Dict[str, Any]])` (function) — Concatenate a compressed head with the verbatim tail, defending
