---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:44'
updated: '2026-06-08T00:38:44'
---

# tests/tools/test_sync_back_backends.py

Symbols in `tests/tools/test_sync_back_backends.py`.

- L20 `ssh_mock_env(monkeypatch)` (function) — Create an SSHEnvironment with mocked connection/sync.
- L40 `_make_mock_modal_env()` (function) — Create a minimal ModalEnvironment without calling __init__.
- L51 `_wire_modal_download(env, *, tar_bytes=b'fake-tar-data', exit_code=0)` (function) — Wire sandbox.exec.aio to return mock tar output for download tests.
- L85 `_make_mock_daytona_env()` (function) — Create a minimal DaytonaEnvironment without calling __init__.
- L103 `TestSSHBulkDownload` (class) — Unit tests for _ssh_bulk_download.
- L106 `test_ssh_bulk_download_runs_tar_over_ssh(self, ssh_mock_env, tmp_path)` (method) — subprocess.run command should include tar cf - over SSH.
- L123 `test_ssh_bulk_download_writes_to_dest(self, ssh_mock_env, tmp_path)` (method) — subprocess.run should receive stdout=open(dest, 'wb').
- L139 `test_ssh_bulk_download_raises_on_failure(self, ssh_mock_env, tmp_path)` (method) — Non-zero returncode should raise RuntimeError.
- L148 `test_ssh_bulk_download_uses_120s_timeout(self, ssh_mock_env, tmp_path)` (method) — The subprocess.run call should use a 120s timeout.
- L159 `TestSSHCleanup` (class) — Verify SSH cleanup() calls sync_back() before closing ControlMaster.
- L162 `test_ssh_cleanup_calls_sync_back(self, monkeypatch)` (method) — cleanup() should call sync_back() before SSH control socket teardown.
- L192 `test_ssh_cleanup_calls_sync_back_before_control_exit(self, monkeypatch)` (method) — sync_back() must run before the ControlMaster exit command.
- L238 `TestModalBulkDownload` (class) — Unit tests for _modal_bulk_download.
- L241 `test_modal_bulk_download_command(self, tmp_path)` (method) — exec should be called with tar cf - -C /root/.hermes .
- L256 `test_modal_bulk_download_writes_to_dest(self, tmp_path)` (method) — Downloaded tar bytes should be written to the dest path.
- L268 `test_modal_bulk_download_handles_str_output(self, tmp_path)` (method) — If stdout returns str instead of bytes, it should be encoded.
- L279 `test_modal_bulk_download_raises_on_failure(self, tmp_path)` (method) — Non-zero exit code should raise RuntimeError.
- L288 `test_modal_bulk_download_uses_120s_timeout(self, tmp_path)` (method) — run_coroutine should be called with timeout=120.
- L308 `TestModalCleanup` (class) — Verify Modal cleanup() calls sync_back() before terminate.
- L311 `test_modal_cleanup_calls_sync_back(self)` (method) — cleanup() should call sync_back() before sandbox.terminate.
- L343 `TestDaytonaBulkDownload` (class) — Unit tests for _daytona_bulk_download.
- L346 `test_daytona_bulk_download_creates_tar_and_downloads(self, tmp_path)` (method) — exec and download_file should both be called.
- L373 `test_daytona_bulk_download_uses_remote_home(self, tmp_path)` (method) — The tar command should use the env's _remote_home.
- L385 `TestDaytonaCleanup` (class) — Verify Daytona cleanup() calls sync_back() before stop.
- L388 `test_daytona_cleanup_calls_sync_back(self)` (method) — cleanup() should call sync_back() before sandbox.stop().
- L410 `TestBulkDownloadWiring` (class) — Verify each backend passes bulk_download_fn to FileSyncManager.
- L413 `test_ssh_passes_bulk_download_fn(self, monkeypatch)` (method) — SSHEnvironment should pass _ssh_bulk_download to FileSyncManager.
- L437 `test_modal_passes_bulk_download_fn(self, monkeypatch)` (method) — ModalEnvironment should pass _modal_bulk_download to FileSyncManager.
- L466 `test_daytona_passes_bulk_download_fn(self, monkeypatch)` (method) — DaytonaEnvironment should pass _daytona_bulk_download to FileSyncManager.
