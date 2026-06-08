---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# hermes_cli/stdio.py

Symbols in `hermes_cli/stdio.py`.

- L41 `is_windows()` (function) — Return True iff running on native Windows (not WSL).
- L46 `_flip_console_code_page_to_utf8()` (function) — Set the attached console's input and output code pages to UTF-8.
- L69 `_reconfigure_stream(stream, *, encoding: str='utf-8', errors: str='replace')` (function) — Reconfigure a text stream to UTF-8 in place.
- L85 `configure_windows_stdio()` (function) — Force UTF-8 stdio on Windows.  No-op elsewhere.
- L161 `_default_windows_editor()` (function) — Return a Windows-appropriate default for ``$EDITOR``.
- L195 `_augment_path_with_known_tools()` (function) — Prepend well-known Hermes-managed tool directories to os.environ['PATH'].
