# atmega.py
# CB: Michael Kukar 2016
# controls communication between atmega sprinklers/sensors and the raspberry pi

import serial, time

class Atmega():

    # DEFAULT SHOULD BE: serial.Serial('/dev/ttyUSB0', 9600, timeout=0.2)
    def __init__(self):
        # saves variables
        self.serial = serial.Serial('/dev/ttyUSB0', 9600, timeout=0.2)
        self.portBusy = False # turns true if we're already writing from another thread, so we wait if this is true

        self.zoneArr = [False, False, False, False, False, False] # defaults all the zones to OFF

        # clears the serial connection
        self.serial.flush()

    # allows a single zone to be updated to ON or OFF at any time
    def setZone(self, zoneNumber, zoneBool):
        self.zoneArr[zoneNumber] = zoneBool

    # writes to the sprinkler zones
    # array of zones with True or False boolean values
    def writeZones(self):
        while self.portBusy: # waits until it has the opportunity to use the port
            time.sleep(1)
        self.portBusy = True
        self.serial.write(chr(122))
        for zone in self.zoneArr:
            if zone == True:
                self.serial.write(chr(49))
            else:
                self.serial.write(chr(48))

        response = self.serial.read()

        if response == 'a':
            print("GOOD TRANSMIT TO ZONES")
        else:
            print("BAD TRANSMIT TO ZONES")

        self.portBusy = False

    # returns the temperature reading from the microcontroller
    def readTemp(self):
        print("IN PROGRESS")

    # returns the humidity reading from the microcontroller
    def readHumidity(self):
        print("IN PROGRESS")

    # returns the soil moisture level
    def readMoisture(self):
        print("IN PROGRESS")