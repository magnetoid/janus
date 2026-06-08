---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/agent/test_external_skills_dirs_cache.py

Symbols in `tests/agent/test_external_skills_dirs_cache.py`.

- L27 `hermes_home_with_config(tmp_path, monkeypatch)` (function) — Isolated ``~/.hermes/`` with a config.yaml referencing one external dir.
- L49 `test_returns_configured_external_dir(hermes_home_with_config)` (function)
- L55 `test_cache_reuses_result_without_reparsing(hermes_home_with_config)` (function) — Subsequent calls hit the cache and skip YAML parsing entirely.
- L73 `test_cache_invalidates_on_mtime_change(hermes_home_with_config)` (function) — A config.yaml edit invalidates the cache on the next call.
- L100 `test_returns_empty_when_config_missing(tmp_path, monkeypatch)` (function) — No config file → empty list, cached as empty.
- L111 `test_returned_list_is_a_copy(hermes_home_with_config)` (function) — Callers can't poison the cache by mutating the returned list.
- L120 `test_cache_key_is_per_config_path(tmp_path, monkeypatch)` (function) — Two different HERMES_HOMEs keep separate cache entries.
