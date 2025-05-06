from solana.rpc.api import Client
from solana.publickey import PublicKey

client = Client("https://api.mainnet-beta.solana.com")
print("RPC ping OK:", client.is_connected())

key = PublicKey("11111111111111111111111111111111")  # Sysvar
print("PublicKey OK:", key) 