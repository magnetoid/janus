from fastapi import APIRouter, HTTPException, Request, Response, WebSocket, WebSocketDisconnect
from fastapi.responses import FileResponse, HTMLResponse, JSONResponse
from pydantic import BaseModel
from typing import Any, Dict, List, Optional, Tuple, Union
import janus_cli.web_server as web_server_mod

router = APIRouter()

@router.get("/api/memory")
async def get_memory_status():
    from plugins.memory import discover_memory_providers

    cfg = web_server_mod.load_config()
    active = ""
    mem = cfg.get("memory")
    if isinstance(mem, dict):
        active = str(mem.get("provider") or "")

    providers = []
    try:
        for name, description, configured in discover_memory_providers():
            providers.append({
                "name": name,
                "description": description,
                "configured": bool(configured),
            })
    except Exception:
        web_server_mod._log.exception("discover_memory_providers failed")

    # Built-in memory file sizes (so the UI can show what a reset would erase).
    mem_dir = web_server_mod.get_janus_home() / "memories"
    files = {}
    for fname, key in (("MEMORY.md", "memory"), ("USER.md", "user")):
        path = mem_dir / fname
        files[key] = path.stat().st_size if path.exists() else 0

    return {
        "active": active,
        "providers": providers,
        "builtin_files": files,
    }

@router.put("/api/memory/provider")
async def set_memory_provider(body: web_server_mod.MemoryProviderSelect):
    provider = (body.provider or "").strip()
    if provider.lower() in {"built-in", "builtin", "none"}:
        provider = ""

    if provider:
        from plugins.memory import discover_memory_providers

        valid = {name for name, _d, _c in discover_memory_providers()}
        if provider not in valid:
            raise web_server_mod.HTTPException(
                status_code=400,
                detail=f"Unknown memory provider '{provider}'. Run `janus memory setup` to configure a new one.",
            )

    cfg = web_server_mod.load_config()
    if not isinstance(cfg.get("memory"), dict):
        cfg["memory"] = {}
    cfg["memory"]["provider"] = provider
    web_server_mod.save_config(cfg)
    return {"ok": True, "active": provider}

@router.post("/api/memory/reset")
async def reset_memory(body: web_server_mod.MemoryReset):
    target = (body.target or "all").strip().lower()
    if target not in {"all", "memory", "user"}:
        raise web_server_mod.HTTPException(status_code=400, detail="target must be all, memory, or user")

    mem_dir = web_server_mod.get_janus_home() / "memories"
    deleted = []
    targets = []
    if target in {"all", "memory"}:
        targets.append("MEMORY.md")
    if target in {"all", "user"}:
        targets.append("USER.md")
    for fname in targets:
        path = mem_dir / fname
        if path.exists():
            try:
                path.unlink()
                deleted.append(fname)
            except OSError as exc:
                raise web_server_mod.HTTPException(status_code=500, detail=f"Could not delete {fname}: {exc}")
    return {"ok": True, "deleted": deleted}

