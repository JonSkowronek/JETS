#!/usr/bin/env python
__author__ = "Nathan Malicki"
__version__ = "1.01"
__maintainer__ = "Nathan Malicki"
__email__ = "ntm5579@gmail.com"
__status__ = "development"
#################################
from tkinter import *
import tkinter as tk
import tkinter.font as font
import random

#colorblind mode vars
#link for python color names: https://python-graph-gallery.com/wp-content/uploads/100_Color_names_python.png
bgColor = "#4d4c4c" #background color for windows and frames
textColor = "white" #color for normal text, text on buttons, labels, etc.
buttonColor = "slateblue" #color for buttons
textBoxBgColor = "darkgray" #colors for the background of textboxes
borderThickness = 2 #borderthickness for textboxes, probrably unncessary
clockInColor = "palegreen" #color for the clock in button
clockOutColor = "lightcoral" #color for the clock out button
#widget.altColor to change the color when the button is pressed. - https://stackoverflow.com/questions/40023841/change-color-when-button-is-sunken-tkinter

#switches the values held in the variables to the ones that match colormode in the argument, can be called when a user is scanned in, find the user's preference with their id number
def colorBlindMode(color):
    global bgColor
    global textColor
    global buttonColor
    global textBoxBgColor
    global clockInColor
    global clockOutColor
    #uses argument to switch to the new mode
    if(color == "dark"):
        bgColor = "#4d4c4c"
        textColor = "white"
        textBoxBgColor = "darkgray"
        buttonColor = "slateblue"
        clockInColor = "palegreen"
        clockOutColor = "lightcoral"
    elif(color == "light"):
        bgColor = "white"
        textColor = "black"
        textBoxBgColor = "gray"
        buttonColor = "dodgerblue"
        clockInColor = "green"
        clockOutColor = "firebrick"
    #for testing - print("colorBlindMode()")

#store all tkinter widgets in here so their color can be switched with changeColorMode(color)
windowElements = []

#switches colors stored in vars to the correct ones then loops through all widgets and changes the colors of the tkninter widgets
def changeColorMode(color):
    global windowElements
    #switches the values stored to the correct theme/mode
    colorBlindMode(color)
    #goes through list of elements in windowElements
    for i in range(len(windowElements)):
        #checks for clockIn/OutButtons bc they are a different color than normal buttons
        #restructure this to have it only check for clockIn/Out when the element is a button
        if(windowElements[i]!= clockInButton and windowElements[i]!= clockOutButton):
            if(isinstance(windowElements[i], Button)):
                windowElements[i].config(fg= textColor, bg=buttonColor)
            elif(isinstance(windowElements[i], Frame)):
                windowElements[i].config(bg=bgColor, highlightbackground= textBoxBgColor)
            elif(isinstance(windowElements[i], Label)):
                windowElements[i].config(fg=textColor,bg=bgColor, highlightbackground= textBoxBgColor)
            elif(isinstance(windowElements[i], Text)):
                windowElements[i].config(fg=textColor,bg=textBoxBgColor)
            else:
                windowElements[i].config(fg= textColor, bg=bgColor)
        elif(windowElements[i] == clockInButton):
            clockInButton.config(fg=textColor,bg= clockInColor)
        else:
            clockOutButton.config(fg=textColor,bg= clockOutColor)
        window.config(bg = bgColor)
    print("changeColorMode()")


#object that represents employees. Holds their name and settings so the device can change settings when they sign in.
class Employee(object):
    #called in from the createAndDestroy function, takes arguments from menu inputs(textboxes and buttons),
    def __init__(self, initfirstname, initlastname, initVisualSettings, initAudioSettings):
        self.firstname= initfirstname
        self.lastname= initlastname
        self.fullname= self.lastname + ", " + self.firstname
        self.visualSettings = initVisualSettings
        self.audiosettings = initAudioSettings
        #generates the digits of the id individually
        #may be unnecessary or unsecure depending on how the nfc or rfid tags work
        self.idNumber = random.randint(0,9)
        for i in range(5):
            self.idNumber *= 10
            self.idNumber += random.randint(0,9)         

