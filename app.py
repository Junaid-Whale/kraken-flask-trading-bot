from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# Load Kraken API keys from environment variables
api_key = os.getenv('KRAKEN_API_KEY')
api_secret = os.getenv('KRAKEN_API_SECRET')

@app.route('/')
def home():
    return "✅ Kraken Trading Bot is running!"

@app.route('/trade', methods=['POST'])
def trade():
    data = request.json
    pair = data.get("pair")
    volume = data.get("volume")
    order_type = data.get("type")
    
    print(f"📥 Received trade: {order_type} {volume} of {pair}")

    # Here, you would call your Kraken API client to place the order
    # Example (pseudocode):
    # kraken_client = KrakenAPI(api_key, api_secret)
    # result = kraken_client.place_order(pair, volume, order_type)

    # For now, just simulate success:
    return jsonify({
        "status": "success",
        "message": f"{order_type} order placed for {volume} {pair}"
    })

if __name__ == '__main__':
    app.run(debug=True)
