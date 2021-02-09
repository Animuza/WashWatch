"Modul zur Bestimmung der verbleibenden Restzeit der Waschmaschine"
import os

def getTime():
	"Für /home/pi/share muss die entsprechende Adresse abgelegt werden, in der das Bild abgelegt wird und das output-file mit den gelesenen Daten"
	os.system('ssocr -T -f white -b black -d -1 -C /home/pi/share/test_pi_3.jpeg > /home/pi/share/output')
	f=open('/home/pi/share/output', 'r')
	data = f.read()
	"Ein ':' wird in den String eingefügt, damit an der Ausgabe nichts mehr verändert werden muss"
	if len(data) > 4:
		data_neu = data[0]+data[1]+':'+data[2]+data[3]
	else:
		data_neu = data[0]+':'+data[1]+data[2]
	"print(data_neu)"
	return data_neu

def main():
	getTime()

if __name__ == "__main__":
    # execute only if run as a script
    main()