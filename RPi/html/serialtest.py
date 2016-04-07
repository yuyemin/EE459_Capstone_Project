#!/usr/bin/env python

# arduino_comm_test.py
# tests communicating with an arduino over its serial USB connection
# Michael Kukar 2016

import serial, time

# creates a serial connection (hopefully with the arduino itself)
arduino = serial.Serial('/dev/ttyUSB0', 9600, timeout=0.2)
arduino.flush()

arduino.write(chr(122))
arduino.write(chr(48))
arduino.write(chr(49))
arduino.write(chr(49))
arduino.write(chr(48))
print(arduino.read())