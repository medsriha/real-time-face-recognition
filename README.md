# Real-Time-Face-Recognition (OpenCV)

This is a full step Python program to create an efficient real-time face recognition app.

<img src = 'https://github.com/medsriha/Real-Time-Face-Recognition/blob/master/gif.gif?raw=true'><center>

## Steps:

`cmd: python face_taker.py`
1) Take pictures using the `face_taker.py` script. The script will save 30 images of your face in the `images` folder after you entered the ID number (MUST be integer and incremental (starts with 1 then 2, 3, ...)
Note: Make sure your face is centered. The window will collapse when all the 30 pictures are taken.


`cmd: python face_train.py`

2) The `face_tain.py` script will train a model to recognize all the faces from the 30 images taken using `face_taker.py` script, and save the training output in the `training.yml` file.


`cmd: python face_recognizer.py`

3) The `face_recognizer.py` is the main script. You need to append the name of each person who sees his/her picture taken in the `face_taker.py` script. The program will recognize the face according to the id given in the `face_taker.py` script. If Joe has an id 1, his name should appear in the list as index 1 like this `names = ['None', 'Joe'] # keep None and append a name into this list`

Requirements:

- `pip install opencv-python`
- `pip install opencv-contrib-python --upgrade` or `pip install opencv-contrib-python --user`
