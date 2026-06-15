from fastapi import APIRouter, HTTPException, Request, Response, WebSocket, WebSocketDisconnect
from fastapi.responses import FileResponse, HTMLResponse, JSONResponse
from pydantic import BaseModel
from typing import Any, Dict, List, Optional, Tuple, Union
import janus_cli.web_server as web_server_mod

router = APIRouter()

@router.get("/api/webhooks")
async def list_webhooks():
    import janus_cli.webhook as wh

    base_url = wh._get_webhook_base_url()
    subs = wh._load_subscriptions()
    return {
        "enabled": wh._is_webhook_enabled(),
        "base_url": base_url,
        "subscriptions": [
            web_server_mod._webhook_route_summary(name, route, base_url)
            for name, route in subs.items()
        ],
    }

@router.post("/api/webhooks")
async def create_webhook(body: web_server_mod.WebhookCreate):
    import re as _re
    import secrets as _secrets
    import time as _time
    import janus_cli.webhook as wh

    if not wh._is_webhook_enabled():
        raise web_server_mod.HTTPException(
            status_code=400,
            detail="Webhook platform is not enabled. Enable it in messaging settings first.",
        )

    name = (body.name or "").strip().lower().replace(" ", "-")
    if not _re.match(r"^[a-z0-9][a-z0-9_-]*$", name):
        raise web_server_mod.HTTPException(
            status_code=400,
            detail="Invalid name. Use lowercase alphanumeric with hyphens/underscores.",
        )

    if body.deliver_only and body.deliver == "log":
        raise web_server_mod.HTTPException(
            status_code=400,
            detail="Direct delivery requires a real target (telegram, discord, …), not 'log'.",
        )

    secret = body.secret or _secrets.token_urlsafe(32)
    route: web_server_mod.Dict[str, web_server_mod.Any] = {
        "description": body.description or f"Dashboard-created subscription: {name}",
        "events": [e.strip() for e in body.events if e.strip()],
        "secret": secret,
        "prompt": body.prompt or "",
        "skills": [s.strip() for s in body.skills if s.strip()],
        "deliver": body.deliver or "log",
        "created_at": _time.strftime("%Y-%m-%dT%H:%M:%SZ", _time.gmtime()),
    }
    if body.deliver_only:
        route["deliver_only"] = True
    if body.deliver_chat_id:
        route["deliver_extra"] = {"chat_id": body.deliver_chat_id}

    subs = wh._load_subscriptions()
    subs[name] = route
    wh._save_subscriptions(subs)

    base_url = wh._get_webhook_base_url()
    summary = web_server_mod._webhook_route_summary(name, route, base_url)
    # Surface the secret exactly once, on create.
    summary["secret"] = secret
    return summary

@router.delete("/api/webhooks/{name}")
async def delete_webhook(name: str):
    import janus_cli.webhook as wh

    key = (name or "").strip().lower()
    subs = wh._load_subscriptions()
    if key not in subs:
        raise web_server_mod.HTTPException(status_code=404, detail=f"No subscription named '{key}'")
    del subs[key]
    wh._save_subscriptions(subs)
    return {"ok": True}

@router.put("/api/webhooks/{name}/enabled")
async def set_webhook_enabled(name: str, body: web_server_mod.WebhookEnabledToggle):
    """Enable or disable a webhook route.

    Disabled routes stay in the subscriptions file (so they can be
    re-enabled) but the gateway rejects incoming events with 403.  The
    gateway hot-reloads the subscriptions file, so this takes effect on the
    next event without a restart.
    """
    import janus_cli.webhook as wh

    key = (name or "").strip().lower()
    subs = wh._load_subscriptions()
    if key not in subs:
        raise web_server_mod.HTTPException(status_code=404, detail=f"No subscription named '{key}'")
    subs[key]["enabled"] = bool(body.enabled)
    wh._save_subscriptions(subs)
    return {"ok": True, "name": key, "enabled": bool(body.enabled)}

