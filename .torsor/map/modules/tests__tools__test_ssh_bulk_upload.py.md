---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:44'
updated: '2026-06-08T00:38:44'
---

# tests/tools/test_ssh_bulk_upload.py

Symbols in `tests/tools/test_ssh_bulk_upload.py`.

- L14 `_mock_proc(*, returncode=0, poll_return=0, communicate_return=(b'', b''), stderr_read=b'')` (function) — Create a MagicMock mimicking subprocess.Popen for tar/ssh pipes.
- L28 `mock_env(monkeypatch)` (function) — Create an SSHEnvironment with mocked connection/sync.
- L42 `TestSSHBulkUpload` (class) — Unit tests for _ssh_bulk_upload — tar pipe mechanics.
- L45 `test_empty_files_is_noop(self, mock_env)` (method) — Empty file list should not spawn any subprocesses.
- L53 `test_mkdir_batched_into_single_call(self, mock_env, tmp_path)` (method) — All parent directories should be created in one SSH call.
- L92 `test_staging_symlinks_mirror_remote_layout(self, mock_env, tmp_path)` (method) — Staged file in staging dir should mirror the remote path structure.
- L138 `test_tar_pipe_commands(self, mock_env, tmp_path)` (method) — Verify tar and SSH commands are wired correctly.
- L182 `test_bulk_upload_never_stages_remote_home_prefix(self, mock_env, tmp_path)` (method) — Regression: do not archive /home/<user> path components.
- L210 `test_mkdir_failure_raises(self, mock_env, tmp_path)` (method) — mkdir failure should raise RuntimeError before tar pipe.
- L221 `test_tar_create_failure_raises(self, mock_env, tmp_path)` (method) — tar create failure should raise RuntimeError.
- L250 `test_ssh_extract_failure_raises(self, mock_env, tmp_path)` (method) — SSH tar extract failure should raise RuntimeError.
- L279 `test_ssh_command_uses_control_socket(self, mock_env, tmp_path)` (method) — SSH command for tar extract should reuse ControlMaster socket.
- L307 `test_custom_port_and_key_in_ssh_command(self, monkeypatch, tmp_path)` (method) — Bulk upload SSH command should include custom port and key.
- L357 `test_parent_dirs_deduplicated(self, mock_env, tmp_path)` (method) — Multiple files in the same dir should produce one mkdir entry.
- L399 `test_tar_stdout_closed_for_sigpipe(self, mock_env, tmp_path)` (method) — tar_proc.stdout must be closed so SIGPIPE propagates correctly.
- L427 `test_timeout_kills_both_processes(self, mock_env, tmp_path)` (method) — TimeoutExpired during communicate should kill both processes.
- L457 `TestSSHBulkUploadWiring` (class) — Verify bulk_upload_fn is wired into FileSyncManager.
- L460 `test_filesyncmanager_receives_bulk_upload_fn(self, monkeypatch)` (method) — SSHEnvironment should pass _ssh_bulk_upload to FileSyncManager.
- L487 `TestSharedHelpers` (class) — Direct unit tests for file_sync.py helpers.
- L490 `test_quoted_mkdir_command_basic(self)` (method)
- L494 `test_quoted_mkdir_command_quotes_special_chars(self)` (method)
- L500 `test_quoted_mkdir_command_empty(self)` (method)
- L504 `test_unique_parent_dirs_deduplicates(self)` (method)
- L513 `test_unique_parent_dirs_sorted(self)` (method)
- L521 `test_unique_parent_dirs_empty(self)` (method)
- L525 `TestSSHBulkUploadEdgeCases` (class) — Edge cases for _ssh_bulk_upload.
- L528 `test_ssh_popen_failure_kills_tar(self, mock_env, tmp_path)` (method) — If SSH Popen raises, tar process must be killed and cleaned up.
