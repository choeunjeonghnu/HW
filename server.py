from flask import Flask, render_template, jsonify, send_from_directory
import os
import random

app = Flask(__name__)

# mp4 파일이 존재하는 경로 설정정
EXPRESSIONS_FOLDER = "static/expressions"

# mp4 파일 감정 유형 키 값 형태
EXPRESSIONS = {
    "neutral": "neutral.mp4",
    "anxious": "anxious.mp4",
    "happy": "happy.mp4"
}

# root 페이지에서 index.html 출력
@app.route('/')
def index():
    return render_template('index.html')

# get_emotion URL 요청을 받았을 때 수행
@app.route('/get_emotion')
def get_emotion():
    # mp4 파일 감정 유형 키를 가져온 후 랜덤하게 emotion 변수에 저장
    # 해당 변수를 json 형태로 반환
    emotions = list(EXPRESSIONS.keys())
    emotion = random.choice(emotions)
    return jsonify({"emotion": emotion})

# get_video/감정종류 URL 요청을 받았을 때 수행
# <emotion>은 URL 파라미터를 가져오는 방식
@app.route('/get_video/<emotion>')
def get_video(emotion):
    if emotion not in EXPRESSIONS:
        return "Emotion not found", 404
    
    video_path = os.path.join(EXPRESSIONS_FOLDER, EXPRESSIONS[emotion])
    if not os.path.exists(video_path):
        return "Video not found", 404
    
    # 동영상을 클라이언트에 반환
    return send_from_directory(EXPRESSIONS_FOLDER, EXPRESSIONS[emotion])

if __name__ == '__main__':
    app.run(port=5001, debug=True)
