from flask import Flask, request, jsonify
from kraken_trader import place_order  # ✅ Add this

app = Flask(__name__)

@app.route('/')
def home():
    return "🚀 Kraken Flask Trading Bot is Running!"

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    symbol = data.get('symbol')
    action = data.get('action')

    if not symbol or not action:
        return jsonify({"error": "Missing 'symbol' or 'action'"}), 400

    result = place_order(symbol.upper(), action.lower())
    return jsonify({"status": "executed", "kraken_response": result})

if __name__ == '__main__':
    app.run(debug=True)
