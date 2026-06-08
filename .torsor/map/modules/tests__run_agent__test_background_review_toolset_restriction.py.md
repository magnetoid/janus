---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/run_agent/test_background_review_toolset_restriction.py

Symbols in `tests/run_agent/test_background_review_toolset_restriction.py`.

- L19 `_make_agent_stub(agent_cls)` (function) — Create a minimal AIAgent-like object with just enough state for _spawn_background_review.
- L46 `_SyncThread` (class) — Drop-in replacement for threading.Thread that runs the target inline.
- L49 `__init__(self, *, target=None, daemon=None, name=None)` (method)
- L52 `start(self)` (method)
- L57 `test_background_review_matches_parent_toolset_config()` (function) — Fork must receive parent's toolset config so ``tools[]`` cache key matches.
- L88 `test_background_review_installs_thread_local_whitelist()` (function) — The review fork must install a memory/skills-only thread-local whitelist.
- L138 `test_background_review_agent_tools_are_limited()` (function) — Verify the resolved memory+skills toolsets only contain memory and skill tools.
