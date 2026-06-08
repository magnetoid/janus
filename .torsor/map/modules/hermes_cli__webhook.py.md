---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# hermes_cli/webhook.py

Symbols in `hermes_cli/webhook.py`.

- L31 `_hermes_home()` (function)
- L36 `_subscriptions_path()` (function)
- L40 `_load_subscriptions()` (function)
- L51 `_save_subscriptions(subs: Dict[str, dict])` (function)
- L83 `_get_webhook_config()` (function) — Load webhook platform config. Returns {} if not configured.
- L93 `_is_webhook_enabled()` (function)
- L97 `_get_webhook_base_url()` (function)
- L105 `_setup_hint()` (function)
- L131 `_require_webhook_enabled()` (function) — Check webhook is enabled. Print setup guide and return False if not.
- L139 `webhook_command(args)` (function) — Entry point for 'hermes webhook' subcommand.
- L161 `_cmd_subscribe(args)` (function)
- L220 `_cmd_list(args)` (function)
- L244 `_cmd_remove(args)` (function)
- L258 `_cmd_test(args)` (function) — Send a test POST to a webhook route.
