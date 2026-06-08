---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/run_agent/test_percentage_clamp.py

Symbols in `tests/run_agent/test_percentage_clamp.py`.

- L10 `TestMemoryToolPercentClamp` (class) — tools/memory_tool.py — _success_response and _render_block pct
- L13 `test_over_limit_clamped_at_100(self)` (method) — Percentage should be capped at 100 even if current > limit.
- L21 `test_normal_percentage(self)` (method)
- L27 `test_zero_limit_returns_zero(self)` (method)
- L34 `TestCLIStatsPercentClamp` (class) — cli.py — /stats command percentage
- L37 `test_over_context_clamped_at_100(self)` (method) — Tokens exceeding context_length should show max 100%.
- L44 `test_normal_context(self)` (method)
- L50 `test_zero_context_length(self)` (method)
- L57 `TestGatewayStatsPercentClamp` (class) — gateway/run.py — _format_usage_stats percentage
- L60 `test_over_context_clamped_at_100(self)` (method)
- L66 `test_normal_context(self)` (method)
- L73 `TestSourceLinesAreClamped` (class) — Verify the actual source files have min(100, ...) applied.
- L77 `_read_file(rel_path: str)` (method)
- L83 `test_gateway_run_clamped(self)` (method)
- L90 `test_cli_clamped(self)` (method)
- L96 `test_memory_tool_clamped(self)` (method)
