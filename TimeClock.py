from tkinter import *
import tkinter as tk
import random
import pickle
#import pandas as pd
#this is another db option related to excel, requires intall that didn't work on my pc, us pip in cmd on linux to install

#dark mode vars and setup
isDarkmode = True
bgColor = "#474342"
textColor = "white"
buttonColor = "slateblue"
borderColor = "black"
borderThickness = 2
clockInColor = "palegreen"
clockOutColor = "lightcoral"

#switches the values held in the variables to the ones that match colormode you are in
def darkMode():
    global bgColor
    global textColor
    global buttonColor
    global borderColor
    global clockInColor
    global clockOutColor
    if(isDarkmode):
        #bgColor = "black"
        #bgColor = "dimgray"
        bgColor = "#474342"
        textColor = "white"
        borderColor = "black"
        buttonColor = "slateblue"
        clockInColor = "palegreen"
        clockOutColor = "lightcoral"
    else:
        bgColor = "white"
        textColor = "black"
        borderColor = "gray"
        buttonColor = "dodgerblue"
        clockInColor = "green"
        clockOutColor = "firebrick"

windowArray = []
windowElements = []

#this is 
class Employee(object):
    def __init__(self, initfirstname, initlastname):
        self.firstname= initfirstname
        self.lastname= initlastname
        self.fullname= self.lastname + ", " + self.firstname
        #generates the digits of the id individually
        #may be unnecessary depending on how the nfc or rfid tags work
        self.idNumber = random.randint(0,9)
        for i in range(5):
            self.idNumber *= 10
            self.idNumber += random.randint(0,9)    

#data
#add employee objects to this array, this will be used to export data
employeeArray = []

#will be used to export data to an excel doc, will have to find a way to make that accessable, maybe use google drive api or some other method
#currently stores data in a database, need to add data retrieval to access the list
def exportData():
    #to put data in the dp: pickle.dump(employeeArray, open("employeeData.dat"),"wb")
    #to retrieve: pickel.load(open(employeeData.dat),"rb")
    print("Test exportData")

#############################
"""
#login window if the admin section is secured by password, other option is an nfc reader that is assigned as an admin
#may not be useful
adminLoginWindowElements = []
adminLoginWindow = None
def createAdminLoginWindow():
    #new window for login
    adminLoginWindow= Tk() 
    adminLoginWindow.title("Admin Login Window")
    adminLoginWindow.geometry("300x150")
    adminLoginWindow.config(bg=bgColor)
    adminLoginWindow.resizable(width=False, height=False)

    userLabel = Label(adminLoginWindow, text="Username:", fg=textColor, bg = bgColor, padx="5", pady="5", relief=FLAT)
    userLabel.pack(anchor=tk.NW)
    adminLoginWindowElements.append(userLabel)
    
    userTextbox = Text(adminLoginWindow, height= "1", width= "20", relief=FLAT)
    userTextbox.pack(anchor=tk.NW)
    adminLoginWindowElements.append(userTextbox)
    
    passLabel = Label(adminLoginWindow,text="Password:", fg=textColor, bg = bgColor, padx="5", pady="5", relief=FLAT)
    passLabel.pack(anchor=tk.NW)
    adminLoginWindowElements.append(passLabel)

    passTextbox = Entry(adminLoginWindow, width= "27", relief=FLAT)
    passTextbox.config(show="*")
    passTextbox.pack(anchor=tk.NW)
    adminLoginWindowElements.append(passTextbox)
    
    adminLoginBtn = Button(adminLoginWindow, text="Log In", fg= textColor, bg= buttonColor, padx="5", pady="5", command=adminWindow())
    #, command=adminWindow(userTextbox.get('1.0', END), passTextbox.get())
    
    adminLoginBtn.config(relief=FLAT)
    adminLoginBtn.pack(anchor=tk.SE)
    adminLoginWindowElements.append(adminLoginBtn) 
    
    adminLoginWindow.mainloop()
    print("Test adminLoginWindow()")

"""

#methods to test if the admin nfc reader or password matches the ones saved in a database
#have to figure out how to securely store passwords and nfc/rfid info
def validUsername(testUsername):
    print(testUsername)
    return True
    #return a boolean

def validPassword(testPassword):
    print(testPassword)
    return True
    #return a boolean

def test():
    print("test()")


adminWindow = None
adminWindowElements = []
def adminWindow():
    #username, password (args for line above) lines below are placeholders
    username = ""
    password = ""
    #check username and password here
    if(validUsername(username) and validPassword(password)):
        adminWindow = Tk() 
        adminWindow.title("Admin Window")
        adminWindow.geometry("750x500") 

        exportButton = Button(adminWindow,text="Export Data", fg= textColor, bg= buttonColor, padx="5", pady="5", command=exportData, relief=FLAT)
        exportButton.pack(anchor=tk.SE)
        adminWindowElements.append(exportButton)

        testButton = Button(adminWindow, text="Test Button", fg= textColor, bg= buttonColor, padx="5", pady="5", command=test, relief=FLAT)
        testButton.pack(anchor= tk.NE)

        #adminLoginWindow.loadtk()
        adminWindow.mainloop()
        print("Test adminWindow()") 
#########################################
#window setup
window = Tk()
window.title("Time Clock")
window.geometry("500x500")
window.config(bg=bgColor)

