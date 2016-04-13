#!/usr/bin/env python

# turns on all of the zones
# Michael Kukar 2016

import serial, time

# creates a serial connection (hopefully with the arduino itself)
arduino = serial.Serial('/dev/ttyUSB0', 9600, timeout=0.2)
arduino.flush()

arduino.write(chr(122))
arduino.write(chr(49))
arduino.write(chr(49))
arduino.write(chr(49))
arduino.write(chr(49))
arduino.write(chr(49))
arduino.write(chr(49))
print(arduino.read())