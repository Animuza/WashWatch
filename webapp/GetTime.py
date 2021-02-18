#Modul zur Bestimmung der verbleibenden Restzeit der Waschmaschine
import os

def getTime():
	
	os.system('ssocr -T -f white -b black -d -1 -C files/picture.jpeg > files/output')
	f=open('files/output', 'r')
	data = f.read()
	# Ein ':' wird in den String eingefügt, damit an der Ausgabe nichts mehr verändert werden muss
	# XX:XX-Digitalanzeige
	if len(data) == 6:
			data_neu = data[0]+data[1]+':'+data[3]+data[4]
	#X:XX-Digitalanzeige
	elif len(data) ==5:
			data_neu= data_neu = data[0]+':'+data[2]+data[3]
	#XXX-Digitalanzeige (ohne Doppelpunkt)
	elif len(data) == 4:
		data_neu = data[0]+':'+data[1]+data[2]
	#Definition eines neuen Zahlenformats der Digitalanzeige notwendig oder Qualität des Bildes unzureichend, bzw. nicht richtig positioniert
	else: 
		data_neu ='Ungültiges Zahlenformat oder Bildqualität zu schlecht, bzw. falsche Positionierung' 
	#print(data_neu)
	return data_neu

def main():
	getTime()

if __name__ == "__main__":
    # execute only if run as a script
    main()