#!/usr/bin/env python
__author__ = "Nathan Malicki"
__version__ = "1.05"
__maintainer__ = "Nathan Malicki"
__email__ = "ntm5579@gmail.com"
__status__ = "development"
#################################
from tkinter import *
from tkinter import ttk
import tkinter as tk
import tkinter.font as font
from threading import *
from time import *
import random
from EmployeeEditor import *
from EmployeeEditor import employeeList
import EmployeeData
from Settings import *

#this might cause circular import
#from AudioSettings import *

#################################
#colorblind and theme stuff, link for python color names: https://python-graph-gallery.com/wp-content/uploads/100_Color_names_python.png
bgColor = "#4d4c4c" #background color for windows and frames
textColor = "white" #color for normal text, text on buttons, labels, etc.
buttonColor = "slateblue" #color for buttons
textBoxBgColor = "darkgray" #colors for the background of textboxes
borderThickness = 2 #borderthickness for textboxes, probrably unncessary
clockInColor = "palegreen" #color for the clock in button (shade of green in noncolorblind themes)
clockOutColor = "lightcoral" #color for the clock out button (shade of red in noncolorblind themes)
#widget.altColor to change the color when the button is pressed, needs to be implimented. - https://stackoverflow.com/questions/40023841/change-color-when-button-is-sunken-tkinter

#switches the values held in the variables to the ones that match colormode in the argument, can be called when a user is scanned in, find the user's preference with their id number
def colorBlindMode(color):
    global bgColor
    global textColor
    global buttonColor
    global textBoxBgColor
    global clockInColor
    global clockOutColor
    #uses argument to switch to the correct new mode
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
    #for testing- print("colorBlindMode()")

#store all tkinter widgets in here so their color can be switched with changeColorMode(color)
windowElements= []
addPersonElements= []
removePersonElements= []
#may need to switch this to a window
exportSettingsWindow= []

#needs to be restructed for the
#switches colors stored in vars to the correct ones then loops through all widgets and changes the colors of the tkninter widgets
def changeColorMode(color):
    global windowElements
    #switches the values stored to the correct theme/mode
    colorBlindMode(color)
    #goes through list of elements in windowElements
    if(True):
        for i in range(len(windowElements)):
            #checks for clockIn/OutButtons bc they are a different color than normal buttons, if specific elements need other colors, check for that specific instance inside their widget type
            if(isinstance(windowElements[i], Button)):
                if(windowElements[i] == clockInButton):
                    clockInButton.config(fg=textColor,bg= clockInColor)
                elif(windowElements[i] == clockOutButton):
                    clockOutButton.config(fg=textColor,bg= clockOutColor)
                else:
                    windowElements[i].config(fg= textColor, bg=buttonColor)
            elif(isinstance(windowElements[i], Frame)):
                windowElements[i].config(bg=bgColor, highlightbackground= textBoxBgColor)
            elif(isinstance(windowElements[i], Label)):
                windowElements[i].config(fg=textColor,bg=bgColor, highlightbackground= textBoxBgColor)
            elif(isinstance(windowElements[i], Text)):
                windowElements[i].config(fg=textColor,bg=textBoxBgColor)
            else:
                windowElements[i].config(fg= textColor, bg=bgColor)
            window.config(bg = bgColor)
    elif(True):    
        #this needs to change
        for i in range(len(addPersonElements)):
            if(isinstance(addPersonElements[i], Button)):
                if(addPersonElements[i] == clockInButton):
                    clockInButton.config(fg=textColor,bg= clockInColor)
                elif(addPersonElements[i] == clockOutButton):
                    clockOutButton.config(fg=textColor,bg= clockOutColor)
                else:
                    addPersonElements[i].config(fg= textColor, bg=buttonColor)
            elif(isinstance(addPersonElements[i], Frame)):
                addPersonElements[i].config(bg=bgColor, highlightbackground= textBoxBgColor)
            elif(isinstance(addPersonElements[i], Label)):
                addPersonElements[i].config(fg=textColor,bg=bgColor, highlightbackground= textBoxBgColor)
            elif(isinstance(addPersonElements[i], Text)):
                addPersonElements[i].config(fg=textColor,bg=textBoxBgColor)
            else:
                addPersonElements[i].config(fg= textColor, bg=bgColor)
            addPersonWindow.config(bg = bgColor)
    elif(True):
        #this needs to change
        if(isinstance(removePersonElements[i], Button)):
            if(removePersonElements[i] == clockInButton):
                clockInButton.config(fg=textColor,bg= clockInColor)
            elif(removePersonElements[i] == clockOutButton):
                clockOutButton.config(fg=textColor,bg= clockOutColor)
            else:
                removePersonElements[i].config(fg= textColor, bg=buttonColor)
        elif(isinstance(removePersonElements[i], Frame)):
            removePersonElements[i].config(bg=bgColor, highlightbackground= textBoxBgColor)
        elif(isinstance(removePersonElements[i], Label)):
            removePersonElements[i].config(fg=textColor,bg=bgColor, highlightbackground= textBoxBgColor)
        elif(isinstance(removePersonElements[i], Text)):
            removePersonElements[i].config(fg=textColor,bg=textBoxBgColor)
        else:
            removePersonElements[i].config(fg= textColor, bg=bgColor)
        removePersonWindow.config(bg = bgColor)

    print("changeColorMode()")

