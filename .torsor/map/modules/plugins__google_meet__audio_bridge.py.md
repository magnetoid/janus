---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# plugins/google_meet/audio_bridge.py

Symbols in `plugins/google_meet/audio_bridge.py`.

- L30 `AudioBridge` (class) — Manages a virtual audio device for Chrome fake-mic input.
- L37 `__init__(self, name_prefix: str='hermes_meet')` (method)
- L48 `device_name(self)` (method)
- L54 `write_target(self)` (method)
- L61 `setup(self)` (method) — Provision the virtual audio device.
- L76 `teardown(self)` (method) — Release the virtual audio device. Idempotent.
- L98 `_setup_linux(self)` (method)
- L167 `_setup_darwin(self)` (method)
- L207 `_parse_module_id(stdout: str)` (method) — pactl load-module prints the new module ID to stdout.
- L223 `chrome_fake_audio_flags(bridge_info: dict)` (function) — Return Chrome flags for using the fake audio input.
