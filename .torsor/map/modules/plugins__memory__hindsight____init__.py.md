---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# plugins/memory/hindsight/__init__.py

Symbols in `plugins/memory/hindsight/__init__.py`.

- L75 `_parse_int_setting(value: Any, default: int)` (function) — Parse an integer config/env value, falling back on invalid input.
- L86 `_check_local_runtime()` (function) — Return whether local embedded Hindsight imports cleanly.
- L113 `_meets_minimum_version(actual: str | None, required: str)` (function) — Return True if *actual* ≥ *required* (semver). False on missing/invalid.
- L124 `_fetch_hindsight_api_version(api_url: str, api_key: str | None=None, timeout: float=5.0)` (function) — GET ``<api_url>/version`` and return the version string (or None on failure).
- L153 `_check_api_supports_update_mode_append(api_url: str, api_key: str | None=None)` (function) — Cached capability check for ``update_mode='append'`` on *api_url*.
- L205 `_get_loop()` (function) — Return a long-lived event loop running on a background thread.
- L222 `_run_sync(coro, timeout: float=_DEFAULT_TIMEOUT)` (function) — Schedule *coro* on the shared loop and block until done.
- L297 `_load_config()` (function) — Load config from profile-scoped path, legacy path, or env vars.
- L342 `_normalize_retain_tags(value: Any)` (function) — Normalize tag config/tool values to a deduplicated list of strings.
- L379 `_utc_timestamp()` (function) — Return current UTC timestamp in ISO-8601 with milliseconds and Z suffix.
- L384 `_embedded_profile_name(config: dict[str, Any])` (function) — Return the Hindsight embedded profile name for this Hermes config.
- L390 `_load_simple_env(path)` (function) — Parse a simple KEY=VALUE env file, ignoring comments and blank lines.
- L404 `_build_embedded_profile_env(config: dict[str, Any], *, llm_api_key: str | None=None)` (function) — Build the profile-scoped env file that standalone hindsight-embed consumes.
- L442 `_embedded_profile_env_path(config: dict[str, Any])` (function)
- L448 `_materialize_embedded_profile_env(config: dict[str, Any], *, llm_api_key: str | None=None)` (function) — Write the profile-scoped env file that standalone hindsight-embed uses.
- L459 `_sanitize_bank_segment(value: str)` (function) — Sanitize a bank_id_template placeholder value.
- L481 `_resolve_bank_id_template(template: str, fallback: str, **placeholders: str)` (function) — Resolve a bank_id template string with the given placeholders.
- L518 `HindsightMemoryProvider` (class) — Hindsight long-term memory with knowledge graph and multi-strategy retrieval.
- L521 `__init__(self)` (method)
- L600 `name(self)` (method)
- L603 `is_available(self)` (method)
- L622 `save_config(self, values, hermes_home)` (method) — Write config to $HERMES_HOME/hindsight/config.json.
- L639 `post_setup(self, hermes_home: str, config: dict)` (method) — Custom setup wizard — installs only the deps needed for the selected mode.
- L841 `get_config_schema(self)` (method)
- L881 `_get_client(self)` (method) — Return the cached Hindsight client (created once, reused).
- L933 `_run_sync(self, coro)` (method) — Schedule *coro* on the shared loop using the configured timeout.
- L937 `_is_retriable_embedded_connection_error(self, exc: Exception)` (method) — Return True for stale embedded-daemon connection failures.
- L952 `_ensure_writer(self)` (method) — Lazy-start the single retain-writer thread.
- L975 `_writer_loop(self)` (method) — Drain the retain queue serially. Exits on sentinel.
- L998 `_register_atexit(self)` (method) — Register an idempotent atexit hook to drain the writer.
- L1011 `_atexit_shutdown(self)` (method)
- L1019 `_run_hindsight_operation(self, operation)` (method) — Run an async Hindsight client operation, retrying once after idle shutdown.
- L1036 `_probe_url(self)` (method) — Return the URL to probe /version on.
- L1049 `_resolve_retain_target(self, fallback_document_id: str)` (method) — Pick (document_id, update_mode) based on live API capability.
- L1070 `initialize(self, session_id: str, **kwargs)` (method)
- L1279 `system_prompt_block(self)` (method)
- L1301 `prefetch(self, query: str, *, session_id: str='')` (method)
- L1319 `queue_prefetch(self, query: str, *, session_id: str='')` (method)
- L1364 `_build_turn_messages(self, user_content: str, assistant_content: str)` (method)
- L1379 `_build_metadata(self, *, message_count: int, turn_index: int)` (method)
- L1407 `_build_retain_kwargs(self, content: str, *, context: str | None=None, document_id: str | None=None, metadata: Dict[str, str] | None=None, tags: List[str] | None=None, retain_async: bool | None=None)` (method)
- L1436 `sync_turn(self, user_content: str, assistant_content: str, *, session_id: str='')` (method) — Enqueue a retain for the current turn. Non-blocking.
- L1513 `get_tool_schemas(self)` (method)
- L1518 `handle_tool_call(self, tool_name: str, args: dict, **kwargs)` (method)
- L1586 `on_session_switch(self, new_session_id: str, *, parent_session_id: str='', reset: bool=False, **kwargs)` (method) — Refresh cached per-session state when the agent rotates session_id.
- L1714 `shutdown(self)` (method)
- L1775 `register(ctx)` (function) — Register Hindsight as a memory provider plugin.
