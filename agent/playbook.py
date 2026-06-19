"""ACE-style evolving playbook over the learning loop's OWN prompts.

The loop's model-driven steps (memory mining, lesson distillation, skill mining,
outcome classification) run on FIXED developer prompts. This adds a small,
curated PLAYBOOK of learned guidance that is prepended to those prompts — so the
loop gets better at *learning* over time. This is the one place Janus improves
its own learning machinery rather than just accumulating facts/skills.

It is an ACE loop (Agentic Context Engineering): guidance is distilled from the
loop's own recent activity (Generator → ``propose``), admitted only through the
dialectic red-team gate (Reflector, inside ``curate``), and merged with dedupe +
score-based pruning (Curator) — never collapsed into a lossy summary (ACE's
anti-brevity rule keeps each bullet discrete).

Safety gates (this modifies the loop's own prompts, so it's deliberately
conservative): default-off; admission FAILS CLOSED — no entry is added without a
passing red-team verdict; the playbook is CAPPED so it can't grow unbounded or
bloat the prompt. Pure + best-effort; never raises.
"""
from __future__ import annotations

import json
import logging
import re
from pathlib import Path
from typing import Any, Callable, Dict, List, Optional

logger = logging.getLogger(__name__)

SCOPES = ("general", "memory", "skills", "lessons", "outcomes")
_DEFAULT_MAX = 40


def get_playbook_path() -> Path:
    from janus_constants import get_janus_home
    return get_janus_home() / "learning" / "playbook.json"


def _now_iso() -> str:
    try:
        from janus_time import now as _now
        return _now().isoformat()
    except Exception:
        return ""


def load() -> List[Dict[str, Any]]:
    p = get_playbook_path()
    if not p.is_file():
        return []
    try:
        data = json.loads(p.read_text(encoding="utf-8"))
        return data if isinstance(data, list) else []
    except (ValueError, OSError):
        return []


