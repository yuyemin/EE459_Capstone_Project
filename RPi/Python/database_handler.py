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

    # returns the schedule for the week as an array
    def getSchedule(self, zoneNumber):
        outputArr = []

        zoneName = "Schedule" + str(zoneNumber) # gets the exact table we want to use

        cur = self.con.cursor()
        cur.execute("SELECT * FROM " + zoneName)
        rows = cur.fetchall()
        for row in rows:
            outputArr.append(row[1])

        return outputArr

    # sets just a single schedule index (1 is Monday, 7 is Sunday)
    def setScheduleIndex(self, inputStr, index, zoneNumber):
        cur = self.con.cursor()
        zoneName = "Schedule" + str(zoneNumber) # gets the exact table we want to use
        cur.execute("UPDATE " + zoneName + " SET Time = %s WHERE Day = %s", (str(inputStr), str(index)))
        self.con.commit()


    # sets the entire schedule with one input array (0 is Sunday, 6 is Saturday)
    def setSchedule(self, inputArr, zoneNumber):
        cur = self.con.cursor()
        zoneName = "Schedule" + str(zoneNumber) # gets the exact table we want to use
        for i in range(len(inputArr)):
            cur.execute("UPDATE " + zoneName + " SET Time = %s WHERE Day = %s", (str(inputArr[i]), str(i + 1)))
        self.con.commit()





