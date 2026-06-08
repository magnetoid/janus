---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:44'
updated: '2026-06-08T00:38:44'
---

# tests/tui_gateway/test_wait_for_mcp_discovery.py

Symbols in `tests/tui_gateway/test_wait_for_mcp_discovery.py`.

- L16 `_restore_thread_slot(saved)` (function)
- L20 `test_no_thread_is_noop()` (function) — When no discovery thread was started (the common no-MCP case), the
- L33 `test_already_finished_thread_is_noop()` (function) — A thread that has already finished is not joined-on (dead thread).
- L48 `test_fast_thread_is_joined()` (function) — A reachable-but-still-connecting (fast) server lands before the agent
- L62 `test_hung_thread_is_bounded_by_timeout()` (function) — A slow/dead server must NOT re-introduce the startup hang — the join is
