from fastapi import APIRouter, HTTPException, Request, Response, WebSocket, WebSocketDisconnect
from fastapi.responses import FileResponse, HTMLResponse, JSONResponse
from pydantic import BaseModel
from typing import Any, Dict, List, Optional, Tuple, Union
import janus_cli.web_server as web_server_mod

router = APIRouter()

@router.get("/api/config")
async def get_config():
    config = web_server_mod._normalize_config_for_web(web_server_mod.load_config())
    # Strip internal keys that the frontend shouldn't see or send back
    return {k: v for k, v in config.items() if not k.startswith("_")}

@router.get("/api/config/defaults")
async def get_defaults():
    return web_server_mod.DEFAULT_CONFIG

@router.get("/api/config/schema")
async def get_schema():
    return {"fields": web_server_mod.CONFIG_SCHEMA, "category_order": web_server_mod._CATEGORY_ORDER}

@router.put("/api/config")
async def update_config(body: web_server_mod.ConfigUpdate):
    try:
        web_server_mod.save_config(web_server_mod._denormalize_config_from_web(body.config))
        return {"ok": True}
    except Exception:
        web_server_mod._log.exception("PUT /api/config failed")
        raise web_server_mod.HTTPException(status_code=500, detail="Internal server error")

@router.get("/api/config/raw")
async def get_config_raw():
    path = web_server_mod.get_config_path()
    if not path.exists():
        return {"yaml": ""}
    return {"yaml": path.read_text(encoding="utf-8")}

@router.put("/api/config/raw")
async def update_config_raw(body: web_server_mod.RawConfigUpdate):
    try:
        parsed = web_server_mod.yaml.safe_load(body.yaml_text)
        if not isinstance(parsed, dict):
            raise web_server_mod.HTTPException(status_code=400, detail="YAML must be a mapping")
        web_server_mod.save_config(parsed)
        return {"ok": True}
    except web_server_mod.yaml.YAMLError as e:
        raise web_server_mod.HTTPException(status_code=400, detail=f"Invalid YAML: {e}")