#ui elements
windowFrame = Frame(window, bg=bgColor)
windowFrame.config(highlightthickness=2, highlightbackground="black")
windowFrame.grid(pady=5,column=0,row=0)
windowElements.append(windowFrame)

nameLabel = Label(windowFrame, text="Name:", width="10", pady="5", fg= textColor, bg=bgColor)
nameLabel.grid(pady=5,column=0,row=1)
windowElements.append(nameLabel)
nameDisplayLabel = Label(windowFrame, text="____________", fg= textColor, bg=bgColor)
nameDisplayLabel.grid(pady=5,column=1,row=1)
windowElements.append(nameDisplayLabel)

idLabel = Label(windowFrame, text="ID:", width="10", pady="5", fg= textColor, bg=bgColor)
idLabel.grid(pady=5,column=3,row=1)
windowElements.append(idLabel)
idDisplayLabel = Label(windowFrame, text="________", fg= textColor, bg=bgColor)
idDisplayLabel.grid(pady=5,column=4,row=1)
windowElements.append(idDisplayLabel)

#test for employee objects, as well as the emplohee arrays
e1 = Employee("John", "Smith")
employeeArray.append(e1)
e2 = Employee("Suzy","Q")
employeeArray.append(e2)
e3 = Employee("Test","Three")
employeeArray.append(e3)
i = 0
def readNFCTEST():
    #change window or hide elements, display id number
    global i
    nameDisplayLabel.config(text=employeeArray[i].fullname)
    idDisplayLabel.config(text=employeeArray[i].idNumber)
    if(i<len(employeeArray)-1):
        i+=1
    else:
        i = 0

#ui elements
readNFCTestButton = Button(window, text="NFCTest", width="10", pady="5", bg= buttonColor, relief=FLAT)
readNFCTestButton.grid(pady=5,column=5,row=8)
windowElements.append(readNFCTestButton)

clockInButton = Button(windowFrame, text="Clock In", width="10", pady="5", bg=clockInColor, state=tk.DISABLED, relief=FLAT)
clockInButton.grid(pady=5,column=0,row=3)
windowElements.append(clockInButton)

clockOutButton = Button(windowFrame, text="Clock Out", width="10", pady="5", bg=clockOutColor, state=tk.DISABLED, relief=FLAT)
clockOutButton.grid(pady=5,column=1,row=3)
windowElements.append(clockOutButton)

adminLoginWindowButton = Button(window, text="Admin Login", padx="5", pady="5", bg= buttonColor,  command=adminWindow, relief=FLAT)
adminLoginWindowButton.grid(pady=5,column=5,row=1)
windowElements.append(adminLoginWindowButton)

def signOut():
    nameDisplayLabel.config(text="____________")
    idDisplayLabel.config(text="________")
    print("test signOut()")

signOutButton = Button(windowFrame, text="Sign Out", width="10", pady="5", bg= buttonColor, state=tk.DISABLED, command = signOut, relief=FLAT)
signOutButton.grid(pady=5,column=5,row=6)
windowElements.append(signOutButton)

def matchID(id):
    global employeeArray
    for i in range(len(employeeArray)):
        if(employeeArray[i].idNumber == id):
            return employeeArray[i]    
    print("matchID did not find a match")
    return None

currentNFCid = 0
currentEmployee = None
def readNFC():
    global currentNFCid
    global currentEmployee
    currentEmployee = matchID(currentNFCid)
    #however data is gotten
    #for now
    readNFCTEST()

    clockInButton.config(state=tk.NORMAL)
    clockOutButton.config(state=tk.NORMAL)
    signOutButton.config(state=tk.NORMAL)
    print("Test readNFC()")
readNFCTestButton.config(command=readNFC)


windowArray= [window, adminWindow]
#adminLoginWindow,

def changeColorMode():
    global isDarkmode
    global windowElements
    #global adminLoginWindow
    if(isDarkmode):
        isDarkmode = False
    else:
        isDarkmode = True
    darkMode()

    for i in range(len(windowElements)):
        if(windowElements[i]!= clockInButton and windowElements[i]!= clockOutButton):
            if(isinstance(windowElements[i], Button)):
                windowElements[i].config(fg= textColor, bg=buttonColor)
            elif(isinstance(windowElements[i], Frame)):
                windowElements[i].config(bg=bgColor, highlightbackground= borderColor)
            else:
                windowElements[i].config(fg= textColor, bg=bgColor)
        elif(windowElements[i] == clockInButton):
            clockInButton.config(bg= clockInColor)
        else:
            clockOutButton.config(bg= clockOutColor)
    if(False):
        #find a condition that can tell if the window was closed, there are problems if hte window has been opened and closed and this function is called.
        adminLoginWindow.config(bg=bgColor)
        for j in range(len(adminLoginWindowElements)):
            if(isinstance(adminLoginWindowElements[j], Button)):
                adminLoginWindowElements[j].config(fg= textColor, bg=buttonColor)

            else:
                adminLoginWindowElements[j].config(fg= textColor, bg=bgColor)
            
    window.config(bg= bgColor)
            
    print("changeColorMode()")

changeColorButton = Button(window, text="Change Colors", padx="5", pady="5", bg= buttonColor,  command=changeColorMode, relief=FLAT)
changeColorButton.grid(pady=5,column=5,row=2)
windowElements.append(changeColorButton)

window.mainloop()