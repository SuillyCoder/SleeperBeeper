To create an exe file, open this in Python, and run: 

python -m PyInstaller --onefile --name "SleeperBeeper" --hidden-import=cv2 --hidden-import=numpy --hidden-import=mediapipe --collect-all mediapipe --add-data "Alarm.mp3;." --add-data "face_landmarker.task;." --add-data "haarcascade_frontalface_default.xml;." SleeperBeeper.py

fuckit, I'll edit this some time soon.
