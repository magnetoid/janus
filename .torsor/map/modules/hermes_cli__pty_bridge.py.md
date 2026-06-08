---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# hermes_cli/pty_bridge.py

Symbols in `hermes_cli/pty_bridge.py`.

- L63 `_clamp_dimension(value: int, maximum: int)` (function) — Clamp a reported terminal dimension into ``[_MIN_DIMENSION, maximum]``.
- L80 `PtyUnavailableError` (class) — Raised when a PTY cannot be created on this platform.
- L89 `PtyBridge` (class) — Thin wrapper around ``ptyprocess.PtyProcess`` for byte streaming.
- L100 `__init__(self, proc: 'ptyprocess.PtyProcess')` (method)
- L108 `is_available(cls)` (method) — True if a PTY can be spawned on this platform.
- L113 `spawn(cls, argv: Sequence[str], *, cwd: Optional[str]=None, env: Optional[dict]=None, cols: int=80, rows: int=24)` (method) — Spawn ``argv`` behind a new PTY and return a bridge.
- L158 `pid(self)` (method)
- L161 `is_alive(self)` (method)
- L171 `read(self, timeout: float=0.2)` (method) — Read up to 64 KiB of raw bytes from the PTY master.
- L201 `write(self, data: bytes)` (method) — Write raw bytes to the PTY master (i.e. the child's stdin).
- L218 `resize(self, cols: int, rows: int)` (method) — Forward a terminal resize to the child via ``TIOCSWINSZ``.
- L243 `close(self)` (method) — Terminate the child (SIGTERM → 0.5s grace → SIGKILL) and close fds.
- L272 `__enter__(self)` (method)
- L275 `__exit__(self, *_exc)` (method)
