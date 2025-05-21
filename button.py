from evdev import InputDevice, ecodes
import select
import sys
from motor import motor_control

# 블루투스 버튼 디바이스 경로
DEVICE_PATH = "/dev/input/event3"

# 장치 열기
try:
    dev = InputDevice(DEVICE_PATH)
    print("장치 연결 완료")
except FileNotFoundError:
    print(f"장치 {DEVICE_PATH} 를 찾을 수 없습니다. 연결 확인 요망.")
    sys.exit(1)

# False = 대기 상태, True = 음성 듣기 중
state = False 

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
            if not state:
                state = True
                motor_control(True)
                #음성 듣는 함수 불러오기

            else:
                state = False
                motor_control(False)
                #음성 듣기 중지 + 음성->텍스트 변환 함수 불러오기

