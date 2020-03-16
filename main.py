from datetime import datetime 
import vlc, pafy, time

url = "https://www.youtube.com/watch?v=MZFg8V6vLLQ&list=LLpn5mWz5UwMscuGkHtclOpw&index=611"
video = pafy.new(url)
best = video.getbest()
media = vlc.MediaPlayer(best.url)
media.play()
print(video.title)
# Alarm = input("What time do you want to wake up?\n")
#now = datetime.now()
#currentTime = now.strftime("%H:%M")

#while currentTime != Alarm:
 #   now = datetime.now()
#    currentTime = now.strftime("%H:%M")
#    print("The time is " + currentTime)
#    if currentTime == Alarm:
#        print("Time to wake up!")

