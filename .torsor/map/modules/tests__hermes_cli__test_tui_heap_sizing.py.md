---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/hermes_cli/test_tui_heap_sizing.py

Symbols in `tests/hermes_cli/test_tui_heap_sizing.py`.

- L21 `_fake_open(files: dict)` (function) — Return an open() shim serving cgroup paths from ``files`` (path->str).
- L36 `_read(files: dict)` (function)
- L41 `TestReadCgroupMemoryLimit` (class)
- L42 `test_v2_max_is_unlimited(self)` (method)
- L45 `test_v2_numeric_limit(self)` (method)
- L48 `test_v1_unlimited_sentinel_is_none(self)` (method)
- L52 `test_v1_numeric_limit_when_no_v2(self)` (method)
- L55 `test_no_files_present(self)` (method)
- L58 `test_empty_v2_falls_through_to_v1(self)` (method)
- L62 `test_v2_wins_over_v1(self)` (method)
- L65 `test_zero_is_skipped(self)` (method)
- L68 `test_petabyte_plus_treated_as_unlimited(self)` (method)
- L72 `TestResolveTuiHeapMb` (class)
- L73 `_resolve(self, limit_bytes)` (method)
- L77 `test_unconstrained_uses_default(self)` (method)
- L80 `test_large_container_clamps_to_default(self)` (method)
- L84 `test_4gb_container_75_percent(self)` (method)
- L87 `test_3gb_container_above_floor(self)` (method)
- L90 `test_2gb_container_at_floor(self)` (method)
- L93 `test_tiny_container_honors_limit_below_floor(self)` (method)
- L98 `test_never_exceeds_default(self)` (method)
- L102 `TestNodeOptionsTokenMerge` (class) — The _launch_tui token-merge block must add the sized cap unless the user
- L106 `_merge(self, node_options, limit_bytes)` (method)
- L113 `test_unconstrained_empty(self)` (method)
- L116 `test_constrained_container(self)` (method)
- L119 `test_user_override_respected(self)` (method)
- L122 `test_preserves_other_flags(self)` (method)
