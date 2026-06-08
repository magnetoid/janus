---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_discord_opus.py

Symbols in `tests/gateway/test_discord_opus.py`.

- L7 `TestOpusFindLibrary` (class) — Opus loading must try ctypes.util.find_library first, with platform fallback.
- L10 `test_uses_find_library_first(self)` (method) — find_library must be the primary lookup strategy.
- L17 `test_homebrew_fallback_is_conditional(self)` (method) — Homebrew paths must only be tried when find_library returns None.
- L33 `test_windows_bundled_discord_opus_dll_is_discovered(self, monkeypatch, tmp_path)` (method) — Native Windows installs should try discord.py's bundled opus DLL.
- L53 `test_opus_decode_error_logged(self)` (method) — Opus decode failure must log the error, not silently return.
