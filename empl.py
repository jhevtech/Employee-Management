#building dictionary for employee info/records
dEmp = {
    1:{"name":"Tyson","job":"Mgr", "salary":90500.25},
    2:{"name":"Miguel","job":"Spvr", "salary":80000.55},
    3:{"name":"Dan","job":"SecAnlst", "salary":75000.25}
}

#function to list employees in database
def listEmp():
    global dEmp
    for keyEmp in dEmp:
        print(keyEmp, dEmp[keyEmp]["name"].capitalize(), ":", dEmp[keyEmp]["job"].capitalize(), ":", dEmp[keyEmp]["salary"])

#function to add new employee info to records
def addEmp():
    global dEmp
    strEmpName = input("Name of employee: ")
    strEmpJob = input("What is the employees job? ")
    floatSalary = float(input("Employees salary: "))
    intKey = getNewId()
    dIndEmp = {"name":strEmpName, "job":strEmpJob, "salary":floatSalary}
    dEmp[intKey] = dIndEmp
    print("List of employees:")
    listEmp()

#function to create ID for new employee
def getNewId():
    global dEmp
    arTemp = []
    for intKey in dEmp:
        arTemp.append(intKey)
    arTemp.sort(reverse=True)
    return arTemp[0] + 1

#function to remove an employee from database
def remEmp():
    global dEmp
    listEmp()
    intKey = int(input("Enter employee number you want to delete:"))
    dEmp.pop(intKey)
    print("Employee has been removed. Here is the updated list.")
    listEmp()
#creating ui
print("~" * 80)
print("|", "Welcome to the Employee Database".center(76),"|")
print("~" * 80)

def intro():
    print("Hi! What would you like to do today?")
#intro()
#print("Hi! What would you like to do today?")
    #loop for program
    while(True):

        # Present a menu choice.
        #listEmp()
        #print("Hi! What would you like to do today?")
        strMenu = input("1: View Employees,  2: Add Employee, 3: Remove Employee, 4: Exit: ")

        #ask user to view list
        if strMenu == "1":
            listEmp() 
        # If user chooses add employee, then add employee
        elif strMenu == "2":
            addEmp()
        # If user chooses remove employee, then remove employee.
        elif strMenu == "3":
            remEmp()
        elif strMenu == "4":
            break
        # Otherwise, invalid input
        else:
            print("Invalid input.")

        # Ask user if they would like to do more.
        print("Do something else?")
        strMenu2 = input("(y)es or (n)o: ")

        # If not, then exit and say goodbye
        if strMenu2 == "n":
            break
        else:
            strMenu = input("1: Add Employee, 2: Remove Employee: ")
            
            if strMenu == "1":
                    addEmp()
                # If user chooses remove employee, then remove employee.
            elif strMenu == "2":
                    remEmp()
            print("Do something else?")
            strMenu2 = input("(y)es or (n)o: ")

            #if strMenu2 == "n":
               # break

intro()
print("Goodbye.")