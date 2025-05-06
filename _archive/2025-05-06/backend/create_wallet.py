from solana.keypair import Keypair
import base58
import json

# יצירת ארנק חדש
new_wallet = Keypair()

# קידוד המפתח הפרטי
private_key = base58.b58encode(new_wallet.secret_key).decode('utf-8')
public_key = str(new_wallet.public_key)

# הדפסת מפתחות למסך
print("Public Key:", public_key)
print("Private Key:", private_key)

# שמירה לקובץ wallet.json
wallet_data = {
    "public_key": public_key,
    "private_key": private_key
}

with open('wallet.json', 'w', encoding='utf-8') as f:
    json.dump(wallet_data, f, indent=4)

print("\nWallet saved successfully to wallet.json!")
