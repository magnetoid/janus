---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# agent/secret_sources/bitwarden.py

Symbols in `agent/secret_sources/bitwarden.py`.

- L88 `_disk_cache_path(home_path: Optional[Path]=None)` (function) — Return the disk cache path under hermes_home/cache/.
- L99 `_cache_key_str(cache_key: _CacheKey)` (function) — Serialize a cache key to a stable string for JSON storage.
- L105 `_read_disk_cache(cache_key: _CacheKey, ttl_seconds: float, home_path: Optional[Path]=None)` (function) — Return a cached entry from disk if fresh, else None.
- L137 `_write_disk_cache(cache_key: _CacheKey, entry: '_CachedFetch', home_path: Optional[Path]=None)` (function) — Persist a cache entry to disk atomically with mode 0600.
- L173 `_CachedFetch` (class)
- L177 `is_fresh(self, ttl_seconds: float)` (method)
- L189 `FetchResult` (class) — Outcome of a single BSM pull.
- L200 `ok(self)` (method)
- L209 `_hermes_bin_dir()` (function) — Where Hermes stores its managed binaries.  Profile-aware.
- L216 `find_bws(*, install_if_missing: bool=False)` (function) — Return a path to a usable ``bws`` binary, or None.
- L243 `_platform_binary_name()` (function)
- L247 `_platform_asset_name()` (function) — Map (uname, arch, libc) → the upstream asset filename.
- L289 `install_bws(*, force: bool=False)` (function) — Download, verify, and install the pinned ``bws`` binary.
- L350 `_http_download(url: str, dest: Path)` (function)
- L360 `_expected_sha256(checksum_file: Path, asset_name: str)` (function) — Parse the upstream ``bws-sha256-checksums-X.Y.Z.txt`` file.
- L376 `_sha256_file(path: Path)` (function)
- L384 `_pick_zip_member(zf: zipfile.ZipFile, binary_name: str)` (function) — Find the binary inside the upstream zip.
- L401 `_safe_extract_member(zf: zipfile.ZipFile, member: str, dest_dir: Path)` (function) — Extract a single archive member, refusing path traversal.
- L433 `_token_fingerprint(token: str)` (function) — SHA-256 prefix used as a cache key — never logged, never displayed.
- L438 `fetch_bitwarden_secrets(*, access_token: str, project_id: str, binary: Optional[Path]=None, cache_ttl_seconds: float=300, use_cache: bool=True, server_url: str='', home_path: Optional[Path]=None)` (function) — Pull the secrets for ``project_id`` from Bitwarden Secrets Manager.
- L505 `_run_bws_list(bws: Path, access_token: str, project_id: str, server_url: str='')` (function)
- L576 `_is_valid_env_name(name: str)` (function)
- L589 `apply_bitwarden_secrets(*, enabled: bool, access_token_env: str='BWS_ACCESS_TOKEN', project_id: str='', override_existing: bool=False, cache_ttl_seconds: float=300, auto_install: bool=True, server_url: str='', home_path: Optional[Path]=None)` (function) — Pull secrets from BSM and set them on ``os.environ``.
- L679 `_reset_cache_for_tests(home_path: Optional[Path]=None)` (function) — Clear in-process AND disk caches.
