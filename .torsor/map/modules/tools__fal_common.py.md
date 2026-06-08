---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:44'
updated: '2026-06-08T00:38:44'
---

# tools/fal_common.py

Symbols in `tools/fal_common.py`.

- L33 `import_fal_client()` (function) — Import ``fal_client`` (via ``lazy_deps`` when available) and return
- L55 `_normalize_fal_queue_url_format(queue_run_origin: str)` (function)
- L62 `_extract_http_status(exc: BaseException)` (function) — Return an HTTP status code from httpx/fal exceptions, else None.
- L80 `_ManagedFalSyncClient` (class) — Small per-instance wrapper around ``fal_client.SyncClient`` for
- L90 `__init__(self, fal_client: Any, *, key: str, queue_run_origin: str)` (method)
- L116 `submit(self, application: str, arguments: Dict[str, Any], *, path: str='', hint: Optional[str]=None, webhook_url: Optional[str]=None, priority: Any=None, headers: Optional[Dict[str, str]]=None, start_timeout: Optional[Union[int, float]]=None)` (method)
