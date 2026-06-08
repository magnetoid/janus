---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/tools/test_file_read_guards.py

Symbols in `tests/tools/test_file_read_guards.py`.

- L34 `_FakeReadResult` (class) — Minimal stand-in for FileOperations.read_file return value.
- L36 `__init__(self, content='line1\nline2\n', total_lines=2, file_size=100)` (method)
- L41 `to_dict(self)` (method)
- L49 `_make_fake_ops(content='hello\n', total_lines=1, file_size=6)` (function)
- L57 `_make_safe_tempdir(prefix: str)` (function) — Create a temp dir outside macOS system-sensitive /private/var paths.
- L66 `TestDevicePathBlocking` (class) — Paths like /dev/zero should be rejected before any I/O.
- L69 `test_blocked_device_detection(self)` (method)
- L75 `test_safe_device_not_blocked(self)` (method)
- L79 `test_proc_fd_blocked(self)` (method)
- L83 `test_proc_fd_other_not_blocked(self)` (method)
- L95 `test_proc_sensitive_pseudo_files_blocked(self)` (method) — environ/cmdline/maps under /proc/<pid> must be blocked (issue #4427).
- L107 `test_proc_legitimate_files_not_blocked(self)` (method) — Top-level /proc files like cpuinfo and meminfo must remain accessible.
- L112 `test_normal_files_not_blocked(self)` (method)
- L116 `test_symlink_to_blocked_device_is_blocked(self)` (method)
- L125 `test_symlink_to_regular_file_not_blocked(self)` (method)
- L137 `test_read_file_tool_rejects_device(self)` (method) — read_file_tool returns an error without any file I/O.
- L144 `test_read_file_tool_rejects_device_symlink_before_io(self, mock_ops)` (method)
- L163 `TestCharacterCountGuard` (class) — Large reads should be rejected with guidance to use offset/limit.
- L166 `setUp(self)` (method)
- L169 `tearDown(self)` (method)
- L174 `test_oversized_read_rejected(self, _mock_limit, mock_ops)` (method) — A read that returns >max chars is rejected.
- L189 `test_small_read_not_rejected(self, mock_ops)` (method) — Normal-sized reads pass through fine.
- L198 `test_content_under_limit_passes(self, _mock_limit, mock_ops)` (method) — Content just under the limit should pass through fine.
- L213 `TestFileDedup` (class) — Re-reading an unchanged file should return a lightweight stub.
- L216 `setUp(self)` (method)
- L223 `tearDown(self)` (method)
- L232 `test_second_read_returns_dedup_stub(self, mock_ops)` (method) — Second read of same file+range returns non-content dedup status.
- L250 `test_write_rejects_internal_read_status_text(self, mock_ops)` (method) — write_file must not persist internal read_file status text.
- L267 `test_write_rejects_status_text_with_small_framing(self, mock_ops)` (method) — write_file rejects small wrappers around the status text too.
- L291 `test_write_allows_large_file_that_quotes_status_text(self, mock_ops)` (method) — Legitimate large content that happens to quote the status is allowed.
- L323 `test_modified_file_not_deduped(self, mock_ops)` (method) — After the file is modified, dedup returns full content.
- L339 `test_different_range_not_deduped(self, mock_ops)` (method) — Same file but different offset/limit should not dedup.
- L352 `test_different_task_not_deduped(self, mock_ops)` (method) — Different task_ids have separate dedup caches.
- L367 `TestDedupStubLoopGuard` (class) — Repeated dedup stubs must escalate to a hard BLOCKED error so weak
- L372 `setUp(self)` (method)
- L379 `tearDown(self)` (method)
- L388 `test_third_read_is_blocked(self, mock_ops)` (method) — read → stub → BLOCKED.  Second stub escalates to hard error.
- L414 `test_subsequent_reads_stay_blocked(self, mock_ops)` (method) — Once blocked, continued hammering keeps returning BLOCKED.
- L430 `test_file_modification_clears_block(self, mock_ops)` (method) — Real file change should break out of the block — new content
- L451 `test_other_tool_call_clears_hits(self, mock_ops)` (method) — An intervening non-read tool call resets stub-hit counters,
- L470 `test_different_ranges_tracked_independently(self, mock_ops)` (method) — Stub-hit counter is keyed by (path, offset, limit), so hammering
- L491 `test_reset_file_dedup_clears_hits(self, mock_ops)` (method) — Post-compression reset must clear stub-hit counters too,
- L514 `TestDedupResetOnCompression` (class) — reset_file_dedup should clear the dedup cache so post-compression
- L518 `setUp(self)` (method)
- L525 `tearDown(self)` (method)
- L534 `test_reset_clears_dedup(self, mock_ops)` (method) — After reset_file_dedup, the same read returns full content.
- L555 `test_reset_all_tasks(self, mock_ops)` (method) — reset_file_dedup(None) clears all tasks.
- L571 `test_reset_preserves_loop_detection(self, mock_ops)` (method) — reset_file_dedup does NOT affect the consecutive-read counter.
- L596 `TestLargeFileHint` (class) — Large truncated files should include a hint about targeted reads.
- L599 `setUp(self)` (method)
- L602 `tearDown(self)` (method)
- L606 `test_large_truncated_file_gets_hint(self, mock_ops)` (method)
- L632 `TestConfigOverride` (class) — file_read_max_chars in config.yaml should control the char guard.
- L635 `setUp(self)` (method)
- L641 `tearDown(self)` (method)
- L648 `test_custom_config_lowers_limit(self, _mock_cfg, mock_ops)` (method) — A config value of 50 should reject reads over 50 chars.
- L658 `test_custom_config_raises_limit(self, _mock_cfg, mock_ops)` (method) — A config value of 500K should allow reads up to 500K chars.
- L673 `TestWriteInvalidatesDedup` (class) — write_file_tool and patch_tool must invalidate the read_file dedup
- L681 `setUp(self)` (method)
- L688 `tearDown(self)` (method)
- L697 `test_write_invalidates_dedup_same_second(self, mock_ops)` (method) — read→write→read within the same mtime second returns fresh content.
- L732 `test_write_invalidates_all_offsets(self, mock_ops)` (method) — A write invalidates dedup entries for ALL offset/limit combos.
- L759 `test_write_does_not_invalidate_other_files(self, mock_ops)` (method) — Writing file A should not invalidate dedup for file B.
- L791 `test_write_does_not_invalidate_other_tasks(self, mock_ops)` (method) — Writing in task A should not invalidate dedup for task B.
- L821 `test_invalidate_dedup_for_path_noop_on_missing_task(self)` (method) — _invalidate_dedup_for_path is safe when task_id doesn't exist.
- L827 `test_invalidate_dedup_for_path_noop_on_empty_dedup(self)` (method) — _invalidate_dedup_for_path is safe when dedup dict is empty.
