"""Dialectic deliberation — two-headed reasoning with an arbiter.

Where Mixture-of-Agents gives BREADTH (many models, one pass, average) and
Reflexion gives DEPTH (one model, iterate), this gives OPPOSITION: stage the
strongest honest disagreement about a question or candidate artifact, then
let an arbiter rule on the stronger ARGUMENT — never the majority. A
conclusion that survives a genuine adversary is load-bearing; one that
collapses was never true.

Three entry points (full design: ``plans/dialectic-learning-gate.md``):

- ``deliberate(question)`` — the on-demand primitive behind the
  ``deliberate`` tool. Advocate argues the strongest answer, Skeptic argues
  the strongest opposing case (or concedes), Synthesizer rules — including
  the frame-stability verdict: when both framings are honestly valid
  ("glass half full / half empty"), the truthful output is
  ``frame_dependent: true`` with both frames, not false confidence.
- ``red_team_claims(claims)`` — batched admission gate for learned
  artifacts (mined facts / skill proposals). All claims ride in ONE
  advocate call, ONE skeptic call, ONE arbiter call — a 10-fact session
  costs 3 calls, not 30.
- ``quorum_classify(question)`` — two opposed-prior judges answer the same
  yes/no question; agreement is a trustworthy label, disagreement is
  honestly reported as contested (``label: None``).

Everything takes an injectable ``llm_caller`` (the miner-test pattern),
runs on auxiliary models, and never raises — deliberation must degrade,
not crash. Per-stance models are pinned via ``auxiliary.dialectic_advocate``
/ ``dialectic_skeptic`` / ``dialectic_arbiter`` in config.yaml; distinct
model families de-correlate blind spots.
"""

from __future__ import annotations

import json
import logging
from typing import Any, Callable, Dict, List, Optional

logger = logging.getLogger(__name__)

VERDICTS = ("accept", "reject", "revise")
CONFIDENCES = ("high", "medium", "low")


# ---------------------------------------------------------------------------
# Config gates (learning.dialectic.*)
# ---------------------------------------------------------------------------

def dialectic_enabled(path: str) -> bool:
    """True when the learning red-team gate is on for *path* (memory/skills/outcomes).

    Master switch ``learning.dialectic.enabled`` defaults to FALSE — the gate
    is an opt-in feature to test and validate, not always-on behavior.
    """
    try:
        from janus_cli.config import read_raw_config
        dialectic = (read_raw_config().get("learning") or {}).get("dialectic") or {}
        if not dialectic.get("enabled", False):
            return False
        return bool(dialectic.get(path, True))
    except Exception:
        return False


# ---------------------------------------------------------------------------
# JSON extraction helpers
# ---------------------------------------------------------------------------

def _extract_json(raw: Optional[str], opener: str, closer: str) -> Optional[Any]:
    if not raw:
        return None
    text = str(raw)
    start = text.find(opener)
    if start == -1:
        return None
    depth = 0
    for i in range(start, len(text)):
        if text[i] == opener:
            depth += 1
        elif text[i] == closer:
            depth -= 1
            if depth == 0:
                try:
                    return json.loads(text[start:i + 1])
                except (ValueError, TypeError):
                    return None
    return None


def _content(resp: Any) -> str:
    return str(resp.choices[0].message.content or "").strip()


# ---------------------------------------------------------------------------
# deliberate() — the on-demand two-headed exchange
# ---------------------------------------------------------------------------

_ADVOCATE_SYSTEM = (
    "You are the first head of a two-headed reasoner. Answer the question with "
    "the strongest defensible position. Commit to a clear answer and argue it "
    "with concrete evidence and reasoning — no hedging, the other head will "
    "supply the opposition. If context is provided, cite it."
)

_OPPONENT_SYSTEM = (
    "You are the second head of a two-headed reasoner. You are given a question "
    "and the first head's answer. Argue the strongest HONEST opposing case: a "
    "different answer, a different framing under which the answer flips, or the "
    "strongest objection to the reasoning. Steelman — a weak or invented "
    "objection discredits you. If the first head is simply correct and no honest "
    "counter-case exists, reply with exactly CONCEDE followed by one sentence "
    "explaining why the answer is robust."
)

