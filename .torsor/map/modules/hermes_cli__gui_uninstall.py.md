---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# hermes_cli/gui_uninstall.py

Symbols in `hermes_cli/gui_uninstall.py`.

- L48 `log_info(msg: str)` (function)
- L52 `log_success(msg: str)` (function)
- L56 `log_warn(msg: str)` (function)
- L65 `_agent_root(hermes_home: Path)` (function) — The agent checkout root — same layout install.sh / install.ps1 use.
- L70 `desktop_userdata_dir()` (function) — Return the Electron ``userData`` directory for the desktop app.
- L90 `source_built_gui_artifacts(hermes_home: Path)` (function) — GUI build artifacts produced by ``hermes desktop`` inside the checkout.
- L111 `packaged_gui_app_paths()` (function) — Standard install locations of the packaged desktop distributable.
- L154 `agent_is_installed(hermes_home: Path)` (function) — Return True when a usable Python agent install exists under HERMES_HOME.
- L171 `gui_is_installed(hermes_home: Path)` (function) — Return True when any desktop GUI artifact exists (built or packaged).
- L184 `gui_install_summary(hermes_home: 'Path | None'=None)` (function) — Structured snapshot of what's installed, for the desktop UI to render.
- L214 `_remove_path(path: Path)` (function) — Remove a file or directory tree. Returns True when something was removed.
- L228 `uninstall_gui(hermes_home: 'Path | None'=None, *, remove_userdata: bool=True)` (function) — Remove the desktop GUI's artifacts, leaving the agent + user data intact.
