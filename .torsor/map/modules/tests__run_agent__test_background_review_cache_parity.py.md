---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/run_agent/test_background_review_cache_parity.py

Symbols in `tests/run_agent/test_background_review_cache_parity.py`.

- L17 `_make_agent_stub(agent_cls)` (function) — Create a minimal AIAgent-like object with just enough state for _spawn_background_review.
- L47 `_SyncThread` (class) — Drop-in replacement for threading.Thread that runs the target inline.
- L50 `__init__(self, *, target=None, daemon=None, name=None)` (method)
- L53 `start(self)` (method)
- L58 `_ReviewAgentRecorder` (class) — Stand-in for the review-fork AIAgent that records the prompt assignment.
- L61 `__init__(self, *args, **kwargs)` (method)
- L72 `run_conversation(self, *args, **kwargs)` (method)
- L75 `shutdown_memory_provider(self)` (method)
- L78 `close(self)` (method)
- L82 `test_review_fork_inherits_parent_cached_system_prompt()` (function) — The review fork's _cached_system_prompt must equal the parent's byte-for-byte.
- L134 `test_review_fork_pins_session_start_and_session_id()` (function) — Defensive complement to cached-system-prompt inheritance.
- L191 `test_review_fork_inherits_parent_toolset_config()` (function) — ``tools[]`` byte-stability: fork must inherit parent's toolset config.
