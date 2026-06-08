---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# plugins/teams_pipeline/subscriptions.py

Symbols in `plugins/teams_pipeline/subscriptions.py`.

- L14 `build_graph_client()` (function)
- L19 `_parse_bool(value: Any, *, default: bool=False)` (function)
- L31 `_parse_int(value: Any, default: int)` (function)
- L38 `_utc_now()` (function)
- L42 `_utc_now_iso()` (function)
- L46 `_parse_datetime(value: Any)` (function)
- L60 `resolve_store_path(path: str | None)` (function)
- L64 `build_store(path: str | None=None)` (function)
- L68 `sync_graph_subscription_record(store: TeamsPipelineStore, subscription_payload: dict[str, Any], *, status: str | None=None, renewed: bool=False)` (function)
- L86 `expected_client_state(raw: str | None=None)` (function)
- L95 `is_managed_subscription(store: TeamsPipelineStore, subscription_payload: dict[str, Any], *, expected_client_state_value: str | None)` (function)
- L117 `maintain_graph_subscriptions(*, client: MicrosoftGraphClient, store: TeamsPipelineStore, renew_within_hours: int=24, extend_hours: int=24, dry_run: bool=False, client_state: str | None=None)` (function)
