from solana.rpc.api import Client
from solana.publickey import PublicKey
from check_balance import get_wallet_balance
from check_semd_balance import get_semd_balance
from check_pool_balance import get_pool_balance

# כתובות (שים כאן את הכתובות שלך)
wallet_pk = PublicKey("הכנס כאן את כתובת הארנק שלך")
pool_pk = PublicKey("הכנס כאן את כתובת הבריכה שלך")

def main():
    print("🔍 Checking wallet and token balances...")

    sol_balance = get_wallet_balance(wallet_pk)
    semd_balance = get_semd_balance(wallet_pk)
    pool_sol = get_pool_balance(pool_pk)

    print(f"🪙 Bot SOL Balance: {sol_balance:.6f} SOL")
    print(f"🪙 Bot SEMD Balance: {semd_balance:.4f} SEMD")
    print(f"🪙 Pool SOL Balance: {pool_sol:.6f} SOL")

if __name__ == "__main__":
    main()
