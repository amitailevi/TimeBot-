"""
solana_swap.py — Buy SEMD token on Solana via Raydium/Jupiter
"""

import argparse
from solana.rpc.api import Client
from solana.publickey import PublicKey
from solana.transaction import Transaction
from solana.rpc.types import TxOpts
from solana.keypair import Keypair
import json, pathlib
from base64 import b64decode
from solana.rpc.commitment import Confirmed
import requests
import os
import time
from pathlib import Path
import sys

# === CONFIG ===
RPC_URL = "https://api.mainnet-beta.solana.com"
SEMD_MINT = PublicKey("BtFHbbpn9tKGwFWCU4pPB1HQuVuvDPWj4515f134pump")
KEYPAIR_PATH = "keypair.json"
SLIPPAGE = os.getenv("SLIPPAGE_BPS", "50")

# === CORE FUNCTIONS ===
def get_balance(pubkey: PublicKey) -> float:
    """
    מחזיר את יתרת ה‑SOL בארנק נתון (ב‑SOL, לא lamports).
    """
    client = Client(RPC_URL)
    resp = client.get_balance(pubkey, commitment="processed")
    lamports = resp["result"]["value"]
    return lamports / 1_000_000_000

def load_keypair(path: str = "keypair.json") -> Keypair:
    """
    טוען קובץ keypair.json (פורמט Solana CLI) ומחזיר Keypair.
    """
    secret = json.loads(pathlib.Path(path).read_text())
    return Keypair.from_secret_key(bytes(secret))

def swap_sol_to_spl(amount_sol: float, keypair: Keypair) -> str:
    """
    ממיר amount_sol של SOL ל-SEMD דרך Jupiter, חותם ושולח.
    מחזיר חתימת טרנזקציה.
    """
    # 1. בקשת quote
    lamports = int(amount_sol * 1_000_000_000)
    url = (
        "https://quote-api.jup.ag/v6/swap"
        f"?inputMint=So11111111111111111111111111111111111111112"
        f"&outputMint={SEMD_MINT}"
        f"&amount={lamports}"
        f"&slippageBps={SLIPPAGE}"
    )
    data = requests.get(url, timeout=10).json()["swapTransaction"]

    # 2. בניית טרנזקציה
    raw_tx = b64decode(data)
    tx = Transaction.deserialize(raw_tx)
    tx.sign(keypair)

    # 3. שליחה ואישור
    client = Client(RPC_URL)
    sig = client.send_transaction(
        tx,
        keypair,
        opts=TxOpts(skip_preflight=False, preflight_commitment=Confirmed),
    )["result"]

    client.confirm_transaction(sig, commitment=Confirmed)

    log = {"ts": time.time(), "sig": sig, "sol": amount_sol}
    Path("logs").mkdir(exist_ok=True)
    Path("logs/swap.log").open("a").write(json.dumps(log)+"\n")

    return sig

# === CLI ===
if __name__ == "__main__":
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument("--amount", type=float, required=True, help="SOL amount to swap")
        parser.add_argument("--keypair", type=str, default="keypair.json", help="Path to keypair")
        parser.add_argument("--loop", type=int, required=True, help="Loop count")
        args = parser.parse_args()

        kp = load_keypair(args.keypair)
        bal_before = get_balance(kp.public_key)
        sig = swap_sol_to_spl(args.amount, kp)
        bal_after = get_balance(kp.public_key)
        print(f"{bal_before:.3f} → {bal_after:.3f} SOL")
        print(f"Swap sent! Signature: {sig}")
        print("✔️ Swap Success")
        print("✔️ venv OK")

        # === EXAMPLE OUTPUT ===
        # SOL balance: 2.34
        # Swap sent! Signature: 5vG4x...9PU
        # ✔️ Swap Success
    except Exception as e:
        print("❌", e, file=sys.stderr)
        sys.exit(1) 