#################################
checkBoxList = []

####################################
#admin settings
#triggered when the add person button is pressed in the admin screen, this is used to bring up a new window where info about the employee is entered to make an object to represent them
def addPerson():
    addPersonWindow = Tk()
    addPersonWindow.title("Adding Employee")
    addPersonWindow.geometry("400x500") #size of the display, may have to resize everything when we have access to the real screen
    addPersonWindow.resizable(width=False, height=False)
    addPersonWindow.config(bg=bgColor)

    firstNameLabel = Label(addPersonWindow, fg=textColor, text="Employee First Name", padx="5", pady="5", bg= bgColor, relief=FLAT)
    firstNameLabel.grid(column=0, row = 0, padx= 10)
    windowElements.append(firstNameLabel)

    firstNameTextbox = Text(addPersonWindow, fg=textColor, height="1", width="35", bg= textBoxBgColor, relief=FLAT)
    firstNameTextbox.grid(column=0, row = 1, columnspan=2, padx = "15")
    windowElements.append(firstNameTextbox)
    
    lastNameLabel = Label(addPersonWindow, fg=textColor, text="Employee Last Name", padx="5", pady="5", bg= bgColor, relief=FLAT)
    lastNameLabel.grid(column=0, row = 2)
    windowElements.append(lastNameLabel)

    lastNameTextbox = Text(addPersonWindow, fg=textColor, height="1", width="35",  bg= textBoxBgColor, relief=FLAT)
    lastNameTextbox.grid(column=0, row = 3, columnspan=2, padx = "15")
    windowElements.append(lastNameTextbox)

    colorOptionLabel = Label(addPersonWindow, fg=textColor, text="Color Options", padx="5", pady="5", bg= bgColor, relief=FLAT)
    colorOptionLabel.grid(column=0, row = 4)
    windowElements.append(colorOptionLabel)

    audioOptionLabel = Label(addPersonWindow, fg=textColor, text="Audio Options", padx="5", pady="5", bg= bgColor, relief=FLAT)
    audioOptionLabel.grid(column=1, row = 4)
    windowElements.append(audioOptionLabel)
    visualSetting = "Dark"
    audioSetting = "Partial Audio"
    
    noAudioButton = Button(addPersonWindow, fg=textColor, text="No Audio", padx="5", pady="5", bg= buttonColor, command= lambda: setAudioModewithButtons("No Audio"), relief=FLAT)
    noAudioButton.grid(column=1, row = 5, pady = 5)
    windowElements.append(noAudioButton)

    partialAudioButton = Button(addPersonWindow, fg=textColor, text="Partial Audio", padx="5", pady="5", bg= buttonColor, command= lambda: setAudioModewithButtons("Partial Audio"), relief=SUNKEN, state= DISABLED)
    partialAudioButton.grid(column=1, row = 6, pady = 5)
    windowElements.append(partialAudioButton)

    #creates the employee obeject with the name and the settings, destroys the employee creation window, only reason for this is bc cant have makeEmployee button do both, and other func is declared way above
    def createAndDestory(firstName, lastName, visualSetting, audioSetting):
        employeeList.append(Employee(firstName, lastName, visualSetting, audioSetting))
        #update the db to store new list?
        addPersonWindow.destroy()

    fullAudioButton = Button(addPersonWindow, fg=textColor, text="Full Audio", padx="5", pady="5", bg= buttonColor, command= lambda: setAudioModewithButtons("Full Audio"), relief=FLAT)
    fullAudioButton.grid(column=1, row = 7, pady = 5)
    windowElements.append(fullAudioButton)
    #executes above func ^
    
    makeEmployeeButton = Button(addPersonWindow, fg=textColor, text="Done", padx="5", pady="5", bg= buttonColor, command= lambda: createAndDestory(firstNameTextbox.get(1.0, "end"), 
    lastNameTextbox.get(1.0, "end"),visualSetting, audioSetting), relief=FLAT)
    makeEmployeeButton.grid(column=0, row = 10, columnspan=2, padx= 5)
    windowElements.append(makeEmployeeButton)

    #################

    darkModeButton = Button(addPersonWindow, fg=textColor, text="Dark Mode", padx="5", pady="5", bg= buttonColor, command= lambda: setColorModewithButtons("dark"), relief=SUNKEN, state=DISABLED)
    darkModeButton.grid(column=0, row = 5, pady= 5)
    windowElements.append(darkModeButton)

    lightModeButton = Button(addPersonWindow, fg=textColor, text="LigthMode", padx="5", pady="5", bg= buttonColor, command= lambda: setColorModewithButtons("light"), relief=FLAT)
    lightModeButton.grid(column=0, row = 6, pady= 5)
    windowElements.append(lightModeButton)

   

    #other frame for addPersonWindow, does not have anything on it rn, made bc I didn't do createAndDestroy yet, should be deleted, just double check
    """
    displayFrame = Frame(addPersonWindow, bg= bgColor, relief=FLAT)
    displayFrame.grid(column=0, row= 1)
    windowElements.append(displayFrame)
    """
    print("AddPerson()")

