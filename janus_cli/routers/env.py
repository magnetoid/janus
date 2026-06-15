from fastapi import APIRouter, HTTPException, Request, Response, WebSocket, WebSocketDisconnect
from fastapi.responses import FileResponse, HTMLResponse, JSONResponse
from pydantic import BaseModel
from typing import Any, Dict, List, Optional, Tuple, Union
import janus_cli.web_server as web_server_mod

router = APIRouter()

@router.get("/api/env")
async def get_env_vars():
    env_on_disk = web_server_mod.load_env()
    channel_keys = web_server_mod._channel_managed_env_keys()
    result = {}
    for var_name, info in web_server_mod.OPTIONAL_ENV_VARS.items():
        value = env_on_disk.get(var_name)
        result[var_name] = {
            "is_set": bool(value),
            "redacted_value": web_server_mod.redact_key(value) if value else None,
            "description": info.get("description", ""),
            "url": info.get("url"),
            "category": info.get("category", ""),
            "is_password": info.get("password", False),
            "tools": info.get("tools", []),
            "advanced": info.get("advanced", False),
            # True when this var is a messaging-platform credential owned by a
            # Channels page card. The Keys/Env page uses this to hide it and
            # avoid duplicating the (richer) Channels configuration UI.
            "channel_managed": var_name in channel_keys,
        }
    return result

@router.put("/api/env")
async def set_env_var(body: web_server_mod.EnvVarUpdate):
    try:
        web_server_mod.save_env_value(body.key, body.value)
        return {"ok": True, "key": body.key}
    except ValueError as exc:
        # save_env_value raises ValueError for invalid names and for keys
        # on the denylist (LD_PRELOAD, PATH, PYTHONPATH, …). Surface the
        # message to the SPA so the user understands why the write was
        # refused instead of seeing an opaque 500.
        raise web_server_mod.HTTPException(status_code=400, detail=str(exc)) from exc
    except Exception:
        web_server_mod._log.exception("PUT /api/env failed")
        raise web_server_mod.HTTPException(status_code=500, detail="Internal server error")

@router.delete("/api/env")
async def remove_env_var(body: web_server_mod.EnvVarDelete):
    try:
        removed = web_server_mod.remove_env_value(body.key)
        if not removed:
            raise web_server_mod.HTTPException(status_code=404, detail=f"{body.key} not found in .env")
        return {"ok": True, "key": body.key}
    except web_server_mod.HTTPException:
        raise
    except ValueError as exc:
        # remove_env_value raises ValueError for invalid key names. Surface
        # the message to the SPA so the user understands why the delete was
        # refused instead of seeing an opaque 500. Mirrors PUT /api/env.
        raise web_server_mod.HTTPException(status_code=400, detail=str(exc)) from exc
    except Exception:
        web_server_mod._log.exception("DELETE /api/env failed")
        raise web_server_mod.HTTPException(status_code=500, detail="Internal server error")

@router.post("/api/env/reveal")
async def reveal_env_var(body: web_server_mod.EnvVarReveal, request: web_server_mod.Request):
    """Return the real (unredacted) value of a single env var.

    Protected by:
    - Ephemeral session token (generated per server start, injected into SPA)
    - Rate limiting (max 5 reveals per 30s window)
    - Audit logging
    """
    # --- Token check ---
    web_server_mod._require_token(request)

    # --- Rate limit ---
    now = web_server_mod.time.time()
    cutoff = now - web_server_mod._REVEAL_WINDOW_SECONDS
    web_server_mod._reveal_timestamps[:] = [t for t in web_server_mod._reveal_timestamps if t > cutoff]
    if len(web_server_mod._reveal_timestamps) >= web_server_mod._REVEAL_MAX_PER_WINDOW:
        raise web_server_mod.HTTPException(status_code=429, detail="Too many reveal requests. Try again shortly.")
    web_server_mod._reveal_timestamps.append(now)

    # --- Reveal ---
    env_on_disk = web_server_mod.load_env()
    value = env_on_disk.get(body.key)
    if value is None:
        raise web_server_mod.HTTPException(status_code=404, detail=f"{body.key} not found in .env")

    web_server_mod._log.info("env/reveal: %s", body.key)
    return {"key": body.key, "value": value}

