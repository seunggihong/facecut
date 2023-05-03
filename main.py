import cv2
import os
from tqdm import trange

# cuttin imgs tracking face
def cut_imgs(img) :
    face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    faces = face_cascade.detectMultiScale(img, scaleFactor=1.1, minNeighbors=5)

    for (x, y, w, h) in faces:
        face = img[y:y+h, x:x+w]
        cv2.imwrite("result/test01.jpg", face)

dirListing = os.listdir("imgs")

if dirListing == 0 :
    print("Empty dir.")
else :
    for x in trange(len(dirListing)) :
        img = cv2.imread("imgs/test{}.jpg".format(str(x+1)))
        cut_imgs(img)
