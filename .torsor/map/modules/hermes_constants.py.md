---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# hermes_constants.py

Symbols in `hermes_constants.py`.

- L21 `set_hermes_home_override(path: str | Path | None)` (function) — Set a context-local Hermes home override and return its reset token.
- L31 `reset_hermes_home_override(token: Token)` (function) — Restore the previous context-local Hermes home override.
- L36 `get_hermes_home_override()` (function) — Return the active context-local Hermes home override, if any.
- L44 `_get_platform_default_hermes_home()` (function) — Return the platform-native default Hermes home path.
- L53 `get_hermes_home()` (function) — Return the Hermes home directory (default: platform-native path).
- L111 `get_default_hermes_root()` (function) — Return the root Hermes directory for profile-level operations.
- L151 `_get_packaged_data_dir(name: str)` (function) — Return an installed data-files directory if one exists.
- L168 `get_optional_skills_dir(default: Path | None=None)` (function) — Return the optional-skills directory, honoring package-manager wrappers.
- L185 `get_optional_mcps_dir(default: Path | None=None)` (function) — Return the optional-mcps directory, honoring package-manager wrappers.
- L204 `get_bundled_skills_dir(default: Path | None=None)` (function) — Return the bundled skills directory for source and packaged installs.
- L224 `get_hermes_dir(new_subpath: str, old_name: str)` (function) — Resolve a Hermes subdirectory with backward compatibility.
- L245 `display_hermes_home()` (function) — Return a user-friendly display string for the current HERMES_HOME.
- L265 `secure_parent_dir(path: Path)` (function) — Chmod ``0o700`` on the parent directory of *path*, but only if safe.
- L285 `get_subprocess_home()` (function) — Return a per-profile HOME directory for subprocesses, or None.
- L314 `parse_reasoning_effort(effort: str)` (function) — Parse a reasoning effort level into a config dict.
- L332 `is_termux()` (function) — Return True when running inside a Termux (Android) environment.
- L345 `is_wsl()` (function) — Return True when running inside WSL (Windows Subsystem for Linux).
- L366 `is_container()` (function) — Return True when running inside a Docker/Podman container.
- L397 `get_config_path()` (function) — Return the path to ``config.yaml`` under HERMES_HOME.
- L406 `get_skills_dir()` (function) — Return the path to the skills directory under HERMES_HOME.
- L412 `get_env_path()` (function) — Return the path to the ``.env`` file under HERMES_HOME.
- L420 `apply_ipv4_preference(force: bool=False)` (function) — Monkey-patch ``socket.getaddrinfo`` to prefer IPv4 connections.
