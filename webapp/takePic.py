#!/bin/python
import subprocess
from picamera import PiCamera
from time import sleep


def takePicture():


    camera = PiCamera()

    camera.start_preview()
    sleep(2)
    camera.capture('files/picture.jpeg')
    camera.stop_preview()
    camera.close() 


def main():
    takePicture()
    # getTime()

if __name__ == "__main__":
    # execute only if run as a script
    main()