from distutils.log import ERROR
import cv2
import os
from tqdm import trange

# cuttin imgs tracking face
def cut_imgs(img, cnt) :
    face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    faces = face_cascade.detectMultiScale(img, scaleFactor=1.1, minNeighbors=5)
    
    if isinstance(faces, tuple) :
        return False
    else :
        for (x, y, w, h) in faces:
            face = img[y:y+h, x:x+w]
            cv2.imwrite("result/result{}.jpg".format(str(cnt+1)), face)
            return True

dirListing = os.listdir("imgs")
done = 0
err = 0

if dirListing == 0 :
    print("Empty dir.")
else :
    for x in trange(len(dirListing)) :
        img = cv2.imread("imgs/test{}.jpg".format(str(x+1)))
        
        if cut_imgs(img, x) :
            done += 1
        else :
            err += 1
            
print("Done : {} Error : {}".format(done, err))