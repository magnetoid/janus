---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# hermes_cli/uninstall.py

Symbols in `hermes_cli/uninstall.py`.

- L19 `log_info(msg: str)` (function)
- L22 `log_success(msg: str)` (function)
- L25 `log_warn(msg: str)` (function)
- L28 `get_project_root()` (function) — Get the project installation directory.
- L33 `find_shell_configs()` (function) — Find shell configuration files that might have PATH entries.
- L53 `remove_path_from_shell_configs()` (function) — Remove Hermes PATH entries from shell configuration files.
- L99 `remove_wrapper_script()` (function) — Remove the hermes wrapper script if it exists.
- L121 `_node_symlink_candidate_dirs()` (function) — Directories where the installer may have placed node/npm/npx symlinks.
- L134 `remove_node_symlinks(hermes_home: Path)` (function) — Remove the node/npm/npx symlinks the installer placed on PATH.
- L179 `uninstall_gateway_service()` (function) — Stop and uninstall the gateway service (systemd, launchd, Windows
- L322 `_hermes_path_markers(hermes_home: Path)` (function) — Path-entry substrings that identify Hermes-owned User-PATH entries.
- L335 `remove_path_from_windows_registry(hermes_home: Path)` (function) — Strip Hermes-owned entries from User-scope PATH in the registry.
- L374 `remove_hermes_env_vars_windows()` (function) — Delete HERMES_HOME and HERMES_GIT_BASH_PATH from User-scope env vars.
- L400 `remove_portable_tooling_windows(hermes_home: Path)` (function) — Delete PortableGit and Node installs the Windows installer created under
- L416 `_is_windows()` (function)
- L421 `_is_default_hermes_home(hermes_home: Path)` (function) — Return True when ``hermes_home`` points at the default (non-profile) root.
- L430 `_discover_named_profiles()` (function) — Return a list of ``ProfileInfo`` for every non-default profile, or ``[]``
- L445 `_uninstall_profile(profile)` (function) — Fully uninstall a single named profile: stop its gateway service,
- L495 `run_gui_uninstall(args)` (function) — GUI-only uninstall: remove the Chat GUI, leave the agent + data intact.
- L567 `run_uninstall(args)` (function) — Run the uninstall process.
- L707 `_perform_uninstall(*, project_root: Path, hermes_home: Path, full_uninstall: bool, remove_profiles: bool, named_profiles: list)` (function) — Execute the uninstall steps. Shared by the interactive and ``--yes``
- L886 `_UninstallArgs` (class) — Lightweight args namespace for the module entrypoint below.
- L889 `__init__(self, *, mode: str)` (method)
- L896 `main(argv=None)` (function) — Module entrypoint: ``python -m hermes_cli.uninstall --mode <gui|lite|full>``.
