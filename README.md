# Raspberry-PI-planteoverv-king

Denne mappen inneholder de tre viktigste kodesnippetsene for å holde planteovervåkeren min gående, i tillegg til kopier av de to txt filene jeg bruker til å lagre info.  

Dersom det skal brukes må det lastes inn på en raspberry pi 5 med en camera module 2 installert. (Det er mulig å bruke koden på andre utgaver med minimale endringer.)

Hvis det skal kjøres bør dette også skrives i terminalen på RPIen: 
Crontab -e # dette gir deg mulighet til å endre i crontab configen din
@reboot /filbane/Bildetager.py #Programmet kjører allerede for alltid og tar bilder hvert 15. minutt, men når RPI rebooter må programmet startes på nytt
*/5 * * * * /filbane/reconnect_wifi.sh #Dette sørger for å opprettholde wifitilkoblingen døgnet rundt
*/15 * * * * /filbane/upload_pics.sh #Denne laster opp det nyeste bildet hvert 15. minutt
Ctrl+X, Y, Enter 
