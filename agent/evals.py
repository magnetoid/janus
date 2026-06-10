"""Eval harness — replayable regression checks for agent behavior.

Closes the measurement gap in the learning loop: skills get mined, memory
gets written, the curator consolidates — but nothing verifies that any of
it actually improved the agent. An eval is a recorded prompt plus a set of
deterministic checks against the agent's response and tool usage. Run the
suite before and after a skill/memory/config change to see whether behavior
regressed.

Eval specs are YAML files in ``$JANUS_HOME/evals/`` (or any path passed to
``janus evals run``). A file holds one spec or a list under ``evals:``::

    name: knows-project-stack
    prompt: "What test runner does this project use?"
    checks:
      - type: contains
        value: pytest
      - type: tool_not_called
        value: terminal

Check types: ``contains``, ``not_contains``, ``regex``, ``min_length``,
``max_length``, ``tool_called``, ``tool_not_called``. String matching is
case-insensitive unless ``case_sensitive: true``.

Runs are hermetic by default (``skip_memory`` / ``skip_context_files``) so
results are reproducible; set ``use_memory: true`` / ``use_context_files:
true`` per spec when the eval is *about* memory or context behavior.

Results are appended to ``$JANUS_HOME/evals/results/<timestamp>.jsonl``.
"""

from __future__ import annotations

import json
import logging
import re
import time
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Callable, Dict, List, Optional

from janus_constants import get_janus_home

logger = logging.getLogger(__name__)

CHECK_TYPES = frozenset({
    "contains",
    "not_contains",
    "regex",
    "min_length",
    "max_length",
    "tool_called",
    "tool_not_called",
})


@dataclass
class EvalSpec:
    name: str
    prompt: str
    checks: List[Dict[str, Any]]
    system: Optional[str] = None
    toolsets: Optional[List[str]] = None
    model: Optional[str] = None
    provider: Optional[str] = None
    max_iterations: int = 15
    use_memory: bool = False
    use_context_files: bool = False
    source_file: Optional[str] = None


def evals_dir() -> Path:
    return get_janus_home() / "evals"


def results_dir() -> Path:
    return evals_dir() / "results"


# ---------------------------------------------------------------------------
# Spec loading
# ---------------------------------------------------------------------------

def _spec_from_dict(raw: Dict[str, Any], source_file: str = "") -> EvalSpec:
    name = str(raw.get("name", "")).strip()
    prompt = str(raw.get("prompt", "")).strip()
    checks = raw.get("checks") or []
    if not name:
        raise ValueError(f"eval spec missing 'name' ({source_file or 'inline'})")
    if not prompt:
        raise ValueError(f"eval '{name}' missing 'prompt'")
    if not isinstance(checks, list) or not checks:
        raise ValueError(f"eval '{name}' needs a non-empty 'checks' list")
    for check in checks:
        ctype = (check or {}).get("type")
        if ctype not in CHECK_TYPES:
            raise ValueError(
                f"eval '{name}': unknown check type {ctype!r} "
                f"(expected one of {sorted(CHECK_TYPES)})"
            )
        if "value" not in (check or {}):
            raise ValueError(f"eval '{name}': check {ctype!r} missing 'value'")

    toolsets = raw.get("toolsets")
    if toolsets is not None and not isinstance(toolsets, list):
        toolsets = [str(toolsets)]

    return EvalSpec(
        name=name,
        prompt=prompt,
        checks=checks,
        system=raw.get("system"),
        toolsets=toolsets,
        model=raw.get("model"),
        provider=raw.get("provider"),
        max_iterations=int(raw.get("max_iterations", 15)),
        use_memory=bool(raw.get("use_memory", False)),
        use_context_files=bool(raw.get("use_context_files", False)),
        source_file=source_file,
    )


def load_eval_specs(path: Optional[Path] = None) -> List[EvalSpec]:
    """Load eval specs from a YAML file or every ``*.yaml`` in a directory.

    Defaults to ``$JANUS_HOME/evals/``. Raises ``ValueError`` on malformed
    specs and ``FileNotFoundError`` when the path doesn't exist.
    """
    import yaml

    root = Path(path) if path else evals_dir()
    if not root.exists():
        raise FileNotFoundError(f"no eval specs at {root}")

    files: List[Path]
    if root.is_dir():
        files = sorted(
            p for p in root.glob("*.yaml")
            if p.is_file() and not p.name.startswith(".")
        )
        files += sorted(
            p for p in root.glob("*.yml")
            if p.is_file() and not p.name.startswith(".")
        )
    else:
        files = [root]

    specs: List[EvalSpec] = []
    seen: set = set()
    for f in files:
        raw = yaml.safe_load(f.read_text(encoding="utf-8"))
        if raw is None:
            continue
        items = raw.get("evals") if isinstance(raw, dict) and "evals" in raw else raw
        if isinstance(items, dict):
            items = [items]
        if not isinstance(items, list):
            raise ValueError(f"{f}: expected a spec mapping or 'evals:' list")
        for item in items:
            spec = _spec_from_dict(item, source_file=str(f))
            if spec.name in seen:
                raise ValueError(f"duplicate eval name '{spec.name}' ({f})")
            seen.add(spec.name)
            specs.append(spec)
    return specs


