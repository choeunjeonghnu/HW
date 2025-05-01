import requests
import time

# 라즈베리파이 IP 또는 localhost
SERVER_URL = "http://192.168.0.52:5001/receive_emotion"

emotions = ["happy", "anxious", "neutral"]

for emotion in emotions:
    print(f"[전송 중] 감정: {emotion}")
    response = requests.post(SERVER_URL, json={"emotion": emotion})

    if response.status_code == 200:
        print(f"[응답 완료] {response.json()}")
    else:
        print(f"[에러] 상태코드: {response.status_code}, 응답: {response.text}")

    time.sleep(5)
