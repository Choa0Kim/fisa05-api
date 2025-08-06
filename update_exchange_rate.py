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

# 2) README.md 업데이트
start_tag = "<!-- EXCHANGE_RATE_START -->"
end_tag = "<!-- EXCHANGE_RATE_END -->"
new_content = f"\n**USD → KRW:** {krw_rate} (업데이트: {timestamp})\n"

readme_path = "README.md"
with open(readme_path, "r", encoding="utf-8") as f:
    content = f.read()

start_index = content.find(start_tag) + len(start_tag)
end_index = content.find(end_tag)

if start_index != -1 and end_index != -1:
    updated_content = content[:start_index] + new_content + content[end_index:]
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(updated_content)

print(f"[{timestamp}] USD → KRW = {krw_rate} (README.md 업데이트 완료)")

