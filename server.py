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
        emotions = {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
        returning_status = 400
    else:    
        emotions = emotion_detector(statement)
        returning_status = 200
    
    formatted_response = (
        f"For the given statement, the system response is:"
        f"<br />'anger': {emotions['anger']}, <br />"
        f"'disgust': {emotions['disgust']}, <br />"
        f"'fear': {emotions['fear']}, <br />"
        f"'joy': {emotions['joy']} <br />"
        f"and 'sadness': {emotions['sadness']}. <br />"
        f"The dominant emotion is <b>{emotions['dominant_emotion']}</b>."
    )

    return (formatted_response, returning_status)

if __name__ == '__main__':
    app.run(host='localhost', port=5050)