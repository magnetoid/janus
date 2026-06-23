from fastapi import APIRouter, HTTPException, Request, Response, WebSocket, WebSocketDisconnect
from fastapi.responses import FileResponse, HTMLResponse, JSONResponse
from pydantic import BaseModel
from typing import Any, Dict, List, Optional, Tuple, Union
import janus_cli.web_server as web_server_mod

router = APIRouter()

@router.get("/api/portal")
async def get_portal_status():
    cfg = web_server_mod.load_config() or {}
    auth: web_server_mod.Dict[str, web_server_mod.Any] = {}
    try:
        from janus_cli.auth import get_nous_auth_status

        auth = get_nous_auth_status() or {}
    except Exception:
        auth = {}

    features = []
    try:
        from janus_cli.nous_subscription import get_nous_subscription_features

        feats = get_nous_subscription_features(cfg)
        if feats is not None:
            for feat in feats.items():
                if getattr(feat, "managed_by_nous", False):
                    state = "via Cloud Industry Portal"
                elif getattr(feat, "active", False) and getattr(feat, "current_provider", None):
                    state = feat.current_provider
                elif getattr(feat, "active", False):
                    state = "active"
                else:
                    state = "not configured"
                features.append({"label": getattr(feat, "label", ""), "state": state})
    except Exception:
        web_server_mod._log.exception("portal features failed")

    model_cfg = cfg.get("model") if isinstance(cfg.get("model"), dict) else {}
    return {
        "logged_in": bool(auth.get("logged_in")),
        "portal_url": auth.get("portal_base_url"),
        "inference_url": auth.get("inference_base_url"),
        "provider": str((model_cfg or {}).get("provider") or ""),
        "subscription_url": "https://portal.cloud-industry.com/manage-subscription",
        "features": features,
    }

