"""consensus tool — answer a prompt with the right-cost model (or an ensemble).

Routes the prompt by complexity (agent/model_routing): the cheap-tier model for
simple work, the smart tier for hard work, and — when the ensemble is enabled —
a consensus of several strong models synthesized by the mixture_of_agents tool.
Saves tokens on easy work and lifts answer quality on hard work.

Exposed only when ``consensus.enabled`` is on (check_fn gate). Routing happens
at this single tool call (task entry), so it never changes the main agent's
model mid-conversation — the prompt cache is untouched.
"""
import json

from tools.registry import registry


def _default_single_caller(provider, model, prompt):
    from agent.auxiliary_client import call_llm
    resp = call_llm(
        task="consensus",
        provider=provider or None, model=model or None,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3, max_tokens=4000,
    )
    return str(resp.choices[0].message.content or "").strip()


def _default_ensemble_caller(prompt, members, task):
    import asyncio
    from tools.mixture_of_agents_tool import mixture_of_agents_tool
    out = asyncio.run(mixture_of_agents_tool(prompt, reference_models=members, task=task))
    try:
        data = json.loads(out)
        return data.get("response") or out
    except (ValueError, TypeError):
        return out


def consensus_answer(
    prompt, task=None, *, config=None, main_model="", main_provider="",
    single_caller=None, ensemble_caller=None,
):
    """Route ``prompt`` and answer it with the chosen model(s).

    Returns ``{answer, complexity, tier, ensemble, models, error}``. Injectable
    callers make routing/dispatch testable without a live model. Never raises.
    """
    from agent.model_routing import route
    single = single_caller or _default_single_caller
    ensemble = ensemble_caller or _default_ensemble_caller
    result = {"answer": "", "complexity": "mid", "tier": "mid",
              "ensemble": False, "models": [], "error": None}
    try:
        d = route(prompt, task=task, config=config,
                  main_model=main_model, main_provider=main_provider)
        result["complexity"] = d["complexity"]
        result["tier"] = d["tier"]
        result["ensemble"] = d["ensemble"]
        if d["ensemble"] and d["members"]:
            result["models"] = list(d["members"])
            result["answer"] = ensemble(prompt, d["members"], task)
        else:
            result["models"] = [d["model"]] if d["model"] else []
            result["answer"] = single(d["provider"], d["model"], prompt)
    except Exception as exc:
        result["error"] = str(exc)
    return result


def _consensus_enabled(*args, **kwargs):
    try:
        from agent.model_routing import enabled
        return enabled()
    except Exception:
        return False


def consensus_tool(prompt: str, task: str = None, task_id: str = None) -> str:
    out = consensus_answer(prompt, task=task)
    return json.dumps({"success": out["error"] is None, **out}, ensure_ascii=False)


registry.register(
    name="consensus",
    toolset="consensus",
    schema={
        "name": "consensus",
        "description": (
            "Answer a prompt with the RIGHT-COST model: a cheap model for simple "
            "work, a strong model for hard work, and — for the hardest problems — "
            "an ensemble of top models whose answers are synthesized. Use this to "
            "save tokens on easy sub-questions and to get a higher-quality, "
            "multi-model answer on genuinely hard ones. Pass an optional 'task' "
            "category (e.g. 'coding', 'math', 'research') to pick the best models."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "prompt": {"type": "string", "description": "The question/task to answer."},
                "task": {
                    "type": "string",
                    "description": "Optional category (coding, math, research, writing) for model selection.",
                },
            },
            "required": ["prompt"],
        },
    },
    handler=lambda args, **kw: consensus_tool(
        prompt=args.get("prompt", ""), task=args.get("task"), task_id=kw.get("task_id")
    ),
    check_fn=_consensus_enabled,
)
