from flask import Flask, request, jsonify, render_template

from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/emotionDetector', methods=['POST'])
def emotion_detector():
    data = request.json
    statement = data.get('statement')
    
    if not statement:
        return jsonify({"error": "No statement provided"}), 400
    
    emotions = detect_emotions(statement)
    dominant_emotion = max(emotions, key=emotions.get)
    
    response = {
        "anger": emotions.get("anger", 0),
        "disgust": emotions.get("disgust", 0),
        "fear": emotions.get("fear", 0),
        "joy": emotions.get("joy", 0),
        "sadness": emotions.get("sadness", 0),
        "dominant_emotion": dominant_emotion
    }
    
    formatted_response = (
        f"For the given statement, the system response is 'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, 'fear': {response['fear']}, 'joy': {response['joy']} "
        f"and 'sadness': {response['sadness']}. The dominant emotion is {response['dominant_emotion']}."
    )
    
    return jsonify({"response": formatted_response})

if __name__ == '__main__':
    app.run(host='localhost', port=5000)