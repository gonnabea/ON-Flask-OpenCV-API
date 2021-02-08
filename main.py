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

    while True:
        ret, frame = testCapture.read()

        # ret은 frame을 받는 지 안 받는지 boolean 값으로 알려주는 것으로 보임.
        if not ret:
            print("Can't receive frame")
            return "Can't receive frame"
            break
        print(ret)
        grayVideo = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # cv2.imshow('frame', grayVideo)


        videoSize = (640, 480)
        duration = 10
        fps = 30
        videoWriter = cv2.VideoWriter('grayVideo.avi', cv2.VideoWriter_fourcc(*'PIM1'), fps, (videoSize[1], videoSize[0]), False)
        for _ in range(fps * duration):
            data = numpy.random.randint(0, 256, videoSize, dtype='uint8')
            videoWriter.write(data)

            print(f"비디오데이터:{data}")
            print(f"비디오:{data}")
            return grayVideo


        if cv2.waitKey(1) == ord('q'):
            break

