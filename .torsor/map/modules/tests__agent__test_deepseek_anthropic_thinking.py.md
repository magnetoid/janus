---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/agent/test_deepseek_anthropic_thinking.py

Symbols in `tests/agent/test_deepseek_anthropic_thinking.py`.

- L27 `TestDeepSeekAnthropicPreservesThinking` (class) — convert_messages_to_anthropic must replay DeepSeek thinking blocks.
- L39 `test_unsigned_thinking_block_survives_replay(self, base_url: str)` (method) — Unsigned thinking (synthesised from reasoning_content) must be preserved.
- L76 `test_unsigned_thinking_preserved_on_non_latest_assistant_turn(self)` (method) — DeepSeek validates history across every prior assistant turn, not just last.
- L122 `test_signed_anthropic_thinking_block_is_stripped(self)` (method) — Anthropic-signed blocks (that leaked through) must still be stripped.
- L159 `test_cache_control_stripped_from_thinking_block(self)` (method) — cache_control must still be stripped even when the block is preserved.
- L197 `test_openai_compat_deepseek_base_is_not_matched(self)` (method) — The OpenAI-compatible ``api.deepseek.com`` base must NOT trigger the
- L210 `test_non_deepseek_third_party_still_strips_all_thinking(self)` (method) — MiniMax and other third-party Anthropic endpoints must keep the
