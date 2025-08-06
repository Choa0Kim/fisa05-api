import requests
import json
from datetime import datetime

url = "https://open.er-api.com/v6/latest/USD"  # 인증키 필요 없음
response = requests.get(url)
data = response.json()

if "rates" not in data:
    raise Exception(f"API 응답에 'rates' 키가 없습니다. 전체 응답: {data}")

krw_rate = data["rates"]["KRW"]
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

output = {
    "timestamp": timestamp,
    "USD_KRW": krw_rate
}

with open("exchange_rate.json", "w", encoding="utf-8") as f:
    json.dump(output, f, ensure_ascii=False, indent=2)

print(f"[{timestamp}] USD → KRW = {krw_rate}")

