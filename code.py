import glob
import os
from openal import *
import time
import vlc 
list_of_files = glob.glob('/home/pi/Desktop/*') 
latest_file = max(list_of_files, key=os.path.getctime)
print(latest_file)

syscmnd = "ffmpeg -i " + latest_file +  " /home/pi/Desktop/file_conv.mp3 -y"

os.system("{}".format(syscmnd))

player = vlc.MediaPlayer("/home/pi/Desktop/file_conv.mp3")
media_player = vlc.MediaPlayer()
media_player.audio_set_volume(300)
player.play()

time.sleep(10)
