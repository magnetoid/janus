---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:44'
updated: '2026-06-08T00:38:44'
---

# tools/computer_use/backend.py

Symbols in `tools/computer_use/backend.py`.

- L16 `UIElement` (class) — One interactable element on the current screen.
- L28 `center(self)` (method)
- L34 `CaptureResult` (class) — Result of a screen capture call.
- L58 `ActionResult` (class) — Result of any action (click / type / scroll / drag / key / wait).
- L71 `ComputerUseBackend` (class) — Lifecycle: `start()` before first use, `stop()` at shutdown.
- L75 `start(self)` (method)
- L78 `stop(self)` (method)
- L81 `is_available(self)` (method) — Return True if the backend can be used on this host right now.
- L89 `capture(self, mode: str='som', app: Optional[str]=None)` (method)
- L93 `click(self, *, element: Optional[int]=None, x: Optional[int]=None, y: Optional[int]=None, button: str='left', click_count: int=1, modifiers: Optional[List[str]]=None)` (method)
- L105 `drag(self, *, from_element: Optional[int]=None, to_element: Optional[int]=None, from_xy: Optional[Tuple[int, int]]=None, to_xy: Optional[Tuple[int, int]]=None, button: str='left', modifiers: Optional[List[str]]=None)` (method)
- L117 `scroll(self, *, direction: str, amount: int=3, element: Optional[int]=None, x: Optional[int]=None, y: Optional[int]=None, modifiers: Optional[List[str]]=None)` (method)
- L130 `type_text(self, text: str)` (method)
- L133 `key(self, keys: str)` (method) — Send a key combo, e.g. 'cmd+s', 'ctrl+alt+t', 'return'.
- L138 `list_apps(self)` (method) — Return running apps with bundle IDs, PIDs, window counts.
- L142 `focus_app(self, app: str, raise_window: bool=False)` (method) — Route input to `app` (by name or bundle ID). Default: focus without raise.
- L147 `set_value(self, value: str, element: Optional[int]=None)` (method) — Set a native value on an element (e.g. AXPopUpButton selection).
- L154 `wait(self, seconds: float)` (method) — Default implementation: time.sleep.
