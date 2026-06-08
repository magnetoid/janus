---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# hermes_cli/profiles.py

Symbols in `hermes_cli/profiles.py`.

- L111 `has_bundled_skills_opt_out(profile_dir: Path)` (function) — Return True if the profile opted out of bundled-skill seeding.
- L119 `_clone_all_copytree_ignore(source_dir: Path)` (function) — Exclude infrastructure artifacts when cloning a profile via --clone-all.
- L212 `_get_profiles_root()` (function) — Return the directory where named profiles are stored.
- L226 `_get_default_hermes_home()` (function) — Return the default (pre-profile) HERMES_HOME path.
- L237 `_get_active_profile_path()` (function) — Return the path to the sticky active_profile file.
- L242 `_get_wrapper_dir()` (function) — Return the directory for wrapper scripts.
- L251 `normalize_profile_name(name: str)` (function) — Return the canonical profile id used on disk and in CLI ``-p`` argv.
- L269 `validate_profile_name(name: str)` (function) — Raise ``ValueError`` if *name* is not a valid profile identifier.
- L299 `get_profile_dir(name: str)` (function) — Resolve a profile name to its HERMES_HOME directory.
- L307 `profile_exists(name: str)` (function) — Check whether a profile directory exists.
- L319 `check_alias_collision(name: str)` (function) — Return a human-readable collision message, or None if the name is safe.
- L356 `_is_wrapper_dir_in_path()` (function) — Check if ~/.local/bin is in PATH.
- L362 `create_wrapper_script(name: str, target: Optional[str]=None)` (function) — Create a shell wrapper script at ~/.local/bin/<name>.
- L401 `remove_wrapper_script(name: str)` (function) — Remove the wrapper script for a profile. Returns True if removed.
- L425 `find_alias_for_profile(profile_name: str)` (function) — Return the alias name of the wrapper that activates *profile_name*, or None.
- L474 `ProfileInfo` (class) — Summary information about a profile.
- L506 `_read_distribution_meta(profile_dir: Path)` (function) — Return ``(name, version, source)`` from the profile's ``distribution.yaml``
- L531 `_read_config_model(profile_dir: Path)` (function) — Read model/provider from a profile's config.yaml. Returns (model, provider).
- L550 `_check_gateway_running(profile_dir: Path)` (function) — Check if a gateway is running for a given profile directory.
- L559 `_count_skills(profile_dir: Path)` (function) — Count installed skills in a profile.
- L586 `_profile_yaml_path(profile_dir: Path)` (function)
- L590 `read_profile_meta(profile_dir: Path)` (function) — Read ``<profile_dir>/profile.yaml`` and return a dict.
- L615 `write_profile_meta(profile_dir: Path, *, description: Optional[str]=None, description_auto: Optional[bool]=None)` (function) — Update ``<profile_dir>/profile.yaml`` in place.
- L652 `list_profiles()` (function) — Return info for all profiles, including the default.
- L718 `create_profile(name: str, clone_from: Optional[str]=None, clone_all: bool=False, clone_config: bool=False, no_alias: bool=False, no_skills: bool=False, description: Optional[str]=None)` (function) — Create a new profile directory.
- L883 `seed_profile_skills(profile_dir: Path, quiet: bool=False)` (function) — Seed bundled skills into a profile via subprocess.
- L928 `delete_profile(name: str, yes: bool=False)` (function) — Delete a profile, its wrapper script, and its gateway service.
- L1071 `_maybe_register_gateway_service(profile_name: str)` (function) — Register a profile's gateway with s6 inside the container.
- L1125 `_maybe_unregister_gateway_service(profile_name: str)` (function) — Tear down a profile's s6 gateway service inside the container.
- L1152 `_cleanup_gateway_service(name: str, profile_dir: Path)` (function) — Disable and remove systemd/launchd service for a profile.
- L1200 `_stop_gateway_process(profile_dir: Path)` (function) — Stop a running gateway process via its PID file.
- L1243 `get_active_profile()` (function) — Read the sticky active profile name.
- L1258 `set_active_profile(name: str)` (function) — Set the sticky active profile.
- L1283 `get_active_profile_name()` (function) — Infer the current profile name from HERMES_HOME.
- L1314 `_default_export_ignore(root_dir: Path)` (function) — Return an *ignore* callable for :func:`shutil.copytree`.
- L1338 `export_profile(name: str, output_path: str)` (function) — Export a profile to a tar.gz archive.
- L1382 `_normalize_profile_archive_parts(member_name: str)` (function) — Return safe path parts for a profile archive member.
- L1402 `_safe_extract_profile_archive(archive: Path, destination: Path)` (function) — Extract a profile archive without allowing path escapes or links.
- L1434 `_inspect_profile_archive_roots(archive: Path)` (function) — Return the archive's top-level directory names.
- L1459 `import_profile(archive_path: str, name: Optional[str]=None)` (function) — Import a profile from a tar.gz archive.
- L1526 `_migrate_honcho_profile_host(old_name: str, new_name: str, new_dir: Path)` (function) — Rename Honcho host blocks for a renamed profile without changing peers.
- L1586 `rename_profile(old_name: str, new_name: str)` (function) — Rename a profile: directory, wrapper script, service, active_profile.
- L1645 `resolve_profile_env(profile_name: str)` (function) — Resolve a profile name to a HERMES_HOME path string.
