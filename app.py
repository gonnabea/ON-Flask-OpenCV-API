from flask_api import FlaskAPI
from grayScreenEffect import giveGrayEffect
from flask import stream_with_context, Response, jsonify
from flask_socketio import SocketIO
from flask_cors import CORS, cross_origin
from engineio.payload import Payload

Payload.max_decode_packets = 10000

app = FlaskAPI(__name__)
cors = CORS(app)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins='*', ping_timeout=100, ping_interval=10)

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
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

@socketio.on('gray-video')
@cross_origin()
def handle_stream(image_base64):
    if(image_base64):
        print("영상 base64 이미지 송신중...")
        # socketio.emit('gray-video', "이미지 서버에서 받음")
        # socketio.emit('gray-video',giveGrayEffect(image))
        socketio.emit("gray-video",giveGrayEffect(image_base64))
        return 'gray video is working...'



if __name__ == "__main__":
    app.run(debug=True)
    socketio.run(app)