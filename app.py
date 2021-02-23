from flask_api import FlaskAPI
from grayScreenEffect import giveGrayEffect
from flask import stream_with_context, Response

app = FlaskAPI(__name__)

@app.route("/", methods=['GET'])
def hello():
    print("welcome to my python server")
    return "welcome to my python server"

@app.route("/gray-effect", methods=['GET'])


def grayEffect():
    videoSrc = "Resources/test_video.mp4"
    return Response(giveGrayEffect(videoSrc), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == "__main__":
    app.run(debug=True)