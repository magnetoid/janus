---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:44'
updated: '2026-06-08T00:38:44'
---

# tools/browser_camofox.py

Symbols in `tools/browser_camofox.py`.

- L55 `get_camofox_url()` (function) — Return the configured Camofox server URL, or empty string.
- L60 `is_camofox_mode()` (function) — True when Camofox backend is configured and no CDP override is active.
- L73 `check_camofox_available()` (function) — Verify the Camofox server is reachable.
- L98 `get_vnc_url()` (function) — Return the VNC URL if the Camofox server exposes one, or None.
- L105 `_get_camofox_config()` (function) — Return the ``browser.camofox`` config block, or an empty dict.
- L115 `_managed_persistence_enabled()` (function) — Return whether Hermes-managed persistence is enabled for Camofox.
- L127 `_camofox_identity_override(task_id: Optional[str], camofox_cfg: Dict[str, Any])` (function) — Return an externally configured Camofox identity, if one is set.
- L146 `_env_flag(name: str)` (function)
- L158 `_adopt_existing_tab_enabled(camofox_cfg: Dict[str, Any])` (function) — Return whether Hermes should recover an existing Camofox tab ID.
- L166 `_loopback_rewrite_enabled(camofox_cfg: Dict[str, Any])` (function) — Return whether loopback navigation URLs should be rewritten for Docker.
- L184 `_loopback_rewrite_host(camofox_cfg: Dict[str, Any])` (function) — Return the host alias used when rewriting loopback page URLs.
- L193 `_is_loopback_hostname(hostname: Optional[str])` (function) — Return True for localhost/127.0.0.0/8/::1-style hostnames.
- L208 `_rewrite_loopback_url_for_camofox(url: str)` (function) — Rewrite loopback page URLs for Docker-hosted Camofox, if configured.
- L257 `_adopt_existing_tab(session: Dict[str, Any])` (function) — Attach process-local state to an already-open managed Camofox tab.
- L295 `_get_session(task_id: Optional[str])` (function) — Get or create a camofox session for the given task.
- L338 `_ensure_tab(task_id: Optional[str], url: str='about:blank')` (function) — Ensure a tab exists for the session, creating one if needed.
- L359 `_drop_session(task_id: Optional[str])` (function) — Remove and return session info.
- L366 `camofox_soft_cleanup(task_id: Optional[str]=None)` (function) — Release the in-memory session without destroying the server-side context.
- L387 `_post(path: str, body: dict, timeout: int=_DEFAULT_TIMEOUT)` (function) — POST JSON to camofox and return parsed response.
- L395 `_get(path: str, params: dict=None, timeout: int=_DEFAULT_TIMEOUT)` (function) — GET from camofox and return parsed response.
- L403 `_get_raw(path: str, params: dict=None, timeout: int=_DEFAULT_TIMEOUT)` (function) — GET from camofox and return raw response (for binary data).
- L411 `_delete(path: str, body: dict=None, timeout: int=_DEFAULT_TIMEOUT)` (function) — DELETE to camofox and return parsed response.
- L423 `camofox_navigate(url: str, task_id: Optional[str]=None)` (function) — Navigate to a URL via Camofox.
- L491 `camofox_snapshot(full: bool=False, task_id: Optional[str]=None, user_task: Optional[str]=None)` (function) — Get accessibility tree snapshot from Camofox.
- L529 `camofox_click(ref: str, task_id: Optional[str]=None)` (function) — Click an element by ref via Camofox.
- L552 `camofox_type(ref: str, text: str, task_id: Optional[str]=None)` (function) — Type text into an element by ref via Camofox.
- L574 `camofox_scroll(direction: str, task_id: Optional[str]=None)` (function) — Scroll the page via Camofox.
- L590 `camofox_back(task_id: Optional[str]=None)` (function) — Navigate back via Camofox.
- L606 `camofox_press(key: str, task_id: Optional[str]=None)` (function) — Press a keyboard key via Camofox.
- L622 `camofox_close(task_id: Optional[str]=None)` (function) — Close the browser session via Camofox.
- L637 `camofox_get_images(task_id: Optional[str]=None)` (function) — Get images on the current page via Camofox.
- L684 `camofox_vision(question: str, annotate: bool=False, task_id: Optional[str]=None)` (function) — Take a screenshot and analyze it with vision AI via Camofox.
- L777 `camofox_console(clear: bool=False, task_id: Optional[str]=None)` (function) — Get console output — limited support in Camofox.
