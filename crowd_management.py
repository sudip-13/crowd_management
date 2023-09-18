import cv2
import numpy as np
import dlib
from win10toast import ToastNotifier
import pyttsx3
from notifypy import Notify

def count_no_of_face(n):
    # Connects with cctv
    cap = cv2.VideoCapture(n)
    
    
    # Detect the coordinates
    detector = dlib.get_frontal_face_detector()
    
    
    # Capture frames continuously
    while True:
    
        # Capture frame-by-frame
        ret, frame = cap.read()
        frame = cv2.flip(frame, 1)
    
        # RGB to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = detector(gray)
    
        # Iterator to count faces
        i = 0
        for face in faces:
    
            # Get the coordinates of faces
            x, y = face.left(), face.top()
            x1, y1 = face.right(), face.bottom()
            cv2.rectangle(frame, (x, y), (x1, y1), (0, 255, 0), 2)
    
            # Increment iterator for each face in faces
            i = i+1
    
            # Display the box and faces
            cv2.putText(frame, 'face num'+str(i), (x-10, y-10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
            print(face, i)
    
        # Display the resulting frame
        cv2.imshow('frame', frame)
    
        # This command let's us quit with the "q" button on a keyboard.
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    
    # Release the capture and destroy the windows
    cap.release()
    cv2.destroyAllWindows()
    return i
c1=count_no_of_face(0)
c2=count_no_of_face(0)
c3=count_no_of_face(0)
c4=count_no_of_face(0)
def notifier(l,r):
    s=f"{l} side is overcrowded please,move towards {r} to avoid disturbance"
    notification = Notify()
    notification.title = "Over_Crowded"
    notification.message = f"{s}"
    notification.urgency = "critical"
    notification.icon = "D:\\PYTHON_GPU\\crowd_management\\images.jpeg"
    notification.timeout = 100000
    notification.send()
    toast = ToastNotifier()
    speaker = pyttsx3.init()
    speaker.say(f"{s}")
    speaker.runAndWait()
def get_notification(cl,cr):
    if(cl>500 and cr<200):
        notifier("left","right")
    elif(cl<200 and cr>500):
        notifier("right","left")
get_notification(c1,c2)
get_notification(c3,c4)
