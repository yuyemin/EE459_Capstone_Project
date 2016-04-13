# water_cycle.py
#
# Handles the water cycle (goes for certain period of time, etc.)

import thread

from atmega import *

class Water_Cycle():

    def __init__(self):
        self.atmega = Atmega() # controls the sprinkler zones
        self.moistureLevel = 0 # sets the moisture level as zero to start with
        self.testMode = False # if true, then we don't update any of the atmega values until test mode is over

    def enterTestMode(self, zoneNumber):
        self.testMode = True
        time.sleep(0.1) # gives it a few seconds to not cause writing conflicts
        self.atmega.setAllOff() # clears the other indexes
        if (zoneNumber > 0):
            print("Test Mode wrote to zone...")
            self.atmega.setZone(zoneNumber - 1, True)
        else:
            print("Test Mode wrote to zone...")
            self.atmega.setAllOff()
        self.atmega.writeZones()

    def exitTestMode(self):
        self.atmega.setAllOff()
        self.atmega.writeZones()
        time.sleep(1)
        self.testMode = False


    # creates a new thread for the zone to water
    def spawnCycle(self, programArr, programNumber):
        thread.start_new_thread( self.startCycle, (programArr, programNumber, ))

    # used for a cycle thread (very basic right now, just waits for the cycle time)
    def startCycle(self, programArr, programNumber):
        print("STARTED PROGRAM " + str(programNumber))

        for i in range(len(programArr) - 1):
            if int(programArr[i]) != 0: # makes sure the zone does turn on for at least one minute
                while(self.testMode): # waits if it is in test mode
                    time.sleep(1)
                self.atmega.setZone(i, True)
                self.atmega.writeZones()
                print("STARTED WATERING ZONE " + str(i + 1))
                # sleeps for 60 seconds, then reads the water level
                runTime = int(programArr[i]) * 60
                saturated = False # starts with saturated as false
                while(runTime > 0):
                    time.sleep(60)
                    moistureLevel = self.atmega.readMoisture()
                    if (moistureLevel == 1) and (saturated == False): # only activates on VERY MOIST
                        print("Zone saturated, waiting until less wet.")
                        saturated = True
                        self.atmega.setZone(i, False)
                        self.atmega.writeZones()
                    elif (moistureLevel != 1) and (saturated == True):
                        print("Zone dried off, resuming watering.")
                        saturated = False
                        self.atmega.setZone(i, True)
                        self.atmega.writeZones()

                time.sleep(int(programArr[i]) * 60)
                while(self.testMode): # waits if it is in test mode
                    time.sleep(1)
                self.atmega.setZone(i, False)
                self.atmega.writeZones()
                print("FINISHED WATERING ZONE " + str(i + 1))
                time.sleep(5) # waits a few seconds between zones to prevent any conflicts on the atmega bus

        print("FINISHED PROGRAM " + str(programNumber))


    # updates the moisture level (good to determine how watering is going)
    def updateMoistureLevel(self, newMoistureLevel):
        self.moistureLevel = newMoistureLevel