#data
#add employee objects to this array, this will be used to export data
employeeArray = []
####################################
#triggered when the add person button is pressed in the admin screen, this is used to bring up a new window where info about the employee is entered to make an object to represent them
def addPerson():
    addPersonWindow = Tk()
    addPersonWindow.title("Adding Employee")
    addPersonWindow.geometry("400x500") #size of the display, may have to resize everything when we have access to the real screen
    addPersonWindow.resizable(width=False, height=False)
    addPersonWindow.config(bg=bgColor)

    #frame in the addPerson window that contains the enetry field and buttons, sets info for employee constructor, should probably shift everything just onto the window, frame is unneccissary
    entryFrame = Frame(addPersonWindow, bg= bgColor, relief=FLAT)
    entryFrame.grid(column= 0, row=0)

    firstNameLabel = Label(entryFrame, fg=textColor, text="Employee First Name", padx="5", pady="5", bg= bgColor, relief=FLAT)
    firstNameLabel.grid(column=0, row = 0, padx= 10)
    windowElements.append(firstNameLabel)

    firstNameTextbox = Text(entryFrame, fg=textColor, height="1", width="20", bg= textBoxBgColor, relief=FLAT)
    firstNameTextbox.grid(column=0, row = 1, columnspan=2)
    windowElements.append(firstNameTextbox)
    
    lastNameLabel = Label(entryFrame, fg=textColor, text="Employee Last Name", padx="5", pady="5", bg= bgColor, relief=FLAT)
    lastNameLabel.grid(column=0, row = 2)
    windowElements.append(lastNameLabel)

    lastNameTextbox = Text(entryFrame, fg=textColor, height="1", width="20", bg= textBoxBgColor, relief=FLAT)
    lastNameTextbox.grid(column=0, row = 3, columnspan=2)
    windowElements.append(lastNameTextbox)

    colorOptionLabel = Label(entryFrame, fg=textColor, text="Color Options", padx="5", pady="5", bg= bgColor, relief=FLAT)
    colorOptionLabel.grid(column=0, row = 4)
    windowElements.append(colorOptionLabel)

    audioOptionLabel = Label(entryFrame, fg=textColor, text="Audio Options", padx="5", pady="5", bg= bgColor, relief=FLAT)
    audioOptionLabel.grid(column=1, row = 4)
    windowElements.append(audioOptionLabel)
    visualSetting = "Dark"
    audioSetting = "Partial Audio"

    #sets Visual Settings for when employee objects are created, handles button sinking and disabling
    def setColorModewithButtons(color):
        global visualSetting
        if(color == "dark"):
            #sets the selected button to sunken, every other button should be reset to normal state and flat
            setDarkModeButton.config(relief=SUNKEN, state = DISABLED)
            setLightModeButton.config(relief=FLAT, state = NORMAL)
            visualSetting = "Dark"
        elif(color == "light"):
            setLightModeButton.config(relief=SUNKEN, state = DISABLED)
            setDarkModeButton.config(relief=FLAT, state = NORMAL)
            visualSetting = "Light"
        #add more options for colormodes here

    setDarkModeButton = Button(entryFrame, fg=textColor, text="Dark Mode", padx="5", pady="5", bg= buttonColor, command= lambda: setColorModewithButtons("dark"), relief=SUNKEN, state=DISABLED)
    setDarkModeButton.grid(column=0, row = 5, pady= 5)
    windowElements.append(setDarkModeButton)

    setLightModeButton = Button(entryFrame, fg=textColor, text="LigthMode", padx="5", pady="5", bg= buttonColor, command= lambda: setColorModewithButtons("light"), relief=FLAT)
    setLightModeButton.grid(column=0, row = 6, pady= 5)
    windowElements.append(setLightModeButton)

    #sets Audio Settings for when employee objects are created, handles button sinking and disabling
    def setAudioModewithButtons(mode):
        global audioSetting
        if(mode == "No Audio"):
            #sets the selected button to sunken, every other button should be reset to normal state and flat
            noAudioButton.config(relief=SUNKEN, state = DISABLED)
            partialAudioButton.config(relief=FLAT, state = NORMAL)
            fullAudioButton.config(relief=FLAT, state = NORMAL)
            audioSetting = "No Audio"
        elif(mode == "Partial Audio"):
            noAudioButton.config(relief=FLAT, state = NORMAL)
            partialAudioButton.config(relief=SUNKEN, state = DISABLED)
            fullAudioButton.config(relief=FLAT, state = NORMAL)
            audioSetting = "Partial Audio"
        elif(mode == "Full Audio"):
            noAudioButton.config(relief=FLAT, state = NORMAL)
            partialAudioButton.config(relief=FLAT, state = NORMAL)
            fullAudioButton.config(relief=SUNKEN, state = DISABLED)
            audioSetting = "Full Audio"
        #add more options for colormodes here, prob an else also,

    noAudioButton = Button(entryFrame, fg=textColor, text="No Audio", padx="5", pady="5", bg= buttonColor, command= lambda: setAudioModewithButtons("No Audio"), relief=FLAT)
    noAudioButton.grid(column=1, row = 5, pady = 5)
    windowElements.append(noAudioButton)

    partialAudioButton = Button(entryFrame, fg=textColor, text="Partial Audio", padx="5", pady="5", bg= buttonColor, command= lambda: setAudioModewithButtons("Partial Audio"), relief=SUNKEN, state= DISABLED)
    partialAudioButton.grid(column=1, row = 6, pady = 5)
    windowElements.append(partialAudioButton)

    fullAudioButton = Button(entryFrame, fg=textColor, text="Full Audio", padx="5", pady="5", bg= buttonColor, command= lambda: setAudioModewithButtons("Full Audio"), relief=FLAT)
    fullAudioButton.grid(column=1, row = 7, pady = 5)
    windowElements.append(fullAudioButton)

    #creates the employee obeject with the name and the settings, destroys the employee creation window, only reason for this is bc cant have makeEmployee button do both, and other func is declared way above
    def createAndDestory(firstName, lastName, visualSetting, audioSetting):
        employeeArray.append(Employee(firstName, lastName, visualSetting, audioSetting))
        addPersonWindow.destroy()
    
    #executes above func ^
    makeEmployeeButton = Button(entryFrame, fg=textColor, text="Done", padx="5", pady="5", bg= buttonColor, command= lambda: createAndDestory(firstNameTextbox.get(1.0, "end"), 
    lastNameTextbox.get(1.0, "end"),visualSetting, audioSetting), relief=FLAT)
    makeEmployeeButton.grid(column=0, row = 10, columnspan=2, padx= 5)
    windowElements.append(makeEmployeeButton)

    #other frame for addPersonWindow, does not have anything on it rn, made bc I didn't do createAndDestroy yet, should be deleted, just double check
    displayFrame = Frame(addPersonWindow, bg= bgColor, relief=FLAT)
    displayFrame.grid(column=0, row= 1)
    windowElements.append(displayFrame)
    print("AddPerson()")

