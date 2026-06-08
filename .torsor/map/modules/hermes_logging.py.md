---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# hermes_logging.py

Symbols in `hermes_logging.py`.

- L56 `_safe_stderr()` (function) — Return a stderr stream that tolerates Unicode on all platforms.
- L112 `set_session_context(session_id: str)` (function) — Set the session ID for the current thread.
- L121 `clear_session_context()` (function) — Clear the session ID for the current thread.
- L130 `_install_session_record_factory()` (function) — Replace the global LogRecord factory with one that adds ``session_tag``.
- L166 `_ComponentFilter` (class) — Only pass records whose logger name starts with one of *prefixes*.
- L173 `__init__(self, prefixes: Sequence[str])` (method)
- L177 `filter(self, record: logging.LogRecord)` (method)
- L202 `setup_logging(*, hermes_home: Optional[Path]=None, log_level: Optional[str]=None, max_size_mb: Optional[int]=None, backup_count: Optional[int]=None, mode: Optional[str]=None, force: bool=False)` (function) — Configure the Hermes logging subsystem.
- L322 `setup_verbose_logging()` (function) — Enable DEBUG-level console logging for ``--verbose`` / ``-v`` mode.
- L358 `_ManagedRotatingFileHandler` (class) — RotatingFileHandler that ensures group-writable perms in managed mode
- L383 `__init__(self, *args, **kwargs)` (method)
- L393 `_chmod_if_managed(self)` (method)
- L400 `_record_stream_stat(self)` (method) — Snapshot dev/ino of ``baseFilename`` so we can detect external rotation.
- L408 `_reopen_if_externally_rotated(self)` (method) — Reopen the stream when ``baseFilename`` no longer matches our fd.
- L457 `emit(self, record: logging.LogRecord)` (method)
- L464 `_open(self)` (method)
- L469 `doRollover(self)` (method)
- L477 `_add_rotating_handler(logger: logging.Logger, path: Path, *, level: int, max_bytes: int, backup_count: int, formatter: logging.Formatter, log_filter: Optional[logging.Filter]=None)` (function) — Add a ``RotatingFileHandler`` to *logger*, skipping if one already
- L516 `_read_logging_config()` (function) — Best-effort read of ``logging.*`` from config.yaml.
