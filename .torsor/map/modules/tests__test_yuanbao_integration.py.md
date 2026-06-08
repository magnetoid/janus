---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/test_yuanbao_integration.py

Symbols in `tests/test_yuanbao_integration.py`.

- L28 `make_config(**kwargs)` (function)
- L44 `TestYuanbaoAdapterInit` (class)
- L45 `test_create_adapter(self)` (method)
- L51 `test_initial_state(self)` (method)
- L63 `TestYuanbaoConfig` (class)
- L64 `test_platform_enum(self)` (method)
- L67 `test_config_fields(self)` (method)
- L72 `test_get_connected_platforms_requires_key_and_secret(self)` (method)
- L102 `TestGatewayRunnerRegistration` (class)
- L103 `test_yuanbao_in_platform_enum(self)` (method) — Platform 枚举包含 YUANBAO
- L108 `_make_minimal_runner(self, config)` (method) — 通过 __new__ + 最小初始化绕过 run.py 的模块级 dotenv/ssl 副作用
- L140 `test_runner_creates_yuanbao_adapter(self)` (method) — GatewayRunner._create_adapter 能为 YUANBAO 返回 YuanbaoAdapter 实例
- L157 `test_runner_adapter_platform_attr(self)` (method) — 创建的 adapter.PLATFORM 为 Platform.YUANBAO
- L178 `TestProtoRoundTrip` (class) — 验证 proto 编解码基本功能
- L181 `test_conn_msg_roundtrip(self)` (method)
- L188 `test_text_elem_encoding(self)` (method)
- L203 `TestMarkdownChunking` (class)
- L204 `test_chunks_are_sent_separately(self)` (method)
- L214 `test_chunk_short_text_no_split(self)` (method)
- L225 `TestSignToken` (class)
- L226 `test_import_ok(self)` (method)
- L236 `TestManagerImports` (class)
- L237 `test_connection_manager_import(self)` (method)
- L241 `test_outbound_manager_import(self)` (method)
- L245 `test_message_sender_import(self)` (method)
- L249 `test_heartbeat_manager_import(self)` (method)
- L253 `test_slow_response_notifier_import(self)` (method)
- L257 `test_adapter_has_outbound_manager(self)` (method)
- L263 `test_outbound_composes_sub_managers(self)` (method)
- L275 `TestMediaModule` (class)
- L276 `test_import_ok(self)` (method)
- L286 `TestToolset` (class)
- L287 `test_yuanbao_toolset_registered(self)` (method) — toolsets.py 中存在 hermes-yuanbao 键
- L295 `test_tools_import(self)` (method)
- L312 `TestPlatformInit` (class)
- L313 `test_yuanbao_adapter_exported(self)` (method) — gateway.platforms.__init__.py 应导出 YuanbaoAdapter
- L327 `TestP0ReconnectGuard` (class) — P0-1: _reconnecting flag prevents concurrent reconnect attempts.
- L330 `test_reconnecting_flag_initialized(self)` (method)
- L335 `test_schedule_reconnect_skips_when_not_running(self)` (method)
- L342 `test_schedule_reconnect_skips_when_already_reconnecting(self)` (method)
- L350 `TestP0InboundTaskTracking` (class) — P0-2: _inbound_tasks set is initialized and usable.
- L353 `test_inbound_tasks_initialized(self)` (method)
- L360 `TestP0ChatLockEviction` (class) — P0-3: get_chat_lock uses OrderedDict and safe eviction.
- L363 `test_chat_locks_is_ordered_dict(self)` (method)
- L367 `test_eviction_skips_locked(self)` (method) — When eviction is needed, locked entries are skipped.
- L389 `test_move_to_end_on_access(self)` (method) — Accessing an existing key moves it to the end (MRU).
- L403 `TestP0PlatformScopedLock` (class) — P0-4: connect() calls _acquire_platform_lock.
- L406 `test_adapter_has_platform_lock_methods(self)` (method)
