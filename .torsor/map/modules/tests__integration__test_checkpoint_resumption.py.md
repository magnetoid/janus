---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/integration/test_checkpoint_resumption.py

Symbols in `tests/integration/test_checkpoint_resumption.py`.

- L36 `create_test_dataset(num_prompts: int=20)` (function) — Create a small test dataset for checkpoint testing.
- L55 `monitor_checkpoint_during_run(checkpoint_file: Path, duration: int=30)` (function) — Monitor checkpoint file during a batch run to see when it gets updated.
- L110 `_cleanup_test_artifacts(*paths)` (function) — Remove test-generated files and directories.
- L120 `test_current_implementation()` (function) — Test the current checkpoint implementation.
- L215 `test_interruption_and_resume()` (function) — Test that resume actually works after interruption.
- L313 `test_simulated_crash()` (function) — Test behavior when process crashes mid-execution.
- L323 `print_test_plan()` (function) — Print the detailed test and fix plan.
- L389 `main(test_current: bool=False, test_resume: bool=False, test_crash: bool=False, compare: bool=False, show_plan: bool=False)` (function) — Run checkpoint behavior tests.
