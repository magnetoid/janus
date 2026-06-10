"""Runtime tool synthesis — the agent forges, verifies, and persists its own tools.

The apex of the self-improvement arc: where Janus already self-creates *skills*
(markdown + scripts), this lets it mint a genuinely new *callable tool*. The
agent supplies a name, a JSON-Schema for the arguments, a ``run(**kwargs) -> str``
implementation, and a smoke-test input. The code is

  1. validated (AST parse + must define ``run`` + threat-scanned), then
  2. sandbox smoke-tested in a separate subprocess (with a timeout), then
  3. persisted to ``~/.janus/dynamic_tools/<name>.py``.

Verified dynamic tools are registered into the ``dynamic`` toolset at startup,
so a forged tool becomes available next session (or after ``/reload-tools``) —
deliberately NOT hot-swapped mid-conversation, which would churn the live
tool array. Activation respects the prompt-cache invariant.

SECURITY: synthesized code runs with the agent's privileges — no more than the
agent already has via ``terminal()``, but it *persists*. So the whole feature is
gated OFF by default (``tool_synthesis.enabled``); code is threat-scanned and
smoke-tested before it is ever saved; and tools land in a plain, user-visible
directory that can be inspected or deleted.
"""
from __future__ import annotations

import ast
import json
import logging
import re
import subprocess
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional

logger = logging.getLogger(__name__)

DYNAMIC_TOOLSET = "dynamic"


def get_dynamic_tools_dir() -> Path:
    from janus_constants import get_janus_home
    return get_janus_home() / "dynamic_tools"


def is_enabled() -> bool:
    """Tool synthesis + dynamic-tool loading are off unless explicitly enabled."""
    try:
        import yaml
        from janus_constants import get_janus_home
        cfg_path = get_janus_home() / "config.yaml"
        if cfg_path.is_file():
            cfg = yaml.safe_load(cfg_path.read_text(encoding="utf-8")) or {}
            return bool((cfg.get("tool_synthesis") or {}).get("enabled", False))
    except Exception:
        pass
    return False


def _slug(name: str) -> str:
    s = re.sub(r"[^a-z0-9_]+", "_", str(name).strip().lower()).strip("_")
    return s or "tool"


def validate_tool_code(code: str) -> List[str]:
    """Return a list of problems with ``code`` (empty == valid).

    Checks: parses, defines a top-level ``run`` function, and passes the strict
    threat scanner (the same one used for memory/skills)."""
    issues: List[str] = []
    if not code or not code.strip():
        return ["empty code"]
    try:
        tree = ast.parse(code)
    except SyntaxError as exc:
        return [f"syntax error: {exc.msg} (line {exc.lineno})"]
    has_run = any(
        isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef)) and n.name == "run"
        for n in tree.body
    )
    if not has_run:
        issues.append("must define a top-level 'run(**kwargs)' function")
    try:
        from tools.threat_patterns import first_threat_message
        threat = first_threat_message(code, scope="strict")
        if threat:
            issues.append(f"blocked by security scan: {threat}")
    except Exception:
        pass
    return issues


def _build_module_source(spec: Dict[str, Any]) -> str:
    """Render the persisted module: a SCHEMA dict + the agent's run() code."""
    schema = {
        "name": spec["name"],
        "description": spec.get("description", ""),
        "parameters": spec.get("parameters") or {"type": "object", "properties": {}},
    }
    return (
        '"""Dynamic tool synthesized by Janus. Review before trusting."""\n'
        f"SCHEMA = {json.dumps(schema, indent=4, ensure_ascii=False)}\n\n"
        f"{spec['code'].strip()}\n"
    )


