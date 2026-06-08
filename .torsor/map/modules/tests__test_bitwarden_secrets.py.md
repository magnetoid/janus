---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/test_bitwarden_secrets.py

Symbols in `tests/test_bitwarden_secrets.py`.

- L35 `_reset_caches()` (function)
- L42 `hermes_home(tmp_path, monkeypatch)` (function) — Point Hermes at an isolated home directory.
- L78 `test_platform_asset_name(system, machine, libc_text, expected)` (function)
- L94 `_make_fake_zip(binary_bytes: bytes)` (function)
- L106 `test_safe_extract_member_extracts_normal_member(tmp_path)` (function)
- L131 `test_safe_extract_member_rejects_traversal(tmp_path, evil_name)` (function)
- L149 `test_safe_extract_member_rejects_absolute_path(tmp_path)` (function)
- L166 `test_install_bws_rejects_malicious_member(hermes_home, monkeypatch)` (function)
- L189 `test_install_bws_happy_path(hermes_home, monkeypatch)` (function)
- L215 `test_install_bws_checksum_mismatch(hermes_home, monkeypatch)` (function)
- L233 `test_install_bws_missing_checksum_entry(hermes_home, monkeypatch)` (function)
- L253 `_fake_bws_payload(items)` (function)
- L257 `test_fetch_happy_path(monkeypatch, tmp_path)` (function)
- L286 `test_fetch_skips_invalid_env_names(monkeypatch, tmp_path)` (function)
- L312 `test_fetch_auth_failure(monkeypatch, tmp_path)` (function)
- L333 `test_fetch_timeout(monkeypatch, tmp_path)` (function)
- L351 `test_fetch_non_json(monkeypatch, tmp_path)` (function)
- L372 `test_fetch_cache_hits(monkeypatch, tmp_path)` (function)
- L391 `test_fetch_server_url_sets_env(monkeypatch, tmp_path)` (function) — server_url must be plumbed into the subprocess as BWS_SERVER_URL.
- L415 `test_fetch_no_server_url_does_not_set_env(monkeypatch, tmp_path)` (function) — When server_url is empty, BWS_SERVER_URL must not be injected.
- L440 `test_fetch_server_url_keyed_in_cache(monkeypatch, tmp_path)` (function) — Different server_url values must produce separate cache entries.
- L474 `test_fetch_cache_disabled(monkeypatch, tmp_path)` (function)
- L496 `test_apply_disabled_returns_empty()` (function)
- L503 `test_apply_missing_token(monkeypatch)` (function)
- L512 `test_apply_missing_project_id(monkeypatch)` (function)
- L521 `test_apply_does_not_override_existing(monkeypatch, tmp_path)` (function)
- L547 `test_apply_override_existing(monkeypatch, tmp_path)` (function)
- L567 `test_apply_never_overrides_bootstrap_token(monkeypatch, tmp_path)` (function) — Even with override_existing=True, the access-token var is preserved.
- L589 `test_apply_swallows_fetch_errors(monkeypatch, tmp_path)` (function) — A fetch failure produces an error, NOT an exception.
- L612 `test_env_loader_skips_when_disabled(tmp_path, monkeypatch)` (function) — No config.yaml present → no BSM call, no crash.
- L624 `test_env_loader_calls_bsm_when_enabled(tmp_path, monkeypatch)` (function)
- L669 `test_disk_cache_written_after_first_fetch(monkeypatch, tmp_path)` (function) — First fetch hits bws AND writes a 0600 file under hermes_home/cache/.
- L705 `test_disk_cache_short_circuits_bws_when_fresh(monkeypatch, tmp_path)` (function) — Second fetch (different process simulation) skips bws entirely.
- L739 `test_disk_cache_expires_with_ttl(monkeypatch, tmp_path)` (function) — Stale disk cache (older than ttl) triggers a refetch.
- L776 `test_disk_cache_key_mismatch_triggers_refetch(monkeypatch, tmp_path)` (function) — Disk cache entry written by a different token/project is ignored.
- L810 `test_disk_cache_use_cache_false_skips_disk(monkeypatch, tmp_path)` (function) — use_cache=False must skip BOTH in-process and disk caches.
- L841 `test_disk_cache_corrupt_file_falls_through(monkeypatch, tmp_path)` (function) — A garbage cache file must NOT crash startup — we refetch.
- L870 `test_reset_cache_for_tests_deletes_disk_file(tmp_path)` (function) — _reset_cache_for_tests(home_path) must also clean disk.
