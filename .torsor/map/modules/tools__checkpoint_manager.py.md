---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:44'
updated: '2026-06-08T00:38:44'
---

# tools/checkpoint_manager.py

Symbols in `tools/checkpoint_manager.py`.

- L157 `_validate_commit_hash(commit_hash: str)` (function) — Validate a commit hash to prevent git argument injection.
- L173 `_validate_file_path(file_path: str, working_dir: str)` (function) — Validate a file path to prevent path traversal outside the working directory.
- L195 `_normalize_path(path_value: str)` (function) — Return a canonical absolute path for checkpoint operations.
- L200 `_project_hash(working_dir: str)` (function) — Deterministic per-project hash: sha256(abs_path)[:16].
- L206 `_store_path(base: Optional[Path]=None)` (function) — Return the single shared shadow store path.
- L211 `_shadow_repo_path(working_dir: str)` (function) — Return the shared store path.
- L222 `_index_path(store: Path, dir_hash: str)` (function)
- L226 `_ref_name(dir_hash: str)` (function)
- L230 `_project_meta_path(store: Path, dir_hash: str)` (function)
- L238 `_git_env(store: Path, working_dir: str, index_file: Optional[Path]=None)` (function) — Build env dict that redirects git to the shared store.
- L275 `_run_git(args: List[str], store: Path, working_dir: str, timeout: int=_GIT_TIMEOUT, allowed_returncodes: Optional[Set[int]]=None, index_file: Optional[Path]=None)` (function) — Run a git command against the shared store.  Returns (ok, stdout, stderr).
- L341 `_migrate_legacy_store(base: Path)` (function) — Move pre-v2 per-project shadow repos into a ``legacy-<ts>/`` dir.
- L389 `_init_store(store: Path, working_dir: str)` (function) — Initialise the shared shadow store if needed.  Returns error or None.
- L455 `_register_project(store: Path, working_dir: str)` (function) — Create or update ``projects/<hash>.json`` with workdir + timestamps.
- L476 `_touch_project(store: Path, working_dir: str)` (function) — Update last_touch for a project, preserving created_at.
- L498 `_list_projects(store: Path)` (function) — Return all registered projects under the store.
- L517 `_dir_file_count(path: str)` (function) — Quick file count estimate (stops early if over _MAX_FILES).
- L530 `_dir_size_bytes(path: Path)` (function) — Best-effort recursive size in bytes.  Returns 0 on error.
- L550 `_init_shadow_repo(shadow_repo: Path, working_dir: str)` (function) — Backwards-compatible initialiser.
- L577 `CheckpointManager` (class) — Manages automatic filesystem checkpoints.
- L599 `__init__(self, enabled: bool=False, max_snapshots: int=20, max_total_size_mb: int=500, max_file_size_mb: int=10)` (method)
- L617 `new_turn(self)` (method) — Reset per-turn dedup.  Call at the start of each agent iteration.
- L625 `ensure_checkpoint(self, working_dir: str, reason: str='auto')` (method) — Take a checkpoint if enabled and not already done this turn.
- L659 `list_checkpoints(self, working_dir: str)` (method) — List available checkpoints for a directory (most recent first).
- L701 `_parse_shortstat(stat_line: str, entry: Dict)` (method) — Parse git --shortstat output into entry dict.
- L713 `diff(self, working_dir: str, commit_hash: str)` (method) — Show diff between a checkpoint and the current working tree.
- L763 `restore(self, working_dir: str, commit_hash: str, file_path: str=None)` (method) — Restore files to a checkpoint state.
- L820 `get_working_dir_for_path(self, file_path: str)` (method) — Resolve a file path to its working directory for checkpointing.
- L842 `_take(self, working_dir: str, reason: str)` (method) — Take a snapshot.  Returns True on success.
- L976 `_drop_oversize_from_index(self, store: Path, working_dir: str, index_file: Path)` (method) — Remove any staged file larger than ``max_file_size_mb`` from the index.
- L1022 `_prune(self, store: Path, working_dir: str, ref: str)` (method) — Keep only the last ``max_snapshots`` commits on the per-project ref.
- L1088 `_enforce_size_cap(self, store: Path)` (method) — If total store size exceeds ``max_total_size_mb``, drop oldest
- L1176 `format_checkpoint_list(checkpoints: List[Dict], directory: str)` (function) — Format checkpoint list for display to user.
- L1216 `_delete_ref(store: Path, ref: str)` (function) — Delete a ref from the store.  Returns True on success.
- L1225 `prune_checkpoints(retention_days: int=7, delete_orphans: bool=True, checkpoint_base: Optional[Path]=None, max_total_size_mb: int=0)` (function) — Delete stale/orphan checkpoints and reclaim store space.
- L1464 `maybe_auto_prune_checkpoints(retention_days: int=7, min_interval_hours: int=24, delete_orphans: bool=True, checkpoint_base: Optional[Path]=None, max_total_size_mb: int=0)` (function) — Idempotent wrapper around ``prune_checkpoints`` for startup hooks.
- L1535 `store_status(checkpoint_base: Optional[Path]=None)` (function) — Return a summary of the shadow store.
- L1602 `clear_all(checkpoint_base: Optional[Path]=None)` (function) — Nuke the entire checkpoint base (store + legacy).  Irreversible.
- L1621 `clear_legacy(checkpoint_base: Optional[Path]=None)` (function) — Delete all ``legacy-*`` archive directories.
