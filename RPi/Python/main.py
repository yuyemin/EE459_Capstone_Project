# final_project_main.py
# CB: Michael Kukar 2016
# Runs the code for the final project sprinkler system

# interacts with a save file that is generated using a mysql database
# the web interface writes to this database, we read from it and control the sprinklers

import time, datetime

from database_handler import *
from water_cycle import *

from atmega import *

'''
# TESTING ONLY
# We read in the schedule data and print it to the screen
database = Database_Handler()

print(database.getSchedule(1))

# now we change Monday (1) to now water at 1300 (1pm)
database.setScheduleIndex("1300", 1, 1)

print(database.getSchedule(1))

# now we change the entire database in one stroke (even though we only edit a single entry)

myDatabase = database.getSchedule(1)

myDatabase[4] = "1300"

database.setSchedule(myDatabase, 1)

print(database.getSchedule(1))

'''

# TESTING THE ATMEGA

# TESTING THE WATER SCHEDULER CREATING A BUNCH OF THREADS TO RUN STUFF WITH
'''
waterCycler = Water_Cycle()

waterCycler.spawnCycle(1, 1, 0)
time.sleep(14)
waterCycler.spawnCycle(1, 1, 1)
time.sleep(14)
waterCycler.spawnCycle(1, 1, 2)
time.sleep(14)
waterCycler.spawnCycle(1, 1, 3)
time.sleep(14)
waterCycler.spawnCycle(1, 1, 4)
time.sleep(14)
waterCycler.spawnCycle(1, 1, 5)

while(True):
    time.sleep(1)

'''

### FOR TESTING ONLY
#db = Database_Handler()
#db.setSchedule()

# PURPOSE OF MAIN PROGRAM
# runs a continuous loop that does a multitude of things
# 1. keep track of time and spawn water cycles when appropriate for the day
# 2. check every so often the data and update all the tables appropriately (read from them too)
# 3. make new predictions every so often based on new data

# #########
# VARIABLES
# #########

# classes
db = Database_Handler()
waterCycler = Water_Cycle()

# general variables
zoneSchedules = []
for i in range(6):
    zoneSchedules.append(db.getSchedule(i+1))

curDay = datetime.datetime.today().weekday() # 0 is Monday, 6 is Sunday (we want 1 is Monday, 7 is Sunday)
print(curDay)

curTime = datetime.datetime.now()
curMilTime = (curTime.hour * 100) + curTime.minute
print(curMilTime)

while (True):

    # RIGHT NOW JUST CORE FUNCTIONALITY, SO WE FOLLOW THE SCHEDULE TO THE DOT

    # updates the current date and time
    curTime = datetime.datetime.now()
    curMilTime = (curTime.hour * 100) + curTime.minute
    curDay = datetime.datetime.today().weekday() # 0 is Monday, 6 is Sunday (we want 1 is Monday, 7 is Sunday)

    #TESTING ONLY, WE"RE GOING TO SET THE ZONE 1 to the current time on the schedule to spawn a thread
    db.setScheduleIndex(str(curMilTime), curDay + 1, 1)
    print("SET SCHEDULE INDEX TO " + str(curMilTime))

    # checks if the current time matches the scheduled time for today for any of our zones
    for i in range(len(zoneSchedules)):
        #print("CHECKING ZONE " + str(i))
        #print("WEEKLY SCHEDULE IS " + str(zoneSchedules[i]))
        #print("CURRENT SCHEDULE FOR TODAY IS " + str(zoneSchedules[i][curDay]))
        if str(zoneSchedules[i][curDay]) == str(curMilTime):
            waterCycler.spawnCycle(2, 2, i)




    time.sleep(60) # doesn't have to update very often so we can wait 30 seconds between cycles (so we don't miss any minutes)