---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# hermes_cli/managed_uv.py

Symbols in `hermes_cli/managed_uv.py`.

- L30 `managed_uv_path()` (function) — Return the path where Hermes keeps *its* uv binary.
- L43 `resolve_uv()` (function) — Return the managed uv path if it exists, else ``None``.
- L54 `_UvResult` (class) — ``ensure_uv()`` return value that survives an update boundary.
- L82 `__new__(cls, path: Optional[str], fresh: bool=False)` (method)
- L87 `__iter__(self)` (method)
- L94 `_ensure_uv_path()` (function) — Resolve the managed uv path, installing it if necessary (plain ``str``/``None``).
- L127 `ensure_uv()` (function) — Return the managed uv path, installing it first if necessary.
- L158 `update_managed_uv()` (function) — Run ``uv self update`` on the managed uv binary.
- L194 `_install_uv(target: Path)` (function) — Bootstrap uv into *target* using the official standalone installer.
- L217 `_install_uv_posix(env: dict[str, str])` (function) — Download + sh the POSIX installer (two-stage to avoid curl|sh pitfalls).
- L241 `_install_uv_windows(env: dict[str, str])` (function) — Invoke the PowerShell installer.
- L253 `rebuild_venv(uv_bin: str, venv_dir: Path, python_version: str='3.11')` (function)
