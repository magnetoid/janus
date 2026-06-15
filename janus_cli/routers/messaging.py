from fastapi import APIRouter, HTTPException, Request, Response, WebSocket, WebSocketDisconnect
from fastapi.responses import FileResponse, HTMLResponse, JSONResponse
from pydantic import BaseModel
from typing import Any, Dict, List, Optional, Tuple, Union
import janus_cli.web_server as web_server_mod

router = APIRouter()

@router.post("/api/messaging/telegram/onboarding/start")
async def start_telegram_onboarding(body: web_server_mod.TelegramOnboardingStart):
    bot_name = (body.bot_name or "Janus").strip() or "Janus"
    payload = await web_server_mod._telegram_onboarding_request(
        "POST",
        "/v1/telegram/pairings",
        body={"bot_name": bot_name},
    )

    pairing_id = str(payload.get("pairing_id") or "").strip()
    poll_token = str(payload.get("poll_token") or "").strip()
    expires_at = str(payload.get("expires_at") or "").strip()
    deep_link = str(payload.get("deep_link") or "").strip()
    qr_payload = str(payload.get("qr_payload") or deep_link).strip()
    suggested_username = str(payload.get("suggested_username") or "").strip()
    if not pairing_id or not poll_token or not expires_at or not deep_link:
        raise web_server_mod.HTTPException(
            status_code=502,
            detail="Telegram setup service returned an incomplete response.",
        )

    with web_server_mod._telegram_onboarding_lock:
        web_server_mod._prune_telegram_onboarding_pairings()
        web_server_mod._telegram_onboarding_pairings[pairing_id] = web_server_mod._TelegramOnboardingPairing(
            poll_token=poll_token,
            expires_at=expires_at,
            expires_at_ts=web_server_mod._parse_expiry_ts(expires_at),
        )

    return {
        "pairing_id": pairing_id,
        "suggested_username": suggested_username,
        "deep_link": deep_link,
        "qr_payload": qr_payload,
        "expires_at": expires_at,
    }

@router.get("/api/messaging/telegram/onboarding/{pairing_id}")
async def get_telegram_onboarding_status(pairing_id: str):
    with web_server_mod._telegram_onboarding_lock:
        web_server_mod._prune_telegram_onboarding_pairings()
        record = web_server_mod._telegram_onboarding_pairings.get(pairing_id)
        if not record:
            raise web_server_mod.HTTPException(
                status_code=404,
                detail="Telegram setup session was not found. Start a new setup.",
            )
        if record.bot_token:
            return {
                "status": "ready",
                "bot_username": record.bot_username,
                "owner_user_id": record.owner_user_id,
                "expires_at": record.expires_at,
            }
        poll_token = record.poll_token

    payload = await web_server_mod._telegram_onboarding_request(
        "GET",
        f"/v1/telegram/pairings/{web_server_mod.urllib.parse.quote(pairing_id, safe='')}",
        bearer_token=poll_token,
    )
    status = str(payload.get("status") or "").strip()
    if status == "waiting":
        with web_server_mod._telegram_onboarding_lock:
            current = web_server_mod._telegram_onboarding_pairings.get(pairing_id)
            expires_at = current.expires_at if current else ""
        return {"status": "waiting", "expires_at": expires_at}

    if status == "ready":
        bot_token = str(payload.get("token") or "").strip()
        bot_username = str(payload.get("bot_username") or "").strip()
        if not bot_token:
            raise web_server_mod.HTTPException(
                status_code=502,
                detail="Telegram setup service returned an incomplete response.",
            )
        owner_user_id = web_server_mod._normalize_telegram_user_id(payload.get("owner_user_id"))
        with web_server_mod._telegram_onboarding_lock:
            record = web_server_mod._telegram_onboarding_pairings.get(pairing_id)
            if not record:
                raise web_server_mod.HTTPException(
                    status_code=404,
                    detail="Telegram setup session was not found. Start a new setup.",
                )
            record.bot_token = bot_token
            record.bot_username = bot_username or None
            record.owner_user_id = owner_user_id
            return {
                "status": "ready",
                "bot_username": record.bot_username,
                "owner_user_id": record.owner_user_id,
                "expires_at": record.expires_at,
            }

    if status in {"expired", "claimed"}:
        with web_server_mod._telegram_onboarding_lock:
            web_server_mod._telegram_onboarding_pairings.pop(pairing_id, None)
        raise web_server_mod.HTTPException(
            status_code=410,
            detail=web_server_mod._telegram_onboarding_error_message(
                status,
                "Telegram setup is no longer available. Start a new setup.",
            ),
        )

    raise web_server_mod.HTTPException(
        status_code=502,
        detail="Telegram setup service returned an unknown status.",
    )