#implement
def removePerson():
    print("removePerson()")

#switches to the settings screen within the admin screen
def Settings():
    mainframe.forget()
    adminFrame.forget()
    signOutButton.forget()
    settingsFrame.pack()
    print("Settings()")

#will be used to export data to an excel doc, will have to find a way to make that accessable, maybe use google drive api or some other method
#currently stores data in a database, need to add data retrieval to access the list
def exportData():
    #to put data in the dp: pickle.dump(employeeArray, open("employeeData.dat"),"wb")
    #to retrieve: pickel.load(open(employeeData.dat),"rb")
    print("Test exportData")

########################################
#methods that switch the frame being displayed.
#displays the admin screen when admin card is swipped/tapped
def makeAdminFrame():
    mainframe.forget()
    settingsFrame.forget()
    adminFrame.pack()
    signOutButton.pack()
#brings up the main menu (employee facing screen)
def mainMenu():
    adminFrame.forget()
    signOutButton.forget()
    settingsFrame.forget()
    mainframe.pack()
#########################################
#main window setup
window = Tk()
window.title("Time Clock")
window.geometry("1024x600") #size of the display, may have to resize everything when the real screen gets here.
window.resizable(width=False, height=False)
window.config(bg=bgColor)
#takes away the title bar above the window, may want to comment out during testing
#window.overrideredirect(1)

