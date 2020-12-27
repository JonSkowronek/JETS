__author__ = "Nathan Malicki"
__version__ = "1.05"
__maintainer__ = "Nathan Malicki"
__email__ = "ntm5579@gmail.com"
__status__ = "development"

import pickle
from datetime import datetime
from datetime import date
from datetime import timedelta
import EmployeeEditor
#from math import abs

def timeParce(parceType):
    if(parceType == "date"):
        return datetime.now()

#to put data in the dp: pickle.dump(employeeList, open("employeeData.dat"),"wb")
#to retrieve: pickel.load(open(employeeData.dat),"rb")

#may need to do some calendar config here, setting the first day of the week, etc

#when the employee clocks in the time and date need to be taken.
def processClockIn(employee):
    currentEmployee = employee
    #saves the current date and time, cuts off the miliseconds 
    currentEmployee.shiftStart = datetime.now().replace(microsecond=0)
    print("ProcessClockIn()", currentEmployee.shiftStart)

#when the employee clocks out the new data of the hours needs to be pickled
#make sure this works for a possible night shift, use time delta to figure out the dif for you
def processClockOut(employee):
    currentEmployee = employee
    #stores the date time in a dictionary with the key being the date of when the object is stored
    currentEmployee.hours[datetime.now().date()] = datetime.now().replace(microsecond=0) - currentEmployee.shiftStart.replace(microsecond=0)
    currentEmployee.shiftStart = None
    #prints are testing
    print("ProcessClockOut()", datetime.now().replace(microsecond=0))
    try:
        print("testing dictionary retrieval", currentEmployee.hours[date(2020, 12, 26)])
    except KeyError:
        print("Error, the key did not match any dates in the database of the retrieval is messed up")

    #current issue: NameError: name 'employeelist' is not defined
    #pickle.dump(employeelist, open("employeeData.dat", "wb"))

    #how to access the info for an employee on a date: Employee.hours[date(2020, 12, 26)]
    #might not need this
    #return currentEmployee.hours[datetime.now().replace(microsecond=0)]
