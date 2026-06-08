---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:44'
updated: '2026-06-08T00:38:44'
---

# tools/credential_files.py

Symbols in `tools/credential_files.py`.

- L38 `_get_registered()` (function) — Get or create the registered credential files dict for the current context/session.
- L52 `_resolve_hermes_home()` (function)
- L57 `register_credential_file(relative_path: str, container_base: str='/root/.hermes')` (function) — Register a credential file for mounting into remote sandboxes.
- L107 `register_credential_files(entries: list, container_base: str='/root/.hermes')` (function) — Register multiple credential files from skill frontmatter entries.
- L132 `_load_config_files()` (function) — Load ``terminal.credential_files`` from config.yaml (cached).
- L177 `get_credential_file_mounts()` (function) — Return all credential files that should be mounted into remote sandboxes.
- L203 `get_skills_directory_mount(container_base: str='/root/.hermes')` (function) — Return mount info for all skill directories (local + external).
- L251 `_safe_skills_path(skills_dir: Path)` (function) — Return *skills_dir* if symlink-free, else a sanitized temp copy.
- L294 `iter_skills_files(container_base: str='/root/.hermes')` (function) — Yield individual (host_path, container_path) entries for skills files.
- L354 `get_cache_directory_mounts(container_base: str='/root/.hermes')` (function) — Return mount entries for each cache directory that exists on disk.
- L378 `map_cache_path_to_container(host_path: str, container_base: str='/root/.hermes')` (function) — Map a host cache path to its mounted path under *container_base*.
- L402 `to_agent_visible_cache_path(host_path: str, container_base: str='/root/.hermes')` (function) — Translate a host cache path to its mounted path inside the sandbox.
- L423 `iter_cache_files(container_base: str='/root/.hermes')` (function) — Return individual (host_path, container_path) entries for cache files.
- L450 `clear_credential_files()` (function) — Reset the skill-scoped registry (e.g. on session reset).
