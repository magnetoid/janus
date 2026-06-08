---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/hermes_cli/test_env_load_cache.py

Symbols in `tests/hermes_cli/test_env_load_cache.py`.

- L18 `_write_env(path: Path, contents: str)` (function)
- L22 `test_load_env_caches_on_repeat_calls()` (function) — Repeated load_env() calls on the same file return the cached dict.
- L50 `test_load_env_invalidates_on_mtime_bump()` (function) — Editing the file (mtime changes) invalidates the cache.
- L82 `test_invalidate_env_cache_forces_reread()` (function) — invalidate_env_cache() forces the next load_env() to hit the disk.
- L116 `test_save_env_value_invalidates_cache(tmp_path, monkeypatch)` (function) — save_env_value() invalidates the cache so subsequent reads see the update.
- L149 `test_remove_env_value_invalidates_cache(tmp_path, monkeypatch)` (function) — remove_env_value() invalidates the cache so the removed key disappears.
- L179 `test_load_env_handles_missing_file()` (function) — A nonexistent .env returns {} and caches the empty result.
