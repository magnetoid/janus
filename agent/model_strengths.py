"""Model-strengths intelligence — learn which models are best per task type.

Janus already does multi-model *consensus* via Mixture-of-Agents
(tools/mixture_of_agents_tool.py), but its reference models are hardcoded and
task-blind. This module is the missing learning layer: a durable knowledge base
mapping a TASK CATEGORY (coding, math, reasoning, writing, research, vision,
long-context, tool-use, …) to ranked models, which can be **seeded by web
research** ("best LLM for coding 2026") and queried to pick the best reference
+ aggregator models for a given task — intersected with what the user actually
has access to.

Pure helpers with injectable ``web_search_caller`` / ``llm_caller`` so the
research path is fully testable without network or a model.
"""
from __future__ import annotations

import json
import logging
import re
from pathlib import Path
from typing import Any, Callable, Dict, List, Optional

logger = logging.getLogger(__name__)


def get_strengths_path() -> Path:
    from janus_constants import get_janus_home
    return get_janus_home() / "model_strengths.json"


def _now_iso() -> str:
    try:
        from janus_time import now as _now
        return _now().isoformat()
    except Exception:
        return ""


def _norm_task(task: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", str(task).strip().lower()).strip("-") or "general"


def load() -> Dict[str, List[Dict[str, Any]]]:
    path = get_strengths_path()
    if not path.is_file():
        return {}
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
        return data if isinstance(data, dict) else {}
    except (ValueError, OSError):
        return {}


def save(data: Dict[str, List[Dict[str, Any]]]) -> None:
    path = get_strengths_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def record(task: str, model: str, *, note: str = "", source: str = "", score: Optional[float] = None) -> None:
    """Add or update a model's strength for ``task``. Higher score = stronger."""
    model = str(model).strip()
    if not model:
        return
    task = _norm_task(task)
    data = load()
    entries = data.setdefault(task, [])
    for e in entries:
        if e.get("model") == model:
            if note:
                e["note"] = note
            if source:
                e["source"] = source
            if score is not None:
                e["score"] = score
            e["updated_at"] = _now_iso()
            save(data)
            return
    entries.append({
        "model": model,
        "note": note,
        "source": source,
        "score": score if score is not None else 0.0,
        "updated_at": _now_iso(),
    })
    save(data)


def best_models_for(
    task: str, available: Optional[List[str]] = None, n: int = 4
) -> List[str]:
    """Return up to ``n`` model names ranked strongest-first for ``task``.

    If ``available`` is given, only models whose name appears in (or as a
    substring of) an available id are returned — so a KB entry like
    ``claude-opus-4.6`` still matches an available ``anthropic/claude-opus-4.6``.
    """
    entries = sorted(
        load().get(_norm_task(task), []),
        key=lambda e: e.get("score", 0.0),
        reverse=True,
    )
    names = [e["model"] for e in entries if e.get("model")]
    if available is not None:
        avail = list(available)
        names = [m for m in names if any(m in a or a in m for a in avail)]
    # de-dup preserving order
    seen, out = set(), []
    for m in names:
        if m not in seen:
            seen.add(m)
            out.append(m)
    return out[:n]


def known_tasks() -> List[str]:
    return sorted(load().keys())


# --- web-research seeding ---------------------------------------------------

_EXTRACT_SYSTEM = (
    "You read web search results about LLM quality and extract a ranked list of "
    "the best models for a specific task. Output only models that genuinely lead "
    "for that task. Prefer concrete model names (e.g. 'claude-opus-4.6', "
    "'gemini-3-pro', 'gpt-5.4', 'deepseek-v3.2')."
)


def _parse_ranked_models(raw: Optional[str]) -> List[Dict[str, Any]]:
    if not raw or not raw.strip():
        return []
    txt = raw.strip()
    if txt.startswith("```"):
        txt = re.sub(r"^```[a-zA-Z]*\n?", "", txt)
        txt = re.sub(r"\n?```$", "", txt).strip()
    m = re.search(r"\[.*\]", txt, re.DOTALL)
    if m:
        txt = m.group(0)
    try:
        data = json.loads(txt)
    except (ValueError, TypeError):
        return []
    if not isinstance(data, list):
        return []
    out = []
    for i, item in enumerate(data):
        if isinstance(item, str) and item.strip():
            out.append({"model": item.strip(), "note": "", "score": float(len(data) - i)})
        elif isinstance(item, dict) and str(item.get("model", "")).strip():
            out.append({
                "model": str(item["model"]).strip(),
                "note": str(item.get("note", "")).strip(),
                "score": float(item.get("score", len(data) - i)),
            })
    return out


def research(
    task: str, *,
    web_search_caller: Optional[Callable[[str], str]] = None,
    llm_caller: Optional[Callable[..., Any]] = None,
    provider: Optional[str] = None, model: Optional[str] = None,
    record_results: bool = True,
) -> Dict[str, Any]:
    """Web-research the best models for ``task`` and record them. Best-effort.

    Returns ``{"task", "ranked": [{model, note, score}], "error"}``. ``ranked``
    is empty on failure. Both callers are injectable for testing.
    """
    result: Dict[str, Any] = {"task": _norm_task(task), "ranked": [], "error": None}
    try:
        if web_search_caller is None:
            from tools.web_tools import web_search as _ws  # type: ignore

            def web_search_caller(q: str) -> str:
                return _ws(q)
        if llm_caller is None:
            from agent.auxiliary_client import call_llm as llm_caller

        query = f"best LLM model for {task} tasks benchmark comparison"
        evidence = str(web_search_caller(query))[:8000]
        prompt = (
            f"Task category: {task}\n\nWeb search findings:\n{evidence}\n\n"
            "From these findings, return a JSON array of the best models for this "
            'task, strongest first, e.g. [{"model":"claude-opus-4.6","note":"why"}]. '
            "Return ONLY the JSON array."
        )
        response = llm_caller(
            task="model_strength_research",
            provider=provider, model=model,
            messages=[
                {"role": "system", "content": _EXTRACT_SYSTEM},
                {"role": "user", "content": prompt},
            ],
            temperature=0, max_tokens=600,
        )
        ranked = _parse_ranked_models(response.choices[0].message.content)
        result["ranked"] = ranked
        if record_results:
            for r in ranked:
                record(task, r["model"], note=r.get("note", ""),
                       source="web-research", score=r.get("score"))
    except Exception as exc:
        logger.debug("model-strength research failed: %s", exc)
        result["error"] = str(exc)
    return result
