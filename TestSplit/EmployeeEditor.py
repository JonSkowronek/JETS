import random
import calendar
#employee stuff
employeeList = []
#may need to fix the next line
employeeList = pickel.load(employeelist, open("employeeData.dat", "rb"))

#object that represents employees. Holds their name and settings so the device can change settings when they sign in.
class Employee(object):
    #called in from the createAndDestroy function, takes arguments from menu inputs(textboxes and buttons),
    def __init__(self, initfirstname, initlastname, initVisualSettings, initAudioSettings):
        self.firstname= initfirstname
        self.lastname= initlastname
        self.fullname= self.lastname + ", " + self.firstname
        self.visualSettings = initVisualSettings
        self.audiosettings = initAudioSettings
        self.shiftStart = None
        self.hours = {}
        #generates the digits of the id individually
        #may be unnecessary or unsecure depending on how the nfc or rfid tags work
        self.idNumber = random.randint(0,9)
        for _ in range(5):
            self.idNumber *= 10
            self.idNumber += random.randint(0,9)

def defaultEmployee():
    return Employee("Steve", "Johnson", "dark", "partial")

#################
#used to look up the employee based on id number, may want to make methods that return x data of the employee when given their id number, might want to declare these methods much higher.
def getEmployeeObject(id):
    global employeeList
    for i in range(len(employeeList)):
        if(employeeList[i].idNumber == id):
            return employeeList[i]    
    print("matchID did not find a match")
    return None

#might not need the rest of these retrieval functions
def getFirstName(id):
    global employeeList
    for i in range(len(employeeList)):
        if(employeeList[i].idNumber == id):
            return employeeList[i].firstname
    print("matchID did not find a match")
    return None

def getLastName(id):
    global employeeList
    for i in range(len(employeeList)):
        if(employeeList[i].idNumber == id):
            return employeeList[i].lastname
    print("matchID did not find a match")
    return None

def getvisualSettings(id):
    global employeeList
    for i in range(len(employeeList)):
        if(employeeList[i].idNumber == id):
            return employeeList[i].visualSettings
    print("matchID did not find a match")
    return None

def getAudioSettings(id):
    global employeeList
    for i in range(len(employeeList)):
        if(employeeList[i].idNumber == id):
            return employeeList[i].audioSettings
    print("matchID did not find a match")
    return None
#####################

#for testing  above method
f = Employee("Nathan", "Malicki", "dark", "partial")
employeeList.append(f)
#print(getFirstName(f.idNumber))