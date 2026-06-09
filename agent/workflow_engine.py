"""Declarative workflow engine — Lobster-style multi-step orchestration.

Janus already has ``delegate_task`` (imperative subagent spawning). This adds
the DECLARATIVE pipeline OpenClaw's "Lobster" engine provides: a workflow is a
YAML file of ordered steps, where each step can

  * restrict the tools/model it runs with (per-step permissions),
  * run conditionally (``when``),
  * loop over a list (``for_each``),

and step outputs thread into later steps via ``{variable}`` substitution.

The engine is pure and injectable (``step_runner``) so the control flow is
fully testable without a live model. The real runner (CLI) executes each step
as a focused ``delegate_task`` subagent.

Example ``~/.janus/workflows/research.yaml``::

    name: research
    description: Research a topic and summarize it
    steps:
      - name: gather
        prompt: "Search the web for {topic}; list the key findings."
        toolsets: [web]
        output: findings
      - name: summarize
        prompt: "Summarize these findings concisely:\\n{findings}"
        when: findings
        output: summary
"""
from __future__ import annotations

import logging
import re
from pathlib import Path
from typing import Any, Callable, Dict, List, Optional

logger = logging.getLogger(__name__)

MAX_FOR_EACH = 50  # safety cap on loop iterations


def get_workflows_dir() -> Path:
    from janus_constants import get_janus_home
    return get_janus_home() / "workflows"


def load_workflow(name_or_path: str) -> Dict[str, Any]:
    """Load a workflow by name (from the workflows dir) or explicit path."""
    import yaml

    p = Path(name_or_path)
    if not p.is_file():
        stem = name_or_path[:-5] if name_or_path.endswith(".yaml") else name_or_path
        p = get_workflows_dir() / f"{stem}.yaml"
    if not p.is_file():
        raise FileNotFoundError(f"Workflow not found: {name_or_path}")
    data = yaml.safe_load(p.read_text(encoding="utf-8")) or {}
    if not isinstance(data, dict) or not isinstance(data.get("steps"), list):
        raise ValueError(f"Invalid workflow (needs a 'steps' list): {p}")
    return data


def list_workflows() -> List[str]:
    d = get_workflows_dir()
    return sorted(p.stem for p in d.glob("*.yaml")) if d.is_dir() else []


_VAR = re.compile(r"\{([a-zA-Z_][a-zA-Z0-9_]*)\}")


def _render(template: Any, context: Dict[str, Any]) -> str:
    """Substitute ``{var}`` from context; unknown vars render empty."""
    def _sub(m):
        return str(context.get(m.group(1), ""))
    return _VAR.sub(_sub, str(template))


def _eval_when(cond: Any, context: Dict[str, Any]) -> bool:
    """Evaluate a step's ``when`` guard. Safe — no arbitrary code.

    Supported:
      - bare var name -> truthy check ("findings")
      - ``a == b`` / ``a != b`` / ``a contains b`` with {var} substitution
    """
    if cond is None:
        return True
    if isinstance(cond, bool):
        return cond
    s = str(cond).strip()
    if not s:
        return True
    for op in ("==", "!=", " contains "):
        if op in s:
            left, right = s.split(op, 1)
            lv = _render(left.strip(), context).strip()
            rv = _render(right.strip(), context).strip().strip("'\"")
            if op == "==":
                return lv == rv
            if op == "!=":
                return lv != rv
            return rv in lv
    # A bare identifier is a context variable name -> truthy check.
    if re.fullmatch(r"[a-zA-Z_][a-zA-Z0-9_]*", s):
        return bool(context.get(s))
    # Otherwise render any {vars} and check the result is non-empty.
    return bool(_render(s, context).strip())


def _resolve_list(name: Any, context: Dict[str, Any]) -> List[Any]:
    val = context.get(str(name))
    if isinstance(val, list):
        return val
    if isinstance(val, str):
        # newline- or comma-separated string -> list
        parts = [p.strip() for p in re.split(r"[\n,]", val) if p.strip()]
        return parts
    return []


def run_workflow(
    workflow: Dict[str, Any],
    *,
    step_runner: Callable[[Dict[str, Any], Dict[str, Any]], str],
    context: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """Execute ``workflow``'s steps in order. Returns {context, ran, skipped, error}.

    ``step_runner(rendered_step, context)`` runs one step and returns its output
    text. ``rendered_step`` is a copy of the step dict with its ``prompt`` already
    substituted and (for loops) an ``item`` key in context.
    """
    ctx: Dict[str, Any] = dict(context or {})
    ran: List[str] = []
    skipped: List[str] = []
    error: Optional[str] = None
    try:
        for step in workflow.get("steps", []):
            if not isinstance(step, dict):
                continue
            name = str(step.get("name") or f"step{len(ran) + len(skipped) + 1}")
            if not _eval_when(step.get("when"), ctx):
                skipped.append(name)
                continue

            iterations = [None]
            if step.get("for_each"):
                iterations = _resolve_list(step["for_each"], ctx)[:MAX_FOR_EACH]
                if not iterations:
                    skipped.append(name)
                    continue

            outputs = []
            for item in iterations:
                step_ctx = dict(ctx)
                if item is not None:
                    step_ctx["item"] = item
                rendered = dict(step)
                rendered["prompt"] = _render(step.get("prompt", ""), step_ctx)
                out = step_runner(rendered, step_ctx)
                outputs.append("" if out is None else str(out))

            result = outputs[0] if len(outputs) == 1 else "\n\n".join(outputs)
            out_key = step.get("output") or name
            ctx[str(out_key)] = result
            ran.append(name)
    except Exception as exc:  # a workflow failure must be reported, not crash
        logger.debug("workflow run failed: %s", exc)
        error = str(exc)
    return {"context": ctx, "ran": ran, "skipped": skipped, "error": error}


def default_step_runner(step: Dict[str, Any], context: Dict[str, Any]) -> str:
    """Run one workflow step as a focused delegate_task subagent (real execution)."""
    from tools.delegate_tool import delegate_task

    kwargs: Dict[str, Any] = {"goal": step.get("prompt", "")}
    if step.get("toolsets"):
        kwargs["toolsets"] = step["toolsets"]
    if step.get("model"):
        kwargs["model"] = step["model"]
    if step.get("provider"):
        kwargs["provider"] = step["provider"]
    try:
        result = delegate_task(**kwargs)
        return result if isinstance(result, str) else str(result)
    except Exception as exc:
        logger.debug("step '%s' delegate failed: %s", step.get("name"), exc)
        return f"[step failed: {exc}]"
