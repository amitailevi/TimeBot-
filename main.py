# main.py

import json
import time
import requests
from config import RPC_URL, BUY_AMOUNT_SOL, TIME_INTERVAL_SECONDS

def load_wallet():
    with open('wallet.json') as f:
        wallet = json.load(f)
    return wallet

def print_wallet_info(wallet):
    print(f"Wallet loaded successfully!")
    print(f"Public Key: {wallet['public_key']}")

def run_bot():
    wallet = load_wallet()
    print_wallet_info(wallet)

    while True:
        print(f"Buying {BUY_AMOUNT_SOL} SOL now... (simulation)")
        # כאן בהמשך נחבר קנייה אמיתית
        time.sleep(TIME_INTERVAL_SECONDS)

if __name__ == "__main__":
    run_bot()
