import krakenex
import os
from dotenv import load_dotenv

load_dotenv()

api = krakenex.API()
api.key = os.getenv("KRAKEN_API_KEY")
api.secret = os.getenv("KRAKEN_API_SECRET")

def place_order(symbol, side, volume="100"):  # default volume
    pair = symbol + "USD"
    order_type = "buy" if side.lower() == "buy" else "sell"
    
    response = api.query_private('AddOrder', {
        'pair': pair,
        'type': order_type,
        'ordertype': 'market',
        'volume': volume,
        'leverage': 3
    })
    
    return response
