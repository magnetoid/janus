"""Sleep — an offline memory-consolidation engine (the flagship).

Inspired by biological sleep and the 2026 "sleep-time compute" line of work:
while the agent is idle, a background cycle consolidates what it learned across
recent sessions, instead of carrying everything forward append-only. One cycle:

  1. REPLAY recent sessions + the daily journal.
  2. GRADUATE (multi-layer memory): distill recent sessions into semantic facts
     (memory_miner) and reusable procedures (skill_miner drafts) — the episodic
     journal -> semantic MEMORY.md -> procedural skills promotion the layers
     lacked.
  3. RECONCILE contradictions (memory_gardener).
  4. IMPORTANCE-TAG + FORGET: score entries by recency/reuse/substance and prune
     the lowest-salience ones (above a kept-floor) — logged to the journal, so
     history is never lost. This is the genuinely new bit; the gardener only
     handled contradictions and the curator only archived skills.
  5. SYNTHESIZE cross-session lessons spanning many sessions (not one).

Pure + injectable ``llm_caller`` so the cycle is testable without a model;
best-effort everywhere (a failure never breaks anything). It orchestrates the
existing learning modules — it does not reimplement them.
"""
from __future__ import annotations

import json
import logging
from pathlib import Path
from typing import Any, Callable, Dict, List, Optional

logger = logging.getLogger(__name__)

_IMPORTANCE_TARGET_LEN = 120  # chars; entries up to this score full on substance


# --- state ------------------------------------------------------------------

def get_sleep_state_path() -> Path:
    from janus_constants import get_janus_home
    return get_janus_home() / "learning" / "sleep_state.json"


def _now_iso() -> str:
    try:
        from janus_time import now as _now
        return _now().isoformat()
    except Exception:
        return ""


def load_sleep_state() -> Dict[str, Any]:
    path = get_sleep_state_path()
    if not path.is_file():
        return {}
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
        return data if isinstance(data, dict) else {}
    except (ValueError, OSError):
        return {}


def save_sleep_state(data: Dict[str, Any]) -> None:
    path = get_sleep_state_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


# --- importance scoring -----------------------------------------------------

def _length_norm(text: str) -> float:
    return min(len(text) / _IMPORTANCE_TARGET_LEN, 1.0)


def importance_score(decay: float, reuse: float, length_norm: float) -> float:
    """Salience in [0,1]: recent (low decay) + reused + substantive scores high."""
    decay = max(0.0, min(1.0, decay))
    reuse = max(0.0, min(1.0, reuse))
    length_norm = max(0.0, min(1.0, length_norm))
    return round((1.0 - decay) * 0.5 + reuse * 0.3 + length_norm * 0.2, 4)


def score_memory_importance(
    entries: List[str], *, decays: Optional[Dict[str, float]] = None,
    reuses: Optional[Dict[str, float]] = None,
) -> Dict[str, float]:
    """Importance per entry. ``decays``/``reuses`` (0..1) are optional signals;
    absent ones default to 0 (treated as recent / unreused)."""
    decays = decays or {}
    reuses = reuses or {}
    return {
        e: importance_score(decays.get(e, 0.0), reuses.get(e, 0.0), _length_norm(e))
        for e in entries
    }


def prune_low_salience(
    store: Any, *, threshold: float = 0.3, keep_min: int = 10,
    scores: Optional[Dict[str, float]] = None, apply: bool = True, target: str = "memory",
) -> List[str]:
    """Drop the lowest-salience entries below ``threshold``, never below the
    ``keep_min`` floor. Pruned entries are logged to the daily journal (history
    preserved). Returns the entries dropped (or that would be dropped)."""
    attr = "user_entries" if target == "user" else "memory_entries"
    entries = list(getattr(store, attr, []))
    if len(entries) <= keep_min:
        return []
    sc = scores if scores is not None else score_memory_importance(entries)
    below = sorted([e for e in entries if sc.get(e, 0.0) < threshold], key=lambda e: sc.get(e, 0.0))
    max_drop = len(entries) - keep_min
    to_drop = below[:max_drop]
    if apply:
        from tools.memory_tool import append_daily_snapshot
        for e in to_drop:
            try:
                store.remove(target, e)
                append_daily_snapshot(target, f"[sleep: pruned low-salience] {e}", "remove")
            except Exception as exc:
                logger.debug("prune remove failed: %s", exc)
    return to_drop


