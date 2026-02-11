<h1>Sleeper-Beeper</h1>

<div display="flex" justify-content="center">
  <img width="1919" height="1199" alt="image" src="https://github.com/user-attachments/assets/5966ff3b-a1fe-47ff-b448-a4e1587d8eea" />
  <img width="1919" height="1199" alt="image" src="https://github.com/user-attachments/assets/4d33e459-3f2e-45dc-aec5-dd1a12e508d8" />
  <img width="1814" height="1037" alt="image" src="https://github.com/user-attachments/assets/5fd2df5e-cf70-48a2-bb54-990586d76a1c" />
</div>



To create an exe file, open this in Python, and run: 

python -m PyInstaller --onefile --name "SleeperBeeper" --hidden-import=cv2 --hidden-import=numpy --hidden-import=mediapipe --collect-all mediapipe --add-data "Alarm.mp3;." --add-data "face_landmarker.task;." --add-data "haarcascade_frontalface_default.xml;." SleeperBeeper.py

fuckit, I'll edit this some time soon.
