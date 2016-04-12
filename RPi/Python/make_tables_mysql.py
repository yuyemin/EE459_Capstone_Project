# creates the tables for us to use
# CB: Michael Kukar

import MySQLdb as mdb

con = mdb.connect('localhost', 'group15', 'finalproject', 'finalproject')

with con:

    # creates the schedule tables (zones 1 - 6)

    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS Schedule1")
    cur.execute("CREATE TABLE Schedule1(Day INT PRIMARY KEY AUTO_INCREMENT, \
                 Time VARCHAR(25))")
    cur.execute("INSERT INTO Schedule1(Time) VALUES('0500')") # SUNDAY
    cur.execute("INSERT INTO Schedule1(Time) VALUES('SKIP')") # MONDAY
    cur.execute("INSERT INTO Schedule1(Time) VALUES('0500')") # TUESDAY
    cur.execute("INSERT INTO Schedule1(Time) VALUES('SKIP')") # WEDNESDAY
    cur.execute("INSERT INTO Schedule1(Time) VALUES('SKIP')") # THURSDAY
    cur.execute("INSERT INTO Schedule1(Time) VALUES('0500')") # FRIDAY
    cur.execute("INSERT INTO Schedule1(Time) VALUES('SKIP')") # SATURDAY

    # prints back created table

    cur.execute("SELECT * FROM Schedule1")

    rows = cur.fetchall()

    for row in rows:
        print row

    # creates the schedule table

    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS Schedule2")
    cur.execute("CREATE TABLE Schedule2(Day INT PRIMARY KEY AUTO_INCREMENT, \
                 Time VARCHAR(25))")
    cur.execute("INSERT INTO Schedule2(Time) VALUES('0500')") # SUNDAY
    cur.execute("INSERT INTO Schedule2(Time) VALUES('SKIP')") # MONDAY
    cur.execute("INSERT INTO Schedule2(Time) VALUES('0500')") # TUESDAY
    cur.execute("INSERT INTO Schedule2(Time) VALUES('SKIP')") # WEDNESDAY
    cur.execute("INSERT INTO Schedule2(Time) VALUES('SKIP')") # THURSDAY
    cur.execute("INSERT INTO Schedule2(Time) VALUES('0500')") # FRIDAY
    cur.execute("INSERT INTO Schedule2(Time) VALUES('SKIP')") # SATURDAY

    # prints back created table

    cur.execute("SELECT * FROM Schedule2")

    rows = cur.fetchall()

    for row in rows:
        print row

    # creates the schedule table

    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS Schedule3")
    cur.execute("CREATE TABLE Schedule3(Day INT PRIMARY KEY AUTO_INCREMENT, \
                 Time VARCHAR(25))")
    cur.execute("INSERT INTO Schedule3(Time) VALUES('0500')") # SUNDAY
    cur.execute("INSERT INTO Schedule3(Time) VALUES('SKIP')") # MONDAY
    cur.execute("INSERT INTO Schedule3(Time) VALUES('0500')") # TUESDAY
    cur.execute("INSERT INTO Schedule3(Time) VALUES('SKIP')") # WEDNESDAY
    cur.execute("INSERT INTO Schedule3(Time) VALUES('SKIP')") # THURSDAY
    cur.execute("INSERT INTO Schedule3(Time) VALUES('0500')") # FRIDAY
    cur.execute("INSERT INTO Schedule3(Time) VALUES('SKIP')") # SATURDAY

    # prints back created table

    cur.execute("SELECT * FROM Schedule3")

    rows = cur.fetchall()

    for row in rows:
        print row

    # creates the schedule table

    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS Schedule4")
    cur.execute("CREATE TABLE Schedule4(Day INT PRIMARY KEY AUTO_INCREMENT, \
                 Time VARCHAR(25))")
    cur.execute("INSERT INTO Schedule4(Time) VALUES('0500')") # SUNDAY
    cur.execute("INSERT INTO Schedule4(Time) VALUES('SKIP')") # MONDAY
    cur.execute("INSERT INTO Schedule4(Time) VALUES('0500')") # TUESDAY
    cur.execute("INSERT INTO Schedule4(Time) VALUES('SKIP')") # WEDNESDAY
    cur.execute("INSERT INTO Schedule4(Time) VALUES('SKIP')") # THURSDAY
    cur.execute("INSERT INTO Schedule4(Time) VALUES('0500')") # FRIDAY
    cur.execute("INSERT INTO Schedule4(Time) VALUES('SKIP')") # SATURDAY

    # prints back created table

    cur.execute("SELECT * FROM Schedule4")

    rows = cur.fetchall()

    for row in rows:
        print row

    # creates the schedule table

    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS Schedule5")
    cur.execute("CREATE TABLE Schedule5(Day INT PRIMARY KEY AUTO_INCREMENT, \
                 Time VARCHAR(25))")
    cur.execute("INSERT INTO Schedule5(Time) VALUES('0500')") # SUNDAY
    cur.execute("INSERT INTO Schedule5(Time) VALUES('SKIP')") # MONDAY
    cur.execute("INSERT INTO Schedule5(Time) VALUES('0500')") # TUESDAY
    cur.execute("INSERT INTO Schedule5(Time) VALUES('SKIP')") # WEDNESDAY
    cur.execute("INSERT INTO Schedule5(Time) VALUES('SKIP')") # THURSDAY
    cur.execute("INSERT INTO Schedule5(Time) VALUES('0500')") # FRIDAY
    cur.execute("INSERT INTO Schedule5(Time) VALUES('SKIP')") # SATURDAY

    # prints back created table

    cur.execute("SELECT * FROM Schedule5")

    rows = cur.fetchall()

    for row in rows:
        print row

    # creates the schedule table

    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS Schedule6")
    cur.execute("CREATE TABLE Schedule6(Day INT PRIMARY KEY AUTO_INCREMENT, \
                 Time VARCHAR(25))")
    cur.execute("INSERT INTO Schedule6(Time) VALUES('0500')") # SUNDAY
    cur.execute("INSERT INTO Schedule6(Time) VALUES('SKIP')") # MONDAY
    cur.execute("INSERT INTO Schedule6(Time) VALUES('0500')") # TUESDAY
    cur.execute("INSERT INTO Schedule6(Time) VALUES('SKIP')") # WEDNESDAY
    cur.execute("INSERT INTO Schedule6(Time) VALUES('SKIP')") # THURSDAY
    cur.execute("INSERT INTO Schedule6(Time) VALUES('0500')") # FRIDAY
    cur.execute("INSERT INTO Schedule6(Time) VALUES('SKIP')") # SATURDAY

    # prints back created table

    cur.execute("SELECT * FROM Schedule6")

    rows = cur.fetchall()

    for row in rows:
        print row

    # creates the data table

    cur.execute("DROP TABLE IF EXISTS Data")
    cur.execute("CREATE TABLE Data(Id INT PRIMARY KEY AUTO_INCREMENT, \
                 Info VARCHAR(25))")
    cur.execute("INSERT INTO Data(Info) VALUES('70.0')") # online temp (F)
    cur.execute("INSERT INTO Data(Info) VALUES('partly cloudy')") # online weather state (string)
    cur.execute("INSERT INTO Data(Info) VALUES('70.0')") # local temp (F)
    cur.execute("INSERT INTO Data(Info) VALUES('10')") # local humidity (%)
    cur.execute("INSERT INTO Data(Info) VALUES('10')") # local water sensor data (%)
    cur.execute("INSERT INTO Data(Info) VALUES('30')") # watering period (minutes)

    cur.execute("SELECT * FROM Data")

    rows = cur.fetchall()

    for row in rows:
        print row