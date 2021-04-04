from flask_api import FlaskAPI
from grayScreenEffect import giveGrayEffect
from flask import stream_with_context, Response, jsonify
from flask_socketio import SocketIO
from flask_cors import CORS, cross_origin
from engineio.payload import Payload
from faceDetection import face_detection


Payload.max_decode_packets = 10000

app = FlaskAPI(__name__)
cors = CORS(app)
app.config['SECRET_KEY'] = 'secret!'


socketio = SocketIO(app, cors_allowed_origins='https://our-now.herokuapp.com', ping_timeout=100, ping_interval=10000, async_mode='eventlet')


@app.route("/", methods=['GET'])
def hello():
    print("welcome to my python server")
    return "welcome to my python server"

@socketio.on('connect')
@cross_origin()
def handle_connect():
    print("새 유저가 소켓 접속을 요청하였습니다.")
    socketio.emit('connect-flask', "플라스크 socket.io 서버에 연결되었습니다.")
    response = jsonify(message="Flask socket server is running")
    # Enable Access-Control-Allow-Origin
    response.headers.add("Access-Control-Allow-Origin", "https://our-now.herokuapp.com")
    return response

# 통화 상대의 영상 처리 효과를 위한 소켓 채널
@socketio.on('gray-video')
@cross_origin()
def handle_stream(image_base64):
    if(image_base64):
        print("상대의 흑백화 모드")
        socketio.emit("gray-video",giveGrayEffect(image_base64))
        return 'gray video is working...'

@socketio.on('face-detection')
@cross_origin()
def handle_stream(image_base64):
    if(image_base64):
        print("상대의 얼굴 인식 모드")
        socketio.emit("face-detection",face_detection(image_base64))
        return 'gray video is working...'

# 자신의 영상에 효과 적용을 위한 소켓 채널
@socketio.on('my-gray-video')
@cross_origin()
def handle_stream(image_base64):
    if(image_base64):
        print("나의 흑백화 모드")
        socketio.emit("my-gray-video",giveGrayEffect(image_base64))
        return 'gray video is working...'

@socketio.on('my-face-detection')
@cross_origin()
def handle_stream(image_base64):
    if(image_base64):
        print("나의 얼굴 인식 모드")
        socketio.emit("my-face-detection",face_detection(image_base64))
        return 'gray video is working...'

if __name__ == '__main__':
    socketio.run(app,debug=True)
