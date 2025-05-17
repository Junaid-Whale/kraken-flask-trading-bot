# Kraken Flask Trading Bot 🤖

This is an **automated crypto trading bot** built with Flask that connects **TradingView alerts** to execute **3x leverage spot margin trades on Kraken**.

It runs 24/7 in the cloud and supports:
- 🚀 Entry via TradingView MA/MACD/EMA signals
- 🔁 Exit with Trailing Stop Loss or Reversal Detection
- 📡 Flask webhook endpoint for real-time trade automation
- ☁️ Cloud-ready for deployment on services like Render

---

## 🔧 Features

- Python + Flask backend for webhook listening
- Secure Kraken Spot Margin API integration
- Reversal detection logic
- Environment variable protection
- Ready for Docker or Render deployment

---

## 🧪 How to Run Locally

1. Clone the repo:
   ```bash
   git clone https://github.com/Junaid-Whale/kraken-flask-trading-bot-.git
   cd kraken-flask-trading-bot-
