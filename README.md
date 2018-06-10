# Real-Time-Face-Recognition (OpenCV)

This is a full step Python program to create an efficient real-time face recognition app.

<img src = 'https://github.com/medsriha/Real-Time-Face-Recognition/blob/master/gif.gif?raw=true'><center>

## Steps:

1) Take pictures using the `Face_taker.py` script. The script will save 30 images of your face in the `image` folder (Create manually the folder).
Note: You will not see the camera pops up on the screen while taking the pictures. However, you will see the light of the camera on. Make sure youe face is entered. The program will end when all the 30 pictures are taken.

2) The `Face_tain.py` script will train a model to recognize your face from the 30 images taken using `Face_taker.py` script, and save the training output in the `training.yaml` file.

3) The `Face_Recognizer.py` is the main script. You need to change the name of each person who sees his/her picture taken in the `Face_taker.py` script. The program will recognize the face according to the id given in the same script. If Joe has an id 1, his name should appear in the list as index 1.
Note: If the recognizer could predict a face, we put a text over the image with the probable id and how much is the "probability" in % that the match is correct ("probability" = 100 - confidence index). If not, an "Who are you?" label is put on the face.

That is it!! enjoy.

A big up to <a href = 'https://www.hackster.io/mjrobot/real-time-face-recognition-an-end-to-end-project-a10826'>Marcelo</a>
