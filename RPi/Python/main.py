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
# 1. keep track of time and spawn programs throughout the day
# 2. check every so often the data and update all the tables appropriately (read from them too)
# 3. make new predictions every so often based on new data

# ################
# HELPER FUNCTIONS
# ################

# updates the variables so we know what schedule to run today
def updateSchedulePlan(todaySchedule):
    global runProgram1
    global runProgram2
    global runProgram3
    global ranProgram1Today
    global ranProgram2Today
    global ranProgram3Today

    print("UPDATING SCHEDULE PLAN")
    for char in todaySchedule: # iterates across all the characters (up to 1, 2, 3 123 eg.)
        if char == '1':
            print("PROG1 ADDED")
            runProgram1 = True
        elif char == '2':
            print("PROG2 ADDED")
            runProgram2 = True
        elif char == '3':
            print("PROG3 ADDED")
            runProgram3 = True

    # resets our programs run today
    ranProgram1Today = False
    ranProgram2Today = False
    ranProgram3Today = False



# #########
# VARIABLES
# #########

# classes
db = Database_Handler()
waterCycler = Water_Cycle()

# general variables
schedule = db.getSchedule()

curDay = datetime.datetime.today().weekday() # 0 is Monday, 6 is Sunday
print("CUR DAY: " + str(curDay))
curTime = datetime.datetime.now()
curMilTime = (curTime.hour * 100) + curTime.minute
print("CUR TIME: " + str(curMilTime))

# make sure we run programs sequentially and don't run them concurrently
runProgram1 = False
runProgram2 = False
runProgram3 = False
ranProgram1Today = False
ranProgram2Today = False
ranProgram3Today = False
runningProgram = False
runDuration = 0 # duration of the current running program (time remaining)

# updates the variables for this schedule
updateSchedulePlan(schedule[curDay])


# TESTING ONLY
# we set each program to start today and be one minute each and start at this current time
db.setScheduleIndex("123", curDay + 1)
db.setProgram(['1', '0', '0', '0', '0', '0', str(curMilTime)], 1)
db.setProgram(['0', '1', '0', '0', '0', '0', str(curMilTime)], 2)
db.setProgram(['0', '0', '1', '0', '0', '0', str(curMilTime)], 3)

print("SCHEDULE " + str(db.getSchedule()))
print("PROGRAM 1 " + str(db.getProgram(1)))
print("PROGRAM 2 " + str(db.getProgram(2)))
print("PROGRAM 3 " + str(db.getProgram(3)))

while(True):

    # updates the current date and time
    curTime = datetime.datetime.now()
    curMilTime = (curTime.hour * 100) + curTime.minute
    curDay = datetime.datetime.today().weekday()


    # checks if the schedule was changed at all and updates accordingly
    updatedSchedule = db.getSchedule()
    if schedule[curDay] != updatedSchedule[curDay]:
        schedule = updatedSchedule
        updateSchedulePlan(schedule[curDay])

    # checks if program is running and handles logic for that state
    if runningProgram:
        print("Program in progress...")
        print("RUN TIME REMAINING " + str(runDuration))
        runDuration = runDuration - 1 # we cycle every minute, so we subtract one from the run duration
        if runDuration <= 0:
            runningProgram = False



    else: # checks if it is time to run a certain program (anytime after the schedule amount) and then runs it
        if runProgram1 and (curMilTime >= int(db.getProgram(1)[6])) and not ranProgram1Today:
            waterCycler.spawnCycle(db.getProgram(1), 1)
            runningProgram = True
            ranProgram1Today = True
            runDuration = 1 # starts with one minute extra time (for delays, ect.)
            for i in range(len(db.getProgram(1)) - 1):
                runDuration += int(db.getProgram(1)[i])
        elif runProgram2 and int(curMilTime) >= int(db.getProgram(2)[6]) and not ranProgram2Today:
            waterCycler.spawnCycle(db.getProgram(2), 2)
            runningProgram = True
            ranProgram2Today = True
            runDuration = 1 # starts with one minute extra time (for delays, ect.)
            for i in range(len(db.getProgram(2)) - 1):
                runDuration += int(db.getProgram(2)[i])
        elif runProgram3 and int(curMilTime) >= int(db.getProgram(3)[6]) and not ranProgram3Today:
            waterCycler.spawnCycle(db.getProgram(3), 3)
            runningProgram = True
            ranProgram3Today = True
            runDuration = 1 # starts with one minute extra time (for delays, ect.)
            for i in range(len(db.getProgram(3)) - 1):
                runDuration += int(db.getProgram(3)[i])

    time.sleep(60)

'''

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

'''