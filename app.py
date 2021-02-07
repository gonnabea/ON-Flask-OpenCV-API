from flask import request, url_for
from flask_api import FlaskAPI
from main import giveGrayEffect

app = FlaskAPI(__name__)

@app.route("/", methods=['GET'])
def hello():
    print("welcome to my python server")
    return "welcome to my python server"

@app.route("/gray-effect", methods=['GET'])
def grayEffect():
    giveGrayEffect("Resources/test_video.mp4")

if __name__ == "__main__":
    app.run(debug=True)