---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# scripts/tool_search_livetest.py

Symbols in `scripts/tool_search_livetest.py`.

- L251 `setup_isolated_home(enabled: bool)` (function) — Create a fresh ~/.hermes/ for one test, copying minimal credentials.
- L297 `_yaml_dump(obj: Any)` (function)
- L305 `register_fake_tools()` (function) — Register the FAKE_MCP_TOOLS into the live tool registry.
- L343 `reset_module_state()` (function) — Drop cached modules so the new HERMES_HOME takes effect.
- L352 `run_one_scenario(scenario: Dict[str, Any], enabled: bool, out_dir: Path)` (function) — Run one (scenario, enabled) combination. Returns the recorded transcript.
- L447 `_redact_secrets(text: str)` (function) — Strip anything secret-shaped from text before it is stored or printed.
- L468 `_trim_args(args: Any, max_chars: int=300)` (function) — Trim long string args so the log stays readable.
- L481 `_count_assistant_turns(messages: List[Dict[str, Any]])` (function)
- L485 `_extract_bridge_calls(messages: List[Dict[str, Any]])` (function) — Pull out every tool_search / tool_describe / tool_call from a transcript.
- L508 `main()` (function)
