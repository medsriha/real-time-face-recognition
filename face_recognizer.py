import cv2
import numpy as np
import json
import os

if __name__ == "__main__":
    
    # Create LBPH Face Recognizer
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    # Load the trained model
    recognizer.read('trainer.yml')
    print(recognizer)
    # Path to the Haar cascade file for face detection
    face_cascade_Path = "haarcascade_frontalface_default.xml"
    
    # Create a face cascade classifier
    faceCascade = cv2.CascadeClassifier(face_cascade_Path)
    
    # Font for displaying text on the image
    font = cv2.FONT_HERSHEY_SIMPLEX
    
    # Initialize user IDs and associated names
    id = 0
    # Don't forget to add names associated with user IDs
    names = ['None']
    with open('names.json', 'r') as fs:
        names = json.load(fs)
        names = list(names.values())
    
    # Video Capture from the default camera (camera index 0)
    cam = cv2.VideoCapture(0)
    cam.set(3, 640)  # Set width
    cam.set(4, 480)  # Set height
    
    # Minimum width and height for the window size to be recognized as a face
    minW = 0.1 * cam.get(3)
    minH = 0.1 * cam.get(4)
    
    while True:
        # Read a frame from the camera
        ret, img = cam.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
        # Detect faces in the frame
        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.2,
            minNeighbors=5,
            minSize=(int(minW), int(minH)),
        )
    
        for (x, y, w, h) in faces:

            # Draw a rectangle around the detected face
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
    
            # Recognize the face using the trained model
            id, confidence = recognizer.predict(gray[y:y + h, x:x + w])
            # Proba greater than 51
            if confidence > 51:
                try:
                    # Recognized face
                    name = names[id]
                    confidence = "  {0}%".format(round(confidence))
                except IndexError as e:
                    name = "Who are you?"
                    confidence = "N/A"
            else:
                # Unknown face
                name = "Who are you?"
                confidence = "N/A"
    
            # Display the recognized name and confidence level on the image
            cv2.putText(img, name, (x + 5, y - 5), font, 1, (255, 255, 255), 2)
            cv2.putText(img, confidence, (x + 5, y + h - 5), font, 1, (255, 255, 0), 1)
    
        # Display the image with rectangles around faces
        cv2.imshow('camera', img)
    
        # Press Escape to exit the webcam / program
        k = cv2.waitKey(10) & 0xff
        if k == 27:
            break
    
    print("\n [INFO] Exiting Program.")
    # Release the camera
    cam.release()
    # Close all OpenCV windows
    cv2.destroyAllWindows()
