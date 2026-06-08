---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:44'
updated: '2026-06-08T00:38:44'
---

# tools/environments/singularity.py

Symbols in `tools/environments/singularity.py`.

- L30 `_find_singularity_executable()` (function) — Locate the apptainer or singularity CLI binary.
- L43 `_ensure_singularity_available()` (function) — Preflight check: resolve the executable and verify it responds.
- L63 `_load_snapshots()` (function)
- L67 `_save_snapshots(data: dict)` (function)
- L71 `_get_scratch_dir()` (function)
- L92 `_get_apptainer_cache_dir()` (function)
- L107 `_get_or_build_sif(image: str, executable: str='apptainer')` (function)
- L156 `SingularityEnvironment` (class) — Hardened Singularity/Apptainer container with resource limits and persistence.
- L164 `__init__(self, image: str, cwd: str='~', timeout: int=60, cpu: float=0, memory: int=0, disk: int=0, persistent_filesystem: bool=False, task_id: str='default')` (method)
- L195 `_start_instance(self)` (method)
- L230 `_run_bash(self, cmd_string: str, *, login: bool=False, timeout: int=120, stdin_data: str | None=None)` (method) — Spawn a bash process inside the Singularity instance.
- L246 `cleanup(self)` (method) — Stop the instance. If persistent, the overlay dir survives.
