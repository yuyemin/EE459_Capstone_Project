# creates the tables for us to use
# CB: Michael Kukar

import MySQLdb as mdb

con = mdb.connect('localhost', 'group15', 'finalproject', 'finalproject')

with con:

    # creates the schedule table (stores day and the program scheduled for that day)

    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS Schedule")
    cur.execute("CREATE TABLE Schedule(Day INT PRIMARY KEY AUTO_INCREMENT, \
                 Time VARCHAR(25))")
    cur.execute("INSERT INTO Schedule(Time) VALUES('1')") # Monday
    cur.execute("INSERT INTO Schedule(Time) VALUES('0')") # Tuesday
    cur.execute("INSERT INTO Schedule(Time) VALUES('0')") # Weds
    cur.execute("INSERT INTO Schedule(Time) VALUES('1')") # Th
    cur.execute("INSERT INTO Schedule(Time) VALUES('0')") # F
    cur.execute("INSERT INTO Schedule(Time) VALUES('2')") # S
    cur.execute("INSERT INTO Schedule(Time) VALUES('0')") # Su

    # prints back created table

    cur.execute("SELECT * FROM Schedule")

    rows = cur.fetchall()

    for row in rows:
        print row

    # creates the program tables (zone matched to the time to run said zone (in minutes))

    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS Program1")
    cur.execute("CREATE TABLE Program1(Day INT PRIMARY KEY AUTO_INCREMENT, \
                 Time VARCHAR(25))")
    cur.execute("INSERT INTO Program1(Time) VALUES('20')") # Zone 1
    cur.execute("INSERT INTO Program1(Time) VALUES('20')") # Zone 2
    cur.execute("INSERT INTO Program1(Time) VALUES('20')") # Zone 3
    cur.execute("INSERT INTO Program1(Time) VALUES('20')") # Zone 4
    cur.execute("INSERT INTO Program1(Time) VALUES('20')") # Zone 5
    cur.execute("INSERT INTO Program1(Time) VALUES('20')") # Zone 6
    cur.execute("INSERT INTO Program1(Time) VALUES('1010')") # START TIME

    # prints back created table

    cur.execute("SELECT * FROM Program1")

    rows = cur.fetchall()

    for row in rows:
        print row

    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS Program2")
    cur.execute("CREATE TABLE Program2(Day INT PRIMARY KEY AUTO_INCREMENT, \
                 Time VARCHAR(25))")
    cur.execute("INSERT INTO Program2(Time) VALUES('10')") # Zone 1
    cur.execute("INSERT INTO Program2(Time) VALUES('10')") # Zone 2
    cur.execute("INSERT INTO Program2(Time) VALUES('10')") # Zone 3
    cur.execute("INSERT INTO Program2(Time) VALUES('10')") # Zone 4
    cur.execute("INSERT INTO Program2(Time) VALUES('10')") # Zone 5
    cur.execute("INSERT INTO Program2(Time) VALUES('10')") # Zone 6
    cur.execute("INSERT INTO Program2(Time) VALUES('1010')") # START TIME

    # prints back created table

    cur.execute("SELECT * FROM Program2")

    rows = cur.fetchall()

    for row in rows:
        print row

    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS Program3")
    cur.execute("CREATE TABLE Program3(Day INT PRIMARY KEY AUTO_INCREMENT, \
                 Time VARCHAR(25))")
    cur.execute("INSERT INTO Program3(Time) VALUES('30')") # Zone 1
    cur.execute("INSERT INTO Program3(Time) VALUES('30')") # Zone 2
    cur.execute("INSERT INTO Program3(Time) VALUES('30')") # Zone 3
    cur.execute("INSERT INTO Program3(Time) VALUES('30')") # Zone 4
    cur.execute("INSERT INTO Program3(Time) VALUES('30')") # Zone 5
    cur.execute("INSERT INTO Program3(Time) VALUES('30')") # Zone 6
    cur.execute("INSERT INTO Program3(Time) VALUES('1010')") # START TIME

    # prints back created table

    cur.execute("SELECT * FROM Program3")

    rows = cur.fetchall()

    for row in rows:
        print row