def _save(entries: List[Dict[str, Any]]) -> None:
    p = get_playbook_path()
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(entries, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def _norm(s: Any) -> str:
    return " ".join(str(s).lower().split())


def enabled(config: Optional[Dict[str, Any]] = None) -> bool:
    """True when the learning-loop playbook is switched on (default off)."""
    try:
        if config is None:
            from janus_cli.config import load_config
            config = load_config()
        lp = (config.get("learning", {}) or {}).get("playbook", {}) if isinstance(config, dict) else {}
        return bool(isinstance(lp, dict) and lp.get("enabled"))
    except Exception:
        return False


def add_entry(scope: str, guidance: str, *, source: str = "", score: float = 0.7) -> Optional[Dict[str, Any]]:
    """Add one guidance bullet (deduped, case-insensitive). Returns it or None."""
    guidance = str(guidance).strip()
    if not guidance or scope not in SCOPES:
        return None
    entries = load()
    norm = _norm(guidance)
    if any(_norm(e.get("guidance", "")) == norm for e in entries):
        return None
    entry = {
        "id": f"pb-{len(entries) + 1}-{abs(hash(norm)) % 100000}",
        "scope": scope, "guidance": guidance, "source": source,
        "score": float(score), "uses": 0, "created_at": _now_iso(),
    }
    entries.append(entry)
    _save(entries)
    return entry


def for_scope(scope: str, *, max_bullets: int = 8) -> str:
    """Render the playbook guidance for ``scope`` (+ ``general``) as a prompt block.

    Highest-scored first, capped at ``max_bullets``. Empty string when none — so
    callers can inject it unconditionally. This is the READ path the learning
    loop prepends to its step prompts.
    """
    try:
        entries = [e for e in load() if e.get("scope") in ("general", scope)]
        if not entries:
            return ""
        entries.sort(key=lambda e: e.get("score", 0), reverse=True)
        bullets = [f"- {str(e.get('guidance', '')).strip()}" for e in entries[:max_bullets]]
        return "Learned guidance for this step (apply where relevant):\n" + "\n".join(bullets)
    except Exception as exc:
        logger.debug("for_scope failed: %s", exc)
        return ""


def augment_system(base_prompt: str, scope: str) -> str:
    """Prepend the scope's playbook guidance to a learning-loop system prompt.

    The single integration point the loop's steps call. No-op (returns the base
    prompt unchanged) when the playbook is disabled or empty — so a step can
    wrap its system prompt unconditionally. Best-effort.
    """
    try:
        if not enabled():
            return base_prompt
        block = for_scope(scope)
        return f"{base_prompt}\n\n{block}" if block else base_prompt
    except Exception as exc:
        logger.debug("augment_system failed: %s", exc)
        return base_prompt


def run_curation(context_text: str, *, llm_caller: Optional[Callable[..., Any]] = None,
                 max_entries: int = _DEFAULT_MAX) -> Dict[str, Any]:
    """Generator → Curator in one call: propose from activity, then admit/merge.

    The entry point the sleep cycle calls. Best-effort.
    """
    proposals = propose(context_text, llm_caller=llm_caller)
    return curate(proposals, transcript=str(context_text)[:4000],
                  llm_caller=llm_caller, max_entries=max_entries)


def prune(max_entries: int = _DEFAULT_MAX) -> List[Dict[str, Any]]:
    """Cap the playbook: keep the highest-scored ``max_entries``, evict the rest."""
    entries = load()
    if len(entries) <= max_entries:
        return []
    entries.sort(key=lambda e: (e.get("score", 0), e.get("uses", 0)), reverse=True)
    kept, evicted = entries[:max_entries], entries[max_entries:]
    _save(kept)
    return evicted


# --- Generator -------------------------------------------------------------

_PROPOSE_SYSTEM = (
    "You improve an AI agent's LEARNING LOOP. From its recent activity, propose "
    "a few SHORT, concrete pieces of guidance the loop should follow when it "
    "mines durable memory, distills lessons from failures, mines reusable "
    "skills, or classifies session outcomes. Each must be specific and reusable "
    "— not a generic platitude."
)


def _build_propose_prompt(context_text: str) -> str:
    return (
        "From the recent learning-loop activity below, propose guidance as a JSON "
        'array. Each item: {"scope": one of ' + "|".join(SCOPES) + ', "guidance": '
        "one concrete sentence}. Only genuinely useful, reusable guidance; skip "
        "platitudes. If nothing qualifies, return []. Return ONLY the JSON array."
        f"\n\nRECENT ACTIVITY:\n{context_text}"
    )


def propose(
    context_text: str, *, llm_caller: Optional[Callable[..., Any]] = None,
    provider: Optional[str] = None, model: Optional[str] = None, max_items: int = 6,
) -> List[Dict[str, str]]:
    """Generator: propose scoped guidance from recent loop activity. Best-effort."""
    try:
        if not str(context_text).strip():
            return []
        if llm_caller is None:
            from agent.auxiliary_client import call_llm as llm_caller
        resp = llm_caller(
            task="playbook_propose", provider=provider, model=model,
            messages=[{"role": "system", "content": _PROPOSE_SYSTEM},
                      {"role": "user", "content": _build_propose_prompt(context_text)}],
            temperature=0, max_tokens=600,
        )
        raw = resp.choices[0].message.content or ""
        m = re.search(r"\[.*\]", raw, re.DOTALL)
        if not m:
            return []
        data = json.loads(m.group(0))
        out: List[Dict[str, str]] = []
        for item in (data if isinstance(data, list) else []):
            if not isinstance(item, dict):
                continue
            scope = str(item.get("scope", "general")).strip().lower()
            guidance = str(item.get("guidance", "")).strip()
            if guidance and scope in SCOPES:
                out.append({"scope": scope, "guidance": guidance})
        return out[:max_items]
    except Exception as exc:
        logger.debug("playbook propose failed: %s", exc)
        return []


# --- Curator (Reflector = dialectic red-team) ------------------------------


def curate(
    proposals: List[Dict[str, str]], *, transcript: str = "",
    llm_caller: Optional[Callable[..., Any]] = None, max_entries: int = _DEFAULT_MAX,
) -> Dict[str, Any]:
    """Admit proposals through the red-team gate, then merge + prune.

    Returns ``{added, revised, rejected: [...], error}``. FAILS CLOSED: if the
    reflector can't run (infrastructure error), nothing is admitted. Never raises.
    """
    result: Dict[str, Any] = {"added": 0, "revised": 0, "rejected": [], "error": None}
    try:
        if not proposals:
            return result
        from agent.deliberation import red_team_claims
        claims = [
            {"id": f"pb-{i}", "kind": "playbook",
             "content": f"[{p.get('scope', 'general')}] {p.get('guidance', '')}",
             "context": "learning-loop guidance"}
            for i, p in enumerate(proposals)
        ]
        rt = red_team_claims(claims, transcript=transcript, llm_caller=llm_caller)
        if rt.get("error") is not None:
            result["error"] = rt["error"]
            return result  # fail closed — admit nothing the reflector couldn't vet
        verdicts = rt.get("verdicts", {})
        for i, p in enumerate(proposals):
            v = verdicts.get(f"pb-{i}")
            if not v:
                continue
            scope = p.get("scope", "general")
            guidance = p.get("guidance", "")
            verdict = v.get("verdict")
            if verdict == "reject":
                result["rejected"].append(
                    {"guidance": guidance, "objection": v.get("skeptic_objection", "")})
            elif verdict == "revise" and v.get("revised_content"):
                revised = re.sub(r"^\s*\[[^\]]*\]\s*", "", str(v["revised_content"])).strip()
                if add_entry(scope, revised, source="ace-revised", score=0.7):
                    result["added"] += 1
                    result["revised"] += 1
            elif verdict == "accept":
                if add_entry(scope, guidance, source="ace", score=0.8):
                    result["added"] += 1
        prune(max_entries)
    except Exception as exc:
        logger.debug("playbook curate failed: %s", exc)
        result["error"] = str(exc)
    return result


def stats() -> Dict[str, Any]:
    entries = load()
    by_scope: Dict[str, int] = {}
    for e in entries:
        s = str(e.get("scope", "general"))
        by_scope[s] = by_scope.get(s, 0) + 1
    return {"total": len(entries), "by_scope": by_scope}
