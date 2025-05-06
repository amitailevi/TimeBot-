import webbrowser
from flask import Flask, jsonify
from flask_cors import CORS
from real_swap import execute_swap
import os
import json

file_path = os.path.abspath('frontend/dashboard.html')
webbrowser.open(f'file://{file_path}')

app = Flask(__name__)
CORS(app)

def get_wallet_address():
    with open('wallet.json', 'r') as f:
        wallet = json.load(f)
    return wallet['public_key']

@app.route("/status")
def status():
    return jsonify({
        "status": "מוכן ✅",
        "sol": 2.34,
        "semd": 5430,
        "last_tx": "טרם בוצע"
    })

@app.route("/run-bot")
def run_bot():
    try:
        tx_signature = execute_swap()
        return jsonify({"success": True, "tx": tx_signature})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)})

if __name__ == "__main__":
    app.run(debug=True) 