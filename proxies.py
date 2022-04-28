from time import sleep
from colorama import *
import os
fichero = open("proxies.txt")
lineas = fichero.readlines()
print("Starting search...")
for linea in lineas:
    sleep(0.4)
    os.system("color 2")
    print("New ip -->", linea)