<h1>Sleeper-Beeper</h1>

<h3>This is a local application that uses CV to tell if you're sleeping and wakes you up if it does.</h3>

<div style="display: flex-; justify-content: space-around;">
  <img width="1919" height="1199" alt="image" src="https://github.com/user-attachments/assets/5966ff3b-a1fe-47ff-b448-a4e1587d8eea" />
  <img width="1919" height="1199" alt="image" src="https://github.com/user-attachments/assets/4d33e459-3f2e-45dc-aec5-dd1a12e508d8" />
  <img width="1814" height="1037" alt="image" src="https://github.com/user-attachments/assets/5fd2df5e-cf70-48a2-bb54-990586d76a1c" />
</div>

<h3>I tend to doze off a lot (I really need proper rest lmao). But, while I need to be on the job, I need to stay awake.</h3>

<img width="1919" height="1199" alt="image" src="https://github.com/user-attachments/assets/a5839fc8-7934-46d2-9b26-60a9079aa913" />

<h3>This program was made with the following:</h3>
<ul>
  <li>Python: Overall Code</li>
  <li>OpenCV: For Camera Vision</li>
  <li>MediaPipe: For eye detection</li>
  <li>TKinter: For GUI</li>
  <li>Audacity: For audio manipulation</li>
  <li>PyInstaller: For .exe conversion</li>
</ul>

<h3>You can actually run your own version, but since .exe file is so big, it's not here. Here's how to create it and have your own version running: </h3>


<h3>To create an exe file, open this in Python, and run: </h3>

python -m PyInstaller --onefile --name "SleeperBeeper" --hidden-import=cv2 --hidden-import=numpy --hidden-import=mediapipe --collect-all mediapipe --add-data "Alarm.mp3;." --add-data "face_landmarker.task;." --add-data "haarcascade_frontalface_default.xml;." SleeperBeeper.py

<h3>Once this is done, navigate to the 'dist' folder, and find your exe file there.</h3>

<img width="1383" height="350" alt="image" src="https://github.com/user-attachments/assets/5c8b808d-e0f2-4812-a1a5-046aabb3337a" />

<h3>Now go and run it!</h3>

<img width="977" height="860" alt="image" src="https://github.com/user-attachments/assets/ecd73821-3d48-4829-81d3-c6242c7161e0" />

I gotta edit this more later, this is an extremely scuffed readme.
