from picamera2 import Picamera2
import os
import sys
import psutil

def drep_existing_instances():
    current_pid = os.getpid()  
    script_name = os.path.basename(__file__)  #Henta koden for å slette eksisterende instances fra ett standardprosjekt på en RPI-blogg
#Dette på grunn av en bug som oppsto hvis RPI kræsja, som gjorde at den ikke kjørte picam.close() nederst i koden 
    for process in psutil.process_iter(['pid', 'name', 'cmdline']): 
        try:
            if process.info['pid'] != current_pid and process.info['cmdline']:
                # Check if the script name appears in the command line arguments
                if script_name in " ".join(process.info['cmdline']):
                    print(f"Stopping existing instance: PID {process.info['pid']}")
                    os.kill(process.info['pid'], 9)  # Force kill the process
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue  

drep_existing_instances()

#Alt etter dette er derimot skrevet for egen maskin

base_dir = "/home/eirik/Desktop/Planteprosjekt/regular pics"
pic_counter_file = "/home/eirik/Desktop/Planteprosjekt/pic_counter.txt"

os.makedirs(base_dir, exist_ok=True)

if os.path.exists(pic_counter_file):
    with open(pic_counter_file, "r") as f:
        try:
            pic_count = int(f.read().strip())
        except ValueError:
            pic_count = 0  # Hvis filen er tom eller inneholder feil verdi
else:
    pic_count = 0
    
picam2 = Picamera2()
filename= f"/home/eirik/Desktop/Planteprosjekt/regular pics/New/plant{pic_count}.jpg"
secondFilename = f"/home/eirik/Desktop/Planteprosjekt/regular pics/temp/plant{pic_count}.jpg"
picam2.start_and_capture_file(filename)
picam2.start_and_capture_file(secondFilename)
pic_count+=1
with open(pic_counter_file, "w") as f:
    f.write(str(pic_count))
picam2.close()
