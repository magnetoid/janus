---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# optional-skills/devops/watchers/scripts/_watermark.py

Symbols in `optional-skills/devops/watchers/scripts/_watermark.py`.

- L30 `_state_dir()` (function) — Where watermark files live — respects WATCHER_STATE_DIR override.
- L40 `Watermark` (class) — Per-watcher state. Persisted to <state_dir>/<name>.json.
- L43 `__init__(self, name: str, *, max_seen: int=500)` (method)
- L54 `load(cls, name: str, *, max_seen: int=500)` (method)
- L67 `is_first_run(self)` (method)
- L71 `seen(self)` (method)
- L74 `filter_new(self, items: Iterable[Dict[str, Any]], *, id_key: str='id')` (method) — Return items whose id isn't in the stored set.
- L107 `save(self)` (method)
- L117 `format_items_as_markdown(items: List[Dict[str, Any]], *, title_key: str='title', url_key: str='url', body_key: Optional[str]=None, max_body_chars: int=500)` (function) — Render a list of items as Markdown for cron delivery.
