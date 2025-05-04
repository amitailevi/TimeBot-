from solana.rpc.api    import Client
from solana.publickey  import PublicKey
from solana.rpc.types  import TokenAccountOpts
import os
import webbrowser
from raydium_py import RaydiumSwap
from flask_cors import CORS

RPC_URL           = "https://api.mainnet-beta.solana.com"
WALLET_ADDRESS    = "9moqeCc6bcgMwebTAJucTVwehFBf94tiFG169soSfmF4"
SEMD_MINT_ADDRESS = "J9DuBB7AFtjwiX2nJbZ1DwHhpnoDBvFtzc8KLscB5Bq1"

client    = Client(RPC_URL)
wallet_pk = PublicKey(WALLET_ADDRESS)
mint_pk   = PublicKey(SEMD_MINT_ADDRESS)

opts = TokenAccountOpts(
    mint     = mint_pk,
    encoding = "jsonParsed",
)

# קריאה חדשה – מחזירה GetTokenAccountsByOwnerResp עם שדה .value
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

# פותח את תיקיית frontend בסייר הקבצים
os.startfile('frontend')

# הנתיב לקובץ
file_path = os.path.abspath('frontend/dashboard.html')
print(file_path)
url = f'file:///{file_path.replace(os.sep, "/")}'
chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'

try:
    webbrowser.get(chrome_path).open(url)
except Exception as e:
    print("ניסיון פתיחה בדפדפן ברירת מחדל...")
    webbrowser.open(url)

# יצירת אובייקט RaydiumSwap
swap = RaydiumSwap()

# הגדרת פרמטרים
pool_id = "Emc6UyFghkRpuXbfqc6TeRuLpU9ZsZT7ypPj1XqpVkEM"  # כתובת הבריכה של SEMD/SOL
amount_in = 0.1  # כמות SOL להמיר
slippage = 0.5   # אחוז סטייה מותרת

# ביצוע ה-Swap
tx_signature = swap.swap(
    pool_id=pool_id,
    amount_in=amount_in,
    slippage=slippage
)

print(f"Transaction Signature: {tx_signature}")

CORS(app)
