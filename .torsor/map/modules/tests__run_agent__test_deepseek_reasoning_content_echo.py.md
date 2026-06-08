---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/run_agent/test_deepseek_reasoning_content_echo.py

Symbols in `tests/run_agent/test_deepseek_reasoning_content_echo.py`.

- L39 `_make_agent(provider: str='', model: str='', base_url: str='')` (function)
- L55 `_sdk_tool_call(call_id: str='c1', name: str='terminal', arguments: str='{}')` (function) — Minimal SDK-shaped tool_call object that satisfies the builder's iteration.
- L66 `_build_sdk_message(reasoning_content=_ATTR_ABSENT, **extra)` (function) — SDK-shaped assistant message; ``reasoning_content`` defaults to absent.
- L74 `TestNeedsDeepSeekToolReasoning` (class) — _needs_deepseek_tool_reasoning() recognises all three detection signals.
- L77 `test_provider_deepseek(self)` (method)
- L81 `test_model_substring(self)` (method)
- L86 `test_base_url_host(self)` (method)
- L94 `test_provider_case_insensitive(self)` (method)
- L98 `test_non_deepseek_provider(self)` (method)
- L106 `test_empty_everything(self)` (method)
- L111 `TestCopyReasoningContentForApi` (class) — _copy_reasoning_content_for_api pads reasoning_content for DeepSeek tool-calls.
- L114 `test_deepseek_tool_call_poisoned_history_gets_space_placeholder(self)` (method) — Already-poisoned history (no reasoning_content, no reasoning) gets ' '.
- L126 `test_deepseek_assistant_no_tool_call_gets_padded(self)` (method) — DeepSeek thinking mode pads ALL assistant turns, even without tool_calls.
- L134 `test_deepseek_explicit_reasoning_content_preserved(self)` (method) — When reasoning_content is already set, it's copied verbatim.
- L146 `test_deepseek_stale_empty_placeholder_upgraded_to_space(self)` (method) — Sessions persisted before #17341 have ``reasoning_content=""`` pinned
- L163 `test_non_thinking_provider_preserves_empty_reasoning_content_verbatim(self)` (method) — The stale-placeholder upgrade ONLY fires when the active provider
- L182 `test_deepseek_reasoning_field_promoted(self)` (method) — When only 'reasoning' is set, it gets promoted to reasoning_content.
- L194 `test_deepseek_poisoned_cross_provider_history_padded(self)` (method) — Cross-provider tool-call turn (#15748): MiniMax reasoning leaks
- L214 `test_kimi_poisoned_cross_provider_history_padded(self)` (method) — Kimi path of #15748 — same rule as DeepSeek.
- L227 `test_kimi_path_still_works(self)` (method) — Existing Kimi detection still pads reasoning_content.
- L239 `test_kimi_moonshot_base_url(self)` (method)
- L252 `test_non_thinking_provider_not_padded(self)` (method) — Providers that don't require the echo are untouched.
- L268 `test_deepseek_custom_base_url(self)` (method) — Custom provider pointing at api.deepseek.com is detected via host.
- L284 `test_non_assistant_role_ignored(self)` (method) — User/tool messages are left alone.
- L293 `TestBuildAssistantMessageDeepSeekReasoningContent` (class) — _build_assistant_message pins replay-safe DeepSeek tool-call state.
- L296 `test_deepseek_tool_call_reasoning_is_backfilled_into_reasoning_content(self)` (method)
- L321 `test_deepseek_model_extra_reasoning_content_is_preserved(self)` (method) — OpenAI SDK stores unknown provider fields in model_extra.
- L347 `test_deepseek_tool_call_without_raw_reasoning_content_gets_space_placeholder(self)` (method)
- L373 `TestBuildAssistantMessagePadsStrictProviders` (class) — Regression for #17400: _build_assistant_message must pin reasoning_content
- L415 `test_tool_call_reasoning_content_pad(self, provider, model, base_url, sdk_reasoning_content, expected)` (method)
- L429 `test_tool_call_preserves_real_reasoning_content(self)` (method)
- L438 `test_text_only_turn_not_padded_by_tool_call_branch(self)` (method) — Plain-text turns rely on _copy_reasoning_content_for_api at replay
- L447 `test_streamed_reasoning_text_promoted_over_pad(self)` (method) — When ``.reasoning`` carries streamed thinking, it must be promoted
- L459 `TestNeedsKimiToolReasoning` (class) — The extracted _needs_kimi_tool_reasoning() helper keeps Kimi behavior intact.
- L472 `test_kimi_signals(self, provider: str, base_url: str)` (method)
- L476 `test_non_kimi_provider(self)` (method)
- L486 `TestReapplyReasoningEchoForProviderSwitch` (class) — Mid-conversation fallover to a require-side provider must re-pad.
- L501 `_codex_built_history()` (method) — Assistant turns as built under a Codex primary: some carry a
- L522 `test_switch_to_deepseek_pads_bare_turns(self)` (method)
- L535 `test_noop_under_non_require_provider(self)` (method)
- L549 `test_idempotent(self)` (method)
- L557 `test_non_assistant_messages_untouched(self)` (method)
