---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# optional-skills/blockchain/evm/scripts/evm_client.py

Symbols in `optional-skills/blockchain/evm/scripts/evm_client.py`.

- L236 `hex_to_int(h: str)` (function)
- L246 `is_valid_address(s: str)` (function) — Return True if `s` looks like a 20-byte hex Ethereum address.
- L265 `is_valid_txhash(s: str)` (function) — Return True if `s` looks like a 32-byte hex transaction hash.
- L280 `require_address(s: str, *, field: str='address')` (function) — Return `s` lowercased if valid, else exit with an error message.
- L294 `require_txhash(s: str, *, field: str='tx hash')` (function) — Return `s` lowercased if valid, else exit with an error message.
- L304 `wei_to_native(wei: int, decimals: int=18)` (function)
- L308 `gwei_from_wei(wei: int)` (function)
- L311 `_short_addr(addr: str)` (function)
- L316 `print_json(data: Any)` (function)
- L323 `_http_post(url: str, payload: Any, retries: int=5, timeout: int=20)` (function)
- L356 `_http_get(url: str, retries: int=5, timeout: int=20)` (function)
- L388 `get_rpc_url(chain: str)` (function)
- L397 `rpc_call(chain: str, method: str, params: List[Any], req_id: int=1)` (function)
- L405 `rpc_batch(chain: str, calls: List[Tuple[str, List[Any]]], batch_limit: int=10)` (function) — Send a batch of JSON-RPC calls; returns list of results in same order.
- L440 `_encode_address(addr: str)` (function) — Pad address to 32 bytes.
- L444 `_keccak256(data: bytes)` (function) — Pure Python Keccak-256 (Ethereum's hash, NOT SHA3-256).
- L493 `_selector(sig: str)` (function) — Compute 4-byte function selector via keccak-256.
- L506 `eth_call_erc20(chain: str, contract: str, fn: str, arg_addr: Optional[str]=None)` (function)
- L514 `decode_string(hex_data: str)` (function) — Decode ABI-encoded string from eth_call result.
- L529 `decode_uint256(hex_data: str)` (function)
- L538 `decode_uint8(hex_data: str)` (function)
- L547 `cg_price_by_id(cg_id: str)` (function)
- L555 `cg_price_by_ids(cg_ids: List[str])` (function) — Fetch multiple prices in one request.
- L567 `cg_price_by_contract(chain: str, contract: str)` (function)
- L595 `get_native_price(chain: str)` (function)
- L603 `cmd_stats(args: argparse.Namespace)` (function)
- L645 `cmd_wallet(args: argparse.Namespace)` (function)
- L722 `cmd_tx(args: argparse.Namespace)` (function)
- L791 `cmd_token(args: argparse.Namespace)` (function)
- L833 `cmd_activity(args: argparse.Namespace)` (function)
- L889 `cmd_gas(args: argparse.Namespace)` (function)
- L920 `cmd_price(args: argparse.Namespace)` (function)
- L958 `_fetch_chain_stats(chain: str)` (function) — Fetch gas price + native price for a single chain (used in compare).
- L986 `cmd_compare(_args: argparse.Namespace)` (function) — Compare gas prices and native token prices across all chains simultaneously.
- L1022 `cmd_whale(args: argparse.Namespace)` (function)
- L1086 `cmd_multichain(args: argparse.Namespace)` (function) — Scan same wallet across all 8 chains simultaneously.
- L1156 `cmd_allowance(args: argparse.Namespace)` (function) — Check dangerous ERC-20 approvals for a wallet (known spenders).
- L1216 `cmd_decode(args: argparse.Namespace)` (function) — Decode transaction input data using 4byte.directory.
- L1274 `cmd_ens(args: argparse.Namespace)` (function) — Resolve ENS name <-> address via ensideas.com public API (no key needed).
- L1301 `cmd_contract(args: argparse.Namespace)` (function) — Inspect a smart contract: bytecode size, proxy detection, creation info.
- L1379 `build_parser()` (function)
- L1483 `main()` (function)
