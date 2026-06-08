---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:44'
updated: '2026-06-08T00:38:44'
---

# tests/tools/test_singularity_preflight.py

Symbols in `tests/tools/test_singularity_preflight.py`.

- L20 `TestFindSingularityExecutable` (class) — _find_singularity_executable resolution tests.
- L23 `test_prefers_apptainer(self)` (method) — When both are available, apptainer should be preferred.
- L31 `test_falls_back_to_singularity(self)` (method) — When only singularity is available, use it.
- L39 `test_raises_when_neither_found(self)` (method) — Must raise RuntimeError with install instructions.
- L46 `TestEnsureSingularityAvailable` (class) — _ensure_singularity_available preflight tests.
- L49 `test_returns_executable_on_success(self)` (method) — Returns the executable name when version check passes.
- L57 `test_raises_on_version_failure(self)` (method) — Raises RuntimeError when version command fails.
- L66 `test_raises_on_timeout(self)` (method) — Raises RuntimeError when version command times out.
- L73 `test_raises_when_not_installed(self)` (method) — Raises RuntimeError when neither executable exists.
