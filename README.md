# Real Time Face Recognition (OpenCV)

Create a fast real-time face recognition app with a few lines of Python code.

![gif](gif.gif)

## Installation

```bash
pip install opencv-python
pip install opencv-contrib-python
pip install pillow
```

## Usage

The system works in three steps:

### 1. Capture Face Data
Run `face_taker.py` to capture training images:
```bash
python src/face_taker.py
```
- Enter your name when prompted
- The script captures 30 images of your face
- Images are saved in the `images` folder
- Your name and ID are stored in `names.json`
- Keep your face centered in the frame
- Window closes automatically after capturing all images

### 2. Train the Model
Run `face_train.py` to create the recognition model:
```bash
python src/face_train.py
```
- Processes all images in the `images` folder
- Creates a trained model file `trainer.yml`

### 3. Run Face Recognition
Run `face_recognizer.py` to start real-time recognition:
```bash
python src/face_recognizer.py
```
- Your webcam will open
- Displays name and confidence level next to the face
- Press 'ESC' to exit

## Data Structure

The `names.json` file maps IDs to names:
```json
{
    "1": "Joe",
    "2": "Jane"
}
```

## Project Structure
```
├── src/
│   ├── face_taker.py
│   ├── face_train.py
│   └── face_recognizer.py
├── images/
├── names.json
└── trainer.yml
```
