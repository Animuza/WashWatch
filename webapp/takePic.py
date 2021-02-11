#!/bin/python
import subprocess
from picamera import PiCamera
from time import sleep


def takePicture():


    camera = PiCamera()

    camera.start_preview() //aktivieren der Kamera
    sleep(2) //Zeit damit Kamera sich fokussieren kann 
    camera.capture('files/picture.jpeg') //Bild wird im Ordner files als picture.jpeg abgespeichert
    camera.stop_preview() //Deaktivieren der Kamera
    camera.close() //Schließen der Kamera 


def main():
    takePicture()

if __name__ == "__main__":
    # execute only if run as a script
    main()