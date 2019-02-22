#!/usr/bin/env python3

# 20 and 22 Feb 2019

import sqlite3

def query1(): # function in python3
    """shows the tables of the database"""
    sqlCommand1 = "SELECT name FROM sqlite_master WHERE type == 'table'"
    print("My command is: ", sqlCommand1)

    # run my query
    result = conn.execute(sqlCommand1)

    print("  Result is:", result)

    # collect my results and parse them
    tables = result.fetchall()

    # print the content to the screen
    print("  Raw tables data :", tables)
    for i in tables: # i is the index of the object ("list")
        print(" i=", i)
# end of query1()

def query2(): # function in python3
    """shows the content of the Instructor tables in the database"""
    sqlCommand2 = "SELECT * FROM Instructor"
    print("My command is: ", sqlCommand2)

    # run my query
    result = conn.execute(sqlCommand2)

    print("  Result is:", result)

    # collect my results and parse them
    tables = result.fetchall()

    # print the content to the screen
    print("  Raw tables data :", tables)
    for i in tables: # i is the index of the object ("list")
        print(" i=", i," column 4 of the table :", i[3])
# end of query2()

def insert1():
    """Simple Insertion"""
    
    PersonID = "10101A"
    name = "Milder"
    student = "S1A"
    deptName = "CompSci"
    salary =  195000.00
    #all on one line

    myInsert2 = "INSERT INTO instructor VALUES(\"{A}\",\"{B}\",\"{C}\",\"{D}\",{E})".format(A = PersonID, B = name, C = student, D = deptName, E = salary)

    print("  Running this command:\n  ",myInsert2)

    result = conn.execute(myInsert2)
    conn.commit() #save the changes
#end of insert1()





###################################
# connect to the database
sqlite3Filename ="myCampusDB.sqlite3"

#open my database connection
#conn = sqlite3.connect("myCampusDB.sqlite3")
conn = sqlite3.connect(sqlite3Filename)
print(" My database has been loaded")


# do something with the database
# functions
query1()
query2()
# finished; we close the database
conn.close()
