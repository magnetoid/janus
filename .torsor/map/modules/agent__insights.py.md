---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# agent/insights.py

Symbols in `agent/insights.py`.

- L36 `_has_known_pricing(model_name: str, provider: str=None, base_url: str=None)` (function) — Check if a model has known pricing (vs unknown/custom endpoint).
- L41 `_estimate_cost(session_or_model: Dict[str, Any] | str, input_tokens: int=0, output_tokens: int=0, *, cache_read_tokens: int=0, cache_write_tokens: int=0, provider: str=None, base_url: str=None)` (function) — Estimate the USD cost for a session row or a model/token tuple.
- L80 `_format_duration(seconds: float)` (function) — Format seconds into a human-readable duration string.
- L85 `_bar_chart(values: List[int], max_width: int=20)` (function) — Create simple horizontal bar chart strings from values.
- L93 `InsightsEngine` (class) — Analyzes session history and produces usage insights.
- L101 `__init__(self, db)` (method) — Initialize with a SessionDB instance.
- L111 `generate(self, days: int=30, source: str=None)` (method) — Generate a complete insights report.
- L199 `_get_sessions(self, cutoff: float, source: str=None)` (method) — Fetch sessions within the time window.
- L207 `_get_tool_usage(self, cutoff: float, source: str=None)` (method) — Get tool call counts from messages.
- L299 `_get_skill_usage(self, cutoff: float, source: str=None)` (method) — Extract per-skill usage from assistant tool calls.
- L375 `_get_message_stats(self, cutoff: float, source: str=None)` (method) — Get aggregate message statistics.
- L411 `_compute_overview(self, sessions: List[Dict], message_stats: Dict)` (method) — Compute high-level overview statistics.
- L485 `_compute_model_breakdown(self, sessions: List[Dict])` (method) — Break down usage by model.
- L522 `_compute_platform_breakdown(self, sessions: List[Dict])` (method) — Break down usage by platform/source.
- L553 `_compute_tool_breakdown(self, tool_usage: List[Dict])` (method) — Process tool usage data into a ranked list with percentages.
- L566 `_compute_skill_breakdown(self, skill_usage: List[Dict])` (method) — Process per-skill usage into summary + ranked list.
- L606 `_compute_activity_patterns(self, sessions: List[Dict])` (method) — Analyze activity patterns by day of week and hour.
- L664 `_compute_top_sessions(self, sessions: List[Dict])` (method) — Find notable sessions (longest, most messages, most tokens).
- L726 `format_terminal(self, report: Dict)` (method) — Format the insights report for terminal display (CLI).
- L866 `format_gateway(self, report: Dict)` (method) — Format the insights report for gateway/messaging (shorter).
