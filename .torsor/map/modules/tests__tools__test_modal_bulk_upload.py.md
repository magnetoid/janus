---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:44'
updated: '2026-06-08T00:38:44'
---

# tests/tools/test_modal_bulk_upload.py

Symbols in `tests/tools/test_modal_bulk_upload.py`.

- L14 `_make_mock_modal_env(monkeypatch, tmp_path)` (function) — Create a minimal mock ModalEnvironment for testing upload methods.
- L29 `_make_mock_stdin()` (function) — Create a mock stdin that captures written data.
- L45 `_wire_async_exec(env, exec_calls=None)` (function) — Wire mock sandbox.exec.aio and a real run_coroutine on the env.
- L82 `TestModalBulkUpload` (class) — Test _modal_bulk_upload method.
- L85 `test_empty_files_is_noop(self, monkeypatch, tmp_path)` (method) — Empty file list should not call worker.run_coroutine.
- L91 `test_tar_archive_contains_all_files(self, monkeypatch, tmp_path)` (method) — The tar archive sent via stdin should contain all files.
- L137 `test_mkdir_includes_all_parents(self, monkeypatch, tmp_path)` (method) — Remote parent directories should be pre-created in the command.
- L156 `test_single_exec_call(self, monkeypatch, tmp_path)` (method) — Bulk upload should use exactly one exec call regardless of file count.
- L172 `test_bulk_upload_wired_in_filesyncmanager(self, monkeypatch)` (method) — Verify ModalEnvironment passes bulk_upload_fn to FileSyncManager.
- L202 `test_timeout_set_to_120(self, monkeypatch, tmp_path)` (method) — Bulk upload uses a 120s timeout (not the per-file 15s).
- L215 `test_nonzero_exit_raises(self, monkeypatch, tmp_path)` (method) — Non-zero exit code from remote exec should raise RuntimeError.
- L250 `test_payload_not_in_command_string(self, monkeypatch, tmp_path)` (method) — The base64 payload must NOT appear in the bash -c argument.
- L271 `test_stdin_chunked_for_large_payloads(self, monkeypatch, tmp_path)` (method) — Payloads larger than _STDIN_CHUNK_SIZE should be split into multiple writes.
