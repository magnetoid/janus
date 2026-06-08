---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/tools/test_local_env_cwd_recovery.py

Symbols in `tests/tools/test_local_env_cwd_recovery.py`.

- L23 `TestResolveSafeCwd` (class) — Pure-function unit tests for the recovery helper.
- L26 `test_returns_cwd_when_directory_exists(self, tmp_path)` (method)
- L30 `test_walks_up_to_first_existing_ancestor(self, tmp_path)` (method)
- L39 `test_falls_back_when_path_is_empty(self)` (method)
- L42 `test_returns_tempdir_when_nothing_on_path_exists(self, monkeypatch)` (method)
- L46 `test_returns_root_when_only_root_exists(self, monkeypatch)` (method) — If every ancestor except the filesystem root is gone, the root
- L55 `_fake_interrupt()` (function)
- L59 `_make_fake_popen(captured: dict, fds: list)` (function) — Build a fake ``Popen`` whose ``stdout`` exposes a real OS file
- L87 `_close_fds(fds)` (function)
- L95 `TestRunBashCwdRecovery` (class) — End-to-end recovery: deleted ``self.cwd`` must not crash Popen.
- L98 `test_recovers_when_cwd_deleted_after_init(self, tmp_path, caplog)` (method) — Reproduces the wedge from #17558: cwd was valid when the
- L133 `test_no_warning_when_cwd_still_exists(self, tmp_path, caplog)` (method)
- L153 `TestUpdateCwdRejectsMissingPaths` (class) — ``_update_cwd`` must not propagate a deleted path back into ``self.cwd``.
- L156 `test_skips_assignment_when_marker_path_missing(self, tmp_path)` (method)
- L173 `test_accepts_assignment_when_marker_path_exists(self, tmp_path)` (method)
