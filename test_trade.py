import requests

url = "http://127.0.0.1:5000/trade"
payload = {
    "action": "buy",
    "side": "long",
    "symbol": "WIFUSDT",
    "price": 0.00000123
}

response = requests.post(url, json=payload)
print("Status Code:", response.status_code)
print("Response:", response.json())
