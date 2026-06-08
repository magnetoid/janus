---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/test_yuanbao_pipeline.py

Symbols in `tests/test_yuanbao_pipeline.py`.

- L52 `make_config(**kwargs)` (function)
- L64 `make_adapter(**kwargs)` (function) — Create a YuanbaoAdapter with test config.
- L72 `make_ctx(adapter=None, conn_data=b'', **overrides)` (function) — Create an InboundContext with sensible defaults for testing.
- L83 `make_json_push(from_account='alice', to_account='bot_123', group_code='', text='Hello!', msg_id='msg-001')` (function) — Build a JSON callback_command push payload.
- L113 `TestInboundPipeline` (class) — Test the pipeline engine itself.
- L117 `test_empty_pipeline(self)` (method) — Empty pipeline executes without error.
- L124 `test_single_middleware(self)` (method) — Single middleware is called with ctx and next_fn.
- L138 `test_middleware_order(self)` (method) — Middlewares execute in registration order.
- L159 `test_middleware_can_stop_pipeline(self)` (method) — A middleware that doesn't call next_fn stops the pipeline.
- L176 `test_conditional_guard_skip(self)` (method) — Middleware with when=False is skipped.
- L202 `test_conditional_guard_pass(self)` (method) — Middleware with when=True is executed.
- L214 `test_use_before(self)` (method) — use_before inserts middleware before the target.
- L223 `test_use_before_nonexistent_appends(self)` (method) — use_before with nonexistent target appends to end.
- L232 `test_use_after(self)` (method) — use_after inserts middleware after the target.
- L241 `test_use_after_nonexistent_appends(self)` (method) — use_after with nonexistent target appends to end.
- L250 `test_remove(self)` (method) — remove deletes middleware by name.
- L259 `test_remove_nonexistent_is_noop(self)` (method) — remove with nonexistent name is a no-op.
- L269 `test_error_propagation(self)` (method) — Errors in middlewares propagate to the caller.
- L278 `test_middleware_names_property(self)` (method) — middleware_names returns ordered list of names.
- L292 `test_onion_model(self)` (method) — Middlewares support before/after processing (onion model).
- L314 `TestInboundContext` (class)
- L315 `test_default_values(self)` (method) — InboundContext has sensible defaults.
- L334 `test_mutable_fields(self)` (method) — InboundContext fields are mutable.
- L347 `TestDecodeMiddleware` (class)
- L349 `test_json_decode(self)` (method) — DecodeMiddleware parses JSON push correctly.
- L363 `test_empty_data_stops_pipeline(self)` (method) — DecodeMiddleware stops pipeline on empty conn_data.
- L374 `test_invalid_data_may_produce_garbage(self)` (method) — DecodeMiddleware: binary data may be parsed by protobuf as garbage fields.
- L391 `TestExtractFieldsMiddleware` (class)
- L393 `test_extracts_fields(self)` (method) — ExtractFieldsMiddleware populates ctx from push dict.
- L418 `TestDedupMiddleware` (class)
- L420 `test_new_message_passes(self)` (method) — DedupMiddleware passes new messages through.
- L430 `test_duplicate_stops_pipeline(self)` (method) — DedupMiddleware stops pipeline for duplicate messages.
- L443 `test_empty_msg_id_passes(self)` (method) — DedupMiddleware passes messages with empty msg_id.
- L452 `TestSkipSelfMiddleware` (class)
- L454 `test_self_message_stops(self)` (method) — SkipSelfMiddleware stops pipeline for bot's own messages.
- L465 `test_other_message_passes(self)` (method) — SkipSelfMiddleware passes messages from other users.
- L476 `TestChatRoutingMiddleware` (class)
- L478 `test_group_routing(self)` (method) — ChatRoutingMiddleware sets group chat fields.
- L491 `test_dm_routing(self)` (method) — ChatRoutingMiddleware sets DM chat fields.
- L504 `test_dm_routing_no_nickname(self)` (method) — ChatRoutingMiddleware falls back to from_account when no nickname.
- L514 `TestAccessGuardMiddleware` (class)
- L516 `test_open_policy_passes(self)` (method) — AccessGuardMiddleware passes with open policy.
- L527 `test_disabled_dm_stops(self)` (method) — AccessGuardMiddleware stops DM when dm_policy=disabled.
- L538 `test_allowlist_dm_allowed(self)` (method) — AccessGuardMiddleware passes DM when sender is in allowlist.
- L549 `test_allowlist_dm_blocked(self)` (method) — AccessGuardMiddleware blocks DM when sender is not in allowlist.
- L560 `test_disabled_group_stops(self)` (method) — AccessGuardMiddleware stops group when group_policy=disabled.
- L571 `test_allowlist_group_allowed(self)` (method) — AccessGuardMiddleware passes group when group_code is in allowlist.
- L582 `TestExtractContentMiddleware` (class)
- L584 `test_extracts_text_and_media(self)` (method) — ExtractContentMiddleware extracts text and media refs.
- L604 `TestPlaceholderFilterMiddleware` (class)
- L606 `test_placeholder_stops(self)` (method) — PlaceholderFilterMiddleware stops on pure placeholder.
- L615 `test_placeholder_with_media_passes(self)` (method) — PlaceholderFilterMiddleware passes placeholder when media exists.
- L627 `test_normal_text_passes(self)` (method) — PlaceholderFilterMiddleware passes normal text.
- L636 `TestGroupAtGuardMiddleware` (class)
- L638 `test_dm_passes(self)` (method) — GroupAtGuardMiddleware passes DM messages.
- L648 `test_group_with_at_bot_passes(self)` (method) — GroupAtGuardMiddleware passes group messages that @bot.
- L673 `test_group_without_at_bot_observes(self)` (method) — GroupAtGuardMiddleware observes group messages without @bot.
- L695 `test_owner_command_skips_at_check(self)` (method) — GroupAtGuardMiddleware passes when owner_command is set.
- L716 `TestCreateInboundPipeline` (class)
- L717 `test_default_pipeline_has_all_middlewares(self)` (method) — InboundPipelineBuilder.build() creates pipeline with all expected middlewares.
- L754 `TestPipelineIntegration` (class)
- L756 `test_full_dm_message_flow(self)` (method) — Full pipeline processes a DM message end-to-end.
- L784 `test_self_message_filtered(self)` (method) — Pipeline stops when message is from bot itself.
- L804 `test_duplicate_message_filtered(self)` (method) — Pipeline stops on duplicate message.
- L827 `test_blocked_dm_filtered(self)` (method) — Pipeline stops when DM is blocked by policy.
- L847 `test_adapter_has_pipeline(self)` (method) — YuanbaoAdapter.__init__ creates an inbound pipeline.
- L863 `TestInboundMiddlewareABC` (class) — Test the InboundMiddleware abstract base class.
- L866 `test_cannot_instantiate_abc(self)` (method) — InboundMiddleware cannot be instantiated directly.
- L871 `test_subclass_must_implement_handle(self)` (method) — Subclass without handle() raises TypeError.
- L878 `test_subclass_with_handle_works(self)` (method) — Subclass with handle() can be instantiated.
- L888 `test_callable_protocol(self)` (method) — Middleware instances are callable via __call__.
- L903 `test_repr(self)` (method) — Middleware has a useful repr.
- L914 `TestMiddlewareClasses` (class) — Test that all concrete middleware classes have correct names and are InboundMiddleware subclasses.
- L933 `test_is_inbound_middleware(self, cls, expected_name)` (method) — Each middleware class is a subclass of InboundMiddleware.
- L938 `test_has_correct_name(self, cls, expected_name)` (method) — Each middleware class has the expected name.
- L944 `test_is_callable(self, cls, expected_name)` (method) — Each middleware instance is callable.
- L950 `TestPipelineOOPRegistration` (class) — Test that InboundPipeline works with OOP middleware instances.
- L954 `test_use_with_middleware_instance(self)` (method) — pipeline.use(SomeMiddleware()) auto-extracts name.
- L970 `test_mixed_oop_and_functional(self)` (method) — Pipeline supports mixing OOP and functional middlewares.
- L994 `test_use_before_with_middleware_instance(self)` (method) — use_before works with OOP middleware instances.
- L1012 `test_use_after_with_middleware_instance(self)` (method) — use_after works with OOP middleware instances.
