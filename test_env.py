from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv('KRAKEN_API_KEY').strip()
api_secret = os.getenv('KRAKEN_API_SECRET').strip()

print("API_KEY:", api_key)
print("API_SECRET repr:", repr(api_secret))
