from evdev import InputDevice, ecodes
import time
import select
import sys
from motor_en import motor_control

# 블루투스 버튼 디바이스 경로
DEVICE_PATH = "/dev/input/event2"

# 장치 열기
try:
    dev = InputDevice(DEVICE_PATH)
    print("장치 연결 완료")
except FileNotFoundError:
    print(f"장치 {DEVICE_PATH} 를 찾을 수 없습니다. 연결 확인 요망.")
    sys.exit(1)

# False = 대기 상태, True = 음성 듣기 중
state = False 
last_event_time = 0
delay = 0.5  # 0.5초 내 중복 입력 무시

while True:
    # 버튼 이벤트가 들어올 때까지 대기
    r, _, _ = select.select([dev], [], [])

    for source in r:
        try:
            event = dev.read_one()
        except OSError:
            print("장치 오류: 연결 끊김 또는 제거")
            sys.exit(1)

        if event and event.type == ecodes.EV_KEY and event.code == ecodes.KEY_VOLUMEUP and event.value == 1:
            now = time.time()
            if now - last_event_time < delay:
                continue
            last_event_time = now
            state = not state

            if state:
                motor_control(True)
                #음성 듣는 함수 불러오기
                print("음성 듣는 중")

            else:
                motor_control(False)
                #음성 듣기 중지 + 음성->텍스트 변환 함수 불러오기
                print("음성 듣기 중지")

