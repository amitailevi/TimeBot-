from solana.rpc.api    import Client
from solana.publickey  import PublicKey
from solana.rpc.types  import TokenAccountOpts
from check_balance import get_wallet_balance
from check_semd_balance import get_semd_balance
from check_pool_balance import get_pool_balance

#–––– CONFIG ––––
RPC_URL           = "https://api.mainnet-beta.solana.com"
BOT_WALLET        = "9moqeCc6bcgMwebTAJucTVwehFBf94tiFG169soSfmF4"
SEMD_MINT_ADDRESS = "J9DuBB7AFtjwiX2nJbZ1DwHhpnoDBvFtzc8KLscB5Bq1"
POOL_ADDRESS      = "Emc6UyFghkRpuXbfqc6TeRuLpU9ZsZT7ypPj1XqpVkEM"

#–––– SETUP ––––
client     = Client(RPC_URL)
wallet_pk  = PublicKey(BOT_WALLET)
mint_pk    = PublicKey(SEMD_MINT_ADDRESS)
pool_pk    = PublicKey(POOL_ADDRESS)

#–––– HELPERS ––––
def get_wallet_balance(pubkey: PublicKey) -> float:
    """מחזיר את יתרת ה-SOL ב-PUBLIC KEY (כעשרוני)."""
    resp = client.get_balance(pubkey)
    # כאן השתנו הקריאות: עכשיו משתמשים ב-.value
    return resp.value / 1_000_000_000

def get_semd_balance(pubkey: PublicKey) -> float:
    """מחזיר סך כל מטבעות SEMD בארנק."""
    opts = TokenAccountOpts(mint=mint_pk, encoding="jsonParsed")
    resp = client.get_token_accounts_by_owner(pubkey, opts)
    accounts = resp.value
    return sum(
        acc["account"]["data"]["parsed"]["info"]["tokenAmount"]["uiAmount"]
        for acc in accounts
    )

def get_pool_balance(pubkey: PublicKey) -> float:
    """מחזיר את יתרת ה-SOL בבריכה."""
    resp = client.get_balance(pubkey)
    return resp.value / 1_000_000_000

#–––– MAIN STATUS CHECK ––––
def main():
    print("🔎 Checking wallet and token balances...")

    sol_balance  = get_wallet_balance(wallet_pk)
    semd_balance = get_semd_balance(wallet_pk)
    pool_sol     = get_pool_balance(pool_pk)

    print(f"💰 Bot SOL Balance: {sol_balance:.6f} SOL")
    print(f"💰 Bot SEMD Balance: {semd_balance:.4f} SEMD")
    print(f"💧 Pool SOL Balance: {pool_sol:.6f} SOL")

if __name__ == "__main__":
    main()