# --- LLM-backed steps -------------------------------------------------------

_SYNTH_SYSTEM = (
    "You distill HIGHER-LEVEL lessons that span MULTIPLE work sessions — patterns, "
    "recurring preferences, durable conventions — that no single session makes "
    "obvious. Be terse and only output genuinely cross-session insights."
)


def synthesize_cross_session_lessons(
    sessions_text: List[str], *, llm_caller: Optional[Callable[..., Any]] = None,
    provider: Optional[str] = None, model: Optional[str] = None, max_lessons: int = 5,
) -> List[str]:
    """Distill lessons spanning many sessions. Best-effort; [] on failure."""
    try:
        joined = "\n\n---\n\n".join(s for s in sessions_text if s.strip())
        if not joined.strip():
            return []
        if llm_caller is None:
            from agent.auxiliary_client import call_llm as llm_caller
        prompt = (
            "Across these recent session summaries, return a JSON array of "
            "higher-level lessons that span MULTIPLE sessions (not one). Each a "
            "concise sentence. If none, return []. Return ONLY the JSON array."
            f"\n\nSESSIONS:\n{joined[:12000]}"
        )
        response = llm_caller(
            task="sleep_synthesis", provider=provider, model=model,
            messages=[{"role": "system", "content": _SYNTH_SYSTEM},
                      {"role": "user", "content": prompt}],
            temperature=0.2, max_tokens=500,
        )
        import re
        raw = response.choices[0].message.content or ""
        m = re.search(r"\[.*\]", raw, re.DOTALL)
        if not m:
            return []
        data = json.loads(m.group(0))
        if not isinstance(data, list):
            return []
        return [str(x).strip() for x in data if str(x).strip()][:max_lessons]
    except Exception as exc:
        logger.debug("cross-session synthesis failed: %s", exc)
        return []


# --- the cycle --------------------------------------------------------------

def run_sleep_cycle(
    store: Any, *, llm_caller: Optional[Callable[..., Any]] = None,
    dry_run: bool = False, sessions: Optional[List[List[Dict[str, Any]]]] = None,
    session_summaries: Optional[List[str]] = None,
    prune_threshold: float = 0.3, keep_min: int = 10, prune_scores: Optional[Dict[str, float]] = None,
    provider: Optional[str] = None, model: Optional[str] = None,
) -> Dict[str, Any]:
    """Run one consolidation cycle over ``store``. Returns a report. Never raises.

    ``dry_run`` reports what *would* happen (reconcile/prune in report-only mode)
    and skips additive graduation/synthesis. ``sessions`` (list of message lists)
    and ``session_summaries`` can be injected for tests; otherwise nothing is
    graduated (callers pass recent sessions).
    """
    report: Dict[str, Any] = {
        "dry_run": dry_run, "graduated_facts": 0, "graduated_skills": 0,
        "reconciled": [], "pruned": [], "lessons": [], "error": None,
    }
    try:
        # 2. GRADUATE — distill recent sessions into facts + skill drafts.
        if not dry_run and sessions:
            from agent.memory_miner import mine_session_memory
            from agent.skill_miner import mine_session_skills
            for msgs in sessions:
                try:
                    mm = mine_session_memory(msgs, store, llm_caller=llm_caller, provider=provider, model=model)
                    a = mm.get("added", {})
                    report["graduated_facts"] += a.get("memory", 0) + a.get("user", 0)
                except Exception as exc:
                    logger.debug("sleep graduate-memory failed: %s", exc)
                try:
                    ms = mine_session_skills(msgs, llm_caller=llm_caller, provider=provider, model=model)
                    report["graduated_skills"] += len(ms.get("written", []))
                except Exception as exc:
                    logger.debug("sleep graduate-skills failed: %s", exc)

        # 3. RECONCILE contradictions.
        try:
            from agent.memory_gardener import reconcile
            rec = reconcile(store, llm_caller=llm_caller, apply=not dry_run, provider=provider, model=model)
            report["reconciled"] = rec.get("removed", [])
        except Exception as exc:
            logger.debug("sleep reconcile failed: %s", exc)

        # 4. IMPORTANCE-TAG + FORGET.
        report["pruned"] = prune_low_salience(
            store, threshold=prune_threshold, keep_min=keep_min,
            scores=prune_scores, apply=not dry_run)

        # 5. SYNTHESIZE cross-session lessons.
        if not dry_run and session_summaries:
            lessons = synthesize_cross_session_lessons(
                session_summaries, llm_caller=llm_caller, provider=provider, model=model)
            report["lessons"] = lessons
            for lesson in lessons:
                try:
                    store.add("memory", lesson)
                except Exception:
                    pass

        # 6. ACE PLAYBOOK: improve the learning loop's OWN prompts. From this
        # cycle's activity, propose guidance, red-team it (fails closed), and
        # merge into the capped playbook. Off by default (learning.playbook).
        if not dry_run and session_summaries:
            try:
                from agent.playbook import enabled as _pb_enabled, run_curation
                if _pb_enabled():
                    report["playbook"] = run_curation(
                        "\n".join(str(s) for s in session_summaries), llm_caller=llm_caller)
            except Exception as exc:
                logger.debug("sleep playbook curation failed: %s", exc)

        if not dry_run:
            state = load_sleep_state()
            state["last_run"] = _now_iso()
            state["last_report"] = {k: (len(v) if isinstance(v, list) else v)
                                    for k, v in report.items() if k != "error"}
            save_sleep_state(state)
    except Exception as exc:  # a consolidation failure must never break anything
        logger.debug("sleep cycle failed: %s", exc)
        report["error"] = str(exc)
    return report


