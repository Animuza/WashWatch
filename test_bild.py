from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.start_preview()
sleep(2)
camera.capture('/home/pi/Bilder/aufnahme_test.jpg')
camera.stop_preview()


