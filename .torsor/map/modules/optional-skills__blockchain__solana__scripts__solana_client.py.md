---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# optional-skills/blockchain/solana/scripts/solana_client.py

Symbols in `optional-skills/blockchain/solana/scripts/solana_client.py`.

- L74 `_http_get_json(url: str, timeout: int=10, retries: int=2)` (function) — GET JSON from a URL with retry on 429 rate-limit. Returns parsed JSON or None.
- L93 `_rpc_call(method: str, params: list=None, retries: int=2)` (function) — Send a JSON-RPC request with retry on 429 rate-limit.
- L131 `rpc_batch(calls: list)` (function) — Send a batch of JSON-RPC requests (with retry on 429).
- L156 `lamports_to_sol(lamports: int)` (function)
- L160 `print_json(obj: Any)` (function)
- L164 `_short_mint(mint: str)` (function) — Abbreviate a mint address for display: first 4 + last 4.
- L175 `fetch_prices(mints: List[str], max_lookups: int=20)` (function) — Fetch USD prices for mint addresses via CoinGecko (one per request).
- L200 `fetch_sol_price()` (function) — Fetch current SOL price in USD via CoinGecko.
- L210 `resolve_token_name(mint: str)` (function) — Look up token name and symbol from CoinGecko by mint address.
- L225 `_token_label(mint: str)` (function) — Return a human-readable label for a mint: symbol if known, else abbreviated address.
- L236 `cmd_stats(_args)` (function) — Live Solana network: slot, epoch, TPS, supply, version, SOL price.
- L284 `cmd_wallet(args)` (function) — SOL balance + SPL token holdings with USD values.
- L396 `cmd_tx(args)` (function) — Full transaction details by signature.
- L451 `cmd_token(args)` (function) — SPL token metadata, supply, decimals, price, top holders.
- L499 `cmd_activity(args)` (function) — Recent transaction signatures for an address.
- L521 `cmd_nft(args)` (function) — NFTs owned by a wallet (amount=1 && decimals=0 heuristic).
- L548 `cmd_whales(args)` (function) — Scan the latest block for large SOL transfers.
- L614 `cmd_price(args)` (function) — Quick price lookup for a token by mint address or known symbol.
- L643 `main()` (function)
