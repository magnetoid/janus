---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/test_dockerfile_tini_compat_shim.py

Symbols in `tests/test_dockerfile_tini_compat_shim.py`.

- L14 `_dockerfile_text()` (function)
- L18 `test_tini_compat_symlink_present()` (function) — The /usr/bin/tini -> /init symlink line must exist for #34192.
- L29 `test_tini_compat_comment_explains_why()` (function) — The symlink line is comment-anchored to #34192 so a future reader
- L40 `test_entrypoint_still_init_not_tini()` (function) — Sanity check: the actual ENTRYPOINT is still /init (s6-overlay).
