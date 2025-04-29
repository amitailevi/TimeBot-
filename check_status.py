import requests
from solana.publickey import PublicKey
from solana.rpc.api import Client

# כתובת ארנק הבוט
BOT_WALLET = "9moqeCc6bcgMwebTAJucTVwehFBf94tiFG169soSfmF4"

# כתובת טוקן SEMD
SEMD_TOKEN_ADDRESS = "J9DuBB7AFtjwiX2nJbZ1DwHhpnoDBvFtzc8KLscB5Bq1"

# חיבור לרשת הראשית של Solana
client = Client("https://api.mainnet-beta.solana.com")

def get_wallet_balance(wallet_address):
    response = client.get_balance(PublicKey(wallet_address))
    sol_balance = response['result']['value'] / 1_000_000_000  # להמיר ל-SOL
    return sol_balance

def get_token_balance(wallet_address, token_address):
    url = f"https://public-api.solscan.io/account/tokens?account={wallet_address}"
    headers = {"accept": "application/json"}
    response = requests.get(url, headers=headers)
    tokens = response.json()
    for token in tokens:
        if token['tokenAddress'] == token_address:
            return float(token['tokenAmount']['uiAmount'])
    return 0

# בדיקות
print("🔎 Checking wallet and token balances...")

# 1. בדיקת יתרת SOL בארנק
sol_balance = get_wallet_balance(BOT_WALLET)
print(f"✅ SOL Balance in bot wallet: {sol_balance} SOL")

# 2. בדיקת יתרת SEMD בארנק
semd_balance = get_token_balance(BOT_WALLET, SEMD_TOKEN_ADDRESS)
print(f"✅ SEMD Balance in bot wallet: {semd_balance} SEMD")

# 3. בדיקת יתרת SEMD בבריכה (נבנה בהמשך בדיקה יותר מדויקת לבריכה)
print("\n📢 המשך הבדיקה - נבדוק את מצב הבריכה בעוד רגע!")
