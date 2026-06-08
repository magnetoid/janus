---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# gateway/memory_monitor.py

Symbols in `gateway/memory_monitor.py`.

- L52 `_get_rss_mb()` (function) — Return current process resident set size in MB, or None if unavailable.
- L83 `log_memory_usage(prefix: str='')` (function) — Log current memory usage in a grep-friendly ``[MEMORY] ...`` line.
- L129 `_monitor_loop(stop_event: threading.Event, interval: float)` (function) — Background thread body — log every ``interval`` seconds until stopped.
- L139 `start_memory_monitoring(interval_seconds: float=300.0)` (function) — Start periodic memory usage logging in a daemon thread.
- L196 `stop_memory_monitoring(timeout: float=2.0)` (function) — Stop the monitor thread and log a final snapshot.
- L227 `is_running()` (function) — True if the background monitor thread is alive.
