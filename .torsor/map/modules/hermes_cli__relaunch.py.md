---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# hermes_cli/relaunch.py

Symbols in `hermes_cli/relaunch.py`.

- L22 `_build_inherited_flag_table()` (function) — Build the ``(option_string, takes_value)`` table of flags that must
- L54 `_extract_inherited_flags(argv: Sequence[str])` (function) — Pull out flags that should carry over into a self-relaunched hermes.
- L80 `resolve_hermes_bin()` (function) — Find the hermes entry point.
- L124 `build_relaunch_argv(extra_args: Sequence[str], *, preserve_inherited: bool=True, original_argv: Optional[Sequence[str]]=None)` (function) — Construct an argv list for replacing the current process with hermes.
- L155 `relaunch(extra_args: Sequence[str], *, preserve_inherited: bool=True, original_argv: Optional[Sequence[str]]=None)` (function) — Replace the current process with a fresh hermes invocation.
