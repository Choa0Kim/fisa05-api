import requests
import json
from datetime import datetime

url = "https://api.exchangerate.host/latest?base=USD&symbols=KRW"
response = requests.get(url)
data = response.json()

krw_rate = data["rates"]["KRW"]
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

output = {
    "timestamp": timestamp,
    "USD_KRW": krw_rate
}

with open("exchange_rate.json", "w", encoding="utf-8") as f:
    json.dump(output, f, ensure_ascii=False, indent=2)

print(f"[{timestamp}] USD → KRW = {krw_rate}")
