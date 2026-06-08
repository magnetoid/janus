---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# plugins/platforms/teams/adapter.py

Symbols in `plugins/platforms/teams/adapter.py`.

- L107 `_parse_bool(value: Any, *, default: bool=False)` (function)
- L119 `_coerce_port(value: Any, *, default: int=_DEFAULT_PORT)` (function)
- L126 `_StaticAccessTokenProvider` (class) — Minimal token-provider shim so outbound Graph delivery can reuse the shared client.
- L129 `__init__(self, access_token: str)` (method)
- L132 `get_access_token(self, *, force_refresh: bool=False)` (method)
- L138 `clear_cache(self)` (method)
- L142 `TeamsSummaryWriter` (class) — Pipeline-facing Teams outbound delivery surface.
- L150 `__init__(self, platform_config: PlatformConfig | None=None, *, graph_client: Any | None=None, transport: httpx.AsyncBaseTransport | None=None)` (method)
- L161 `write_summary(self, payload: Any, config: dict[str, Any] | None, existing_record: Optional[dict[str, Any]]=None)` (method)
- L187 `_resolve_delivery_config(self, config: dict[str, Any] | None)` (method)
- L211 `_write_summary_via_incoming_webhook(self, payload: Any, config: dict[str, Any])` (method)
- L234 `_write_summary_via_graph(self, payload: Any, config: dict[str, Any])` (method)
- L278 `_build_graph_client(self, config: dict[str, Any])` (method)
- L296 `_render_summary_markdown(self, payload: Any)` (method)
- L313 `_render_summary_html(self, payload: Any)` (method)
- L334 `_title(payload: Any)` (method)
- L343 `_text(value: Any, default: str)` (method)
- L348 `_bullet_lines(cls, values: Any)` (method)
- L353 `_AiohttpBridgeAdapter` (class) — HttpServerAdapter that bridges the Teams SDK into an aiohttp server.
- L361 `__init__(self, aiohttp_app: 'web.Application')` (method)
- L364 `register_route(self, method: 'HttpMethod', path: str, handler: 'HttpRouteHandler')` (method) — Register an SDK route handler as an aiohttp route.
- L383 `serve_static(self, path: str, directory: str)` (method)
- L386 `start(self, port: int)` (method)
- L389 `stop(self)` (method)
- L393 `check_requirements()` (function) — Return True when all Teams dependencies and credentials are present.
- L398 `validate_config(config)` (function) — Return True when the config has the minimum required credentials.
- L407 `is_connected(config)` (function) — Check whether Teams is configured (env or config.yaml).
- L412 `_env_enablement()` (function) — Seed ``PlatformConfig.extra`` from env vars during gateway config load.
- L473 `_validate_teams_service_url(raw: str)` (function) — Return a normalized service URL or ``None`` if it is not allowed.
- L496 `_standalone_send(pconfig, chat_id: str, message: str, *, thread_id: Optional[str]=None, media_files: Optional[list]=None, force_document: bool=False)` (function) — Acquire a Bot Framework bearer token and POST a single message activity.
- L622 `TeamsAdapter` (class) — Microsoft Teams adapter using the microsoft-teams-apps SDK.
- L627 `__init__(self, config: PlatformConfig)` (method)
- L643 `connect(self)` (method)
- L719 `disconnect(self)` (method)
- L728 `_on_message(self, ctx: ActivityContext[MessageActivity])` (method) — Process an incoming Teams message and dispatch to the gateway.
- L809 `_send_card(self, chat_id: str, card: 'AdaptiveCard')` (method) — Send an AdaptiveCard, using a stored ConversationReference when available.
- L821 `_on_card_action(self, ctx: 'ActivityContext[AdaptiveCardInvokeActivity]')` (method) — Handle an Adaptive Card Action.Execute button click.
- L916 `send_exec_approval(self, chat_id: str, command: str, session_key: str, description: str='dangerous command', metadata: Optional[Dict[str, Any]]=None)` (method) — Send an Adaptive Card approval prompt with Allow/Deny buttons.
- L978 `send(self, chat_id: str, content: str, reply_to: Optional[str]=None, metadata: Optional[Dict[str, Any]]=None)` (method)
- L1014 `send_typing(self, chat_id: str, metadata: Optional[Dict[str, Any]]=None)` (method)
- L1022 `send_image(self, chat_id: str, image_url: str, caption: Optional[str]=None, reply_to: Optional[str]=None, metadata: Optional[Dict[str, Any]]=None)` (method)
- L1064 `send_image_file(self, chat_id: str, image_path: str, caption: Optional[str]=None, reply_to: Optional[str]=None, **kwargs)` (method)
- L1079 `get_chat_info(self, chat_id: str)` (method)
- L1085 `interactive_setup()` (function) — Guide the user through Teams setup using the Teams CLI.
- L1158 `register(ctx)` (function) — Plugin entry point — called by the Hermes plugin system.
