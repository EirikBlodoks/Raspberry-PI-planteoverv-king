#!/bin/bash

# Define local folder and remote drive folder
LOCAL_FOLDER="/home/eirik/Desktop/Planteprosjekt/regular pics/temp"
REMOTE_FOLDER="Planteprosjekt:/Plantebilder"

# Find the most recent PNG file in the folder
LATEST_FILE=$(ls -t "$LOCAL_FOLDER"/*.jpg | head -n 1)

# Check if a file was found
if [ -n "$LATEST_FILE" ]; then
    # Upload the latest PNG file to Google Drive
    rclone copy "$LATEST_FILE" "$REMOTE_FOLDER"
    echo "Uploaded: $LATEST_FILE to Google Drive!"
else
    echo "⚠No PNG files found in $LOCAL_FOLDER!"
fi
