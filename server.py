"""
server.py file providing emotion of the input text
"""
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)


@app.route('/')
def index():
    """
    main index function
    """
    return render_template('index.html')

@app.route('/emotionDetector')
def emotion_detector_func():
    """
    emotion detector function gets the emotion of the file and displays it out
    """
    statement = request.args.get('textToAnalyze')
    emotions = emotion_detector(statement)
    if emotions["dominant_emotion"] is None:
        formatted_response = "Invalid text! Please try again!."
    else:
        formatted_response = (
            f"For the given statement, the system response is <br />"
            f"'anger': {emotions['anger']}, <br />"
            f"'disgust': {emotions['disgust']}, <br />"
            f"'fear': {emotions['fear']}, <br />"
            f"'joy': {emotions['joy']} <br />"
            f"and 'sadness': {emotions['sadness']}. <br />"
            f"The dominant emotion is <b>{emotions['dominant_emotion']}</b>."
        )
    return formatted_response

if __name__ == '__main__':
    app.run(host='localhost', port=5001)