#started but not finished, have to get db working to pull the data
#issues because of file split, not sure how to fix
def removePerson():
    removePersonWindow = Tk()
    removePersonWindow.title("Remove Employee")
    removePersonWindow.geometry("400x500") #size of the display, may have to resize everything when we have access to the real screen
    removePersonWindow.resizable(width=False, height=False)
    removePersonWindow.config(bg=bgColor)

    removePersonCanvas = Canvas(removePersonWindow, bg= bgColor, width = 400, height= 500, scrollregion= (0,0,400,700))#may want to change scroll region based on how many employees there are
    removePersonCanvas.pack(fill= BOTH, expand = 1)
    windowElements.append(removePersonCanvas)
    ybar = Scrollbar(removePersonCanvas, orient= VERTICAL)
    ybar.pack(side= RIGHT, fill= Y)
    ybar.config(command= removePersonCanvas.yview)
    removePersonCanvas.config(yscrollcommand=ybar.set)
    #as of now do not need: removePersonCanvas.bind("<configure>", lambda e: removePersonCanvas.bbox('all'))

    removePersonFrame = Frame(removePersonCanvas, bg= bgColor)
    windowElements.append(removePersonFrame)

    removePersonCanvas.create_window((0,0), window=removePersonFrame, anchor= "nw")
    
    ##############
    #for testing
    testLabel = Label(removePersonFrame, fg= textColor, text = "Test", bg= bgColor, relief= FLAT)
    testLabel.pack()

    testEmployee = defaultEmployee()
    employeeList.append(testEmployee)
    ########################
    #currently not working, does not check properly
    global checkBoxList
    for employee in employeeList:
        checkBoxList.append(Checkbutton(removePersonFrame, fg= textColor, text= employee.fullname, bg= bgColor, relief= FLAT))
    for checkbox in checkBoxList:
        #checkbox.pack(anchor= N)
        checkbox.pack(anchor= CENTER)

    completeRemoveButton = Button(removePersonFrame, fg= textColor, text= "Done", bg= buttonColor, relief= FLAT)
    completeRemoveButton.pack(side= BOTTOM)

    print("removePerson()")

