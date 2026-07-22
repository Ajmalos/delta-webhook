from flask import Flask, request, jsonify
import os
import time
import json
import hmac
import hashlib
import requests
app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "CoinDCX Futures Webhook Running"

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json

    print("Webhook received:")
    print(data)

    api_key = os.getenv("COINDCX_API_KEY")
    api_secret = os.getenv("COINDCX_API_SECRET")
    ORDER_URL = "https://api.coindcx.com/exchange/v1/derivatives/futures/orders/create"

    if not api_key or not api_secret:
        return jsonify({
            "status": "error",
            "message": "API keys not found"
        }), 500

    return jsonify({
        "status": "success",
        "received": data
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
