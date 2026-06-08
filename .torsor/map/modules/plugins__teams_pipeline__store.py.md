---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# plugins/teams_pipeline/store.py

Symbols in `plugins/teams_pipeline/store.py`.

- L21 `_utc_now_iso()` (function)
- L25 `resolve_teams_pipeline_store_path(path: str | Path | None=None)` (function)
- L38 `TeamsPipelineStore` (class) — JSON-backed durable store for Teams pipeline state.
- L41 `__init__(self, path: str | Path)` (method)
- L53 `_load(self)` (method)
- L66 `_persist(self)` (method)
- L79 `list_subscriptions(self)` (method)
- L83 `get_subscription(self, subscription_id: str)` (method)
- L88 `upsert_subscription(self, subscription_id: str, payload: Dict[str, Any])` (method)
- L99 `delete_subscription(self, subscription_id: str)` (method)
- L108 `build_notification_receipt_key(cls, notification: Dict[str, Any])` (method)
- L116 `has_notification_receipt(self, receipt_key: str)` (method)
- L120 `record_notification_receipt(self, receipt_key: str, payload: Optional[Dict[str, Any]]=None, *, received_at: Optional[str]=None)` (method)
- L137 `record_event_timestamp(self, event_key: str, timestamp: Optional[str]=None)` (method)
- L144 `get_event_timestamp(self, event_key: str)` (method)
- L149 `stats(self)` (method)
- L159 `upsert_job(self, job_id: str, payload: Dict[str, Any])` (method)
- L170 `get_job(self, job_id: str)` (method)
- L175 `list_jobs(self)` (method)
- L179 `upsert_sink_record(self, sink_key: str, payload: Dict[str, Any])` (method)
- L190 `get_sink_record(self, sink_key: str)` (method)
