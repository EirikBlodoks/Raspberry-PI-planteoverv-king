#!/bin/bash

# Ping Google to check internet connection
ping -c 4 8.8.8.8 > /dev/null 2>&1

# If ping fails, restart WiFi
if [ $? -ne 0 ]; then
    echo "$(date) - Internet down! Restarting WiFi..." >> /home/eirik/wifi_log.txt
    sudo systemctl restart networking
    sudo systemctl restart dhcpcd
    sudo systemctl restart wpa_supplicant
    echo "$(date) - WiFi restarted!" >> /home/eirik/wifi_log.txt
else
    echo "$(date) - Internet is working fine." >> /home/eirik/wifi_log.txt
fi
