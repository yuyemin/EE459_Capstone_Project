# atmega.py
# CB: Michael Kukar 2016
# controls communication between atmega sprinklers/sensors and the raspberry pi

import serial, time

class Atmega():

    # only argument in is the serial connection to read from
    # DEFAULT SHOULD BE: serial.Serial('/dev/ttyUSB0', 9600, timeout=0.2)
    def __init__(self, ser):
        # saves variables
        self.serial = ser

        # clears the serial connection
        self.serial.flush()

    # writes to the sprinkler zones
    # array of zones with True or False boolean values
    def writeZones(self, zoneArr):
        for zone in zoneArr:
            if zone == True:
                self.serial.write(chr(49))
            else:
                self.serial.write(chr(48))

        response = self.serial.read()
        if response == 'a':
            print("GOOD TRANSMIT TO ZONES")
        else:
            print("BAD TRANSMIT TO ZONES")

    # returns the temperature reading from the microcontroller
    def readTemp(self):
        print("IN PROGRESS")

    # returns the humidity reading from the microcontroller
    def readHumidity(self):
        print("IN PROGRESS")

    # returns the soil moisture level
    def readMoisture(self):
        print("IN PROGRESS")