from flask import Flask, request, jsonify, render_template

from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/emotionDetector')
def emotion_detector_func():
    statement = request.args.get('textToAnalyze')
    
    if not statement:
        return ("No statement provided", 400)
    
    print(statement)
    emotions = emotion_detector(statement)
    dominant_emotion = emotions["dominant_emotion"]
    
    
    formatted_response = (
        f"For the given statement, the system response is <br />'anger': {emotions['anger']}, <br />"
        f"'disgust': {emotions['disgust']}, <br />'fear': {emotions['fear']}, <br />'joy': {emotions['joy']} <br />"
        f"and 'sadness': {emotions['sadness']}. <br />The dominant emotion is <b>{emotions['dominant_emotion']}</b>."
    )
    
    return (formatted_response)

if __name__ == '__main__':
    app.run(host='localhost', port=5000)