# ---------------------------------------------------------------------------
# Checks
# ---------------------------------------------------------------------------

def _called_tools(messages: List[Dict[str, Any]]) -> List[str]:
    names: List[str] = []
    for msg in messages or []:
        if msg.get("role") != "assistant":
            continue
        for tool_call in msg.get("tool_calls") or []:
            if isinstance(tool_call, dict):
                name = (tool_call.get("function") or {}).get("name")
                if name:
                    names.append(name)
    return names


def evaluate_checks(
    checks: List[Dict[str, Any]],
    final_response: str,
    messages: Optional[List[Dict[str, Any]]] = None,
) -> List[Dict[str, Any]]:
    """Run every check; returns one result dict per check.

    Each result: ``{"type", "value", "passed", "detail"}``. Never raises —
    a check that errors counts as failed with the error in ``detail``.
    """
    response = final_response or ""
    tools = _called_tools(messages or [])
    results: List[Dict[str, Any]] = []

    for check in checks:
        ctype = check.get("type")
        value = check.get("value")
        case_sensitive = bool(check.get("case_sensitive", False))
        passed = False
        detail = ""
        try:
            if ctype == "contains":
                haystack = response if case_sensitive else response.lower()
                needle = str(value) if case_sensitive else str(value).lower()
                passed = needle in haystack
                detail = "" if passed else f"{value!r} not in response"
            elif ctype == "not_contains":
                haystack = response if case_sensitive else response.lower()
                needle = str(value) if case_sensitive else str(value).lower()
                passed = needle not in haystack
                detail = "" if passed else f"{value!r} found in response"
            elif ctype == "regex":
                flags = 0 if case_sensitive else re.IGNORECASE
                passed = re.search(str(value), response, flags) is not None
                detail = "" if passed else f"regex {value!r} did not match"
            elif ctype == "min_length":
                passed = len(response) >= int(value)
                detail = "" if passed else f"response length {len(response)} < {value}"
            elif ctype == "max_length":
                passed = len(response) <= int(value)
                detail = "" if passed else f"response length {len(response)} > {value}"
            elif ctype == "tool_called":
                passed = str(value) in tools
                detail = "" if passed else f"tool {value!r} not called (called: {tools})"
            elif ctype == "tool_not_called":
                passed = str(value) not in tools
                detail = "" if passed else f"tool {value!r} was called"
            else:
                detail = f"unknown check type {ctype!r}"
        except Exception as exc:
            passed = False
            detail = f"check error: {exc}"
        results.append(
            {"type": ctype, "value": value, "passed": passed, "detail": detail}
        )
    return results


# ---------------------------------------------------------------------------
# Runner
# ---------------------------------------------------------------------------

def _default_agent_runner(spec: EvalSpec) -> Dict[str, Any]:
    """Run one spec through a fresh AIAgent; returns the run_conversation dict."""
    from run_agent import AIAgent

    agent = AIAgent(
        model=spec.model or "",
        provider=spec.provider,
        max_iterations=spec.max_iterations,
        enabled_toolsets=spec.toolsets,
        quiet_mode=True,
        save_trajectories=False,
        skip_context_files=not spec.use_context_files,
        skip_memory=not spec.use_memory,
    )
    return agent.run_conversation(spec.prompt, system_message=spec.system)


def run_evals(
    specs: List[EvalSpec],
    agent_runner: Optional[Callable[[EvalSpec], Dict[str, Any]]] = None,
    on_progress: Optional[Callable[[str], None]] = None,
    save_results: bool = True,
) -> Dict[str, Any]:
    """Run every spec, returning a summary dict.

    ``agent_runner`` is injectable for tests; it takes a spec and returns a
    ``run_conversation``-shaped dict (``final_response`` + ``messages``).
    An exception from one eval marks it failed and the suite continues.
    """
    runner = agent_runner or _default_agent_runner
    say = on_progress or (lambda _msg: None)
    results: List[Dict[str, Any]] = []
    started = datetime.now(timezone.utc)

    for spec in specs:
        say(f"eval: {spec.name} ...")
        t0 = time.monotonic()
        error = ""
        check_results: List[Dict[str, Any]] = []
        try:
            run = runner(spec) or {}
            check_results = evaluate_checks(
                spec.checks,
                run.get("final_response") or "",
                run.get("messages") or [],
            )
        except Exception as exc:
            logger.warning("eval '%s' errored: %s", spec.name, exc)
            error = str(exc)
        duration = round(time.monotonic() - t0, 2)
        passed = bool(check_results) and all(c["passed"] for c in check_results)
        results.append({
            "name": spec.name,
            "passed": passed,
            "error": error,
            "checks": check_results,
            "duration_s": duration,
            "source_file": spec.source_file,
        })
        say(f"  {'PASS' if passed else 'FAIL'} ({duration}s)")

    summary = {
        "started_at": started.isoformat(),
        "total": len(results),
        "passed": sum(1 for r in results if r["passed"]),
        "failed": sum(1 for r in results if not r["passed"]),
        "results": results,
    }

    if save_results and results:
        try:
            summary["results_path"] = str(_save_results(summary))
        except OSError as exc:
            logger.warning("could not save eval results: %s", exc)
    return summary


