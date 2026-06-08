---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:44'
updated: '2026-06-08T00:38:44'
---

# tools/environments/ssh.py

Symbols in `tools/environments/ssh.py`.

- L24 `_ensure_ssh_available()` (function) — Fail fast with a clear error when the SSH client is unavailable.
- L36 `SSHEnvironment` (class) — Run commands on a remote machine over SSH.
- L45 `__init__(self, host: str, user: str, cwd: str='~', timeout: int=60, port: int=22, key_path: str='')` (method)
- L83 `_build_ssh_command(self, extra_args: list | None=None)` (method)
- L100 `_establish_connection(self)` (method)
- L117 `_detect_remote_home(self)` (method) — Detect the remote user's home directory.
- L143 `_ensure_remote_dirs(self)` (method) — Create base ~/.hermes directory tree on remote in one SSH call.
- L159 `_scp_upload(self, host_path: str, remote_path: str)` (method) — Upload a single file via scp over ControlMaster.
- L188 `_ssh_bulk_upload(self, files: list[tuple[str, str]])` (method) — Upload many files in a single tar-over-SSH stream.
- L303 `_ssh_bulk_download(self, dest: Path)` (method) — Download remote .hermes/ as a tar archive.
- L321 `_ssh_delete(self, remote_paths: list[str])` (method) — Batch-delete remote files in one SSH call.
- L335 `_before_execute(self)` (method) — Sync files to remote via FileSyncManager (rate-limited internally).
- L343 `_run_bash(self, cmd_string: str, *, login: bool=False, timeout: int=120, stdin_data: str | None=None)` (method) — Spawn an SSH process that runs bash on the remote host.
- L355 `cleanup(self)` (method)
