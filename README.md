# Raspberry-PI-planteoverv-king

Denne mappen inneholder de tre viktigste kodesnippetsene for å holde planteovervåkeren min gående, i tillegg til kopier av de to txt filene jeg bruker til å lagre info.  

Dersom det skal brukes må det lastes inn på en raspberry pi 5 med en camera module 2 installert. (Det er mulig å bruke koden på andre utgaver med minimale endringer.)

Hvis det skal kjøres bør dette også skrives i terminalen på RPIen: 
Crontab -e # dette gir deg mulighet til å endre i crontab configen din
  GNU nano 7.2               /tmp/crontab.bOB0oM/crontab                        
*/15 * * * * python3 /home/eirik/Desktop/Planteprosjekt/Bildetager.py
#Denne kjører koden for å ta ett bilde hvert 15. min
*/5 * * * * /home/eirik/Desktop/Planteprosjekt/reconnect_wifi.sh
#Dette sørger for å opprettholde wifitilkoblingen døgnet rundt
*/15 * * * * /home/eirik/Desktop/Planteprosjekt/upload_pics.sh
#Denne laster opp det nyeste bildet hvert 15. minutt
Ctrl+X, Y, Enter 
