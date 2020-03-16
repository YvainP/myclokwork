from datetime import datetime 
import vlc, pafy, time

url = "https://www.youtube.com/watch?v=LDU_Txk06tM"
media = vlc.MediaPlayer("./test.mp3")
media.play()
# Alarm = input("What time do you want to wake up?\n")
#now = datetime.now()
#currentTime = now.strftime("%H:%M")

#while currentTime != Alarm:
 #   now = datetime.now()
#    currentTime = now.strftime("%H:%M")
#    print("The time is " + currentTime)
#    if currentTime == Alarm:
#        print("Time to wake up!")