#####################################################################
#frame that contains the main screeen that employees interact with
mainframe = Frame(window)
mainframe.pack()
windowElements.append(mainframe)

#button used to clock in, disabled until employee taps/swipe card
clockInButton = Button(mainframe, fg=textColor, text="Clock In", width="22", height= "11", bg=clockInColor, state=tk.DISABLED, relief=FLAT)
clockInButton['font'] = font.Font(size="30")
clockInButton.grid(column=0,row=0)
windowElements.append(clockInButton)

#button used to clock out, disabled until employee taps/swipe card
clockOutButton = Button(mainframe, fg=textColor, text="Clock Out", width="22", height= "11",  bg=clockOutColor, state=tk.DISABLED, relief=FLAT)
clockOutButton.grid(column=1,row=0)
clockOutButton['font'] = font.Font(size="30")
windowElements.append(clockOutButton)

#might not need, this could be brought up by swiping the admin card, mostly for testing
adminLoginWindowButton = Button(mainframe, fg=textColor, text="Admin Login", width="85", height="2", bg= buttonColor,  command=makeAdminFrame, relief=FLAT)
adminLoginWindowButton['font'] = font.Font(size="16")
adminLoginWindowButton.grid(column=0, columnspan = 2, row=1)
windowElements.append(adminLoginWindowButton)

########################
#all for testing, switch buttons to enable when I don't have cards or nfc reader.
def quick():
    if(clockInButton['state'] == NORMAL):
        clockInButton.config(state=DISABLED)
        clockOutButton.config(state=DISABLED)
    else:
        clockInButton.config(state=NORMAL)
        clockOutButton.config(state=NORMAL)

enableButtonsButtonWindowButton = Button(mainframe, fg=textColor, text="Enable", width="85", height="2", bg= "pink",  command=quick, relief=FLAT)
enableButtonsButtonWindowButton['font'] = font.Font(size="16")
enableButtonsButtonWindowButton.grid(column=0, columnspan = 2, row=2)
windowElements.append(enableButtonsButtonWindowButton)

#####################################################
#frame that comes up when an admin swipes their card, contains menu for settings, adding and removing users, as well as exporting the data.
adminFrame = Frame(window, bg= bgColor)
windowElements.append(adminFrame)

#button used to bring up a window to add people as employees
addPersonButton = Button(adminFrame, fg=textColor, text="Add Person", width="32", height="16", bg= buttonColor,  command=addPerson, relief=FLAT)
addPersonButton.grid(column= 0, row = 0, padx = 10, pady = 10)
windowElements.append(addPersonButton)

#buttons used to remove an employee, should have a confirm button before anything is done.
removePersonButton = Button(adminFrame, fg=textColor, text="Remove Person", width="32", height="16", bg= buttonColor,  command=removePerson, relief=FLAT)
removePersonButton.grid(column= 0, row = 1, padx = 10, pady = 10)
windowElements.append(removePersonButton)

#settings button in the adminWindow, brings up the settingsFrame
settingsIcon = PhotoImage(file= "D:\Coding\Time Clock\Gear.png")
settingsIcon = settingsIcon.subsample(2,2)
settingsButton = Button(adminFrame, fg=textColor, text="Settings", image= settingsIcon, compound=TOP, width="235", height="235", bg= buttonColor,  command=Settings, relief=FLAT)
settingsButton.grid(column= 1, row = 0, padx = 10, pady = 10)
windowElements.append(settingsButton)

#exports the data for week/month of the work hours of employees
exportButton = Button(adminFrame, fg=textColor, text="Export Data", width="32", height="16", bg= buttonColor,  command=exportData, relief=FLAT)
exportButton.grid(column= 1, row = 1, padx = 10, pady = 10)
windowElements.append(exportButton)

#used by the admin to sign out and returns to the main menu (employee screen), pack() above for arrangement reasons.
signOutButton = Button(window, fg=textColor, text="Sign Out", padx = "5", pady= "5", bg= buttonColor, command=mainMenu, relief=FLAT)
windowElements.append(signOutButton)
###########################################