#switches to the settings screen within the admin screen
def Settings():
    mainframe.forget()
    adminFrame.forget()
    exportSettingsFrame.forget()
    settingsFrame.pack()
    print("Settings()")

exportMethod = "wifi"

#will be used to export data to an excel doc, will have to find a way to make that accessable, maybe use google drive api or some other method
#currently stores data in a database, need to add data retrieval to access the list
def exportData():
    #to put data in the dp: pickle.dump(employeeList, open("employeeData.dat"),"wb")
    #to retrieve: pickel.load(open(employeeData.dat),"rb")
    '''
    exportSettingsWindow = Tk()
    exportSettingsWindow.title("Export Settings")
    exportSettingsWindow.geometry("275x200")
    exportSettingsWindow.resizable(width=False, height=False)
    exportSettingsWindow.config(bg=bgColor)
    
    '''
    mainframe.forget()
    adminFrame.forget()
    settingsFrame.forget()
    exportSettingsFrame.pack()

################################################
#methods that switch the frame being displayed.
#displays the admin screen when admin card is swipped/tapped
def makeAdminFrame():
    mainframe.forget()
    settingsFrame.forget()
    exportSettingsFrame.forget()
    adminFrame.pack()
#brings up the main menu (employee facing screen)
def mainMenu():
    adminFrame.forget()
    settingsFrame.forget()
    exportSettingsFrame.forget()
    mainframe.pack()
#########################################
#main window setup
window = Tk()
window.title("Time Clock")
window.geometry("1024x600") #size of the display, may have to resize everything when the real screen gets here.
window.resizable(width=False, height=False)
#window.resizable(width=True, height=True)
window.config(bg=bgColor)
#takes away the title bar above the window, may want to comment out during testing
#window.overrideredirect(1)

#####################################################################
#frame that contains the main screeen that employees interact with
mainframe = Frame(window)
mainframe.pack()
windowElements.append(mainframe)

#keepsleeping and other stuff has to be figured out
threadObjList = []
keepSleeping = TRUE

#when done with this method remove the currentEmployee = ___ code in the last few lines
def clockIn():
    global currentEmployee
    clockOutButton.config(state= tk.NORMAL)
    clockInButton.config(state= tk.DISABLED)
    EmployeeData.processClockIn(currentEmployee)

    #code in production for threading, used to auto sign out after a specified amount of time., add this code to any of the buttons on the main screen(Clock out Button, etc).
    """
    global threadObjList
    global keepSleeping
    keepSleeping = FALSE
    #may not work, only works if return ends the thread
    #keepSleeping = TRUE
    threadObjList.append(ThreadObj())
    print(threadObjList[len(threadObjList) - 1].num)
    threadObjList[len(threadObjList) - 1].thread.start()
    """
    #To Be Done: disable the buttons accordingly when they are clicked to prevent an error from setting current employee to None

#button used to clock in, disabled until employee taps/swipe card
clockInButton = Button(mainframe, fg=textColor, text="Clock In", width="22", height= "11", bg=clockInColor, command=clockIn, state=tk.DISABLED, relief=FLAT)
clockInButton['font'] = font.Font(size="30")
clockInButton.grid(column=0,row=0)
windowElements.append(clockInButton)

def clockOut():
    global currentEmployee
    #Switches Stuff IDK
    clockInButton.config(state= tk.NORMAL)
    clockOutButton.config(state= tk.DISABLED)
    EmployeeData.processClockOut(currentEmployee)
    #To Be Done: disable clock out button when card is swiped, only enable the sign out button when the person who is logged in is currently clocked in

#button used to clock out, disabled until employee taps/swipe card
clockOutButton = Button(mainframe, fg=textColor, text="Clock Out", width="22", height= "11",  bg=clockOutColor, command=clockOut, state=tk.DISABLED, relief=FLAT)
clockOutButton.grid(column=1,row=0)
clockOutButton['font'] = font.Font(size="30")
windowElements.append(clockOutButton)

