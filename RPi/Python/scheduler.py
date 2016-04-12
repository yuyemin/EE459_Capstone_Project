# scheduler.py
# CB: Michael Kukar 2016
# reads in database entries, sensors, etc. and comes up with a schedule to follow

from database_handler import *



class Scheduler():

    def __init__(self):
        self.database = Database_Handler() # reference to the database that we will use
        self.curSchedule = self.database.getSchedule()


    # takes in all sensor and database input and creates a schedule from it
    # returns the new planned schedule
    def updateScheduleBasedOnData(self):
        print("IN PROGRESS")
