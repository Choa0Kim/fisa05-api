import requests
from datetime import datetime
import json

# 현재 시각에서 '분' 추출 후 +1
minute = datetime.now().minute
next_minute = (minute + 1) % 60  # 0~59 범위 유지
url = f"https://jsonplaceholder.typicode.com/todos/{next_minute}"

# API 호출
test = requests.get(url)
data = test.json()

# /tmp/test.json에 저장
with open("/tmp/test.json", "w") as f:
    json.dump(data, f, indent=2)

