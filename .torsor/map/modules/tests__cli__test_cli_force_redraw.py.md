---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/cli/test_cli_force_redraw.py

Symbols in `tests/cli/test_cli_force_redraw.py`.

- L21 `bare_cli()` (function) — A HermesCLI with no __init__ — we only exercise the redraw helper.
- L27 `TestForceFullRedraw` (class)
- L28 `test_no_app_is_safe(self, bare_cli)` (method)
- L33 `test_missing_app_attr_is_safe(self, bare_cli)` (method)
- L37 `test_sends_full_clear_replays_then_invalidates(self, bare_cli, monkeypatch)` (method)
- L74 `test_resize_preserves_scrollback_and_resets_renderer(self, bare_cli, monkeypatch)` (method) — Resize recovery must NOT erase screen or scrollback.
- L109 `test_force_redraw_uses_full_screen_clear_without_scrollback_clear(self, bare_cli)` (method)
- L119 `test_resize_recovery_is_debounced(self, bare_cli, monkeypatch)` (method)
- L166 `test_invalidate_is_suppressed_while_resize_recovery_is_pending(self, bare_cli)` (method)
- L176 `test_swallows_renderer_exceptions(self, bare_cli)` (method)
- L188 `test_swallows_invalidate_exceptions(self, bare_cli)` (method)
