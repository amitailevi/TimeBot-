from solana.rpc.api    import Client
from solana.publickey  import PublicKey
from solana.rpc.types  import TokenAccountOpts

RPC_URL           = "https://api.mainnet-beta.solana.com"
WALLET_ADDRESS    = "9moqeCc6bcgMwebTAJucTVwehFBf94tiFG169soSfmF4"
SEMD_MINT_ADDRESS = "J9DuBB7AFtjwiX2nJbZ1DwHhpnoDBvFtzc8KLscB5Bq1"

# מתחברים ל־RPC
client    = Client(RPC_URL)
wallet_pk = PublicKey(WALLET_ADDRESS)
mint_pk   = PublicKey(SEMD_MINT_ADDRESS)

# בוחרים opts רשמי
opts = TokenAccountOpts(
    mint     = mint_pk,
    encoding = "jsonParsed",
)

# מבקשים את כל חשבונות ה־SEMD של הארנק
resp     = client.get_token_accounts_by_owner(wallet_pk, opts)
accounts = resp.value

if not accounts:
    print("🔎 No SEMD tokens found in this wallet.")
else:
    total = sum(
        acc["account"]["data"]["parsed"]["info"]["tokenAmount"]["uiAmount"]
        for acc in accounts
    )
    print(f"💰 SEMD balance in wallet: {total} SEMD")
