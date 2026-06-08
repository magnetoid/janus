---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# plugins/platforms/irc/adapter.py

Symbols in `plugins/platforms/irc/adapter.py`.

- L59 `_parse_irc_message(raw: str)` (function) — Parse a raw IRC protocol line into components.
- L86 `_extract_nick(prefix: str)` (function) — Extract nickname from IRC prefix (nick!user@host).
- L95 `IRCAdapter` (class) — Async IRC adapter implementing the BasePlatformAdapter interface.
- L102 `__init__(self, config, **kwargs)` (method)
- L150 `name(self)` (method)
- L155 `connect(self)` (method) — Connect to the IRC server, register, and join the channel.
- L222 `disconnect(self)` (method) — Quit and close the connection.
- L258 `send(self, chat_id: str, content: str, reply_to: Optional[str]=None, metadata: Optional[Dict[str, Any]]=None)` (method)
- L281 `send_typing(self, chat_id: str, metadata=None)` (method) — IRC has no typing indicator — no-op.
- L285 `get_chat_info(self, chat_id: str)` (method)
- L294 `_split_message(self, content: str, target: str)` (method) — Split a long message into IRC-safe chunks.
- L339 `_strip_markdown(text: str)` (method) — Convert basic markdown to plain text for IRC.
- L359 `_send_raw(self, line: str)` (method) — Send a raw IRC protocol line.
- L367 `_receive_loop(self)` (method) — Main receive loop — reads lines and dispatches them.
- L393 `_handle_line(self, raw: str)` (method) — Dispatch a single IRC protocol line.
- L482 `_dispatch_message(self, text: str, chat_id: str, chat_type: str, user_id: str, user_name: str)` (method) — Build a MessageEvent and hand it to the base class handler.
- L517 `check_requirements()` (function) — Check if IRC is configured.
- L530 `validate_config(config)` (function) — Validate that the platform config has enough info to connect.
- L538 `interactive_setup()` (function) — Interactive `hermes gateway setup` flow for the IRC platform.
- L645 `is_connected(config)` (function) — Check whether IRC is configured (env or config.yaml).
- L653 `_env_enablement()` (function) — Seed ``PlatformConfig.extra`` from env vars during gateway config load.
- L704 `_strip_irc_control_chars(text: str)` (function) — Strip IRC line terminators and the NUL byte from ``text``.
- L715 `_is_irc_channel(target: str)` (function)
- L719 `_standalone_send(pconfig, chat_id: str, message: str, *, thread_id: Optional[str]=None, media_files: Optional[List[str]]=None, force_document: bool=False)` (function) — Open an ephemeral IRC connection, send a PRIVMSG, and quit.
- L929 `register(ctx)` (function) — Plugin entry point: called by the Hermes plugin system.
