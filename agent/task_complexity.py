"""Task complexity classification — route work to the right-cost model.

The cheap half of consensus routing: decide whether a request is ``simple``,
``mid``, or ``hard`` so the router can pick the cheapest capable model and
reserve the strongest models (and the ensemble) for genuinely hard work.

The default is a FREE local heuristic — no model call — because spending tokens
to classify would defeat the token savings the feature exists to create. An
optional ``mode="model"`` escalates only the ambiguous middle band to a cheap
auxiliary model. Pure + best-effort; never raises.
"""
from __future__ import annotations

import logging
import re
from typing import Any, Callable, Optional

logger = logging.getLogger(__name__)

BANDS = ("simple", "mid", "hard")

_HARD_KEYWORDS = (
    "design", "architect", "architecture", "prove", "derive", "optimize",
    "optimise", "refactor", "debug", "analyze", "analyse", "research", "plan",
    "strategy", "tradeoff", "trade-off", "compare", "evaluate", "root cause",
    "root-cause", "migrate", "algorithm", "concurren", "distributed",
    "security", "threat model", "reason about", "step by step", "step-by-step",
    "multi-step", "implement", "diagnose",
)
_SIMPLE_KEYWORDS = (
    "list", "summarize", "summarise", "define", "translate", "rename",
    "format", "capitalize", "lowercase", "uppercase", "what is", "what's",
    "when is", "who is", "spell", "convert", "echo", "repeat", "tldr", "tl;dr",
    "one line", "one-line", "in a word",
)
_CODE_SIGNALS = re.compile(
    r"```|^\s*def |\bclass \w|\bfunction \b|\bimport \b|SELECT \b|\bregex\b|"
    r"stack ?trace|traceback|exception",
    re.I | re.M,
)
_MATH_SIGNALS = re.compile(
    r"\b(integral|derivative|matrix|theorem|proof|equation|probability)\b|"
    r"\d+\s*[+\-*/^]\s*\d+\s*[+\-*/^=]",
    re.I,
)
_MULTISTEP = re.compile(r"\b(and then|step \d|first .*then|multiple|several)\b", re.I)


def _heuristic(prompt: str, history_len: int = 0) -> str:
    text = str(prompt or "")
    low = text.lower()
    n = len(text)
    score = 0.0

    # keyword signals (capped so a keyword-stuffed prompt can't dominate)
    hard_hits = min(sum(1 for k in _HARD_KEYWORDS if k in low), 3)
    simple_hits = min(sum(1 for k in _SIMPLE_KEYWORDS if k in low), 3)
    score += 0.8 * hard_hits
    score -= 0.8 * simple_hits

    # length / verbosity — a SHORT prompt only leans "simple" when it lacks
    # hard signals (a terse "design and prove X, analyze tradeoffs" is still hard).
    if n < 80 and hard_hits < 2:
        score -= 1.0
    elif n > 600:
        score += 1.0
    if len(text.split()) > 120:
        score += 1.0

    # structural signals
    if _CODE_SIGNALS.search(text):
        score += 0.8
    if _MATH_SIGNALS.search(text):
        score += 1.0
    if _MULTISTEP.search(low) or " both" in low:
        score += 0.6
    if text.count("?") >= 3:
        score += 0.5

    # a long live conversation is harder context to reason over
    if history_len >= 12:
        score += 0.5

    if score >= 1.5:
        return "hard"
    if score <= -0.8:
        return "simple"
    return "mid"


_MODEL_SYSTEM = (
    "Classify how hard a user request is for an LLM. Answer with ONE word: "
    "simple, mid, or hard. 'simple' = a lookup/format/one-liner; 'hard' = "
    "multi-step reasoning, design, debugging, proofs, or research."
)


def _model_classify(prompt: str, llm_caller: Callable[..., Any]) -> Optional[str]:
    try:
        resp = llm_caller(
            task="complexity_classify",
            messages=[
                {"role": "system", "content": _MODEL_SYSTEM},
                {"role": "user", "content": str(prompt)[:1500]},
            ],
            temperature=0, max_tokens=3,
        )
        word = str(resp.choices[0].message.content or "").strip().lower()
        for band in BANDS:
            if word.startswith(band):
                return band
        return None
    except Exception as exc:
        logger.debug("model complexity classify failed: %s", exc)
        return None


def classify_complexity(
    prompt: Any, *, history_len: int = 0,
    mode: str = "heuristic", llm_caller: Optional[Callable[..., Any]] = None,
) -> str:
    """Return ``"simple"``, ``"mid"``, or ``"hard"`` for ``prompt``.

    Heuristic by default (free). With ``mode="model"`` and an ``llm_caller``,
    only the ambiguous ``mid`` band is escalated to a cheap model — clear simple
    / hard verdicts never spend a token. Best-effort; never raises.
    """
    try:
        band = _heuristic(prompt, history_len)
        if mode == "model" and band == "mid" and llm_caller is not None:
            refined = _model_classify(prompt, llm_caller)
            if refined in BANDS:
                return refined
        return band
    except Exception as exc:
        logger.debug("classify_complexity failed: %s", exc)
        return "mid"
