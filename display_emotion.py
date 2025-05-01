import os
import time
import win32com.client

EXPRESSIONS_FOLDER = "expressions"

EXPRESSIONS = {
    "neutral": "neutral.mp4",
    "anxious": "anxious.mp4",
    "happy": "happy.mp4"
}

def show_expression(emotion):
    if emotion not in EXPRESSIONS:
        print(f"[오류] '{emotion}' 감정은 정의되어 있지 않습니다.")
        return
    
    video_path = os.path.join(EXPRESSIONS_FOLDER, EXPRESSIONS[emotion])

    if not os.path.exists(video_path):
        print(f"[오류] 동영상 파일이 존재하지 않습니다: {video_path}")
        return

    print(f"[표정 재생] 감정: {emotion} → 파일: {video_path}")

    # Windows Media Player로 동영상 재생
    wmp = win32com.client.Dispatch("WMPlayer.OCX")
    media = wmp.newMedia(video_path)
    wmp.currentPlaylist.appendItem(media)
    wmp.controls.play()

    # 동영상이 끝날 때까지 기다림
    time.sleep(2)  # 동영상 길이에 맞게 조정 가능

# 테스트
if __name__ == "__main__":
    show_expression("happy")
    time.sleep(2)
    show_expression("anxious")
    time.sleep(2)
    show_expression("neutral")
