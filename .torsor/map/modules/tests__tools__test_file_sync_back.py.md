---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/tools/test_file_sync_back.py

Symbols in `tests/tools/test_file_sync_back.py`.

- L27 `_make_tar(files: dict[str, bytes], dest: Path)` (function) — Write a tar archive containing the given arcname->content pairs.
- L36 `_make_download_fn(files: dict[str, bytes])` (function) — Return a bulk_download_fn that writes a tar of the given files.
- L43 `_sha256_bytes(data: bytes)` (function) — Compute SHA-256 hex digest of raw bytes (for test convenience).
- L49 `_write_file(path: Path, content: bytes)` (function) — Write bytes to *path*, creating parents, and return the string path.
- L56 `_make_manager(tmp_path: Path, file_mapping: list[tuple[str, str]] | None=None, bulk_download_fn=None, seed_pushed_state: bool=True)` (function) — Create a FileSyncManager wired for testing.
- L97 `TestSyncBackNoop` (class) — sync_back() is a no-op when there is no download function.
- L100 `test_sync_back_noop_without_download_fn(self, tmp_path)` (method)
- L107 `TestSyncBackNoChanges` (class) — When all remote files match pushed hashes, nothing is applied.
- L110 `test_sync_back_no_changes(self, tmp_path)` (method)
- L133 `TestSyncBackAppliesChanged` (class) — Remote file differs from pushed version -- gets copied to host.
- L136 `test_sync_back_applies_changed_file(self, tmp_path)` (method)
- L157 `TestSyncBackNewRemoteFile` (class) — File created on remote (not in _pushed_hashes) is applied via _infer_host_path.
- L160 `test_sync_back_detects_new_remote_file(self, tmp_path)` (method)
- L183 `TestSyncBackConflict` (class) — Host AND remote both changed since push -- warning logged, remote wins.
- L186 `test_sync_back_conflict_warns(self, tmp_path, caplog)` (method)
- L216 `TestSyncBackRetries` (class) — Retry behaviour with exponential backoff.
- L220 `test_sync_back_retries_on_failure(self, mock_sleep, tmp_path)` (method)
- L241 `test_sync_back_all_retries_exhausted(self, mock_sleep, tmp_path, caplog)` (method)
- L258 `TestPushedHashesPopulated` (class) — _pushed_hashes is populated during sync() and cleared on delete.
- L261 `test_pushed_hashes_populated_on_sync(self, tmp_path)` (method)
- L279 `test_pushed_hashes_cleared_on_delete(self, tmp_path)` (method)
- L307 `TestSyncBackFileLock` (class) — Verify that fcntl.flock is used during sync-back.
- L311 `test_sync_back_file_lock(self, mock_flock, tmp_path)` (method)
- L325 `test_sync_back_skips_flock_when_fcntl_none(self, tmp_path)` (method) — On Windows (fcntl=None), sync_back should skip file locking.
- L335 `TestInferHostPath` (class) — Edge cases for _infer_host_path prefix matching.
- L338 `test_infer_no_matching_prefix(self, tmp_path)` (method) — Remote path in unmapped directory should return None.
- L351 `test_infer_partial_prefix_no_false_match(self, tmp_path)` (method) — A partial prefix like /root/.hermes/sk should NOT match /root/.hermes/skills/.
- L366 `test_infer_matching_prefix(self, tmp_path)` (method) — A file in a mapped directory should be correctly inferred.
- L381 `TestSyncBackSIGINT` (class) — SIGINT deferral during sync-back.
- L384 `test_sync_back_defers_sigint_on_main_thread(self, tmp_path)` (method) — On the main thread, SIGINT handler should be swapped during sync.
- L402 `test_sync_back_skips_signal_on_worker_thread(self, tmp_path)` (method) — From a non-main thread, signal.signal should NOT be called.
- L432 `TestSyncBackSizeCap` (class) — The size cap refuses to extract tars above the configured limit.
- L435 `test_sync_back_refuses_oversized_tar(self, tmp_path, caplog)` (method) — A tar larger than _SYNC_BACK_MAX_BYTES should be skipped with a warning.
- L459 `test_sync_back_applies_when_under_cap(self, tmp_path)` (method) — A tar under the cap should extract normally (sanity check).
