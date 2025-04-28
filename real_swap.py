import time
import json
import base58
from solana.rpc.api import Client
from solana.transaction import Transaction
from solana.keypair import Keypair
from solana.publickey import PublicKey
from solana.rpc.types import TxOpts
from spl.token.instructions import get_associated_token_address, create_associated_token_account, transfer_checked

# טעינת הארנק
with open('wallet.json', 'r') as f:
    wallet_data = json.load(f)

private_key_bytes = base58.b58decode(wallet_data["private_key"])
keypair = Keypair.from_secret_key(private_key_bytes)
wallet_public_key = str(keypair.public_key)

# חיבור לרשת סולנה
RPC_URL = "https://api.mainnet-beta.solana.com"
client = Client(RPC_URL)

# פרטי Swap
SWAP_AMOUNT_SOL = 0.001  # כמה SOL שולחים כל פעם
SEMD_MINT = PublicKey("J9DuBB7AFtjwiX2nJbZ1DwHhpnoDBvFtzc8KLscB5Bq1")  # טוקן SEMD
POOL_ADDRESS = PublicKey("Emc6UyFghkRpuXbfqc6TeRuLpU9ZsZT7ypPj1XqpVkEM")  # בריכה שלנו
RAYDIUM_SWAP_PROGRAM_ID = PublicKey("RVKd61ztZW9GdKExkx4v8mBdtFCSoxkN3aK8P2z6yDb")  # תוכנית Raydium Swap

def get_balance(public_key):
    balance = client.get_balance(PublicKey(public_key))
    return balance['result']['value'] / 1e9

def swap_sol_to_semd():
    print("🔄 Preparing real Raydium Swap transaction...")

    # יצירת טרנזקציה
    transaction = Transaction()

    # (פה בשלב הבא נוסיף יצירת הוראת Swap חכמה)

    print("🛠️ Transaction prepared (not sent yet)")

if __name__ == "__main__":
    print("🛠️ Real Swap Bot for SEMD Initialized...")
    print(f"Using Wallet: {wallet_public_key}")

    while True:
        balance = get_balance(wallet_public_key)
        print(f"Wallet Balance: {balance} SOL")

        if balance > SWAP_AMOUNT_SOL:
            swap_sol_to_semd()
        else:
            print("❗ Not enough SOL to continue swapping. Stopping bot.")
            break

        print("🕒 Waiting 60 seconds before next swap...")
        time.sleep(60)