#might not need, this could be brought up by swiping the admin card, mostly for testing
adminLoginWindowButton = Button(mainframe, fg=textColor, text="Admin Login", width="85", height="2", bg= buttonColor,  command=makeAdminFrame, relief=FLAT)
adminLoginWindowButton['font'] = font.Font(size="16")
adminLoginWindowButton.grid(column=0, columnspan = 2, row=1)
windowElements.append(adminLoginWindowButton)

########################
#all for testing, switch buttons to enable when I don't have cards or nfc reader. Should be deleted when nfc is fully implemented.
#threading has been disbaled for now to test other methods
def clockingButtonToggle():
    #put something to start thread/process here
    if(clockInButton['state'] == NORMAL):
        clockInButton.config(state=DISABLED)
        clockOutButton.config(state=DISABLED)
    else:
        clockInButton.config(state=NORMAL)
        #clockInBUtton.config(state=DISABLED), this should stay commented, but is here for testing, should only be able to clock out if you are currently clocked in
        #waitThread.start()

enableButtonsButtonWindowButton = Button(mainframe, fg=textColor, text="Enable", width="85", height="2", bg= "pink",  command=clockingButtonToggle, relief=FLAT)
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
#settingsIcon = PhotoImage(file= "D:\Coding\Time Clock\Images\Gear.png")
#settingsIcon = settingsIcon.subsample(2,2)
#adjust height and width below to somewhere in the 200s range if you add back the pictures
settingsButton = Button(adminFrame, fg=textColor, text="Settings", compound=TOP, width="32", height="16", bg= buttonColor,  command=Settings, relief=FLAT)
settingsButton.grid(column= 1, row = 0, padx = 10, pady = 10)
windowElements.append(settingsButton)

#exports the data for week/month of the work hours of employees
exportButton = Button(adminFrame, fg=textColor, text="Export Data", width="32", height="16", bg= buttonColor,  command=exportData, relief=FLAT)
exportButton.grid(column= 1, row = 1, padx = 10, pady = 10)
windowElements.append(exportButton)

#used by the admin to sign out and returns to the main menu (employee screen), pack() above for arrangement reasons.
signOutButton = Button(adminFrame, fg=textColor, text="Sign Out", padx = "5", pady= "5", bg= buttonColor, command=mainMenu, relief=FLAT)
signOutButton.grid(column = 0, row = 3, columnspan = 2)
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
colorblindModeLabel = Label(colorBlindSettingsFrame, fg=textColor, text="Set Default Theme/Colorblind Settings", padx="5", pady="5", bg= bgColor, relief=FLAT)
colorblindModeLabel.grid(column= 0, row = 0, pady= 5)
windowElements.append(colorblindModeLabel)

def sinkButtonsChangeColor(color):
    global visualSetting
    if(color == "dark"):
        #sets the selected button to sunken, every other button should be reset to normal state and flat
        defaultDarkModeButton.config(relief=SUNKEN, state = DISABLED)
        defaultLightModeButton.config(relief=FLAT, state = NORMAL)
        changeColorMode("dark")
    elif(color == "light"):
        defaultLightModeButton.config(relief=SUNKEN, state = DISABLED)
        defaultDarkModeButton.config(relief=FLAT, state = NORMAL)
        changeColorMode("light")

#button that sets the current theme to dark mode
defaultDarkModeButton = Button(colorBlindSettingsFrame, fg=textColor, text="Dark Mode", padx="5", pady="5", bg= buttonColor, command= lambda: sinkButtonsChangeColor("dark"), relief=SUNKEN, state= DISABLED)
defaultDarkModeButton.grid(column= 0, row = 1, pady= 5)
windowElements.append(defaultDarkModeButton)

#button that sets the current theme to light mode
defaultLightModeButton = Button(colorBlindSettingsFrame, fg=textColor, text="Light Mode", padx="5", pady="5", bg= buttonColor, command= lambda: sinkButtonsChangeColor("light"),  relief=FLAT)
defaultLightModeButton.grid(column= 0, row = 2, pady= 5)
windowElements.append(defaultLightModeButton)

