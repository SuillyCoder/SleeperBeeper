<h1>Sleeper-Beeper</h1>

<h5>This is a locally-run, Python CV-based application that detects if you're sleeping using face detection and eye aspect ratio (EAR) calculations, and wakes you up if it does via a blaring alarm. This application is ideally designed to be run in the background so you may catch yourself falling asleep and wake right back up after you've napped off.</h5>

<div style="display: flex-; justify-content: space-around;">
  <img width="1919" height="1199" alt="image" src="https://github.com/user-attachments/assets/5966ff3b-a1fe-47ff-b448-a4e1587d8eea" style="width: 30%;"/>
  <img width="1919" height="1199" alt="image" src="https://github.com/user-attachments/assets/4d33e459-3f2e-45dc-aec5-dd1a12e508d8" style="width: 30%;"/>
  <img width="1814" height="1037" alt="image" src="https://github.com/user-attachments/assets/5fd2df5e-cf70-48a2-bb54-990586d76a1c" style="width: 30%;"/>
</div>

<h5>Third year tends to get pretty tiring, and from that tiredness, I tend to doze off. A lot (I really need proper rest lmao). The work is demanding, and I can't afford to doze off on the job as easily as I want to. I have to find ways to keep myself awake just for a little longer, and that's where the idea for this app came in:.</h5>

<img width="1919" height="1199" alt="image" src="https://github.com/user-attachments/assets/a5839fc8-7934-46d2-9b26-60a9079aa913" />

<h5>As mentioned, this Python-based program uses computer vision and a lot of other libraries in order to detect my face, the state of my eyes, and blare out an alarm. Specifically, this program was made with the following:</h5>
<ul>
  <li>Python: Serves as the overall backend of the code, which handles ALL the logic performed within the application.</li>
  <li>OpenCV: Integrates the Computer Vision aspect of the application, using the Haar Cascades library for Face Detection and EAR Calculation for Eye Status</li>
  <li>MediaPipe: Used for processing of various media, in this case: video, and running other commands from that processed data</li>
  <li>TKinter: Creates the overall minimalistic look and style of the application</li>
  <li>PyGame and Audacity: Used for the initial amplification of audio (in Audacity), and actually playing it when certain scripts are ran.</li>
  <li>PyInstaller: Converts the entire Python project into an exe file for you to use.</li>
</ul>

<h5>You can actually run your own version, but since .exe file is so big, it's not here. Additionally, there are a few steps to follow if you REALLY wanna go ahead and execute it. Here's how to create it and have your own version running: </h5>

<h3>Step 1: Clone the Repository</h3>
```bash
git clone https://github.com/SuillyCoder/SleeperBeeper.git
cd SleeperBeeper
```

<h3>Step 2: Install Required Dependencies</h3>
```bash
pip install opencv-python mediapipe pygame-ce scipy pyinstaller --break-system-packages
```

<h3>Step 3: Build the Executable</h3>
<p>Run the following command in your terminal (make sure you're in the project directory):</p>
```bash
python -m PyInstaller --onefile --windowed --name "SleeperBeeper" --hidden-import=cv2 --hidden-import=numpy --hidden-import=mediapipe --collect-all mediapipe --add-data "Alarm.mp3;." --add-data "face_landmarker.task;." --add-data "haarcascade_frontalface_default.xml;." SleeperBeeper.py
```

<p><em>Note: This process may take a few minutes as PyInstaller bundles all dependencies into a single executable.</em></p>

<h3>Step 4: Locate Your Executable</h3>
<p>Once the build completes, navigate to the <code>dist</code> folder in your project directory:</p>

<img width="1383" height="350" alt="image" src="https://github.com/user-attachments/assets/5c8b808d-e0f2-4812-a1a5-046aabb3337a" />

<h3>Step 5: Run SleeperBeeper! 🎉</h3>
<p>Double-click <code>SleeperBeeper.exe</code> to launch the application.</p>

<img width="977" height="860" alt="image" src="https://github.com/user-attachments/assets/ecd73821-3d48-4829-81d3-c6242c7161e0" />

<h3>🐍 Alternative: Run Directly with Python</h3>
<p>If you don't want to build an executable, you can run the program directly:</p>
```bash
python SleeperBeeper.py
```

<h3>⚠️ Troubleshooting</h3>
<ul>
  <li><strong>Camera not opening?</strong> Make sure no other application is using your webcam.</li>
  <li><strong>PyInstaller not recognized?</strong> Use <code>python -m PyInstaller</code> instead of just <code>pyinstaller</code>.</li>
  <li><strong>Missing modules?</strong> Double-check that all dependencies are installed with pip.</li>
</ul>
