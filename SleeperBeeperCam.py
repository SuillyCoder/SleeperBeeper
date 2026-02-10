#All necessary imports
import cv2
import mediapipe as mp
import time
import pygame
import sys
import os
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
from scipy.spatial import distance as dist
import threading

def resource_path(relative_path):    
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

class SleeperBeeperCamera: 
    def __init__(self, on_stop_callback=None):

    #import face cascade classifier
        self.face_cascade = cv2.CascadeClassifier(resource_path('haarcascade_frontalface_default.xml'))

        # Create FaceLandmarker using MediaPipe
        base_options = python.BaseOptions(model_asset_path=resource_path('face_landmarker.task'))
        options = vision.FaceLandmarkerOptions(
            base_options=base_options,
            output_face_blendshapes=False,
            output_facial_transformation_matrixes=False,
            num_faces=1
        )
        self.detector = vision.FaceLandmarker.create_from_options(options)

        #Eye location indices
        self.LEFT_EYE_INDICES = [362, 385, 387, 263, 373, 380]
        self.RIGHT_EYE_INDICES = [33, 160, 158, 133, 153, 144]

        # Initialize blaring alarm audio file
        pygame.mixer.init()
        self.alarm_sound = pygame.mixer.Sound(resource_path('Alarm.mp3'))
        self.alarm_sound.set_volume(1.0)

        # 5 Second Threshold:
        self.eyes_closed_start_time = None
        self.SLEEP_THRESHOLD_SECONDS = 5.0

        #Set camera off, just in case
        self.cap = None
        self.running=False

        #Callback function
        self.on_stop_callback = on_stop_callback

        #EAR calculation
    def calculate_ear(self, eye_landmarks):
        # Compute the euclidean distances between the vertical eye landmarks
        A = dist.euclidean(eye_landmarks[1], eye_landmarks[5])
        B = dist.euclidean(eye_landmarks[2], eye_landmarks[4])
    
        # Compute the euclidean distance between the horizontal eye landmarks
        C = dist.euclidean(eye_landmarks[0], eye_landmarks[3])
    
        # Compute the eye aspect ratio
        ear = (A + B) / (2.0 * C)
        return ear

    def camera_start(self, show_window=True):
        self.running = True
        self.show_window = show_window
        
        #Find local camera
        self.cap = cv2.VideoCapture(0)

        #Checking if camera is opened successfully
        if not self.cap.isOpened():
            print("Cannot Open Camera!")
            return False

        print("Camera opened successfully. Press 'q' to quit.")

        self.detection_thread = threading.Thread(target=self._detection_loop, daemon=True)
        self.detection_thread.start()
        return True
    
    def _detection_loop(self):
        #Continuoisly read frames
        while self.running: 
            ret, frame = self.cap.read()
            if not ret: 
                print("Can't retrieve frame (stream end?). Exiting....")
                break

            # Convert the frame to grayscale (face detection works better on grayscale)
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # Detect faces in the grayscale frame
            faces = self.face_cascade.detectMultiScale(
                rgb_frame,
                scaleFactor=1.1,  # Compensates for faces that are closer or farther away
                minNeighbors=5,   # Higher values reduce false positives but might miss some faces
                minSize=(30, 30)  # Minimum possible object size. Objects smaller than this are ignored
            )

            # Draw rectangles around the detected faces
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2) # Green rectangle

            mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb_frame)
            detection_result = self.detector.detect(mp_image)

            # Eye Landmark Extraction using EAR Calculations
            if detection_result.face_landmarks:
                for face_landmarks in detection_result.face_landmarks:
                # Get frame dimensions
                    h, w, _ = frame.shape
        
                    # Extract left eye landmarks
                    left_eye = []
                    for idx in self.LEFT_EYE_INDICES:
                        landmark = face_landmarks[idx]
                        left_eye.append((landmark.x * w, landmark.y * h))
        
                    # Extract right eye landmarks
                    right_eye = []
                    for idx in self.RIGHT_EYE_INDICES:
                        landmark = face_landmarks[idx]
                        right_eye.append((landmark.x * w, landmark.y * h))
        
                    # Calculate EAR for both eyes
                    left_ear = self.calculate_ear(left_eye)
                    right_ear = self.calculate_ear(right_eye)
            
                    # Average EAR
                    avg_ear = (left_ear + right_ear) / 2.0
        
                    # Print EAR value for testing
                    print(f"EAR: {avg_ear:.3f}")

                    # Replace your if (avg_ear <= 0.18) block with:
                    if avg_ear <= 0.18:  # Eyes closed
                        if self.eyes_closed_start_time is None:
                            # Just closed eyes, start timer
                            self.eyes_closed_start_time = time.time()
                        else:
                            # Eyes still closed, check duration
                            eyes_closed_duration = time.time() - self.eyes_closed_start_time
                            print(f"Eyes closed for: {eyes_closed_duration:.2f} seconds")
        
                            if eyes_closed_duration >= self.SLEEP_THRESHOLD_SECONDS:
                                if not pygame.mixer.get_busy():
                                    self.alarm_sound.play()
                        
                    else:  # Eyes open
                        pygame.mixer.stop()
                        self.eyes_closed_start_time = None  # Reset timer
                    

                                # Draw the eye landmarks on the frame
                    for point in left_eye + right_eye:
                        cv2.circle(frame, (int(point[0]), int(point[1])), 2, (0, 255, 0), -1)

            #Display current frame
            if self.show_window:
                cv2.imshow('SleeperBeeper', frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    self.stop()
                    break
            else:
                time.sleep(0.03)

        self.cap.release()
        cv2.destroyAllWindows()
    
    def stop(self):
        self.running=False
        pygame.mixer.stop()
        if self.cap:
            self.cap.release()
        cv2.destroyAllWindows()

        #Call the callback when stopping
        if self.on_stop_callback:
            self.on_stop_callback()


