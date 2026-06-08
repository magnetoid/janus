---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# hermes_cli/telegram_managed_bot.py

Symbols in `hermes_cli/telegram_managed_bot.py`.

- L39 `TelegramPairing` (class) — Pairing record returned by the Telegram onboarding service.
- L51 `TelegramBotSetupResult` (class) — Successful Telegram onboarding result returned by the setup service.
- L59 `_api_url(api_url: str | None=None)` (function) — Resolve the onboarding API URL, honoring the PoC env override.
- L66 `is_valid_telegram_bot_token(token: object)` (function) — Return True when *token* has Telegram's bot-token shape.
- L71 `_parse_owner_user_id(value: object)` (function)
- L82 `render_qr_terminal(url: str)` (function) — Render a URL as a QR code string suitable for terminal output.
- L105 `print_qr_code(url: str, *, include_link: bool=True)` (function) — Print a QR code to stdout, with URL fallback if qrcode is missing.
- L116 `generate_username_slug(length: int=16)` (function) — Generate a base32-ish slug for Telegram username correlation.
- L125 `generate_bot_username(profile_name: Optional[str]=None)` (function) — Generate a secure suggested bot username like ``hermes_<slug>_bot``.
- L136 `generate_deep_link(manager_bot: str=DEFAULT_MANAGER_BOT, suggested_username: Optional[str]=None, suggested_name: Optional[str]=None)` (function) — Build a ``t.me/newbot`` deep link for managed bot creation.
- L156 `generate_pairing_nonce()` (function) — Generate a legacy-compatible random nonce string.
- L166 `create_pairing(api_url: str | None=None, bot_name: str=DEFAULT_BOT_NAME, timeout: float=10.0)` (function) — Create a Telegram onboarding pairing.
- L208 `poll_pairing_result_once(api_url: str | None, pairing: TelegramPairing, timeout: float=10.0)` (function) — Poll the onboarding service once. Returns setup metadata when ready.
- L239 `poll_pairing_once(api_url: str | None, pairing: TelegramPairing, timeout: float=10.0)` (function) — Poll the onboarding service once. Returns the token when ready.
- L249 `poll_for_setup_result(api_url: str | None, pairing: TelegramPairing, timeout: float=DEFAULT_POLL_TIMEOUT, interval: float=POLL_INTERVAL)` (function) — Poll the pairing API until setup metadata is available or timeout.
- L268 `poll_for_token(api_url: str | None, pairing: TelegramPairing, timeout: float=DEFAULT_POLL_TIMEOUT, interval: float=POLL_INTERVAL)` (function) — Poll the pairing API until the bot token is available or timeout.
- L279 `auto_setup_telegram_bot_result(api_url: str | None=None, manager_bot: str=DEFAULT_MANAGER_BOT, profile_name: Optional[str]=None, poll_timeout: float=DEFAULT_POLL_TIMEOUT)` (function) — Run the full automatic Telegram bot creation flow.
- L345 `auto_setup_telegram_bot(api_url: str | None=None, manager_bot: str=DEFAULT_MANAGER_BOT, profile_name: Optional[str]=None, poll_timeout: float=DEFAULT_POLL_TIMEOUT)` (function) — Run automatic Telegram bot creation and return only the bot token.
