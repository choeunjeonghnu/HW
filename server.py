from flask import Flask, request, jsonify, render_template, send_from_directory
import os

app = Flask(__name__)

EXPRESSIONS_FOLDER = "static/expressions"
EXPRESSIONS = {
    "neutral": "neutral.mp4",
    "anxious": "anxious.mp4",
    "happy": "happy.mp4"
}

# 현재 감정 상태 저장 (서버 메모리)
current_emotion = {"emotion": "neutral"}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/receive_emotion', methods=['POST'])
def receive_emotion():
    data = request.get_json()
    emotion = data.get("emotion")

    if emotion in EXPRESSIONS:
        current_emotion["emotion"] = emotion
        print(f"[감정 수신] → {emotion}")
        return jsonify({"status": "ok", "emotion": emotion})
    else:
        return jsonify({"status": "error", "message": "Unknown emotion"}), 400

@app.route('/get_emotion')
def get_emotion():
    return jsonify(current_emotion)

@app.route('/get_video/<emotion>')
def get_video(emotion):
    if emotion not in EXPRESSIONS:
        return "Emotion not found", 404
    return send_from_directory(EXPRESSIONS_FOLDER, EXPRESSIONS[emotion])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
