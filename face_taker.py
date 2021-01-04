import numpy as np
import cv2
import os

# Check if folder exists
if not os.path.exists('images'):
    os.makedirs('images')

faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cam = cv2.VideoCapture(0)
cam.set(3,640)
cam.set(4,480)
count = 0

face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# For each person, enter one unique numeric face id
face_id = input('\n enter user id (MUST be an integer) and press <return> -->  ')
print("\n [INFO] Initializing face capture. Look the camera and wait ...")


while(True):
    ret, img = cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)
        count += 1
        # Save the captured image into the images directory
        cv2.imwrite("./images/Users." + str(face_id) + '.' + str(count) + ".jpg", gray[y:y+h,x:x+w])
        cv2.imshow('image', img)
    # Press Escape to end the program.
    k = cv2.waitKey(100) & 0xff
    if k < 30:
        break
    # Take 30 face samples and stop video. You may increase or decrease the number of
    # images. The more the better while training the model.
    elif count >= 30:
         break

print("\n [INFO] Exiting Program.")
cam.release()
cv2.destroyAllWindows()
