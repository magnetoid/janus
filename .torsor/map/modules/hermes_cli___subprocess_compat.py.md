---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# hermes_cli/_subprocess_compat.py

Symbols in `hermes_cli/_subprocess_compat.py`.

- L52 `resolve_node_command(name: str, argv: Sequence[str])` (function) — Resolve a Node-ecosystem command name to an absolute-path argv.
- L113 `windows_detach_flags()` (function) — Return Win32 creationflags that detach a child from the parent
- L156 `windows_detach_flags_without_breakaway()` (function) — Same as :func:`windows_detach_flags` minus ``CREATE_BREAKAWAY_FROM_JOB``.
- L186 `windows_hide_flags()` (function) — Return Win32 creationflags that merely hide the child's console
- L204 `windows_detach_popen_kwargs()` (function) — Return a dict of Popen kwargs that detach a child on Windows and
