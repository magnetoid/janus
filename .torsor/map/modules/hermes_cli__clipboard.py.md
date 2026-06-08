---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# hermes_cli/clipboard.py

Symbols in `hermes_cli/clipboard.py`.

- L28 `save_clipboard_image(dest: Path)` (function) — Extract an image from the system clipboard and save it as PNG.
- L41 `has_clipboard_image()` (function) — Quick check: does the clipboard currently contain an image?
- L60 `_macos_save(dest: Path)` (function) — Try pngpaste first (fast, handles more formats), fall back to osascript.
- L65 `_macos_has_image()` (function) — Check if macOS clipboard contains image data.
- L77 `_macos_pngpaste(dest: Path)` (function) — Use pngpaste (brew install pngpaste) — fastest, cleanest.
- L93 `_macos_osascript(dest: Path)` (function) — Use osascript to extract PNG data from clipboard (always available).
- L200 `_run_powershell(exe: str, script: str, timeout: int)` (function)
- L207 `_write_base64_image(dest: Path, b64_data: str)` (function)
- L213 `_powershell_has_image(exe: str, *, timeout: int, label: str)` (function)
- L227 `_powershell_save_image(exe: str, dest: Path, *, timeout: int, label: str)` (function)
- L255 `_find_powershell()` (function) — Return the first available PowerShell executable, or None.
- L276 `_get_ps_exe()` (function)
- L283 `_windows_has_image()` (function) — Check if the Windows clipboard contains an image.
- L291 `_windows_save(dest: Path)` (function) — Extract clipboard image on native Windows via PowerShell → base64 PNG.
- L302 `_linux_save(dest: Path)` (function) — Try clipboard backends in priority order: WSL → Wayland → X11.
- L319 `_wsl_has_image()` (function) — Check if Windows clipboard has an image (via powershell.exe).
- L324 `_wsl_save(dest: Path)` (function) — Extract clipboard image via powershell.exe → base64 → decode to PNG.
- L331 `_wayland_has_image()` (function) — Check if Wayland clipboard has image content.
- L348 `_wayland_save(dest: Path)` (function) — Use wl-paste to extract clipboard image (Wayland sessions).
- L400 `_convert_to_png(path: Path)` (function) — Convert an image file to PNG in-place (requires Pillow or ImageMagick).
- L440 `_is_png_file(path: Path)` (function) — Return True when *path* starts with the PNG file signature.
- L451 `_xclip_has_image()` (function) — Check if X11 clipboard has image content.
- L466 `_xclip_save(dest: Path)` (function) — Use xclip to extract clipboard image (X11 sessions).
