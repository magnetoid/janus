---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:44'
updated: '2026-06-08T00:38:44'
---

# tools/env_probe.py

Symbols in `tools/env_probe.py`.

- L56 `_run(cmd: list[str], timeout: float=3.0)` (function) — Run a short subprocess.  Returns (returncode, stdout, stderr).
- L78 `_python_version_of(binary: str)` (function) — Return a short version string like ``3.12.4`` for ``binary``, or None.
- L88 `_has_pip_module(binary: str)` (function) — True if ``<binary> -m pip --version`` succeeds.
- L96 `_detect_pep668(binary: str)` (function) — True when ``<binary>``'s install location is PEP-668 externally-managed.
- L114 `_pip_python_version()` (function) — If ``pip`` is on PATH, return the Python version it's bound to.
- L138 `_build_probe_line()` (function) — Build the one-liner.  Returns "" when nothing notable is detected.
- L214 `get_environment_probe_line(*, force_refresh: bool=False)` (function) — Return the cached probe line (building it on first call).
- L243 `_reset_cache_for_tests()` (function) — Test helper — clear the cache between probe scenarios.
