import time
import cv2
import numpy
from flask import stream_with_context, Response
from base64 import b64decode, b64encode
from PIL import Image
from base64 import decodestring
from io import BytesIO


# 이미지 흑백 처리
# testImg = cv2.imread("Resources/react-logo.png", 0)
#
# resizedImg = cv2.resize(testImg, (800,600))
#
#
# cv2.imshow("testImg", resizedImg)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# 동영상 흑백 처리
def giveGrayEffect(img_uri):
    if img_uri:
        img_uri = img_uri.split(',')[1]

        img = b64decode(img_uri)
        img = Image.open(BytesIO(img))
        img = numpy.array(img)
        imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        cv2.imshow("0", imgGray)
        cv2.waitKey(0)
        # imgGray, buffer = cv2.imencode('.jpg', imgGray)
        # # jpg_as_text = base64.b64encode(buffer)
        # cv2.imshow("gray",imgGray)




