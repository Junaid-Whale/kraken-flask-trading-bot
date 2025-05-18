import os
from dotenv import load_dotenv
import requests
import time
import urllib.parse
import hashlib
import hmac
import base64

# Load API keys from .env
load_dotenv()
API_KEY = os.getenv('KRAKEN_API_KEY')
API_SECRET = os.getenv('KRAKEN_API_SECRET')

# Kraken API URLs
API_URL = "https://api.kraken.com"
API_PATH = "/0/private/Balance"

def get_kraken_signature(urlpath, data, secret):
    postdata = urllib.parse.urlencode(data)
    encoded = (str(data['nonce']) + postdata).encode()
    message = urlpath.encode() + hashlib.sha256(encoded).digest()
    mac = hmac.new(base64.b64decode(secret), message, hashlib.sha512)
    sigdigest = base64.b64encode(mac.digest())
    return sigdigest.decode()

def get_kraken_balance():
    nonce = int(1000*time.time())
    data = {
        'nonce': nonce
    }
    headers = {
        'API-Key': API_KEY,
        'API-Sign': get_kraken_signature(API_PATH, data, API_SECRET)
    }

    response = requests.post(API_URL + API_PATH, headers=headers, data=data)
    return response.json()

# Test
if __name__ == "__main__":
    print("Testing Kraken API connection...")
    result = get_kraken_balance()
    print(result)
