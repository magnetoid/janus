"""Auto-fire session-end mining (memory + procedures) — opt-in, best-effort.

When a session ends (e.g. ``/new``), if the user has opted in via config
(``memory.session_mining`` / ``skills.session_mining``), distill the just-ended
transcript into memory facts and/or draft skills — in a background thread so it
never blocks the UI, swallowing all errors.

OFF by default: flip the flags on only after eyeballing a manual
``janus memory mine`` / ``janus skills mine`` run, so quality is checked before
it runs unattended. A short session is skipped (nothing worth mining).
"""
from __future__ import annotations

import logging
import threading
from typing import Any, Dict, List, Optional

logger = logging.getLogger(__name__)

_MIN_MESSAGES = 6  # don't mine trivial sessions


def _flag(section: str, key: str, *, default: bool = False) -> bool:
    from agent.feature_flags import flag_enabled
    return flag_enabled(section, key, default=default)


def maybe_automine(
    messages: List[Dict[str, Any]], *, run_in_thread: bool = True,
    active_persona: Optional[str] = None,
) -> Optional[threading.Thread]:
    """Mine the just-ended session for memory/skills if opted in.

    Returns the worker thread (or None if nothing was scheduled). Fully
    best-effort — never raises, never blocks meaningful work.
    """
    try:
        if not messages or len(messages) < _MIN_MESSAGES:
            return None
        mine_memory = _flag("memory", "session_mining")
        mine_skills = _flag("skills", "session_mining")
        track_outcomes = _flag("learning", "track_outcomes")
        if not (mine_memory or mine_skills or track_outcomes):
            return None
        snapshot = list(messages)
        session_id = next(
            (str(m["session_id"]) for m in reversed(snapshot) if m.get("session_id")), ""
        )

        def _work():
            if track_outcomes:
                try:
                    from agent.outcome_tracker import (
                        classify_session, record_outcome, skills_used_in,
                        tool_failure_rate,
                    )
                    verdict = classify_session(snapshot)
                    if verdict is not None:  # skip UNCLEAR sessions
                        # Cheap topic (first user turn) so failures can be clustered
                        # into knowledge gaps later — no extra model call.
                        topic = next(
                            (str(m.get("content", "")).strip()[:120]
                             for m in snapshot
                             if m.get("role") == "user" and str(m.get("content", "")).strip()),
                            "",
                        )
                        # Secondary reward penalty: a success reached only after
                        # many failed tool calls is a weaker positive signal.
                        record_outcome(session_id, verdict,
                                       skills=skills_used_in(snapshot), note=topic,
                                       active_persona=active_persona,
                                       tool_failure_rate=tool_failure_rate(snapshot))
                        # Reflexion write-back: a failed session becomes a
                        # retrievable "do X instead" lesson keyed to the task
                        # type, so the next similar attempt starts smarter.
                        if verdict is False and _flag("learning", "reflexion", default=True):
                            try:
                                from agent.lessons import reflect_on_failure, record_lesson
                                r = reflect_on_failure(snapshot)
                                if r:
                                    record_lesson(r["lesson"], task_type=r.get("task_type", ""),
                                                  session_id=session_id)
                                # Self-growing benchmark: draft a quarantined
                                # regression-pin eval from the same failure.
                                if _flag("evals", "autopin", default=False):
                                    from agent.eval_miner import (
                                        draft_eval_from_failure, write_eval_draft,
                                    )
                                    spec = draft_eval_from_failure(
                                        snapshot, lesson=(r or {}).get("lesson", ""))
                                    if spec:
                                        write_eval_draft(spec)
                            except Exception as exc:
                                logger.debug("reflexion/autopin write-back failed: %s", exc)
                except Exception as exc:
                    logger.debug("auto outcome tracking failed: %s", exc)
            if mine_memory:
                try:
                    from tools.memory_tool import MemoryStore
                    from agent.memory_miner import mine_session_memory

                    store = MemoryStore()
                    store.load_from_disk()
                    mine_session_memory(snapshot, store)
                except Exception as exc:
                    logger.debug("auto memory mining failed: %s", exc)
            if mine_skills:
                try:
                    from agent.skill_miner import mine_session_skills

                    try:
                        from tools.skills_tool import _find_all_skills
                        existing = [s["name"] for s in _find_all_skills()]
                    except Exception:
                        existing = []
                    mine_session_skills(snapshot, existing_skill_names=existing)
                except Exception as exc:
                    logger.debug("auto skill mining failed: %s", exc)

        if run_in_thread:
            t = threading.Thread(target=_work, daemon=True, name="auto-mine")
            t.start()
            return t
        _work()
        return None
    except Exception as exc:  # the session boundary must never break
        logger.debug("maybe_automine failed: %s", exc)
        return None
