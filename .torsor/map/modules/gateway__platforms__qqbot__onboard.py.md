---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# gateway/platforms/qqbot/onboard.py

Symbols in `gateway/platforms/qqbot/onboard.py`.

- L43 `BindStatus` (class) — Status codes returned by ``_poll_bind_result``.
- L62 `_render_qr(url: str)` (function) — Try to render a QR code in the terminal. Returns True if successful.
- L84 `_create_bind_task(timeout: float=ONBOARD_API_TIMEOUT)` (function) — Create a bind task and return *(task_id, aes_key_base64)*.
- L111 `_poll_bind_result(task_id: str, timeout: float=ONBOARD_API_TIMEOUT)` (function) — Poll the bind result for *task_id*.
- L144 `build_connect_url(task_id: str)` (function) — Build the QR-code target URL for a given *task_id*.
- L156 `qr_register(timeout_seconds: int=600)` (function) — Run the QQBot scan-to-configure QR registration flow.
