---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# hermes_cli/dingtalk_auth.py

Symbols in `hermes_cli/dingtalk_auth.py`.

- L37 `RegistrationError` (class) — Raised when a DingTalk registration API call fails.
- L41 `_api_post(path: str, payload: dict)` (function) — POST to the registration API and return the parsed JSON body.
- L60 `begin_registration()` (function) — Start a device-flow registration.
- L89 `poll_registration(device_code: str)` (function) — Poll the registration status once.
- L106 `wait_for_registration_success(device_code: str, interval: int=3, expires_in: int=7200, on_waiting: Optional[callable]=None)` (function) — Block until the registration succeeds or times out.
- L156 `_ensure_qrcode_installed()` (function) — Try to import qrcode; if missing, auto-install it via pip/uv.
- L180 `render_qr_to_terminal(url: str)` (function) — Render *url* as a compact QR code in the terminal.
- L230 `dingtalk_qr_auth()` (function) — Run the interactive QR-code device-flow authorization.
