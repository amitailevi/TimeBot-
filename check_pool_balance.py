from solana.rpc.api   import Client
from solana.publickey import PublicKey

RPC_URL      = "https://api.mainnet-beta.solana.com"
POOL_ADDRESS = "Emc6UyFghkRpuXbfqc6TeRuLpU9ZsZT7ypPj1XqpVkEM"

# יצירת क्लיינט וכתובת הבריכה
client  = Client(RPC_URL)
pool_pk = PublicKey(POOL_ADDRESS)

# קריאה ל־get_balance ומעבר מלמפורט ל־SOL
resp       = client.get_balance(pool_pk)
lamports   = resp.value
sol_amount = lamports / 1_000_000_000

print(f"💧 Pool SOL Balance: {sol_amount} SOL")
