---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# plugins/teams_pipeline/cli.py

Symbols in `plugins/teams_pipeline/cli.py`.

- L31 `register_cli(subparser: argparse.ArgumentParser)` (function)
- L91 `teams_pipeline_command(args: argparse.Namespace)` (function)
- L132 `_run_async(coro)` (function)
- L136 `_store_path(path_arg: str | None)` (function)
- L140 `_graph_setup_hint()` (function)
- L152 `_iso_utc_timestamp(hours_from_now: int)` (function)
- L158 `_default_change_type_for_resource(resource: str)` (function)
- L169 `_compact_job(job: dict)` (function)
- L179 `_sync_subscription_record(store: TeamsPipelineStore, subscription_payload: dict[str, Any], *, status: str='active', renewed: bool=False)` (function)
- L193 `_validate_configuration_snapshot(store: TeamsPipelineStore)` (function)
- L253 `_cmd_list(args)` (function)
- L282 `_cmd_show(args)` (function)
- L295 `_cmd_run(args)` (function)
- L306 `_cmd_fetch(args)` (function)
- L346 `_cmd_subscriptions(args)` (function)
- L371 `_cmd_subscribe(args)` (function)
- L398 `_cmd_renew_subscription(args)` (function)
- L417 `_cmd_delete_subscription(args)` (function)
- L428 `_cmd_maintain_subscriptions(args)` (function)
- L443 `_cmd_token_health(args)` (function)
- L458 `_cmd_validate(args)` (function)
