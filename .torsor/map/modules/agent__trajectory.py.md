---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# agent/trajectory.py

Symbols in `agent/trajectory.py`.

- L16 `convert_scratchpad_to_think(content: str)` (function) — Convert <REASONING_SCRATCHPAD> tags to <think> tags.
- L23 `has_incomplete_scratchpad(content: str)` (function) — Check if content has an opening <REASONING_SCRATCHPAD> without a closing tag.
- L30 `save_trajectory(trajectory: List[Dict[str, Any]], model: str, completed: bool, filename: str=None)` (function) — Append a trajectory entry to a JSONL file.
