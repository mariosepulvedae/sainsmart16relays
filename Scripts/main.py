#!/usr/bin/env python3

"""
Example code for driving the Sainsmart 16-Channel 9-36V USB Relay Module (Product 101-70-208)
Documents for this module were found at:
  https://s3.amazonaws.com/s3.image.smart/download/101-70-208/101-70-208.zip
        
The protocol appears to be MODBUS ASCII: 
  https://en.wikipedia.org/wiki/Modbus#Protocol_versions
This script depends on python serial library: 
  https://pythonhosted.org/pyserial/
  
  Este codigo se utilizo para pruebas del relay 
  La logica para automatizar los relays ya es despues 
  
  
  
"""

import serial
import time
import random


# header functions (included in the original repository)

from headerFunctions import *


# Secuencias de encendido

from initialConfiguration import initialConf
from settingTVTP import settVTP
from engageTheRestraint import engageTR
from openTheDoor import openDoor
from deployingTheLeveler import deployLeveler
from forkliftPresent import forkliftP
from forkliftGoneFT import forkliftGFT
from levelerRaise import levelerR
from closingDoor import closingD
from restraintRelease import restraint
from vehicleTrailerGFD import vehicleTGFD



def main():
    ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)  # open serial port

    print("Status")
    ser.write(status())
    print(ser.readline().hex())

    print("All On")
    ser.write(all_on())
    print(ser.readline().hex())
    time.sleep(1)

    print("All Off")
    ser.write(all_off())
    print(ser.readline().hex())
    time.sleep(1)
    
    i=0

    reles=dict([(0,False),(1,False),(2,False),(3,False),(4,False),(5,False),(6,False),(7,False),(8,False),(9,False),(10,False),(11,False),(12,False),(13,False),(14,False),(15,False)])
	
	


    while(True):
    	print("Seleccione configuracion")
    	print("[ 1] Initial configuration")
    	print("[ 2] Setting the Vehicle/Trailer Present")
    	print("[ 3] Engage the restraint")
    	print("[ 4] Open the door")
    	print("[ 5] Deploying the Leveler")
    	print("[ 6] Forklift Present")
    	print("[ 7] Forklift gone from Trailer")
    	print("[ 8] Leveler Raise")
    	print("[ 9] Closing door")
    	print("[10] Restraint release")
    	print("[11] Vehicle-Trailer Gonde from Dock")
    	print("[ 0] Salir")
    	seguir=int(input("Seleccion: "))
    	if seguir==1:
    	    reles=initialConf(reles)
    	    print(reles)
    	elif seguir==2:
    	    reles=settVTP(reles)
    	    print(reles)
    	elif seguir==3:
    	    reles=engageTR(reles)
    	    print(reles)
    	elif seguir==4:
    	    reles=openDoor(reles)
    	    print(reles)
    	elif seguir==5:
    	    reles=deployLeveler(reles)
    	    print(reles)
    	elif seguir==6:
    	    reles=forkliftP(reles)
    	    print(reles)
    	elif seguir==7:
    	    reles=forkliftGFT(reles)
    	    print(reles)
    	elif seguir==8:
    	    reles=levelerR(reles)
    	    print(reles)
    	elif seguir==9:
    	    reles=closingD(reles)
    	    print(reles)
    	elif seguir==10:
    	    reles=restraint(reles)
    	    print(reles)
    	elif seguir==11:
    	    reles=vehicleTGFD(reles)
    	    print(reles)
    	else:
    	    ser.write(all_off())
    	    break
    	
    	#Encendido y apagado de relays
    	i=0
    	while i<16:
    	    if reles[i]==True:
    	        ser.write(on_cmd(i))
    	    else:
    	    	ser.write(off_cmd(i))
    	    i=i+1
 
    	    
    	    
    	       
    ser.close()             # close port



if __name__ == "__main__":
    main()