#called when the settings are accessed. This allows the admins to change the current visual and audio settings of the device, as well as other options
settingsFrame = Frame(window, bg= bgColor)
windowElements.append(settingsFrame)

#Holds the label and buttons for the colorblind modes, subframe of settingsFrame
colorBlindSettingsFrame = Frame(settingsFrame, bg= bgColor)
colorBlindSettingsFrame.grid(column= 0, row = 0, padx=5, pady= 5)
windowElements.append(colorBlindSettingsFrame)

#label above the colorblined modes in the admin settings.
colorblindModeLabel = Label(colorBlindSettingsFrame, text="Change Colorblind Settings", padx="5", pady="5", bg= bgColor, relief=FLAT)
colorblindModeLabel.grid(column= 0, row = 0, pady= 5)
windowElements.append(colorblindModeLabel)

#button that sets the current theme to dark mode
darkModeButton = Button(colorBlindSettingsFrame, text="Dark Mode", padx="5", pady="5", bg= buttonColor, command= lambda: changeColorMode("dark"), relief=FLAT)
darkModeButton.grid(column= 0, row = 1, pady= 5)
windowElements.append(darkModeButton)

#button that sets the current theme to light mode
lightModeButton = Button(colorBlindSettingsFrame, text="Light Mode", padx="5", pady="5", bg= buttonColor, command= lambda: changeColorMode("light"),  relief=FLAT)
lightModeButton.grid(column= 0, row = 2, pady= 5)
windowElements.append(lightModeButton)

#subframe of settingsframe that contains the label and the buttons of the audio options
audioSettingsFrame = Frame(settingsFrame, bg= bgColor)
audioSettingsFrame.grid(column= 1, row = 0, padx=5, pady= 5)
windowElements.append(audioSettingsFrame)

#label above the audio option buttons
audioModeLabel = Label(audioSettingsFrame, text="Change Audio Settings", padx="5", pady="5", bg= bgColor, relief=FLAT)
audioModeLabel.grid(column= 0, row = 0, pady= 5)
windowElements.append(audioModeLabel)

#button that sets the current audio mode to full audio, not sure what that means yet.
setFullAudioButton = Button(audioSettingsFrame, text="Full Audio", padx="5", pady="5", bg= buttonColor, command= None, relief=FLAT)
setFullAudioButton.grid(column= 0, row = 3, pady= 5)
windowElements.append(setFullAudioButton)

#button that sets the current audio mode to partial audio, not sure what that means yet.
setPartialAudioButton = Button(audioSettingsFrame, text="Partial Audio", padx="5", pady="5", bg= buttonColor, command= None, relief=FLAT)
setPartialAudioButton.grid(column= 0, row = 2, pady= 5)
windowElements.append(setPartialAudioButton)

#button that sets the current audio mode to no audio, not sure what that means yet, not even sure this will be a mode in production build.
setNoAudioButton = Button(audioSettingsFrame, text="No Audio", padx="5", pady="5", bg= buttonColor, command= None, relief=FLAT)
setNoAudioButton.grid(column= 0, row = 1, pady= 5)
windowElements.append(setNoAudioButton)

#button that takes you back to the admin screen from the admin settings menu.
backToAdmin = Button(settingsFrame, text="Back", padx="5", pady="5", bg= buttonColor, command=makeAdminFrame, relief=FLAT)
backToAdmin.grid(column= 0, row = 1, columnspan=2, pady= 5)
windowElements.append(backToAdmin)


#a method that will sign the user out if another card is swiped or the user has not interacted with the screen in x seconds.
def signOut():
    print("test signOut()")

#used to look up the employee based on id number, may want to make methods that return x data of the employee when given their id number, might want to declare these methods much higher.
def matchID(id):
    global employeeArray
    for i in range(len(employeeArray)):
        if(employeeArray[i].idNumber == id):
            return employeeArray[i]    
    print("matchID did not find a match")
    return None

#values for when the id is scanned.
currentNFCid = 0
currentEmployee = None

window.mainloop()