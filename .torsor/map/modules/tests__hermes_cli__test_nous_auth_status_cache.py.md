---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/hermes_cli/test_nous_auth_status_cache.py

Symbols in `tests/hermes_cli/test_nous_auth_status_cache.py`.

- L17 `_seed_auth_file(tmp_path)` (function) — Drop a placeholder auth.json into the test HERMES_HOME.
- L28 `test_get_nous_auth_status_caches_consecutive_calls(tmp_path, monkeypatch)` (function) — A second call within the TTL skips re-computing the snapshot.
- L60 `test_get_nous_auth_status_invalidates_on_auth_file_mtime(tmp_path, monkeypatch)` (function) — Touching auth.json (login/logout) forces a re-compute.
- L91 `test_invalidate_nous_auth_status_cache_forces_recompute(tmp_path, monkeypatch)` (function) — Explicit invalidate forces the next call to re-compute.
- L116 `test_get_nous_auth_status_caches_failure_path(tmp_path, monkeypatch)` (function) — Logged-out snapshots are cached too — that's where the cost was.