#this is to fill space and make the ui look better, should be move or removed if there are more options added to the defaults page
defaultSpacingLabel = Label(colorBlindSettingsFrame, fg=bgColor, text=" ", pady="5", bg= bgColor)
defaultSpacingLabel.grid(column= 0, row = 3, pady= 5)
windowElements.append(defaultSpacingLabel)

#subframe of settingsframe that contains the label and the buttons of the audio options
audioSettingsFrame = Frame(settingsFrame, bg= bgColor)
audioSettingsFrame.grid(column= 1, row = 0, padx=5, pady= 5)
windowElements.append(audioSettingsFrame)

def sinkButtonsChangeAudio(audio):
    global audioSetting
    if(audio == "no"):
        #sets the selected button to sunken, every other button should be reset to normal state and flat
        defaultNoAudioButton.config(relief=SUNKEN, state = DISABLED)
        defaultPartialAudioButton.config(relief=FLAT, state = NORMAL)
        defaultFullAudioButton.config(relief=FLAT, state = NORMAL)
        audioSetting = "no" # maybe
        #call whatever audio mode changing method
    elif(audio == "partial"):
        defaultNoAudioButton.config(relief=FLAT, state = NORMAL)
        defaultPartialAudioButton.config(relief=SUNKEN, state = DISABLED)
        defaultFullAudioButton.config(relief=FLAT, state = NORMAL)
        audioSetting = "partial" # maybe
        #call whatever audio mode changing method
    elif(audio == "full"):
        defaultNoAudioButton.config(relief=FLAT, state = NORMAL)
        defaultPartialAudioButton.config(relief=FLAT, state = NORMAL)
        defaultFullAudioButton.config(relief=SUNKEN, state = DISABLED)
        audioSetting = "partial" # maybe
        #call whatever audio mode changing method

#label above the audio option buttons
audioModeLabel = Label(audioSettingsFrame, fg=textColor, text="Set Default Audio Settings", padx="5", pady="5", bg= bgColor, relief=FLAT)
audioModeLabel.grid(column= 0, row = 0, pady= 5)
windowElements.append(audioModeLabel)

#button that sets the current audio mode to full audio, not sure what that means yet.
defaultFullAudioButton = Button(audioSettingsFrame, fg=textColor, text="Full Audio", padx="5", pady="5", bg= buttonColor, command= lambda: sinkButtonsChangeAudio("full"), relief=FLAT)
defaultFullAudioButton.grid(column= 0, row = 3, pady= 5)
windowElements.append(defaultFullAudioButton)

#button that sets the current audio mode to partial audio, not sure what that means yet.
defaultPartialAudioButton = Button(audioSettingsFrame, fg=textColor, text="Partial Audio", padx="5", pady="5", bg= buttonColor, command= lambda: sinkButtonsChangeAudio("partial"), relief=SUNKEN, state= DISABLED)
defaultPartialAudioButton.grid(column= 0, row = 2, pady= 5)
windowElements.append(defaultPartialAudioButton)

#button that sets the current audio mode to no audio, not sure what that means yet, not even sure this will be a mode in production build.
defaultNoAudioButton = Button(audioSettingsFrame, fg=textColor, text="No Audio", padx="5", pady="5", bg= buttonColor, command= lambda: sinkButtonsChangeAudio("no"), relief=FLAT)
defaultNoAudioButton.grid(column= 0, row = 1, pady= 5)
windowElements.append(defaultNoAudioButton)

#button that takes you back to the admin screen from the admin settings menu.
backToAdmin = Button(settingsFrame, fg=textColor, text="Back", padx="5", pady="5", bg= buttonColor, command=makeAdminFrame, relief=FLAT)
backToAdmin.grid(column= 1, row = 1, pady= 5)
windowElements.append(backToAdmin)

saveButton = Button(settingsFrame, fg=textColor, text="Save", padx="5", pady="5", bg= buttonColor, command=updateSettings, relief=FLAT)
saveButton.grid(column= 0, row = 1, pady= 5)
windowElements.append(saveButton)


#####################################################
exportSettingsFrame = Frame(window, bg= bgColor)

