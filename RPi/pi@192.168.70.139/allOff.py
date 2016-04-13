#!/usr/bin/env python

# turns off all of the zones
# Michael Kukar 2016

import serial, time

# creates a serial connection (hopefully with the arduino itself)
arduino = serial.Serial('/dev/ttyUSB0', 9600, timeout=0.2)
arduino.flush()

arduino.write(chr(122))
arduino.write(chr(48))
arduino.write(chr(48))
arduino.write(chr(48))
arduino.write(chr(48))
arduino.write(chr(48))
arduino.write(chr(48))
print(arduino.read())