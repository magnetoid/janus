---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/test_batch_runner_checkpoint.py

Symbols in `tests/test_batch_runner_checkpoint.py`.

- L17 `runner(tmp_path)` (function) — Create a BatchRunner with all paths pointing at tmp_path.
- L31 `TestSaveCheckpoint` (class) — Verify _save_checkpoint writes valid, atomic JSON.
- L34 `test_writes_valid_json(self, runner)` (method)
- L42 `test_adds_last_updated(self, runner)` (method)
- L50 `test_overwrites_previous_checkpoint(self, runner)` (method)
- L57 `test_with_lock(self, runner)` (method)
- L65 `test_without_lock(self, runner)` (method)
- L72 `test_creates_parent_dirs(self, tmp_path)` (method)
- L81 `test_no_temp_files_left(self, runner)` (method)
- L89 `TestLoadCheckpoint` (class) — Verify _load_checkpoint reads existing data or returns defaults.
- L92 `test_returns_empty_when_no_file(self, runner)` (method)
- L96 `test_loads_existing_checkpoint(self, runner)` (method)
- L105 `test_handles_corrupt_json(self, runner)` (method)
- L113 `TestResumePreservesProgress` (class) — Verify that initializing a run with resume=True loads prior checkpoint.
- L116 `test_completed_prompts_loaded_from_checkpoint(self, runner)` (method)
- L139 `test_different_run_name_starts_fresh(self, runner)` (method)
- L160 `TestBatchWorkerResumeBehavior` (class)
- L161 `test_discarded_no_reasoning_prompts_are_marked_completed(self, tmp_path, monkeypatch)` (method)
- L189 `TestFinalCheckpointNoDuplicates` (class) — Regression: the final checkpoint must not contain duplicate prompt
- L199 `_simulate_final_aggregation_fixed(self, batch_results)` (method) — Mirror the fixed code path in batch_runner.run().
- L207 `test_no_duplicates_in_final_list(self)` (method)
- L217 `test_persisted_checkpoint_has_unique_prompts(self, runner)` (method) — Write what run()'s fixed aggregation produces to disk; the file
- L235 `test_old_buggy_pattern_would_have_duplicates(self)` (method) — Document the bug this PR fixes: the old code shape produced
