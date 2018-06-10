# Real-Time-Face-Recognition

This program is a full step in how to create an efficient real-time face recognition program.

## Step in how to use the scripts:
1) Take pictures using the `Face_taker.py` script. The script will save 30 images of your face in the `image` directory.
Note: You will not see the camera pops up on the screen while taking the pictures. However, you will see the light of the camera/Webcam on. Make sure you face is entered. The program will end when the 30 pictures are taken.

2) The `Face_tain.py` script will train a model to recognize your face from the 30 images taken using `Face_taker.py` script.

3) The `Face_Recognizer.py` is the main script. You need to change the name of each person who sees his/her picture taken in the `Face_taker.py` script. The program will recognize the face according to the id given in the same script. If Joe has an id 1, his name should appear in the list as index 1.
