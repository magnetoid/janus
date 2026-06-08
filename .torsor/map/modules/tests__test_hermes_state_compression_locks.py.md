---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/test_hermes_state_compression_locks.py

Symbols in `tests/test_hermes_state_compression_locks.py`.

- L25 `db(tmp_path: Path)` (function)
- L34 `test_acquire_succeeds_when_unlocked(db: SessionDB)` (function)
- L39 `test_acquire_blocks_second_holder(db: SessionDB)` (function)
- L46 `test_release_allows_reacquire(db: SessionDB)` (function)
- L53 `test_release_with_wrong_holder_is_noop(db: SessionDB)` (function)
- L60 `test_release_when_unlocked_is_noop(db: SessionDB)` (function)
- L71 `test_locks_are_per_session(db: SessionDB)` (function)
- L84 `test_expired_lock_is_reclaimable(db: SessionDB)` (function) — A crashed compressor must not permanently block the session.
- L96 `test_non_expired_lock_is_held(db: SessionDB)` (function)
- L107 `test_acquire_empty_session_id_returns_false(db: SessionDB)` (function)
- L111 `test_release_empty_session_id_is_noop(db: SessionDB)` (function)
- L116 `test_holder_empty_session_id_returns_none(db: SessionDB)` (function)
- L125 `test_concurrent_acquire_only_one_winner(db: SessionDB)` (function) — Damien's race shape: N threads call acquire on the same session_id;
