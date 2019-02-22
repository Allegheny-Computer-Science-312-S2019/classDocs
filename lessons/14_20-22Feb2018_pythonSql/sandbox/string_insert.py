#strings

myCollege_str = "Allegheny"
mesg_str = "I go to {A} College".format(A = myCollege_str)
print(mesg_str)


##################
### Insert something
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
