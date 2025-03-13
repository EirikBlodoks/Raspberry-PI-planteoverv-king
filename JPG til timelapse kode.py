import cv2
import os
import glob

# filbaner for hvor jeg vil hente og legge filene
image_folder = "/home/eirik/Desktop/Planteprosjekt/regular_pics/sessionx"
output_video = "/home/eirik/Desktop/Planteprosjekt/timelapse.mp4"

#sorter etter alder
images = sorted(glob.glob(os.path.join(image_folder, "*.jpg")), key=os.path.getmtime)

#Sjekker etter filer i mappen
if not images:
    print("No images found in the folder!")
    exit()

#Bruker det første bildet til å hente dimensjonene til videoen
frame = cv2.imread(images[0])
height, width, layers = frame.shape

fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Kode for .mp4
video = cv2.VideoWriter(output_video, fourcc, 10, (width, height))#setter opp videoskriveren

# Prosesserer hvert enkelt bilde og legger det til i videoen
for img in images:
    frame = cv2.imread(img)
    video.write(frame)

video.release()#legger videoen i den definerte mappen
print("Suksess")#Sjekk om hele koden har kjørt
