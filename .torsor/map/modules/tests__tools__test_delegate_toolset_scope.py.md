---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/tools/test_delegate_toolset_scope.py

Symbols in `tests/tools/test_delegate_toolset_scope.py`.

- L14 `TestToolsetIntersection` (class) — Subagent toolsets must be a subset of parent's enabled_toolsets.
- L17 `test_requested_toolsets_intersected_with_parent(self)` (method) — LLM requests toolsets parent doesn't have — extras are dropped.
- L31 `test_all_requested_toolsets_available_on_parent(self)` (method) — LLM requests subset of parent tools — all pass through.
- L41 `test_no_toolsets_requested_inherits_parent(self)` (method) — When toolsets is None/empty, child inherits parent's set.
- L49 `test_strip_blocked_removes_delegation(self)` (method) — Blocked toolsets (delegation, clarify, etc.) are always removed.
- L57 `test_empty_intersection_yields_empty_toolsets(self)` (method) — If parent has no overlap with requested, child gets nothing extra.
