# Real Time Face Recognition (OpenCV)

Create a fast real-time face recognition app with a few lines of Python code.

![gif](gif.gif)

## Steps:

`face_taker.py`

1) Take pictures using the `face_taker.py` script. After you enter the user name, the script will save 30 images of your face in the `images` folder and `names.json` file with association between ID number and user name. The ID number represents a single face. Note: Make sure your face is centered. The window will collapse when all the 30 pictures are taken.

`face_train.py`

2) The `face_tain.py` script will train a model to recognize all the faces from the 30 images taken using `face_taker.py` and save the training output in the `trainer.yml` file.

`face_recognizer.py`

3) The `face_recognizer.py` is the main script. The script will recognize the face according to the ID. i.e., If Joe has an ID = 1, their name should appear in the dictionary of `names.json` as attribute 1 like such:

```json
{
    "1": "Joe"
}
```

Requirements:

- `pip install opencv-python`
- `pip install opencv-contrib-python --upgrade` or `pip install opencv-contrib-python`
- `pip install pillow`
