import time
import cv2
import numpy
from flask import stream_with_context, Response

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
def giveGrayEffect(videoSrc):
    testCapture = cv2.VideoCapture(videoSrc)
    while(testCapture.isOpened()):

        ret, img = testCapture.read()
        if ret == True:
            img = cv2.resize(img, (0,0), fx=0.5, fy=0.5)
            capture_frame = cv2.imencode('.jpg', img)[1].tobytes()
            yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + capture_frame + b'\r\n')
            time.sleep(0.1)
        else:
            break



