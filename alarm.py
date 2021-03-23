import time
import winsound
import datetime

class Alarm:
    def __init__(self,minute):
        self.minute=minute

    def set_alarm(self):
        times=datetime.datetime.now()
        print(f"After {self.minute} minutes the alarm will go off")
        print(f"The date the alarm was set {datetime.datetime.ctime(times)}")
        #Set Minute
        time.sleep(self.minute*60)
        #Current Time
        times=datetime.datetime.now()
        print(f"ALARM !!!  {datetime.datetime.ctime(times)}")
        winsound.Beep(frequency=2500,duration=5000)

minute=int(input("Minute: "))
test=Alarm(minute)
test.set_alarm()