exportLabelSpacing = Label(exportSettingsFrame, bg= bgColor)
exportLabelSpacing.grid(column= 0, row= 0)

exportMethodLabel = Label(exportSettingsFrame, fg= textColor, text= "Choose Export Method", padx="5", pady="5", bg= bgColor, relief=FLAT)
exportMethodLabel.grid(column= 1 , row= 0, columnspan = 2, pady= "5")
windowElements.append(exportMethodLabel)

def send(method):
    if(method == "wifi"):
        print("Method: Wifi. This is where we send it to excel or whatever")
    elif(method == "usb"):
        print("Method: USB. This is where we send it to excel or whatever")

def switchExportMethod(exportMethodarg):
    global exportMethod
    exportMethod = exportMethodarg
    if(exportMethod == "wifi"):
        #sets the selected button to sunken, every other button should be reset to normal state and flat
        exportWithWifiButton.config(relief=SUNKEN, state = DISABLED)
        exportWithUSBButton.config(relief=FLAT,state = NORMAL)
    elif(exportMethod == "usb"):
        exportWithWifiButton.config(relief=FLAT, state = NORMAL)
        exportWithUSBButton.config(relief=SUNKEN, state = DISABLED)


exportWithWifiButton = Button(exportSettingsFrame, fg= textColor, text= "Wifi", padx="5", pady="5", bg= buttonColor, command= lambda: switchExportMethod("wifi"), relief=SUNKEN, state= DISABLED)
exportWithWifiButton.grid(column= 1, row= 1, columnspan = 2, pady= "5")
windowElements.append(exportWithWifiButton)

exportWithUSBButton = Button(exportSettingsFrame, fg= textColor, text= "Usb", padx="5", pady="5", bg= buttonColor, command= lambda: switchExportMethod("usb"), relief=FLAT)
exportWithUSBButton.grid(column= 1, row= 2, columnspan = 2, pady= "5")
windowElements.append(exportWithUSBButton)

def exportExit(response):
    if(response == "done"):
        exportSettingsFrame.forget()
        adminFrame.pack()
        #add another line here to activate a function that exports the data
    else:
        exportSettingsFrame.forget()
        adminFrame.pack()

exportDoneButton = Button(exportSettingsFrame, fg= textColor, text= "Done", padx="5", pady="5", bg= buttonColor, command= lambda: exportExit("done"), relief=FLAT)
exportDoneButton.grid(column= 2, row= 3, pady= "5")
windowElements.append(exportDoneButton)

exportCancelButton = Button(exportSettingsFrame, fg= textColor, text= "Cancel", padx= "5", pady = "5", bg= buttonColor, command= lambda: exportExit("cancel"), relief=FLAT)
exportCancelButton.grid(column= 1, row= 3, pady= "5")
windowElements.append(exportCancelButton)

#attempt to make different threads for each object so a new object can be made each time a new thread is needed.
count = -1
class ThreadObj(object):
    global count
    def __init__(self):
        self.num= count + 1
        self.thread= Thread(target= waitForSignout)
    #def func():
        #return

#a method that will sign the user out if another card is swiped. Called by waitForSignout when x seconds has gone by.
def signOut():
    global currentNFCid
    global currentEmployee
    clockInButton.config(state= DISABLED)
    clockOutButton.config(state= DISABLED)
    currentNFCid = 0
    currentEmployee = None
    print("test signOut()")

#work in progress, uses threads to sign out the user automatically if they have not interacted with the screen in x seconds
def waitForSignout():
    print("new start of the thread")
    global keepSleeping
    #range should be num of secs
    for i in range(7):
        if(keepSleeping):
            if(i < 4):
                print("sleeping for 1 sec now")
                sleep(1)
            elif(i == 5):
                signOut()
                print("Should Disable buttons")
                break
        else:
            print("Not sleeping")
            break

waitThread = Thread(target= waitForSignout)

#values for when the id is scanned.
currentNFCid = 0
currentEmployee = None
#for testing, delete this when the nfc is working
currentEmployee = defaultEmployee()
employeeList.append(currentEmployee)

window.mainloop()