@router.post("/api/messaging/telegram/onboarding/{pairing_id}/apply")
async def apply_telegram_onboarding(
    pairing_id: str, body: web_server_mod.TelegramOnboardingApply
):
    allowed_user_ids = []
    seen = set()
    for raw_id in body.allowed_user_ids:
        normalized = web_server_mod._normalize_telegram_user_id(raw_id)
        if not normalized:
            raise web_server_mod.HTTPException(
                status_code=400,
                detail="Allowed Telegram user IDs must be numeric.",
            )
        if normalized not in seen:
            seen.add(normalized)
            allowed_user_ids.append(normalized)
    if not allowed_user_ids:
        raise web_server_mod.HTTPException(
            status_code=400,
            detail="Add at least one allowed Telegram user ID.",
        )

    with web_server_mod._telegram_onboarding_lock:
        web_server_mod._prune_telegram_onboarding_pairings()
        record = web_server_mod._telegram_onboarding_pairings.get(pairing_id)
        if not record:
            raise web_server_mod.HTTPException(
                status_code=404,
                detail="Telegram setup session was not found. Start a new setup.",
            )
        bot_token = record.bot_token
        bot_username = record.bot_username
        if not bot_token:
            raise web_server_mod.HTTPException(
                status_code=409,
                detail="Telegram setup is not ready yet.",
            )

    try:
        web_server_mod.save_env_value("TELEGRAM_BOT_TOKEN", bot_token)
        web_server_mod.save_env_value("TELEGRAM_ALLOWED_USERS", ",".join(allowed_user_ids))
        web_server_mod._write_platform_enabled("telegram", True)
    except ValueError as exc:
        raise web_server_mod.HTTPException(status_code=400, detail=str(exc)) from exc
    except Exception as exc:
        web_server_mod._log.exception("Telegram onboarding apply failed")
        raise web_server_mod.HTTPException(
            status_code=500,
            detail="Failed to save Telegram setup.",
        ) from exc

    with web_server_mod._telegram_onboarding_lock:
        web_server_mod._telegram_onboarding_pairings.pop(pairing_id, None)

    return {
        "ok": True,
        "platform": "telegram",
        "bot_username": bot_username,
        "needs_restart": True,
    }

@router.delete("/api/messaging/telegram/onboarding/{pairing_id}")
async def cancel_telegram_onboarding(pairing_id: str):
    with web_server_mod._telegram_onboarding_lock:
        web_server_mod._telegram_onboarding_pairings.pop(pairing_id, None)
    return {"ok": True}

@router.get("/api/messaging/platforms")
async def get_messaging_platforms():
    env_on_disk = web_server_mod.load_env()
    runtime = web_server_mod.read_runtime_status()
    return {
        "platforms": [
            web_server_mod._messaging_platform_payload(entry, env_on_disk, runtime)
            for entry in web_server_mod._messaging_platform_catalog()
        ]
    }

@router.put("/api/messaging/platforms/{platform_id}")
async def update_messaging_platform(platform_id: str, body: web_server_mod.MessagingPlatformUpdate):
    entry = web_server_mod._catalog_lookup(platform_id)
    if not entry:
        raise web_server_mod.HTTPException(
            status_code=404, detail=f"Unknown messaging platform: {platform_id}"
        )

    allowed_env = set(entry["env_vars"])
    try:
        for key in body.clear_env:
            if key not in allowed_env:
                raise web_server_mod.HTTPException(
                    status_code=400,
                    detail=f"{key} is not configurable for {entry['name']}",
                )
            web_server_mod.remove_env_value(key)

        for key, value in body.env.items():
            if key not in allowed_env:
                raise web_server_mod.HTTPException(
                    status_code=400,
                    detail=f"{key} is not configurable for {entry['name']}",
                )
            trimmed = value.strip()
            if trimmed:
                web_server_mod.save_env_value(key, trimmed)

        if body.enabled is not None:
            web_server_mod._write_platform_enabled(platform_id, body.enabled)

        return {"ok": True, "platform": platform_id}
    except web_server_mod.HTTPException:
        raise
    except Exception:
        web_server_mod._log.exception("PUT /api/messaging/platforms/%s failed", platform_id)
        raise web_server_mod.HTTPException(status_code=500, detail="Internal server error")

@router.post("/api/messaging/platforms/{platform_id}/test")
async def test_messaging_platform(platform_id: str):
    entry = web_server_mod._catalog_lookup(platform_id)
    if not entry:
        raise web_server_mod.HTTPException(
            status_code=404, detail=f"Unknown messaging platform: {platform_id}"
        )

    env_on_disk = web_server_mod.load_env()
    payload = web_server_mod._messaging_platform_payload(entry, env_on_disk, web_server_mod.read_runtime_status())
    if not payload["enabled"]:
        message = f"{entry['name']} is disabled. Enable it, then restart the gateway."
        return {"ok": False, "state": payload["state"], "message": message}
    if not payload["configured"]:
        missing = [
            field["key"]
            for field in payload["env_vars"]
            if field["required"] and not field["is_set"]
        ]
        message = (
            f"Missing required setup: {', '.join(missing)}"
            if missing
            else "Platform setup is incomplete."
        )
        return {"ok": False, "state": payload["state"], "message": message}
    if not payload["gateway_running"]:
        return {
            "ok": False,
            "state": payload["state"],
            "message": "Gateway is not running. Restart the gateway to connect this platform.",
        }
    if payload["state"] == "connected":
        return {
            "ok": True,
            "state": payload["state"],
            "message": f"{entry['name']} is connected.",
        }
    if payload.get("error_message"):
        return {
            "ok": False,
            "state": payload["state"],
            "message": payload["error_message"],
        }
    return {
        "ok": False,
        "state": payload["state"],
        "message": "Setup looks complete, but the gateway has not reported a connection yet. Restart the gateway.",
    }

