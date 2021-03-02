import cv2

face_cascade = cv2.CascadeClassifier('Resources/haarcascade_frontalface_default.xml')

image = cv2.imread('Resources/lena.png')

gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray_img,1.1,4) # the input image, scaleFactor and minNeighbours.

for(x,y,w,h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)

cv2.imshow('img', image)
cv2.waitKey()