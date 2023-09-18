from win10toast import ToastNotifier
import pyttsx3
from notifypy import Notify
c1=800
c2=50
c3=100
c4=900
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