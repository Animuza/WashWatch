"Modul zur Bestimmung der verbleibenden Restzeit der Waschmaschine"
import os

def getTime():
	
	os.system('ssocr -T -f white -b black -d -1 -C files/picture_1.jpg > files/output')
	f=open('files/output', 'r')
	data = f.read()
	"Ein ':' wird in den String eingefügt, damit an der Ausgabe nichts mehr verändert werden muss"
	"XX:XX-Digitalanzeige"
	if len(data) > 5:
		"Der Doppelpunkt wird oft als 1 erkannt"
		if(data[2]=='1'):
			data_neu = data[0]+data[1]+':'+data[3]+data[4]
		else:
			data_neu = data[0]+data[1]+':'+data[2]+data[3]
	elif len(data) == 4:
		data_neu = data[0]+':'+data[1]+data[2]
	else: 
		if(data[1]=='1'):
			data_neu = data[0]+':'+data[2]+data[3]
	print(data_neu)
	return data_neu

def main():
	getTime()

if __name__ == "__main__":
    # execute only if run as a script
    main()