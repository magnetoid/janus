---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/e2e/matrix_xsign_bootstrap/test_bootstrap.py

Symbols in `tests/e2e/matrix_xsign_bootstrap/test_bootstrap.py`.

- L52 `_hs_reachable()` (function)
- L60 `_first_time_token()` (function) — Continuwuity prints a one-time registration token on first boot.
- L82 `_post_json(url: str, body: dict, headers: dict | None=None)` (function)
- L98 `_register_bot(*, prefer_token: str=CONFIG_REG_TOKEN, fallback_token: str | None=None)` (function) — Register a fresh bot. Tries the configured token first; falls back to
- L123 `_query_keys(token: str, mxid: str)` (function)
- L132 `XsignBootstrapE2E` (class) — Drive the patched MatrixAdapter.connect() against real continuwuity.
- L136 `setUpClass(cls)` (method)
- L151 `_connect_with_bootstrap(self, creds: dict, store_dir: Path)` (method) — Drive matrix.py's bootstrap branch directly.
- L233 `asyncSetUp(self)` (method)
- L242 `_publish_device_keys(self, creds, store_dir)` (method) — Tiny helper: open OlmMachine, share device keys, close.
- L265 `asyncTearDown(self)` (method)
- L268 `test_bootstrap_publishes_unpadded_keys(self)` (method) — Fresh bot → bootstrap fires, keys published unpadded, device signed.
- L295 `test_second_startup_skips_bootstrap(self)` (method) — Second startup with same crypto store → no second recovery key.
- L306 `test_recovery_key_path_takes_precedence(self)` (method) — If MATRIX_RECOVERY_KEY is set, no fresh bootstrap happens.
