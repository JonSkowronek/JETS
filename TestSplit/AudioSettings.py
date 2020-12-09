from tkinter import *

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

noAudioButton = Button(addPersonWindow, fg=textColor, text="No Audio", padx="5", pady="5", bg= buttonColor, command= lambda: setAudioModewithButtons("No Audio"), relief=FLAT)
noAudioButton.grid(column=1, row = 5, pady = 5)
windowElements.append(noAudioButton)

partialAudioButton = Button(addPersonWindow, fg=textColor, text="Partial Audio", padx="5", pady="5", bg= buttonColor, command= lambda: setAudioModewithButtons("Partial Audio"), relief=SUNKEN, state= DISABLED)
partialAudioButton.grid(column=1, row = 6, pady = 5)
windowElements.append(partialAudioButton)

fullAudioButton = Button(addPersonWindow, fg=textColor, text="Full Audio", padx="5", pady="5", bg= buttonColor, command= lambda: setAudioModewithButtons("Full Audio"), relief=FLAT)
fullAudioButton.grid(column=1, row = 7, pady = 5)
windowElements.append(fullAudioButton)

#creates the employee obeject with the name and the settings, destroys the employee creation window, only reason for this is bc cant have makeEmployee button do both, and other func is declared way above
def createAndDestory(firstName, lastName, visualSetting, audioSetting):
    employeeList.append(Employee(firstName, lastName, visualSetting, audioSetting))
    #update the db to store new list?
    addPersonWindow.destroy()

#executes above func ^
makeEmployeeButton = Button(addPersonWindow, fg=textColor, text="Done", padx="5", pady="5", bg= buttonColor, command= lambda: createAndDestory(firstNameTextbox.get(1.0, "end"), 
lastNameTextbox.get(1.0, "end"),visualSetting, audioSetting), relief=FLAT)
makeEmployeeButton.grid(column=0, row = 10, columnspan=2, padx= 5)
windowElements.append(makeEmployeeButton)