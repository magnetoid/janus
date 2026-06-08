---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/tools/test_env_probe.py

Symbols in `tests/tools/test_env_probe.py`.

- L11 `reset_probe_cache()` (function) — Each test starts with a clean cache.
- L18 `TestSilentWhenHealthy` (class) — The probe must emit nothing when the environment is clean — otherwise
- L22 `test_clean_env_returns_empty(self, monkeypatch)` (method) — python3 + pip module + no PEP 668 → silent.
- L32 `test_pep668_with_uv_returns_empty(self, monkeypatch)` (method) — PEP 668 alone shouldn't trigger output if uv is installed —
- L45 `TestEmitsOnRealProblems` (class) — The probe must produce a usable line for the real failure modes
- L49 `test_allen_scenario_python_version_mismatch(self, monkeypatch)` (method) — python3 is 3.11 (no pip module), pip on PATH is 3.12, PEP 668 on,
- L72 `test_missing_python3_is_named(self, monkeypatch)` (method) — If python3 isn't installed at all, say so.
- L83 `test_python_missing_but_python3_present(self, monkeypatch)` (method) — Common on Debian: only python3 exists, agent shouldn't type
- L101 `TestSkipsRemoteBackends` (class) — Remote backends have their own probe; this one must stay out.
- L104 `test_docker_returns_empty(self, monkeypatch)` (method)
- L111 `test_modal_returns_empty(self, monkeypatch)` (method)
- L115 `test_ssh_returns_empty(self, monkeypatch)` (method)
- L120 `TestCaching` (class) — The probe runs once per process — the result is deterministic for
- L124 `test_result_cached(self, monkeypatch)` (method)
- L146 `TestRobustness` (class) — The probe must NEVER crash the prompt build.
- L149 `test_subprocess_failure_returns_empty(self, monkeypatch)` (method) — If every subprocess fails, just stay silent.
