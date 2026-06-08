---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/tools/test_file_ops_cwd_tracking.py

Symbols in `tests/tools/test_file_ops_cwd_tracking.py`.

- L25 `_FakeEnv` (class) — Minimal terminal env that tracks cwd across execute() calls.
- L34 `__init__(self, start_cwd: str)` (method)
- L38 `execute(self, command: str, cwd: str=None, **kwargs)` (method)
- L62 `TestShellFileOpsCwdTracking` (class) — _exec() must use live env.cwd, not the init-time cached cwd.
- L65 `test_exec_follows_env_cwd_after_cd(self, tmp_path)` (method)
- L90 `test_patch_replace_targets_live_cwd_not_init_cwd(self, tmp_path)` (method) — The exact bug reported: patch lands in wrong dir after cd.
- L117 `test_explicit_cwd_arg_still_wins(self, tmp_path)` (method) — An explicit cwd= arg to _exec must override both env.cwd and self.cwd.
- L136 `test_env_without_cwd_attribute_falls_back_to_self_cwd(self, tmp_path)` (method) — Backends without a cwd attribute still work via init-time cwd.
- L155 `test_patch_returns_success_only_when_file_actually_written(self, tmp_path)` (method) — Safety rail: patch_replace success must reflect the real file state.
