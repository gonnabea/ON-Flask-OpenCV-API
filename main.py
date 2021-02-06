import cv2
import numpy

testImg = cv2.imread("Resources/react-logo.png", 0)

resizedImg = cv2.resize(testImg, (800,600))


cv2.imshow("testImg", resizedImg)
cv2.waitKey(0)
cv2.destroyAllWindows()