def _save_results(summary: Dict[str, Any]) -> Path:
    out_dir = results_dir()
    out_dir.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S")
    out_path = out_dir / f"{stamp}.jsonl"
    with out_path.open("w", encoding="utf-8") as fh:
        for r in summary["results"]:
            fh.write(json.dumps(r, ensure_ascii=False) + "\n")
    return out_path


EXAMPLE_SPEC = """\
# Janus eval spec — run with `janus evals run`.
# One spec per file, or several under an `evals:` list.
name: example-arithmetic
prompt: "What is 6 * 7? Reply with just the number."
checks:
  - type: contains
    value: "42"
  - type: max_length
    value: 200
# Optional fields:
#   system: custom system prompt
#   toolsets: [web, file]
#   model: claude-sonnet-4-6        # override the configured model
#   max_iterations: 15
#   use_memory: true                # default false (hermetic)
#   use_context_files: true         # default false (hermetic)
# Check types: contains, not_contains, regex, min_length, max_length,
#              tool_called, tool_not_called  (case_sensitive: true to opt in)
"""


_DIALECTIC_SPEC = """\
# Validation pair for the dialectic `deliberate` tool (see
# website/docs/user-guide/features/deliberation.md). Requires the moa
# toolset and a configured auxiliary model. Run with:
#   janus evals run --filter dialectic
#
# Pins the frame-stability behavior: a genuinely frame-dependent question
# must flag frame_dependent, a frame-stable one must not. Run this suite
# before and after enabling learning.dialectic to validate the feature.
evals:
  - name: dialectic-frame-dependent-flags
    prompt: >-
      Use the deliberate tool on this question, then report the tool's raw
      JSON verdict verbatim: "Is remote work better than office work?"
    toolsets: [moa]
    checks:
      - type: tool_called
        value: deliberate
      - type: regex
        value: '"frame_dependent":\\s*true'
  - name: dialectic-frame-stable-does-not-flag
    prompt: >-
      Use the deliberate tool on this question, then report the tool's raw
      JSON verdict verbatim: "Is 17 a prime number?"
    toolsets: [moa]
    checks:
      - type: tool_called
        value: deliberate
      - type: regex
        value: '"frame_dependent":\\s*false'
"""

_BASICS_SPEC = """\
# Baseline behavior pins — cheap, model-agnostic sanity checks. A failure
# here after a config/model/skill change means something fundamental moved.
evals:
  - name: instruction-following-brevity
    prompt: "Reply with exactly the word OK and nothing else."
    checks:
      - type: contains
        value: OK
        case_sensitive: true
      - type: max_length
        value: 40
  - name: honest-uncertainty
    prompt: >-
      What is my favorite color? If you have no way to know, say you
      don't know.
    checks:
      - type: regex
        value: "don't know|do not know|no way (?:to|of) know|haven't told|not sure"
"""

STARTER_SPECS = {
    "example.yaml": EXAMPLE_SPEC,
    "basics.yaml": _BASICS_SPEC,
    "dialectic-validation.yaml": _DIALECTIC_SPEC,
}


def scaffold_example(force: bool = False) -> Path:
    """Write the example spec to ``$JANUS_HOME/evals/example.yaml``."""
    root = evals_dir()
    root.mkdir(parents=True, exist_ok=True)
    path = root / "example.yaml"
    if path.exists() and not force:
        return path
    path.write_text(EXAMPLE_SPEC, encoding="utf-8")
    return path


def scaffold_starters(force: bool = False) -> List[Path]:
    """Write every starter spec missing from ``$JANUS_HOME/evals/``.

    Returns the paths written this call (existing files are skipped unless
    ``force``), so user-edited specs are never clobbered by a re-init.
    """
    root = evals_dir()
    root.mkdir(parents=True, exist_ok=True)
    written: List[Path] = []
    for name, content in STARTER_SPECS.items():
        path = root / name
        if path.exists() and not force:
            continue
        path.write_text(content, encoding="utf-8")
        written.append(path)
    return written