def smoke_test(code: str, test_input: Optional[Dict[str, Any]] = None, *, timeout: float = 10.0) -> Dict[str, Any]:
    """Run ``run(**test_input)`` in an isolated subprocess. Returns {ok, output, error}."""
    test_input = test_input or {}
    harness = (
        f"{code}\n\n"
        "import json, sys\n"
        "try:\n"
        "    _out = run(**json.loads(sys.argv[1]))\n"
        "    print('__SMOKE_OK__' + json.dumps(str(_out)))\n"
        "except Exception as _e:\n"
        "    print('__SMOKE_ERR__' + json.dumps(repr(_e)))\n"
    )
    try:
        proc = subprocess.run(
            [sys.executable, "-c", harness, json.dumps(test_input)],
            capture_output=True, text=True, timeout=timeout,
        )
    except subprocess.TimeoutExpired:
        return {"ok": False, "output": None, "error": f"timed out after {timeout}s"}
    out = (proc.stdout or "").strip()
    if "__SMOKE_OK__" in out:
        payload = out.split("__SMOKE_OK__", 1)[1].splitlines()[0]
        try:
            return {"ok": True, "output": json.loads(payload), "error": None}
        except Exception:
            return {"ok": True, "output": payload, "error": None}
    if "__SMOKE_ERR__" in out:
        payload = out.split("__SMOKE_ERR__", 1)[1].splitlines()[0]
        return {"ok": False, "output": None, "error": json.loads(payload) if payload else "error"}
    return {"ok": False, "output": None, "error": (proc.stderr or "no output").strip()[:300]}


def save_dynamic_tool(spec: Dict[str, Any]) -> Dict[str, Any]:
    """Validate + smoke-test + persist a synthesized tool. Returns {ok, path|error}.

    ``spec``: {name, description, parameters(dict), code(str), test_input(dict)}.
    """
    name = _slug(spec.get("name", ""))
    if not name:
        return {"ok": False, "error": "a tool name is required"}
    code = spec.get("code", "")
    issues = validate_tool_code(code)
    if issues:
        return {"ok": False, "error": "; ".join(issues)}
    smoke = smoke_test(code, spec.get("test_input") or {})
    if not smoke["ok"]:
        return {"ok": False, "error": f"smoke test failed: {smoke['error']}"}
    spec = {**spec, "name": name}
    d = get_dynamic_tools_dir()
    d.mkdir(parents=True, exist_ok=True)
    path = d / f"{name}.py"
    path.write_text(_build_module_source(spec), encoding="utf-8")
    return {"ok": True, "path": str(path), "smoke_output": smoke["output"]}


def list_dynamic_tools() -> List[str]:
    d = get_dynamic_tools_dir()
    return sorted(p.stem for p in d.glob("*.py")) if d.is_dir() else []


def remove_dynamic_tool(name: str) -> bool:
    path = get_dynamic_tools_dir() / f"{_slug(name)}.py"
    if path.is_file():
        try:
            path.unlink()
            return True
        except OSError:
            return False
    return False


def _make_handler(run_fn):
    def _handler(args, **kw):
        try:
            result = run_fn(**(args or {}))
            return result if isinstance(result, str) else json.dumps(result, ensure_ascii=False, default=str)
        except Exception as exc:
            return json.dumps({"success": False, "error": str(exc)})
    return _handler


def load_dynamic_tools() -> int:
    """Register all persisted dynamic tools into the registry. Returns the count.

    No-op (and loads nothing) unless ``tool_synthesis.enabled`` — loading exec's
    the saved modules, so it stays behind the same gate as synthesis. Each tool
    is re-validated before it's loaded; a broken/poisoned file is skipped."""
    if not is_enabled():
        return 0
    from tools.registry import registry

    loaded = 0
    for path in sorted(get_dynamic_tools_dir().glob("*.py")) if get_dynamic_tools_dir().is_dir() else []:
        try:
            code = path.read_text(encoding="utf-8")
            if validate_tool_code(code):  # re-validate on every load
                logger.debug("dynamic tool %s failed re-validation; skipped", path.stem)
                continue
            ns: Dict[str, Any] = {}
            exec(compile(code, str(path), "exec"), ns)  # noqa: S102 — gated, validated
            schema = ns.get("SCHEMA")
            run_fn = ns.get("run")
            if not isinstance(schema, dict) or not callable(run_fn):
                continue
            registry.register(
                name=schema.get("name", path.stem),
                toolset=DYNAMIC_TOOLSET,
                schema=schema,
                handler=_make_handler(run_fn),
                description=schema.get("description", ""),
                override=True,
            )
            loaded += 1
        except Exception as exc:
            logger.debug("failed to load dynamic tool %s: %s", path, exc)
    return loaded
