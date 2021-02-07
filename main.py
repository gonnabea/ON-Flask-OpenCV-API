import cv2
import numpy

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

def giveGrayEffect(video):
    testCapture = cv2.VideoCapture(video)

    while True:
        ret, frame = testCapture.read()

        # ret은 frame을 받는 지 안 받는지 boolean 값으로 알려주는 것으로 보임.
        if not ret:
            print("Can't receive frame")
            return "Can't receive frame"
            break
        print(ret)
        grayVideo = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        cv2.imshow('frame', grayVideo)
        if cv2.waitKey(1) == ord('q'):
            break

