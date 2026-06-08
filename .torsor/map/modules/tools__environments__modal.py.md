---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:44'
updated: '2026-06-08T00:38:44'
---

# tools/environments/modal.py

Symbols in `tools/environments/modal.py`.

- L38 `_load_snapshots()` (function)
- L42 `_save_snapshots(data: dict)` (function)
- L46 `_direct_snapshot_key(task_id: str)` (function)
- L50 `_get_snapshot_restore_candidate(task_id: str)` (function)
- L62 `_store_direct_snapshot(task_id: str, snapshot_id: str)` (function)
- L69 `_delete_direct_snapshot(task_id: str, snapshot_id: str | None=None)` (function)
- L83 `_ensure_modal_sdk()` (function) — Lazy-install modal on demand. Idempotent — fast no-op once installed.
- L94 `_resolve_modal_image(image_spec: Any)` (function) — Convert registry references or snapshot ids into Modal image objects.
- L127 `_AsyncWorker` (class) — Background thread with its own event loop for async-safe Modal calls.
- L130 `__init__(self)` (method)
- L135 `start(self)` (method)
- L140 `_run_loop(self)` (method)
- L146 `run_coroutine(self, coro, timeout=600)` (method)
- L157 `stop(self)` (method)
- L164 `ModalEnvironment` (class) — Modal cloud execution via native Modal sandboxes.
- L174 `__init__(self, image: str, cwd: str='/root', timeout: int=60, modal_sandbox_kwargs: Optional[dict[str, Any]]=None, persistent_filesystem: bool=True, task_id: str='default')` (method)
- L295 `_modal_upload(self, host_path: str, remote_path: str)` (method) — Upload a single file via base64 piped through stdin.
- L325 `_modal_bulk_upload(self, files: list[tuple[str, str]])` (method) — Upload many files via tar archive piped through stdin.
- L369 `_modal_bulk_download(self, dest: Path)` (method) — Download remote .hermes/ as a tar archive.
- L390 `_modal_delete(self, remote_paths: list[str])` (method) — Batch-delete remote files via exec.
- L400 `_before_execute(self)` (method) — Sync files to sandbox via FileSyncManager (rate-limited internally).
- L408 `_run_bash(self, cmd_string: str, *, login: bool=False, timeout: int=120, stdin_data: str | None=None)` (method) — Return a _ThreadedProcessHandle wrapping an async Modal sandbox exec.
- L442 `cleanup(self)` (method) — Snapshot the filesystem (if persistent) then stop the sandbox.
