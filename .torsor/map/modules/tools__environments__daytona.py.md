---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:44'
updated: '2026-06-08T00:38:44'
---

# tools/environments/daytona.py

Symbols in `tools/environments/daytona.py`.

- L30 `DaytonaEnvironment` (class) — Daytona cloud sandbox execution backend.
- L40 `__init__(self, image: str, cwd: str='/home/daytona', timeout: int=60, cpu: int=1, memory: int=5120, disk: int=10240, persistent_filesystem: bool=True, task_id: str='default')` (method)
- L154 `_daytona_upload(self, host_path: str, remote_path: str)` (method) — Upload a single file via Daytona SDK.
- L160 `_daytona_bulk_upload(self, files: list[tuple[str, str]])` (method) — Upload many files in a single HTTP call via Daytona SDK.
- L182 `_daytona_bulk_download(self, dest: Path)` (method) — Download remote .hermes/ as a tar archive.
- L198 `_daytona_delete(self, remote_paths: list[str])` (method) — Batch-delete remote files via SDK exec.
- L206 `_ensure_sandbox_ready(self)` (method) — Restart sandbox if it was stopped (e.g., by a previous interrupt).
- L213 `_before_execute(self)` (method) — Ensure sandbox is ready, then sync files via FileSyncManager.
- L219 `_run_bash(self, cmd_string: str, *, login: bool=False, timeout: int=120, stdin_data: str | None=None)` (method) — Return a _ThreadedProcessHandle wrapping a blocking Daytona SDK call.
- L244 `cleanup(self)` (method)
