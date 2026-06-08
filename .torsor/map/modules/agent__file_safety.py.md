---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# agent/file_safety.py

Symbols in `agent/file_safety.py`.

- L10 `_hermes_home_path()` (function) — Resolve the active HERMES_HOME (profile-aware) without circular imports.
- L19 `_hermes_root_path()` (function) — Resolve the Hermes root dir (always the parent of any profile, never per-profile).
- L28 `build_write_denied_paths(home: str)` (function) — Return exact sensitive paths that must never be written.
- L66 `build_write_denied_prefixes(home: str)` (function) — Return sensitive directory prefixes that must never be written.
- L85 `get_safe_write_root()` (function) — Return the resolved HERMES_WRITE_SAFE_ROOT path, or None if unset.
- L96 `is_write_denied(path: str)` (function) — Return True if path is blocked by the write denylist or safe root.
- L165 `get_read_block_error(path: str)` (function) — Return an error message when a read targets a denied Hermes path.
- L339 `_resolve_active_profile_name()` (function) — Return the active profile name derived from HERMES_HOME.
- L364 `classify_cross_profile_target(path: str)` (function) — Classify a write target as cross-profile if it lands in another
- L427 `get_cross_profile_warning(path: str)` (function) — Return a model-facing warning string when ``path`` is cross-profile.
- L480 `_find_sandbox_mirror_segments(parts: tuple)` (function) — Return the index of the inner ``.hermes`` part in a sandbox-mirror path.
- L498 `classify_sandbox_mirror_target(path: str)` (function) — Classify a write target as a sandbox-mirror of authoritative Hermes state.
- L534 `get_sandbox_mirror_warning(path: str)` (function) — Return a model-facing warning when ``path`` lands in a sandbox mirror.
- L582 `classify_container_mirror_target(path: str, mirror_prefix: str | None=None)` (function) — Classify a write target as a container-side sandbox mirror.
- L613 `get_container_mirror_warning(path: str, mirror_prefix: str | None=None)` (function) — Return a model-facing warning when *path* lands in the container's
