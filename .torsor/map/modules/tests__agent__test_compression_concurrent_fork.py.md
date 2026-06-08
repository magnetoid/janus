---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/agent/test_compression_concurrent_fork.py

Symbols in `tests/agent/test_compression_concurrent_fork.py`.

- L42 `_build_agent_with_db(db: SessionDB, session_id: str)` (function) — Build an AIAgent that's wired to ``db`` and pinned to ``session_id``.
- L83 `_count_children(db: SessionDB, parent_sid: str)` (function) — Count rows in state.db whose parent_session_id == parent_sid.
- L92 `test_concurrent_compression_does_not_fork_session(tmp_path: Path)` (function) — Two AIAgents that share a session_id MUST NOT both rotate it.
- L147 `test_skipped_compression_returns_messages_unchanged(tmp_path: Path)` (function) — The loser of the lock race must return its input messages verbatim.
- L176 `_NoLockSubsystemDB` (class) — Wraps a real SessionDB but simulates a pre-#34351 version skew.
- L189 `__init__(self, real_db: SessionDB)` (method)
- L192 `try_acquire_compression_lock(self, *_a, **_k)` (method)
- L197 `get_compression_lock_holder(self, *_a, **_k)` (method)
- L200 `release_compression_lock(self, *_a, **_k)` (method)
- L203 `__getattr__(self, name)` (method)
- L209 `test_missing_lock_subsystem_fails_open_not_infinite_loop(tmp_path: Path)` (function) — Version skew (no lock methods) must fail OPEN, not raise into the loop.