# --- scheduling -------------------------------------------------------------

def _config(section: str, key: str, default: Any) -> Any:
    try:
        import yaml
        from janus_constants import get_janus_home
        cfg_path = get_janus_home() / "config.yaml"
        if cfg_path.is_file():
            cfg = yaml.safe_load(cfg_path.read_text(encoding="utf-8")) or {}
            sec = cfg.get(section, {})
            if isinstance(sec, dict) and key in sec:
                return sec[key]
    except Exception:
        pass
    return default


def _parse_iso(s: str) -> Optional[float]:
    try:
        from datetime import datetime
        return datetime.fromisoformat(s).timestamp()
    except Exception:
        return None


def should_run_sleep(now_ts: float, state: Dict[str, Any], interval_hours: float) -> bool:
    """True if at least ``interval_hours`` have passed since the last run."""
    last = state.get("last_run")
    if not last:
        return True
    last_ts = _parse_iso(last)
    if last_ts is None:
        return True
    return (now_ts - last_ts) >= interval_hours * 3600


def maybe_run_sleep(
    idle_for_seconds: Optional[float] = None, *, now_ts: Optional[float] = None,
    store: Any = None,
) -> Optional[Dict[str, Any]]:
    """Run a sleep cycle iff enabled, not paused, idle long enough, and due.
    Returns the report if it ran, else None. Best-effort."""
    try:
        if not bool(_config("sleep", "enabled", True)):
            return None
        state = load_sleep_state()
        if state.get("paused"):
            return None
        min_idle_hours = float(_config("sleep", "min_idle_hours", 2.0))
        if idle_for_seconds is not None and idle_for_seconds < min_idle_hours * 3600:
            return None
        if now_ts is None:
            import time
            now_ts = time.time()
        interval_hours = float(_config("sleep", "interval_hours", 168))
        if not should_run_sleep(now_ts, state, interval_hours):
            return None
        if store is None:
            from tools.memory_tool import MemoryStore
            store = MemoryStore()
            store.load_from_disk()
        return run_sleep_cycle(
            store,
            prune_threshold=float(_config("sleep", "importance_threshold", 0.3)),
            keep_min=int(_config("sleep", "keep_min_entries", 10)),
        )
    except Exception as exc:
        logger.debug("maybe_run_sleep failed: %s", exc)
        return None
