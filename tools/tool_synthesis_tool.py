"""synthesize_tool — let the agent forge, verify, and persist a new tool.

Gated OFF by default (config ``tool_synthesis.enabled``): the tool only appears
to the agent when the user opts in. The forged tool is validated, sandbox
smoke-tested, and saved to ~/.janus/dynamic_tools/; it becomes callable next
session (or after /reload-tools), NOT mid-conversation — that keeps the live
tool array and prompt cache stable.
"""
import json

from tools.registry import registry


def _synthesis_enabled() -> bool:
    try:
        from agent.tool_synthesis import is_enabled
        return is_enabled()
    except Exception:
        return False


def synthesize_tool(name: str, description: str = "", parameters=None,
                    code: str = "", test_input=None, **_kw) -> str:
    try:
        from agent.tool_synthesis import save_dynamic_tool

        if isinstance(parameters, str):
            try:
                parameters = json.loads(parameters)
            except Exception:
                parameters = None
        if isinstance(test_input, str):
            try:
                test_input = json.loads(test_input)
            except Exception:
                test_input = None
        res = save_dynamic_tool({
            "name": name, "description": description,
            "parameters": parameters, "code": code, "test_input": test_input or {},
        })
        if not res.get("ok"):
            return json.dumps({"success": False, "error": res.get("error")})
        return json.dumps({
            "success": True,
            "saved": res["path"],
            "smoke_output": res.get("smoke_output"),
            "note": "Tool verified + saved. It becomes callable next session "
                    "(or after /reload-tools) — not mid-conversation.",
        }, ensure_ascii=False)
    except Exception as exc:
        return json.dumps({"success": False, "error": str(exc)})


registry.register(
    name="synthesize_tool",
    toolset="tool_synthesis",
    schema={
        "name": "synthesize_tool",
        "description": (
            "Create a NEW reusable tool at runtime when no existing tool fits and the "
            "capability is worth keeping. Provide a Python 'run(**kwargs) -> str' "
            "implementation; it is validated, security-scanned, and sandbox smoke-tested "
            "before being saved. The new tool becomes callable in your NEXT session (or "
            "after /reload-tools), not immediately. Prefer a skill for prose procedures; "
            "use this for a genuinely new callable capability."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "name": {"type": "string", "description": "snake_case tool name"},
                "description": {"type": "string", "description": "what the tool does (for the model)"},
                "parameters": {"type": "object", "description": "JSON-Schema for the tool's arguments"},
                "code": {"type": "string", "description": "Python source defining 'def run(**kwargs) -> str:'"},
                "test_input": {"type": "object", "description": "sample kwargs to smoke-test run() with"},
            },
            "required": ["name", "code"],
        },
    },
    handler=lambda args, **kw: synthesize_tool(
        name=args.get("name", ""), description=args.get("description", ""),
        parameters=args.get("parameters"), code=args.get("code", ""),
        test_input=args.get("test_input"),
    ),
    check_fn=_synthesis_enabled,
)
