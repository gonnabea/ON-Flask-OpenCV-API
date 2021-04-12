import cv2
import binascii
import numpy
from PIL import Image
from io import BytesIO

def face_detection(img_uri):
    img_uri = img_uri.split(',')[1]
    img = binascii.a2b_base64(img_uri)
    img = Image.open(BytesIO(img))
    img = numpy.array(img)
    # img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # numpy.ndarray 타입 데이터 반환

    x = img_uri
    face_cascade = cv2.CascadeClassifier('Resources/haarcascade_frontalface_default.xml')


    faces = face_cascade.detectMultiScale(img,1.8,1) # the input image, scaleFactor and minNeighbours.
    # print(faces)
    def nparray_to_img(img):
        # Reshape the array into a
        # familiar resoluition
        # print(img.shape)
        array = numpy.reshape(img, (240, 240, 3))  # width, height, color로 보임.

        # # show the shape of the array
        #
        # # show the array
        # print(array)

        # creating image object of
        # print(array.shape)
        # above array
        data = Image.fromarray(array)

        # saving the final output
        # as a PNG file
        # data.save('gfg_dummy_pic.png')
        fd = BytesIO()
        data.save(fd, "webp")

        return fd.getvalue()

    # 얼굴이 검출될 시
    if len(faces) > 0:
        for(x,y,w,h) in faces:
            cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

            # 얼굴에 붙일 이미지
            image_for_face = cv2.imread('Resources/rabbit.jpg')
            image_for_face = cv2.resize(image_for_face, (w, h))

            img[y:y+h,x:x+w] = image_for_face # 순서가 x,y가 아닌 y,x로 반대인 이유는?

            img = nparray_to_img(img)

        return img
    # 얼굴이 검출되지 않았을 시
    else:

        return nparray_to_img(img)