_SYNTH_SYSTEM = (
    "You are the synthesizer for a two-headed reasoner. You see a question, an "
    "advocate's answer, and an opponent's counter-case. Rule on the stronger "
    "ARGUMENT — never on length, tone, or which side you'd have picked yourself.\n"
    "Decide whether the disagreement is frame-dependent: both sides are honestly "
    "right under different framings or value weightings (the glass is half full "
    "AND half empty). When it is, say so — reporting frame-dependence is the "
    "truthful answer, not a failure to decide.\n"
    "Respond with ONLY JSON:\n"
    '{"answer": "<the synthesized answer; when frame_dependent, state both '
    'frames and what each depends on>", "confidence": "high|medium|low", '
    '"frame_dependent": true|false, "crux": "<the single load-bearing '
    'consideration, one sentence>", "dissent": "<the strongest surviving '
    'objection, or empty string>"}'
)


def deliberate(
    question: str,
    context: str = "",
    *,
    llm_caller: Optional[Callable[..., Any]] = None,
) -> Dict[str, Any]:
    """Run advocate → opponent → synthesizer on *question*. Never raises.

    Returns ``{"answer", "confidence", "frame_dependent", "crux", "dissent",
    "conceded", "calls", "error"}``. On infrastructure error the advocate's
    answer (if any) is preserved and ``error`` is set.
    """
    result: Dict[str, Any] = {
        "answer": "", "confidence": "low", "frame_dependent": False,
        "crux": "", "dissent": "", "conceded": False, "calls": 0, "error": None,
    }
    if not question or not question.strip():
        result["error"] = "empty question"
        return result
    try:
        if llm_caller is None:
            from agent.auxiliary_client import call_llm as llm_caller

        user_q = question if not context.strip() else f"CONTEXT:\n{context}\n\nQUESTION:\n{question}"

        case = _content(llm_caller(
            task="dialectic_advocate",
            messages=[{"role": "system", "content": _ADVOCATE_SYSTEM},
                      {"role": "user", "content": user_q}],
            temperature=0.3, max_tokens=1200,
        ))
        result["calls"] += 1
        result["answer"] = case  # best answer so far if later calls fail

        rebuttal = _content(llm_caller(
            task="dialectic_skeptic",
            messages=[{"role": "system", "content": _OPPONENT_SYSTEM},
                      {"role": "user", "content": (
                          f"{user_q}\n\nFIRST HEAD'S ANSWER:\n{case}\n\n"
                          "Your strongest honest counter-case (or CONCEDE):"
                      )}],
            temperature=0.4, max_tokens=1200,
        ))
        result["calls"] += 1
        conceded = rebuttal.strip().upper().startswith("CONCEDE")
        result["conceded"] = conceded

        synth_raw = _content(llm_caller(
            task="dialectic_arbiter",
            messages=[{"role": "system", "content": _SYNTH_SYSTEM},
                      {"role": "user", "content": (
                          f"{user_q}\n\nADVOCATE'S ANSWER:\n{case}\n\n"
                          f"OPPONENT'S CASE:\n{rebuttal}\n\nRule."
                      )}],
            temperature=0, max_tokens=1200,
        ))
        result["calls"] += 1

        data = _extract_json(synth_raw, "{", "}")
        if not isinstance(data, dict) or not str(data.get("answer", "")).strip():
            result["error"] = "synthesizer returned no parseable verdict"
            return result
        result["answer"] = str(data.get("answer", "")).strip()
        conf = str(data.get("confidence", "low")).lower()
        result["confidence"] = conf if conf in CONFIDENCES else "low"
        result["frame_dependent"] = bool(data.get("frame_dependent"))
        result["crux"] = str(data.get("crux", "")).strip()
        result["dissent"] = str(data.get("dissent", "")).strip()
        return result
    except Exception as exc:  # deliberation must degrade, not crash
        logger.debug("deliberation failed: %s", exc)
        result["error"] = str(exc)
        return result


# ---------------------------------------------------------------------------
# red_team_claims() — batched admission gate for learned artifacts
# ---------------------------------------------------------------------------

_RT_ADVOCATE_SYSTEM = (
    "You argue that candidate learned artifacts (memories/facts/skills mined "
    "from an agent session) SHOULD be committed to long-term storage. For each "
    "claim give the strongest concrete evidence from the transcript that it is "
    "durable, general, and correct. Concede weak claims explicitly — a "
    "selective advocate is a credible advocate. Answer per claim id."
)

