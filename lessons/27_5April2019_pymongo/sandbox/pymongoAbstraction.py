#!/usr/bin/env python

# Date 2 April 2019
# pymongo demo for python2

# Inspiration of the source code (3 April 2018)
# ref: https://codehandbook.org/pymongo-tutorial-crud-operation-mongodb/

# To run this code, we must first establish a data directory and start up the mongod server
# Commands:
# Make the data directory
# mkdir ~/mondoDbData
# Run the MongoDB server
# . mongod --dbpath ~/mondoDbData
# ./pymongoAbstraction.py

from pymongo import MongoClient
import string

# creating connectioons for communicating with Mongo DB
client = MongoClient('localhost:27017')

db = client.AGENTS # the name of the database in mongo. this base may be found by the command, "show dbs" in mongo



def begin():
# driver method for the program
    print "  The agents database for use with MongoDB."
    print "  Uses the pymongo client"
    while(1):

	# choose an option to select a dataEmployee operation
        prmt = "   Welcome to the pyMongo automation program!\n   Select: 0 for DB information,\n\t  1 to insert,\n\t  2 to update,\n\t  3 to read,\n\t  4 to delete, or\n\t  q to Quit\n\t : "
        selection = raw_input(prmt)


        if selection == '0':
            info()
        elif selection == '1':
	    insert()
    	elif selection == '2':
	    update()
    	elif selection == '3':
	    read()
    	elif selection == '4':
            print 'delete'
	    delete()
        elif string.upper(selection) == 'Q':
            print " Exiting ... ",
            exit()
    	else:
	    print '\n INVALID SELECTION \n'
# end of begin()



def info():
# Function to get some information about the dataEmployee itself.
    print " Information about the dataEmployee."
    try:
        result = db.Employee.db
        print '\n Info: ',result

    except Exception, e:
        print str(e)

# end of info()



def insert():
# Function to insert data into mongo db
    try:
	employeeId = raw_input('Enter Employee id :')
	employeeFirstName = raw_input('Enter FirstName :')
	employeeLastName = raw_input('Enter LastName :')
	employeeAge = raw_input('Enter age :')
	employeeCountry = raw_input('Enter Country :')

# insert the data into the base
	db.Employee.insert_one(
	    {
		"id": employeeId,
	        "FirstName":employeeFirstName,
		"LastName":employeeLastName,
		"age":employeeAge,
		"country":employeeCountry
	    })
        print '\nInserted data successfully\n'

    except Exception, e:
        print str(e)
# end of insert()



def update():
# Function to update record to mongo db
    print "  Update:"
    try:

	employeeId = raw_input('  Enter Employee id :')
	employeeFirstName = raw_input('  Enter FirstName :')
	employeeLastName = raw_input('  Enter LastName :')
	employeeAge = raw_input('  Enter age :')
	employeeCountry = raw_input('  Enter Country :')


# update the record with the new information
	db.Employee.update_one(
	    {"id": employeeId},
	    {
		"$set": {
		    "firstName":employeeFirstName,
		    "lastName":employeeLastName,
		    "age":employeeAge,
		    "country":employeeCountry
		}
	    }
	)
	print "\nRecords updated successfully. \n"
    except Exception, e:
	print str(e)
# end of update()



def read():
# function to read records from mongo db
    try:
	empCol = db.Employee.find()
	print '\n Found: all data from DataEmployee \n'
	for emp in empCol:
	    print emp
    except Exception, e:
	print str(e)
# end of read()



# Function to delete record from mongo db
def delete():
    try:
	employeeId = raw_input('\nEnter employee id to delete\n')
        db.Employee.delete_many({"id":employeeId})
	print '\nDeletion successful\n'
    except Exception, e:
	print str(e)
#end of deltete()


begin() # start up the program: call the main function to begin
