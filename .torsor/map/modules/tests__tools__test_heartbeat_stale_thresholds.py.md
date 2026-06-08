---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/tools/test_heartbeat_stale_thresholds.py

Symbols in `tests/tools/test_heartbeat_stale_thresholds.py`.

- L5 `TestHeartbeatStaleThresholds` (class) — Verify the heartbeat stale threshold constants are correct.
- L8 `test_idle_cycles_value(self)` (method) — IDLE stale cycles should be 15 (15 * 30s = 450s).
- L13 `test_in_tool_cycles_value(self)` (method) — IN_TOOL stale cycles should be 40 (40 * 30s = 1200s).
- L18 `test_idle_timeout_seconds(self)` (method) — Effective idle stale timeout: 15 * 30 = 450s (> typical LLM response time).
- L25 `test_in_tool_timeout_seconds(self)` (method) — Effective in-tool stale timeout: 40 * 30 = 1200s (= 20 minutes).
- L31 `test_interval_unchanged(self)` (method) — Heartbeat interval should remain 30s.
