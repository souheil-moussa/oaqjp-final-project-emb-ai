from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")
@app.route("/emotionDetector")
def detector():
    text_to_analyze = request.args.get("textToAnalyze")
    res = emotion_detector(text_to_analyze)
    response = f'For the given statement, the system response is "anger":{ res["anger"]}, "disgust": {res["disgust"]}, "fear": {res["fear"]}, "joy": {res["joy"]} and "sadness": {res["sadness"]}. The dominant emotion is {res["dominant_emotion"]}.'
    return response

@app.route("/")
def render_index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000)