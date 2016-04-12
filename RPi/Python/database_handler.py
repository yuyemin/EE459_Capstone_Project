# database_handler.py
# CB: Michael Kukar 2016
# maintains the save file mysql database and accesses information from it

import MySQLdb as mdb


class Database_Handler():

    # needs the string filename as input
    def __init__(self):

        # connects to our mysql database
        self.con =  mdb.connect('localhost', 'group15', 'finalproject', 'finalproject')

    # SCHEDULE TABLE

    # returns the schedule for the week as an array with what program is running on each schedule
    def getSchedule(self):
        outputArr = []

        zoneName = "Schedule"  # gets the exact table we want to use

        cur = self.con.cursor()
        cur.execute("SELECT * FROM " + zoneName)
        rows = cur.fetchall()
        for row in rows:
            outputArr.append(row[1])

        return outputArr

    # returns the program number with each zone as an index
    def getProgram(self, programNumber):
        outputArr = []
        programName = "Program" + str(programNumber)

        cur = self.con.cursor()
        cur.execute("SELECT * FROM " + programName)
        rows = cur.fetchall()
        for row in rows:
            outputArr.append(row[1])

        return outputArr


    # sets the entire program schedule (index 0 is zone 1, index 5 is zone 5, index 6 is the time to start)
    def setProgram(self, inputArr, programNumber):
        cur = self.con.cursor()
        programName = "Program" + str(programNumber)
        for i in range(len(inputArr)):
            cur.execute("UPDATE " + programName + " SET Time = %s WHERE Day = %s", (str(inputArr[i]), str(i + 1)))
        self.con.commit()


    # sets just a single schedule index (1 is Monday, 7 is Sunday) so we can change what program(s) run on a given day
    def setScheduleIndex(self, inputStr, index):
        cur = self.con.cursor()
        zoneName = "Schedule" # gets the exact table we want to use
        cur.execute("UPDATE " + zoneName + " SET Time = %s WHERE Day = %s", (str(inputStr), str(index)))
        self.con.commit()


    # sets the entire schedule with one input array (0 is Monday, 6 is Sunday)
    def setSchedule(self, inputArr):
        cur = self.con.cursor()
        zoneName = "Schedule" # gets the exact table we want to use
        for i in range(len(inputArr)):
            cur.execute("UPDATE " + zoneName + " SET Time = %s WHERE Day = %s", (str(inputArr[i]), str(i + 1)))
        self.con.commit()





