---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/tools/test_delegate_composite_toolsets.py

Symbols in `tests/tools/test_delegate_composite_toolsets.py`.

- L8 `TestExpandParentToolsets` (class) — Verify _expand_parent_toolsets recognises individual toolsets within composites.
- L11 `test_composite_hermes_cli_expands_web(self)` (method) — hermes-cli includes web_search/web_extract → 'web' should be in expansion.
- L20 `test_individual_toolset_unchanged(self)` (method) — When parent already uses individual toolsets, expansion keeps them.
- L26 `test_empty_parent_toolsets(self)` (method)
- L30 `test_unknown_toolset_passthrough(self)` (method) — Unknown toolset names pass through without error.
- L35 `test_intersection_with_expanded_composite(self)` (method) — End-to-end: requesting ['web'] from parent with ['hermes-cli'] yields ['web'].
