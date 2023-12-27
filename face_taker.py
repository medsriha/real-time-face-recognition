import numpy as np
import cv2
import os

if __name__ == "__main__":

    
    def create_directory(directory):
        """
        Create a directory if it doesn't exist.
    
        Parameters:
            directory (str): The path of the directory to be created.
        """
        if not os.path.exists(directory):
            os.makedirs(directory)
    
    # Create 'images' directory if it doesn't exist
    create_directory('images')
    
    # Load the pre-trained face cascade classifier
    faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    
    # Open a connection to the default camera (camera index 0)
    cam = cv2.VideoCapture(0)
    
    # Set camera dimensions
    cam.set(3, 640)
    cam.set(4, 480)
    
    # Initialize face capture variables
    count = 0
    face_id = input('\nEnter user id (MUST be an integer) and press <return> -->  ')
    print("\n[INFO] Initializing face capture. Look at the camera and wait...")
    
    while True:
        # Read a frame from the camera
        ret, img = cam.read()
    
        # Convert the frame to grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
        # Detect faces in the frame
        faces = faceCascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
    
        # Process each detected face
        for (x, y, w, h) in faces:
            # Draw a rectangle around the detected face
            cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    
            # Increment the count for naming the saved images
            count += 1

            # Save the captured image into the 'images' directory
            cv2.imwrite(f"./images/Users-{face_id}-{count}.jpg", gray[y:y+h, x:x+w])
    
            # Display the image with rectangles around faces
            cv2.imshow('image', img)
    
        # Press Escape to end the program
        k = cv2.waitKey(100) & 0xff
        if k < 30:
            break
    
        # Take 30 face samples and stop video. You may increase or decrease the number of
        # images. The more, the better while training the model.
        elif count >= 30:
            break
    
    print("\n[INFO]Success! Exiting Program.")
    
    # Release the camera
    cam.release()
    
    # Close all OpenCV windows
    cv2.destroyAllWindows()
