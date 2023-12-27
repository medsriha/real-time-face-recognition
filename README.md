# Real-Time-Face-Recognition (OpenCV)

Create a fast real-time face recognition app with a few lines of Python code.

<img src = 'https://github.com/medsriha/Real-Time-Face-Recognition/blob/master/gif.gif?raw=true'><center>

## Steps:

`python face_taker.py`
1) Take pictures using the `face_taker.py` script. After you enter the ID number, the script will save 30 images of your face in the `images` folder. The ID number represents a single face. The ID MUST be an integer and incremental starting with 1, then 2, 3, ...
Note: Make sure your face is centered. The window will collapse when all the 30 pictures are taken.


`python face_train.py`

2) The `face_tain.py` script will train a model to recognize all the faces from the 30 images taken using `face_taker.py` and save the training output in the `training.yml` file.


`python face_recognizer.py`

3) The `face_recognizer.py` is the main script. You need to append each person's name with the picture taken in the `face_taker.py` script. The program will recognize the face according to the ID  in the `face_taker.py` script. i.e., If Joe has an id 1, his name should appear in the list as index 1 like such 
`names = ['None', 'Joe']. # Keep None and append a name into this list`

Requirements:

- `pip install opencv-python`
- `pip install opencv-contrib-python --upgrade` or `pip install opencv-contrib-python --user`
