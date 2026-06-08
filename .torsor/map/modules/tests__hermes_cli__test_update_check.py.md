---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/hermes_cli/test_update_check.py

Symbols in `tests/hermes_cli/test_update_check.py`.

- L13 `test_version_string_no_v_prefix()` (function) — __version__ should be bare semver without a 'v' prefix.
- L19 `test_check_for_updates_uses_cache(tmp_path, monkeypatch)` (function) — When cache is fresh, check_for_updates should return cached value without calling git.
- L40 `test_check_for_updates_invalidates_on_version_change(tmp_path, monkeypatch)` (function) — A fresh cache from a different installed version must be re-checked, not reused.
- L77 `test_check_for_updates_expired_cache(tmp_path, monkeypatch)` (function) — When cache is expired, check_for_updates should call git fetch.
- L99 `test_check_for_updates_no_git_dir(tmp_path, monkeypatch)` (function) — Falls back to PyPI check when .git directory doesn't exist anywhere.
- L117 `test_check_for_updates_fallback_to_project_root(tmp_path, monkeypatch)` (function) — Dev install: falls back to Path(__file__).parent.parent when HERMES_HOME has no git repo.
- L134 `test_check_for_updates_docker_returns_none(tmp_path, monkeypatch)` (function) — Inside the Docker image, check_for_updates() must short-circuit to None.
- L164 `test_check_for_updates_non_docker_still_checks(tmp_path, monkeypatch)` (function) — The docker guard must NOT over-broaden: a pip install still version-checks.
- L190 `test_prefetch_non_blocking()` (function) — prefetch_update_check() should return immediately without blocking.
- L211 `test_invalidate_update_cache_clears_all_profiles(tmp_path)` (function) — _invalidate_update_cache() should delete .update_check from ALL profiles.
- L236 `test_invalidate_update_cache_no_profiles_dir(tmp_path)` (function) — Works fine when no profiles directory exists (single-profile setup).
