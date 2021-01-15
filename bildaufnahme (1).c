#include <stdio.h>
#include <stdlib.h>

//Nimmt ein Foto um 180 Grad gedreht auf und speichert es in dem Ordner Bilder
void takepicture(){
	int bild;
	printf("Bild wird aufgenommen....\n");
	bild = system("raspistill -vf -hf -o /home/pi/Bilder/zeitaufnahme.jpg  -n");
	printf("Fertig \n");
	}
//Zeigt das aufgenommene Bild an. Achtung Paket Fim muss instaliert sein
void getpicture(){
	int retBild;
	printf("Oeffne Bild... \n");
	retBild = system("fim -a /home/pi/Bilder/zeitaufnahme.jpg");
	}

int main(int argc, char *argv[])
{

	takepicture();
	getpicture();


	return 0;

	}
