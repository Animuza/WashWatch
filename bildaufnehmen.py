#!/bin/python
import subprocess
print ("Bild wird aufgenommen...\n")
subprocess.call(["raspistill","-vf","-hf","-o", "/home/pi/Bilder/zeitaufnahme_V2.jpg","-n"])
print ("Fertig \n")
print ("Oeffne Bild \n")
subprocess.call(["fim","-a","/home/pi/Bilder/test.jpg"])

