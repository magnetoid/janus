"""deliberate — answer a contested question via two-headed adversarial reasoning.

Complements the moa toolset's other deliberate-spend tools: mixture_of_agents
gives breadth (many models, average), deep_reason gives depth (one model,
iterate), deliberate gives OPPOSITION — an advocate argues the strongest
answer, an opponent argues the strongest honest counter-case, a synthesizer
rules on the stronger argument and reports when the question is genuinely
frame-dependent (both framings honestly valid) instead of feigning
confidence. Spends 3 auxiliary-model calls — reach for it deliberately.
"""
import json

from tools.registry import registry


def deliberate_tool(question: str, context: str = "", **_kw) -> str:
    try:
        from agent.deliberation import deliberate
        res = deliberate(question, context)
        return json.dumps({
            "success": res.get("error") is None,
            "answer": res.get("answer", ""),
            "confidence": res.get("confidence"),
            "frame_dependent": res.get("frame_dependent"),
            "crux": res.get("crux", ""),
            "dissent": res.get("dissent", ""),
            "conceded": res.get("conceded"),
            "error": res.get("error"),
        }, ensure_ascii=False)
    except Exception as exc:
        return json.dumps({"success": False, "error": str(exc)})


registry.register(
    name="deliberate",
    toolset="moa",
    schema={
        "name": "deliberate",
        "description": (
            "Answer a contested or high-stakes question by staging structured "
            "disagreement: an advocate argues the strongest answer, an opponent "
            "argues the strongest honest counter-case, and a synthesizer rules on "
            "the stronger argument. Reports frame_dependent=true when both sides "
            "are honestly right under different framings (state both frames to the "
            "user instead of picking one). Best for judgment calls, contested "
            "claims, and decisions where a wrong confident answer is costly. "
            "Spends multiple model calls — use deliberately, like mixture_of_agents."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "question": {
                    "type": "string",
                    "description": "The contested question or claim to deliberate.",
                },
                "context": {
                    "type": "string",
                    "description": "Optional evidence/background both heads should consider.",
                },
            },
            "required": ["question"],
        },
    },
    handler=lambda args, **kw: deliberate_tool(
        question=args.get("question", ""), context=args.get("context", "")
    ),
)
