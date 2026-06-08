---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# agent/tool_guardrails.py

Symbols in `agent/tool_guardrails.py`.

- L64 `ToolCallGuardrailConfig` (class) — Thresholds for per-turn tool-call loop detection.
- L84 `from_mapping(cls, data: Mapping[str, Any] | None)` (method) — Build config from the `tool_loop_guardrails` config.yaml section.
- L128 `ToolCallSignature` (class) — Stable, non-reversible identity for a tool name plus canonical args.
- L135 `from_call(cls, tool_name: str, args: Mapping[str, Any] | None)` (method)
- L139 `to_metadata(self)` (method) — Return public metadata without raw argument values.
- L145 `ToolGuardrailDecision` (class) — Decision returned by the tool-call guardrail controller.
- L156 `allows_execution(self)` (method)
- L160 `should_halt(self)` (method)
- L163 `to_metadata(self)` (method)
- L176 `canonical_tool_args(args: Mapping[str, Any])` (function) — Return sorted compact JSON for parsed tool arguments.
- L189 `classify_tool_failure(tool_name: str, result: str | None)` (function) — Safety-fallback classifier used only when callers don't pass ``failed``.
- L224 `ToolCallGuardrailController` (class) — Per-turn controller for repeated failed/non-progressing tool calls.
- L227 `__init__(self, config: ToolCallGuardrailConfig | None=None)` (method)
- L231 `reset_for_turn(self)` (method)
- L238 `halt_decision(self)` (method)
- L241 `before_call(self, tool_name: str, args: Mapping[str, Any] | None)` (method)
- L285 `after_call(self, tool_name: str, args: Mapping[str, Any] | None, result: str | None, *, failed: bool | None=None)` (method)
- L377 `_is_idempotent(self, tool_name: str)` (method)
- L383 `toolguard_synthetic_result(decision: ToolGuardrailDecision)` (function) — Build a synthetic role=tool content string for a blocked tool call.
- L394 `append_toolguard_guidance(result: str, decision: ToolGuardrailDecision)` (function) — Append runtime guidance to the current tool result content.
- L406 `_tool_failure_recovery_hint(tool_name: str, count: int)` (function) — Action-oriented guidance for recovering from repeated tool failures.
- L426 `_coerce_args(args: Mapping[str, Any] | None)` (function)
- L430 `_result_hash(result: str | None)` (function)
- L448 `_as_bool(value: Any, default: bool)` (function)
- L464 `_positive_int(value: Any, default: int)` (function)
- L474 `_sha256(value: str)` (function)
