---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/hermes_cli/test_graphical_browser_detection.py

Symbols in `tests/hermes_cli/test_graphical_browser_detection.py`.

- L23 `_FakeController` (class)
- L24 `__init__(self, name: str)` (method)
- L27 `open(self, *_a, **_kw)` (method)
- L32 `_clean_browser_env(monkeypatch)` (function) — Each test controls DISPLAY / WAYLAND_DISPLAY / BROWSER explicitly.
- L39 `_force_platform_linux(monkeypatch)` (function)
- L43 `_force_resolved_browser(monkeypatch, name: str)` (function)
- L47 `test_headless_linux_no_display_refuses(monkeypatch)` (function) — The reported bug: headless Linux, no display server → don't auto-open.
- L55 `test_browser_env_pointing_at_console_browser_refuses(monkeypatch)` (function) — $BROWSER=w3m must refuse even with a display server present.
- L64 `test_resolved_console_browser_refuses(monkeypatch, console)` (function) — When webbrowser resolves to a console browser, refuse to auto-open.
- L72 `test_graphical_browser_with_display_allows(monkeypatch)` (function) — Real GUI browser + display server → auto-open is fine.
- L80 `test_webbrowser_get_raises_refuses(monkeypatch)` (function) — No resolvable browser at all → don't auto-open.
- L92 `test_non_linux_with_gui_allows(monkeypatch)` (function) — macOS / Windows always have a usable default GUI browser.
