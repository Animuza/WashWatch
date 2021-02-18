"Modul zur Bestimmung der verbleibenden Restzeit der Waschmaschine"
import os

def getTime():
	
	os.system('ssocr -T -f white -b black -d -1 -C files/picture.jpeg > files/output')
	f=open('files/output', 'r')
	data = f.read()
	"Ein ':' wird in den String eingefügt, damit an der Ausgabe nichts mehr verändert werden muss"
	if len(data) > 4:
		if(data[2]='1'):
			data_neu = data[0]+data[1]+':'+data[3]+data[4]
		else:
			data_neu = data[0]+data[1]+':'+data[2]+data[3]		
	else:
		if(data[1]='1'):
			data_neu = data[0]+':'+data[2]+data[3]
		else:
			data_neu = data[0]+':'+data[1]+data[2]
	print(data_neu)
	return data_neu

def main():
	getTime()

if __name__ == "__main__":
    # execute only if run as a script
    main()