---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:44'
updated: '2026-06-08T00:38:44'
---

# tools/environments/local.py

Symbols in `tools/environments/local.py`.

- L22 `_msys_to_windows_path(cwd: str)` (function) — Translate a Git Bash / MSYS-style POSIX path (``/c/Users/x``) to the
- L42 `_resolve_safe_cwd(cwd: str)` (function) — Return ``cwd`` if it exists as a directory, else the nearest existing
- L100 `_build_provider_env_blocklist()` (function) — Derive the blocklist from provider, tool, and gateway config.
- L194 `_inject_context_hermes_home(env: dict)` (function) — Bridge the context-local Hermes home override into subprocess env.
- L206 `_sanitize_subprocess_env(base_env: dict | None, extra_env: dict | None=None)` (function) — Filter Hermes-managed secrets from a subprocess environment.
- L239 `_find_bash()` (function) — Find bash for command execution.
- L303 `_make_run_env(env: dict)` (function) — Build a run environment with a sane PATH and provider-var stripping.
- L354 `_read_terminal_shell_init_config()` (function) — Return (shell_init_files, auto_source_bashrc) from config.yaml.
- L374 `_resolve_shell_init_files()` (function) — Resolve the list of files to source before the login-shell snapshot.
- L416 `_prepend_shell_init(cmd_string: str, files: list[str])` (function) — Prepend ``source <file>`` lines (guarded + silent) to a bash script.
- L437 `LocalEnvironment` (class) — Run commands directly on the host machine.
- L445 `__init__(self, cwd: str='', timeout: int=60, env: dict=None)` (method)
- L451 `get_temp_dir(self)` (method) — Return a shell-safe writable temp dir for local execution.
- L499 `_run_bash(self, cmd_string: str, *, login: bool=False, timeout: int=120, stdin_data: str | None=None)` (method)
- L569 `_kill_process(self, proc)` (method) — Kill the entire process group (all children).
- L639 `_update_cwd(self, result: dict)` (method) — Read CWD from temp file (local-only, no round-trip needed).
- L667 `_extract_cwd_from_output(self, result: dict)` (method) — Same semantics as the base class, but on Windows the value
- L691 `cleanup(self)` (method) — Clean up temp files.
