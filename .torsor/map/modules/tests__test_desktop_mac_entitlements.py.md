---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/test_desktop_mac_entitlements.py

Symbols in `tests/test_desktop_mac_entitlements.py`.

- L37 `_load(plist: Path)` (function)
- L43 `test_inherit_plist_grants_microphone()` (function) — The helper-inherited plist must grant audio-input (regression #37718).
- L53 `test_device_entitlements_are_inherited()` (function) — Every device.* entitlement on the main app must also be inherited.
- L73 `test_entitlement_files_are_valid_plists(plist: Path)` (function) — Both entitlement files must remain well-formed plist dictionaries.
