"""Interest-driven self-learning — Janus keeps up with the user's field.

The capstone of the proactive/self-learning stack. Janus tracks the user's
domains of interest (e.g. "graphic design", "rust", "biotech"), and a recurring
cron job periodically researches the latest trends/news/tech in each field,
then **proposes** what it found and asks permission — *"I noticed a trend in X;
want me to learn more?"* — before deep-diving and absorbing anything into
memory/skills. Consent-gated: it never pollutes its own knowledge unilaterally.

Composes the rest of the stack: web search + MoA for research, model-strengths
for routing, cron for the cadence, and memory/skill mining to absorb on a yes.

Pure helpers with injectable ``web_search_caller`` / ``llm_caller`` for tests.
"""
from __future__ import annotations

import json
import logging
import re
from pathlib import Path
from typing import Any, Callable, Dict, List, Optional

logger = logging.getLogger(__name__)

DISCOVERY_JOB_NAME = "interest-discovery"
DISCOVERY_SCRIPT_NAME = "interest_discover.py"


def get_interests_path() -> Path:
    from janus_constants import get_janus_home
    return get_janus_home() / "interests.json"


def _now_iso() -> str:
    try:
        from janus_time import now as _now
        return _now().isoformat()
    except Exception:
        return ""


def _new_id(field: str, existing: set) -> str:
    base = re.sub(r"[^a-z0-9]+", "-", field.strip().lower()).strip("-")[:24] or "interest"
    cand, n = base, 2
    while cand in existing:
        cand, n = f"{base}-{n}", n + 1
    return cand


def load() -> List[Dict[str, Any]]:
    path = get_interests_path()
    if not path.is_file():
        return []
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
        return data if isinstance(data, list) else []
    except (ValueError, OSError):
        return []


def save(items: List[Dict[str, Any]]) -> None:
    path = get_interests_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(items, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def add(field: str, *, note: str = "", source: str = "user") -> Dict[str, Any]:
    field = field.strip()
    items = load()
    for a in items:  # don't duplicate the same field
        if a.get("field", "").lower() == field.lower():
            return a
    rec = {
        "id": _new_id(field, {a.get("id") for a in items}),
        "field": field,
        "note": note,
        "source": source,
        "status": "active",
        "added_at": _now_iso(),
        "last_researched_at": "",
    }
    items.append(rec)
    save(items)
    return rec


def get(interest_id: str) -> Optional[Dict[str, Any]]:
    for a in load():
        if a.get("id") == interest_id:
            return a
    return None


def list_active() -> List[Dict[str, Any]]:
    return [a for a in load() if a.get("status") == "active"]


def remove(interest_id: str) -> bool:
    items = load()
    kept = [a for a in items if a.get("id") != interest_id]
    if len(kept) == len(items):
        return False
    save(kept)
    return True


def mark_researched(interest_id: str) -> None:
    items = load()
    stamp = _now_iso()
    for a in items:
        if a.get("id") == interest_id:
            a["last_researched_at"] = stamp
    save(items)


# --- research ---------------------------------------------------------------

_RESEARCH_SYSTEM = (
    "You scan web search findings for a field and surface the NOTABLE recent "
    "trends, news, tools, or techniques worth a practitioner's attention. Be "
    "specific and current; skip evergreen basics and marketing fluff."
)


def _parse_findings(raw: Optional[str]) -> List[Dict[str, str]]:
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
    for item in data:
        if isinstance(item, str) and item.strip():
            out.append({"trend": item.strip(), "why": ""})
        elif isinstance(item, dict) and str(item.get("trend", "")).strip():
            out.append({
                "trend": str(item["trend"]).strip(),
                "why": str(item.get("why", "")).strip(),
            })
    return out[:6]


def research_interest(
    field: str, *,
    web_search_caller: Optional[Callable[[str], str]] = None,
    llm_caller: Optional[Callable[..., Any]] = None,
    provider: Optional[str] = None, model: Optional[str] = None,
) -> Dict[str, Any]:
    """Research the latest in ``field``. Returns {field, findings, error}. Best-effort."""
    result: Dict[str, Any] = {"field": field, "findings": [], "error": None}
    try:
        if web_search_caller is None:
            from tools.web_tools import web_search as _ws  # type: ignore

            def web_search_caller(q: str) -> str:
                return _ws(q)
        if llm_caller is None:
            from agent.auxiliary_client import call_llm as llm_caller

        evidence = str(web_search_caller(f"latest {field} trends news tools 2026"))[:8000]
        prompt = (
            f"Field: {field}\n\nRecent web findings:\n{evidence}\n\n"
            "Return a JSON array of the most notable recent trends/news/tools, "
            'e.g. [{"trend":"short title","why":"why it matters"}]. '
            "Return ONLY the JSON array."
        )
        response = llm_caller(
            task="interest_research",
            provider=provider, model=model,
            messages=[
                {"role": "system", "content": _RESEARCH_SYSTEM},
                {"role": "user", "content": prompt},
            ],
            temperature=0.2, max_tokens=700,
        )
        result["findings"] = _parse_findings(response.choices[0].message.content)
    except Exception as exc:
        logger.debug("interest research failed for %s: %s", field, exc)
        result["error"] = str(exc)
    return result


def format_discovery(field: str, findings: List[Dict[str, str]]) -> str:
    """The consent-gated proposal Janus surfaces to the user."""
    if not findings:
        return ""
    lines = [f"I've been keeping an eye on **{field}** and a few things stand out:\n"]
    for f in findings:
        why = f" — {f['why']}" if f.get("why") else ""
        lines.append(f"- **{f['trend']}**{why}")
    lines.append(
        "\nWant me to dig deeper into any of these and fold what I learn into my "
        "memory/skills? (Tell me which — or 'no thanks'.)"
    )
    return "\n".join(lines)


DISCOVERY_PROMPT = (
    "For each of the user's standing interests above, briefly research the LATEST "
    "trends/news/tools (use web_search; use the mixture_of_agents tool for a "
    "deeper synthesis if the topic is complex). Then tell the user what you found "
    "and ASK whether they'd like you to learn more about any of it. Do NOT absorb "
    "anything into memory or create skills yet — get their agreement first. Keep "
    "it warm and brief; this is an unprompted nudge, not a report."
)


def discovery_script_source() -> str:
    """Self-contained script the discovery cron runs; prints active interests."""
    return (
        "import json, os\n"
        "from pathlib import Path\n"
        "home = Path(os.environ.get('JANUS_HOME') or (Path.home() / '.janus'))\n"
        "p = home / 'interests.json'\n"
        "data = json.loads(p.read_text(encoding='utf-8')) if p.is_file() else []\n"
        "active = [a for a in data if a.get('status') == 'active']\n"
        "if not active:\n"
        "    print('No active interests.')\n"
        "else:\n"
        "    print('User interests to research the latest in:')\n"
        "    for a in active:\n"
        "        note = f\" — {a['note']}\" if a.get('note') else ''\n"
        "        print(f\"- {a.get('field','')}{note}\")\n"
    )
