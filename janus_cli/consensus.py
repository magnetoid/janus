"""CLI subcommand: ``janus consensus <subcommand>``.

  janus consensus status          Show routing config (tiers, ensemble, on/off)
  janus consensus route "<text>"  Show how a prompt would route (free, no model)
  janus consensus run "<text>"    Answer a prompt through consensus routing

Thin shell over agent/model_routing.py + tools/consensus_tool.py. No import-time
side effects — main.py wires the argparse subparsers on demand.
"""
from __future__ import annotations

import argparse
import sys


def _fmt_model(provider: str, model: str) -> str:
    model = model or "(inherit main model)"
    return f"{provider}:{model}" if provider else model


def _cmd_status(args) -> int:
    from agent.model_routing import _consensus_config, enabled

    cfg = _consensus_config()
    print(f"consensus: {'ENABLED' if enabled() else 'disabled'}  "
          f"(complexity={cfg.get('complexity_mode', 'heuristic')})")
    tiers = cfg.get("model_tiers", {}) or {}
    for name in ("cheap", "mid", "smart"):
        t = tiers.get(name, {}) or {}
        print(f"  {name:6s} {_fmt_model(str(t.get('provider', '')), str(t.get('model', '')))}")
    ens = cfg.get("ensemble", {}) or {}
    print(f"  ensemble: {'on' if ens.get('enabled') else 'off'} "
          f"(>= {ens.get('min_complexity', 'hard')}, {ens.get('member_count', 3)} members)")
    if not enabled():
        print("\nEnable with: janus config set consensus.enabled true  (or run `janus setup`)")
    return 0


def _cmd_route(args) -> int:
    from agent.model_routing import route

    d = route(args.prompt, task=getattr(args, "task", None))
    print(f"complexity: {d['complexity']}  →  tier: {d['tier']}")
    if d["ensemble"]:
        print(f"ensemble:   {', '.join(d['members'])}")
    else:
        print(f"model:      {_fmt_model(d['provider'], d['model'])}")
    return 0


def _cmd_run(args) -> int:
    from tools.consensus_tool import consensus_answer

    out = consensus_answer(args.prompt, task=getattr(args, "task", None))
    if out["error"]:
        print(f"consensus: error — {out['error']}", file=sys.stderr)
        return 1
    print(out["answer"])
    if getattr(args, "verbose", False):
        tag = ("ensemble:" + ",".join(out["models"])) if out["ensemble"] else \
            ("model:" + (out["models"][0] if out["models"] else "main"))
        print(f"\n[{out['complexity']} → {out['tier']} | {tag}]", file=sys.stderr)
    return 0


def register_cli(parent: argparse.ArgumentParser) -> None:
    """Wire ``janus consensus`` subcommands onto an existing parser."""
    parent.set_defaults(func=lambda a: (parent.print_help(), 0)[1])
    subs = parent.add_subparsers(dest="consensus_command")

    p_status = subs.add_parser("status", help="Show consensus routing config")
    p_status.set_defaults(func=_cmd_status)

    p_route = subs.add_parser("route", help="Show how a prompt would route (free, no model call)")
    p_route.add_argument("prompt", help="The prompt to classify/route")
    p_route.add_argument("--task", help="Optional task category (coding, math, research, …)")
    p_route.set_defaults(func=_cmd_route)

    p_run = subs.add_parser("run", help="Answer a prompt through consensus routing")
    p_run.add_argument("prompt", help="The prompt to answer")
    p_run.add_argument("--task", help="Optional task category (coding, math, research, …)")
    p_run.add_argument("-v", "--verbose", action="store_true",
                       help="Print the routing decision to stderr")
    p_run.set_defaults(func=_cmd_run)
