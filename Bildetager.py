from picamera2 import Picamera2
from time import sleep
import os

base_dir = "/home/eirik/Desktop/Planteprosjekt/regular pics"
restart_counter_file = "/home/eirik/Desktop//Planteprosjekt/reboot_counter.txt"

os.makedirs(base_dir, exist_ok=True)

if os.path.exists(restart_counter_file):
    with open(restart_counter_file, "r") as f:
        restart_count = int(f.read().strip())
else:
    restart_count = 0
    
restart_count+=1
with open(restart_counter_file, "w") as f:
    f.write(str(restart_count))

session_dir = os.path.join(base_dir, f"session_{restart_count}")
os.makedirs(session_dir, exist_ok=True)
pic_count=0

picam2 = Picamera2()
while True:
	filename= f"{session_dir}/plant{pic_count}.jpg"
	secondFilename = f"{base_dir}/temp/plant{pic_count}.jpg"
	picam2.start_and_capture_file(filename)
	picam2.start_and_capture_file(secondFilename)
	pic_count+=1
	sleep(900)
picam2.close()
