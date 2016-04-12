# water_cycle.py
#
# Handles the water cycle (goes for certain period of time, etc.)

import thread

from atmega import *

class Water_Cycle():

    def __init__(self):
        self.atmega = Atmega() # controls the sprinkler zones
        self.moistureLevel = 0 # sets the moisture level as zero to start with


    # creates a new thread for the zone to water
    def spawnCycle(self, cycleTime, maxCycleTime, zoneNumber):
        thread.start_new_thread( self.startCycle, (cycleTime, maxCycleTime, zoneNumber, ))

    # used for a cycle thread (very basic right now, just waits for the cycle time)
    def startCycle(self, cycleTime, maxCycleTime, zoneNumber):
        self.atmega.setZone(zoneNumber, True)
        self.atmega.writeZones()
        print("STARTED WATERING ZONE " + str(zoneNumber))
        cycleTimeSeconds = cycleTime * 60 # 60 seconds in a minute
        time.sleep(cycleTimeSeconds)
        self.atmega.setZone(zoneNumber, False)
        self.atmega.writeZones()
        print("FINISHED WATERING ZONE " + str(zoneNumber))


    # updates the moisture level (good to determine how watering is going)
    def updateMoistureLevel(self, newMoistureLevel):
        self.moistureLevel = newMoistureLevel