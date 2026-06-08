---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/tools/test_file_staleness.py

Symbols in `tests/tools/test_file_staleness.py`.

- L33 `_FakeReadResult` (class)
- L34 `__init__(self, content='line1\nline2\n', total_lines=2, file_size=100)` (method)
- L39 `to_dict(self)` (method)
- L47 `_FakeWriteResult` (class)
- L48 `__init__(self)` (method)
- L51 `to_dict(self)` (method)
- L55 `_FakePatchResult` (class)
- L56 `__init__(self)` (method)
- L59 `to_dict(self)` (method)
- L63 `_make_fake_ops(read_content='hello\n', file_size=6)` (function)
- L77 `TestStalenessCheck` (class)
- L79 `setUp(self)` (method)
- L87 `tearDown(self)` (method)
- L97 `test_no_warning_when_file_unchanged(self, mock_ops)` (method) — Read then write with no external modification — no warning.
- L106 `test_warning_when_file_modified_externally(self, mock_ops)` (method) — Read, then external modify, then write — should warn.
- L121 `test_no_warning_when_file_never_read(self, mock_ops)` (method) — Writing a file that was never read — no warning.
- L128 `test_no_warning_for_new_file(self, mock_ops)` (method) — Creating a new file — no warning.
- L140 `test_different_task_isolated(self, mock_ops)` (method) — Task A reads, file changes, Task B writes — no warning for B.
- L153 `test_relative_path_uses_live_cwd_for_staleness_tracking(self, mock_ops)` (method) — Relative-path stale tracking must follow the live terminal cwd.
- L204 `TestPatchStaleness` (class)
- L206 `setUp(self)` (method)
- L214 `tearDown(self)` (method)
- L224 `test_patch_warns_on_stale_file(self, mock_ops)` (method) — Patch should warn if the target file changed since last read.
- L242 `test_patch_no_warning_when_fresh(self, mock_ops)` (method) — Patch with no external changes — no warning.
- L259 `TestCheckFileStalenessHelper` (class)
- L261 `setUp(self)` (method)
- L265 `tearDown(self)` (method)
- L269 `test_returns_none_for_unknown_task(self)` (method)
- L272 `test_returns_none_for_unread_file(self)` (method)
- L283 `test_returns_none_when_stat_fails(self)` (method)
