import json
import time
from datetime import datetime

# פונקציה לטעינת הארנק
def load_wallet():
    with open('wallet.json', 'r', encoding='utf-8') as f:
        wallet = json.load(f)
    return wallet

# פונקציה לשמירת לוג
def save_log(message):
    with open('swap_log.txt', 'a', encoding='utf-8') as f:
        f.write(f"{datetime.now()} - {message}\n")

# פונקציית הרצת הבוט
def run_bot():
    try:
        wallet = load_wallet()
        public_key = wallet.get("public_key", "Unknown")

        print("Swap Bot for SEMD initialized...")
        print(f"Using Wallet: {public_key}")
        save_log("Bot started successfully.")

        while True:
            print("Performing simulated swap: 0.001 SOL -> SEMD")
            save_log("Simulated swap: 0.001 SOL -> SEMD")
            time.sleep(60)  # לחכות 60 שניות

    except Exception as e:
        print(f"Error: {e}")
        save_log(f"Error occurred: {e}")

# נקודת התחלה
if __name__ == "__main__":
    run_bot()