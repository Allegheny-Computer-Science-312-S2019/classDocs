#!/usr/bin/env python3

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


def insert1(): # function in python3
#TODO: complete insert statement

    """inserting data in to Instructor table"""
    insertCommand1 = "SELECT * FROM Instructor"
    print("My command is: ", insertCommand1)

    # run my query
    result = conn.execute(insertCommand1)

    print("  Result is:", result)

    # collect my results and parse them
    tables = result.fetchall()

    # print the content to the screen
    print("  Raw tables data :", tables)
    for i in tables: # i is the index of the object ("list")
        print(" i=", i," column 4 of the table :", i[3])
# end of insert1()




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
