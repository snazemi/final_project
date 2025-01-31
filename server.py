from flask import Flask, request, jsonify, render_template

from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/emotionDetector')
def emotion_detector():
    statement = request.args.get('textToAnalyze')
    
    if not statement:
        return jsonify({"error": "No statement provided"}), 400
    
    print(statement)
    emotions = emotion_detector(statement)
    dominant_emotion = emotions["dominant_emotion"]
    
    
    formatted_response = (
        f"For the given statement, the system response is 'anger': {emotions['anger']}, "
        f"'disgust': {emotions['disgust']}, 'fear': {emotions['fear']}, 'joy': {emotions['joy']} "
        f"and 'sadness': {emotions['sadness']}. The dominant emotion is {emotions['dominant_emotion']}."
    )
    
    return (formatted_response)

if __name__ == '__main__':
    app.run(host='localhost', port=5000)