---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:44'
updated: '2026-06-08T00:38:44'
---

# tools/environments/file_sync.py

Symbols in `tools/environments/file_sync.py`.

- L50 `iter_sync_files(container_base: str='/root/.hermes')` (function) — Enumerate all files that should be synced to a remote environment.
- L79 `quoted_rm_command(remote_paths: list[str])` (function) — Build a shell ``rm -f`` command for a batch of remote paths.
- L84 `quoted_mkdir_command(dirs: list[str])` (function) — Build a shell ``mkdir -p`` command for a batch of directories.
- L89 `unique_parent_dirs(files: list[tuple[str, str]])` (function) — Extract sorted unique parent directories from (host, remote) pairs.
- L94 `_sha256_file(path: str)` (function) — Return hex SHA-256 digest of a file.
- L108 `FileSyncManager` (class) — Tracks local file changes and syncs to a remote environment.
- L119 `__init__(self, get_files_fn: GetFilesFn, upload_fn: UploadFn, delete_fn: DeleteFn, sync_interval: float=_SYNC_INTERVAL_SECONDS, bulk_upload_fn: BulkUploadFn | None=None, bulk_download_fn: BulkDownloadFn | None=None)` (method)
- L138 `sync(self, *, force: bool=False)` (method) — Run a sync cycle: upload changed files, delete removed files.
- L217 `sync_back(self, hermes_home: Path | None=None)` (method) — Pull remote changes back to the host filesystem.
- L257 `_sync_back_once(self, lock_path: Path)` (method) — Single sync-back attempt with SIGINT protection and file lock.
- L282 `_sync_back_locked(self, lock_path: Path)` (method) — Sync-back under file lock (serializes concurrent gateways).
- L299 `_sync_back_impl(self)` (method) — Download, diff, and apply remote changes to host.
- L377 `_resolve_host_path(self, remote_path: str, file_mapping: list[tuple[str, str]] | None=None)` (method) — Find the host path for a known remote path from the file mapping.
- L386 `_infer_host_path(self, remote_path: str, file_mapping: list[tuple[str, str]] | None=None)` (method) — Infer a host path for a new remote file by matching path prefixes.
