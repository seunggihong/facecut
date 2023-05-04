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
            cv2.imwrite("result/change_data_set{}.jpg".format(str(cnt+1)), face)
            return True

# rename file
def rename_img(dir_path) :
    diractory = os.listdir(dir_path)
    for i in range(len(diractory)) :
        if ".jpg" in diractory[i] or ".jpeg" in diractory[i]:
            print(diractory[i])
            os.rename("{}/{}".format(dir_path, diractory[i]),"{}/data_set{}.jpg".format(dir_path, i+1))

# main
if __name__ == "__main__" :
    dirListing = os.listdir("imgs")
    done = 0
    err = 0

    if dirListing == 0 :
        print("Empty dir.")
    else :
        rename_img("imgs")
        for x in trange(len(dirListing)) :
            img = cv2.imread("imgs/data_set{}.jpg".format(str(x+1)))
            if cut_imgs(img, x) :
                done += 1
            else :
                err += 1
                
    print("Done : {} Error : {}".format(done, err))