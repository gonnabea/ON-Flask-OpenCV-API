from flask_api import FlaskAPI
from grayScreenEffect import giveGrayEffect
from flask import stream_with_context, Response, jsonify
from flask_socketio import SocketIO
from flask_cors import CORS, cross_origin


app = FlaskAPI(__name__)
cors = CORS(app)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins='*')


@app.route("/", methods=['GET'])
def hello():
    print("welcome to my python server")
    return "welcome to my python server"

@app.route("/gray-effect", methods=['GET'])
def grayEffect():
    videoSrc = "Resources/test_video.mp4"
    return Response(giveGrayEffect(videoSrc), mimetype='multipart/x-mixed-replace; boundary=frame')

@socketio.on('connect')
@cross_origin()
def handle_connect():
    print("새 유저가 소켓 접속을 요청하였습니다.")
    response = jsonify(message="Flask socket server is running")
    # Enable Access-Control-Allow-Origin
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

@socketio.on('streamVideo')
def handle_stream(image):
    print("영상 재생 중")
    print(image)


if __name__ == "__main__":
    app.run(debug=True)
    socketio.run(app)