_RT_SKEPTIC_SYSTEM = (
    "You argue that candidate learned artifacts should NOT be committed. For "
    "each claim, check: overfit to this one session (a temporary instruction "
    "phrased as a permanent fact)? a 'success' that was trivial or lucky? "
    "stale, or contradicting existing knowledge provided to you? duplicating "
    "an existing skill (names provided)? speculation phrased as fact? Cite the "
    "transcript. If a claim has no real flaw, say NO OBJECTION for it — "
    "invented objections discredit you. Answer per claim id."
)

_RT_ARBITER_SYSTEM = (
    "You rule on whether each candidate learned artifact is committed, given "
    "an advocate's case and a skeptic's objections. Reward the stronger "
    "ARGUMENT, never the majority and never the longer text. Prefer "
    '"revise" with a narrowed/corrected claim when the objection is real but '
    "fixable (e.g. scope a fact to the project it came from). Respond with "
    "ONLY a JSON array, one object per claim:\n"
    '[{"id": "<claim id>", "verdict": "accept|reject|revise", '
    '"confidence": "high|medium|low", "revised_content": "<only for revise, '
    'else null>", "crux": "<one sentence>", "skeptic_objection": '
    '"<the objection that mattered, or empty>"}]'
)


def _render_claims(claims: List[Dict[str, Any]]) -> str:
    lines = []
    for c in claims:
        kind = c.get("kind", "fact")
        ctx = f" (context: {c['context']})" if c.get("context") else ""
        lines.append(f"[{c['id']}] ({kind}) {c.get('content', '')}{ctx}")
    return "\n".join(lines)


def red_team_claims(
    claims: List[Dict[str, Any]],
    *,
    transcript: str = "",
    existing: str = "",
    llm_caller: Optional[Callable[..., Any]] = None,
) -> Dict[str, Any]:
    """Batch advocate → skeptic → arbiter over candidate artifacts.

    ``claims``: ``[{"id", "kind": "fact"|"skill", "content", "context"?}]``.
    ``existing``: existing knowledge/skill names the skeptic may cite for
    staleness/duplication objections.

    Returns ``{"verdicts": {id: verdict_dict}, "calls": N, "error": None|str}``.
    On any error ``verdicts`` is empty and callers MUST fail open to their
    current behavior — an infrastructure failure is not a rejection.
    """
    result: Dict[str, Any] = {"verdicts": {}, "calls": 0, "error": None}
    if not claims:
        return result
    try:
        if llm_caller is None:
            from agent.auxiliary_client import call_llm as llm_caller

        claims_block = _render_claims(claims)
        evidence = f"\n\nSESSION TRANSCRIPT (evidence):\n{transcript}" if transcript.strip() else ""
        known = f"\n\nEXISTING KNOWLEDGE / SKILL NAMES:\n{existing}" if existing.strip() else ""

        case = _content(llm_caller(
            task="dialectic_advocate",
            messages=[{"role": "system", "content": _RT_ADVOCATE_SYSTEM},
                      {"role": "user", "content": f"CANDIDATE CLAIMS:\n{claims_block}{evidence}"}],
            temperature=0, max_tokens=1500,
        ))
        result["calls"] += 1

        objections = _content(llm_caller(
            task="dialectic_skeptic",
            messages=[{"role": "system", "content": _RT_SKEPTIC_SYSTEM},
                      {"role": "user", "content": (
                          f"CANDIDATE CLAIMS:\n{claims_block}{evidence}{known}\n\n"
                          f"ADVOCATE'S CASE:\n{case}"
                      )}],
            temperature=0, max_tokens=1500,
        ))
        result["calls"] += 1

        ruling_raw = _content(llm_caller(
            task="dialectic_arbiter",
            messages=[{"role": "system", "content": _RT_ARBITER_SYSTEM},
                      {"role": "user", "content": (
                          f"CANDIDATE CLAIMS:\n{claims_block}\n\n"
                          f"ADVOCATE:\n{case}\n\nSKEPTIC:\n{objections}\n\nRule per claim."
                      )}],
            temperature=0, max_tokens=2000,
        ))
        result["calls"] += 1

        rulings = _extract_json(ruling_raw, "[", "]")
        if not isinstance(rulings, list):
            result["error"] = "arbiter returned no parseable ruling"
            return result

        claim_ids = {str(c["id"]) for c in claims}
        for r in rulings:
            if not isinstance(r, dict):
                continue
            cid = str(r.get("id", ""))
            verdict = str(r.get("verdict", "")).lower()
            if cid not in claim_ids or verdict not in VERDICTS:
                continue
            conf = str(r.get("confidence", "low")).lower()
            revised = r.get("revised_content")
            result["verdicts"][cid] = {
                "verdict": verdict,
                "confidence": conf if conf in CONFIDENCES else "low",
                "revised_content": str(revised).strip() if verdict == "revise" and revised else None,
                "crux": str(r.get("crux", "")).strip(),
                "skeptic_objection": str(r.get("skeptic_objection", "")).strip(),
            }
        # A "revise" with no revised text cannot be applied — treat as accept
        # of the original rather than dropping the claim on a formatting slip.
        for v in result["verdicts"].values():
            if v["verdict"] == "revise" and not v["revised_content"]:
                v["verdict"] = "accept"
        return result
    except Exception as exc:
        logger.debug("red-team gate failed: %s", exc)
        result["error"] = str(exc)
        result["verdicts"] = {}
        return result


