---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# optional-skills/productivity/telephony/scripts/telephony.py

Symbols in `optional-skills/productivity/telephony/scripts/telephony.py`.

- L59 `TelephonyError` (class) — Domain-specific failure surfaced to the skill/user.
- L64 `OwnedTwilioNumber` (class)
- L71 `_hermes_home()` (function)
- L75 `_env_path()` (function)
- L79 `_config_path()` (function)
- L83 `_state_path()` (function)
- L87 `_load_root_config()` (function)
- L103 `_config_lookup(*paths: tuple[str, ...], default: str='')` (function)
- L117 `_load_dotenv_values(path: Path | None=None)` (function)
- L135 `_env_or_config(env_key: str, *config_paths: tuple[str, ...], default: str='')` (function)
- L145 `_load_state(path: Path | None=None)` (function)
- L159 `_save_state(state: dict[str, Any], path: Path | None=None)` (function)
- L166 `_quote_env_value(value: str)` (function)
- L173 `_upsert_env_file(updates: dict[str, str], env_path: Path | None=None)` (function)
- L206 `_normalize_phone(number: str)` (function)
- L220 `_mask_phone(number: str)` (function)
- L227 `_parse_twilio_date(value: str | None)` (function)
- L237 `_json_request(method: str, url: str, *, headers: dict[str, str] | None=None, params: dict[str, Any] | None=None, form: dict[str, Any] | None=None, json_body: dict[str, Any] | None=None)` (function)
- L275 `_twilio_creds()` (function)
- L294 `_twilio_basic_headers()` (function)
- L300 `_twilio_request(method: str, path: str, *, params=None, form=None)` (function)
- L311 `_twilio_owned_numbers(limit: int=50)` (function)
- L330 `_remember_twilio_number(*, phone_number: str, phone_sid: str='', save_env: bool=False, state_path: Path | None=None, env_path: Path | None=None)` (function)
- L359 `_remember_vapi_number(*, phone_number_id: str, save_env: bool=False, state_path: Path | None=None, env_path: Path | None=None)` (function)
- L382 `_resolve_twilio_number(identifier: str | None=None)` (function)
- L427 `_vapi_api_key()` (function)
- L435 `_vapi_phone_number_id()` (function)
- L446 `_bland_api_key()` (function)
- L454 `_ai_provider(default: str=DEFAULT_AI_PROVIDER)` (function)
- L463 `_twilio_search_numbers(*, country: str='US', area_code: str | None=None, contains: str | None=None, limit: int=10, sms_enabled: bool=True, voice_enabled: bool=True)` (function)
- L512 `_twilio_buy_number(phone_number: str, *, save_env: bool=False, state_path: Path | None=None, env_path: Path | None=None)` (function)
- L542 `_twilio_list_owned()` (function)
- L560 `_twilio_set_default(identifier: str, *, save_env: bool=False)` (function)
- L579 `_twiml_say(message: str, voice: str)` (function)
- L583 `_twiml_play(audio_url: str)` (function)
- L587 `_twilio_call(to_number: str, *, message: str | None=None, audio_url: str | None=None, voice: str=TWILIO_DEFAULT_TTS_VOICE, send_digits: str | None=None, from_identifier: str | None=None, record: bool=False)` (function)
- L627 `_twilio_call_status(call_sid: str)` (function)
- L644 `_twilio_send_sms(to_number: str, body: str, *, media_urls: list[str] | None=None, from_identifier: str | None=None)` (function)
- L675 `_checkpoint_for_messages(messages: list[dict[str, Any]])` (function)
- L682 `_messages_after_checkpoint(messages: list[dict[str, Any]], last_sid: str)` (function)
- L693 `_twilio_inbox(*, limit: int=20, since_last: bool=False, mark_seen: bool=False, phone_identifier: str | None=None, state_path: Path | None=None)` (function)
- L749 `_vapi_import_twilio_number(*, phone_identifier: str | None=None, save_env: bool=False, state_path: Path | None=None, env_path: Path | None=None)` (function)
- L795 `_bland_call(phone_number: str, task: str, *, voice: str | None=None, first_sentence: str | None=None, max_duration: int=3)` (function)
- L845 `_bland_status(call_id: str, analyze: str | None=None)` (function)
- L873 `_vapi_call(phone_number: str, task: str, *, voice_id: str | None=None, first_sentence: str | None=None, max_duration: int=3)` (function)
- L948 `_vapi_status(call_id: str)` (function)
- L971 `_provider_decision_tree()` (function)
- L996 `diagnose()` (function)
- L1079 `save_twilio(account_sid: str, auth_token: str, phone_number: str='', phone_sid: str='')` (function)
- L1101 `save_bland(api_key: str, voice: str=BLAND_DEFAULT_VOICE)` (function)
- L1118 `save_vapi(api_key: str, *, phone_number_id: str='', voice_provider: str=VAPI_DEFAULT_VOICE_PROVIDER, voice_id: str=VAPI_DEFAULT_VOICE_ID, model: str=VAPI_DEFAULT_MODEL)` (function)
- L1148 `_build_parser()` (function)
- L1233 `_dispatch(args: argparse.Namespace)` (function)
- L1330 `main(argv: list[str] | None=None)` (function)
