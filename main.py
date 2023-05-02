import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

img = cv2.imread("imgs/test01.jpg")

faces = face_cascade.detectMultiScale(img, scaleFactor=1.1, minNeighbors=5)

for (x, y, w, h) in faces:
    face = img[y:y+h, x:x+w]
    cv2.imwrite("result/test01.jpg", face)