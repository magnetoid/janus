"""Proactive aspirations — long-horizon goals Janus holds across sessions.

Distinct from the session ``/goal`` Ralph loop (a short-term "grind until this
task is done" mechanism). An *aspiration* is a north-star the user is working
toward over weeks: Janus stores it, drafts a milestone roadmap, and a recurring
cron check-in proactively asks "is this still your goal?" and suggests the next
step.

This module owns the durable store + roadmap drafting + check-in formatting.
The CLI (`janus aspire`) and a self-scheduled cron job drive it. Pure helpers
with an injectable ``llm_caller`` so they're testable without a model.
"""
from __future__ import annotations

import json
import logging
import re
from pathlib import Path
from typing import Any, Callable, Dict, List, Optional

logger = logging.getLogger(__name__)

CHECKIN_JOB_NAME = "aspiration-checkin"
CHECKIN_SCRIPT_NAME = "aspire_checkin.py"


def get_aspirations_path() -> Path:
    from janus_constants import get_janus_home
    return get_janus_home() / "aspirations.json"


def _now_iso() -> str:
    try:
        from janus_time import now as _now
        return _now().isoformat()
    except Exception:
        return ""


def _new_id(title: str, existing_ids: set) -> str:
    base = re.sub(r"[^a-z0-9]+", "-", title.strip().lower()).strip("-")[:24] or "goal"
    cand = base
    n = 2
    while cand in existing_ids:
        cand = f"{base}-{n}"
        n += 1
    return cand


def load() -> List[Dict[str, Any]]:
    path = get_aspirations_path()
    if not path.is_file():
        return []
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
        return data if isinstance(data, list) else []
    except (ValueError, OSError):
        return []


def save(aspirations: List[Dict[str, Any]]) -> None:
    path = get_aspirations_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(aspirations, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def add(title: str, roadmap: Optional[List[str]] = None) -> Dict[str, Any]:
    """Add an aspiration and persist it. Returns the new record."""
    title = title.strip()
    items = load()
    rec = {
        "id": _new_id(title, {a.get("id") for a in items}),
        "title": title,
        "roadmap": [str(m).strip() for m in (roadmap or []) if str(m).strip()],
        "status": "active",
        "created_at": _now_iso(),
        "last_checkin_at": "",
    }
    items.append(rec)
    save(items)
    return rec


def get(aspiration_id: str) -> Optional[Dict[str, Any]]:
    for a in load():
        if a.get("id") == aspiration_id:
            return a
    return None


def list_active() -> List[Dict[str, Any]]:
    return [a for a in load() if a.get("status") == "active"]


def set_status(aspiration_id: str, status: str) -> bool:
    items = load()
    hit = False
    for a in items:
        if a.get("id") == aspiration_id:
            a["status"] = status
            hit = True
    if hit:
        save(items)
    return hit


def remove(aspiration_id: str) -> bool:
    items = load()
    kept = [a for a in items if a.get("id") != aspiration_id]
    if len(kept) == len(items):
        return False
    save(kept)
    return True


def mark_checked_in(ids: Optional[List[str]] = None) -> None:
    items = load()
    stamp = _now_iso()
    for a in items:
        if ids is None or a.get("id") in ids:
            a["last_checkin_at"] = stamp
    save(items)


# --- roadmap drafting -------------------------------------------------------

_ROADMAP_SYSTEM = (
    "You are a planning partner. Given a user's long-term goal, produce a short, "
    "concrete milestone roadmap — the ordered steps that move from today to the "
    "goal. Be specific and realistic, not generic."
)


def _parse_roadmap(raw: Optional[str]) -> List[str]:
    if not raw or not raw.strip():
        return []
    txt = raw.strip()
    if txt.startswith("```"):
        txt = re.sub(r"^```[a-zA-Z]*\n?", "", txt)
        txt = re.sub(r"\n?```$", "", txt).strip()
    # Try a JSON array first.
    m = re.search(r"\[.*\]", txt, re.DOTALL)
    if m:
        try:
            data = json.loads(m.group(0))
            if isinstance(data, list):
                return [str(x).strip() for x in data if str(x).strip()][:8]
        except (ValueError, TypeError):
            pass
    # Fall back to numbered/bulleted lines.
    out: List[str] = []
    for line in txt.splitlines():
        s = re.sub(r"^\s*(?:\d+[.)]|[-*•])\s*", "", line).strip()
        if s:
            out.append(s)
    return out[:8]


def draft_roadmap(
    title: str, *, llm_caller: Optional[Callable[..., Any]] = None,
    provider: Optional[str] = None, model: Optional[str] = None,
) -> List[str]:
    """Draft a milestone roadmap for ``title``. Best-effort; [] on failure."""
    try:
        if llm_caller is None:
            from agent.auxiliary_client import call_llm as llm_caller
        prompt = (
            f"My long-term goal: {title}\n\n"
            "Give me an ordered roadmap of 3-6 concrete milestones to get there. "
            'Return a JSON array of short strings, e.g. ["milestone 1", "milestone 2"]. '
            "Return ONLY the JSON array."
        )
        response = llm_caller(
            task="aspiration_roadmap",
            provider=provider, model=model,
            messages=[
                {"role": "system", "content": _ROADMAP_SYSTEM},
                {"role": "user", "content": prompt},
            ],
            temperature=0.3, max_tokens=500,
        )
        return _parse_roadmap(response.choices[0].message.content)
    except Exception as exc:
        logger.debug("roadmap drafting failed: %s", exc)
        return []


# --- check-in ---------------------------------------------------------------

def format_checkin_context(aspirations: Optional[List[Dict[str, Any]]] = None) -> str:
    """Markdown summary of active aspirations + roadmaps, for a check-in prompt."""
    items = aspirations if aspirations is not None else list_active()
    if not items:
        return ""
    lines = ["The user is working toward these standing aspirations:\n"]
    for a in items:
        lines.append(f"### {a.get('title', '(untitled)')}  [id: {a.get('id')}]")
        roadmap = a.get("roadmap") or []
        if roadmap:
            lines.append("Roadmap:")
            for i, m in enumerate(roadmap, 1):
                lines.append(f"  {i}. {m}")
        if a.get("last_checkin_at"):
            lines.append(f"_(last checked in: {a['last_checkin_at']})_")
        lines.append("")
    return "\n".join(lines)


CHECKIN_PROMPT = (
    "Proactively check in with the user on their standing aspiration(s) above. "
    "For each: briefly reflect likely progress, ask whether it's still their goal, "
    "and suggest ONE concrete next step on the roadmap. Be warm and brief — this "
    "is an unprompted nudge, not a report."
)


def checkin_script_source() -> str:
    """Self-contained script the cron check-in runs; prints active aspirations."""
    return (
        "import json, os\n"
        "from pathlib import Path\n"
        "home = Path(os.environ.get('JANUS_HOME') or (Path.home() / '.janus'))\n"
        "p = home / 'aspirations.json'\n"
        "data = json.loads(p.read_text(encoding='utf-8')) if p.is_file() else []\n"
        "active = [a for a in data if a.get('status') == 'active']\n"
        "if not active:\n"
        "    print('No active aspirations.')\n"
        "else:\n"
        "    for a in active:\n"
        "        print(f\"ASPIRATION [{a.get('id')}]: {a.get('title','')}\")\n"
        "        for i, m in enumerate(a.get('roadmap') or [], 1):\n"
        "            print(f'  {i}. {m}')\n"
        "        print()\n"
    )
