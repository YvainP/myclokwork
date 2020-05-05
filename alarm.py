import datetime
import time
import playsound
now = datetime.datetime.now()

alarm_time = datetime.datetime.combine(now.date(), datetime.time(17, 8, 0))

time.sleep((alarm_time - now).total_seconds())

playsound('test.mp3')