def apply_verdicts(
    claims: List[Dict[str, Any]],
    verdicts: Dict[str, Dict[str, Any]],
) -> Dict[str, List[Dict[str, Any]]]:
    """Split claims by ruling. Claims the arbiter didn't rule on pass through
    accepted (fail open per-claim — silence is not a rejection)."""
    out: Dict[str, List[Dict[str, Any]]] = {"accepted": [], "rejected": []}
    for c in claims:
        v = verdicts.get(str(c["id"]))
        if v is None or v["verdict"] == "accept":
            out["accepted"].append(c)
        elif v["verdict"] == "revise":
            revised = dict(c)
            revised["content"] = v["revised_content"]
            out["accepted"].append(revised)
        else:
            rejected = dict(c)
            rejected["objection"] = v.get("skeptic_objection") or v.get("crux") or ""
            out["rejected"].append(rejected)
    return out


# ---------------------------------------------------------------------------
# quorum_classify() — opposed-prior judges for yes/no labels
# ---------------------------------------------------------------------------

_JUDGE_SYSTEMS = {
    "charitable": (
        "You judge agent sessions generously: did the assistant materially "
        "advance the user's goal? Partial but real progress counts as success. "
        "Reply with ONLY the word SUCCESS or FAILURE."
    ),
    "strict": (
        "You judge agent sessions strictly: would the user call this a success "
        "without qualification — task fully done, no unresolved errors? "
        "Partial credit is FAILURE. Reply with ONLY the word SUCCESS or FAILURE."
    ),
}


def quorum_classify(
    question: str,
    transcript: str,
    *,
    stances: tuple = ("charitable", "strict"),
    llm_caller: Optional[Callable[..., Any]] = None,
) -> Dict[str, Any]:
    """Two opposed-prior judges answer the same yes/no question.

    Returns ``{"agreed": bool, "label": True|False|None, "votes": [...],
    "error": None|str}`` — ``label`` is None when the judges disagree
    (contested) or on error. Never raises.
    """
    result: Dict[str, Any] = {"agreed": False, "label": None, "votes": [], "error": None}
    try:
        if llm_caller is None:
            from agent.auxiliary_client import call_llm as llm_caller
        for stance in stances:
            system = _JUDGE_SYSTEMS.get(stance, _JUDGE_SYSTEMS["strict"])
            raw = _content(llm_caller(
                task="dialectic_arbiter",
                messages=[{"role": "system", "content": system},
                          {"role": "user", "content": f"{transcript}\n\n{question}"}],
                temperature=0, max_tokens=5,
            )).upper()
            if raw.startswith("SUCCESS"):
                result["votes"].append(True)
            elif raw.startswith("FAILURE"):
                result["votes"].append(False)
            else:
                result["votes"].append(None)
        votes = [v for v in result["votes"] if v is not None]
        if len(votes) == len(stances) and len(set(votes)) == 1:
            result["agreed"] = True
            result["label"] = votes[0]
        return result
    except Exception as exc:
        logger.debug("quorum classify failed: %s", exc)
        result["error"] = str(exc)
        return result
