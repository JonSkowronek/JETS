from tkinter import *

tempAudioSetting = "No Audio"
tempVisualSetting = "darks"

#sets Audio Settings for when employee objects are created, handles button sinking and disabling
def setAudioModewithButtons(mode):
    global tempAudioSetting
    if(mode == "No Audio"):
        #sets the selected button to sunken, every other button should be reset to normal state and flat
        noAudioButton.config(relief=SUNKEN, state = DISABLED)
        partialAudioButton.config(relief=FLAT, state = NORMAL)
        fullAudioButton.config(relief=FLAT, state = NORMAL)
        tempAudioSetting = "No Audio"
    elif(mode == "Partial Audio"):
        noAudioButton.config(relief=FLAT, state = NORMAL)
        partialAudioButton.config(relief=SUNKEN, state = DISABLED)
        fullAudioButton.config(relief=FLAT, state = NORMAL)
        tempaAudioSetting = "Partial Audio"
    elif(mode == "Full Audio"):
        noAudioButton.config(relief=FLAT, state = NORMAL)
        partialAudioButton.config(relief=FLAT, state = NORMAL)
        fullAudioButton.config(relief=SUNKEN, state = DISABLED)
        tempAudioSetting = "Full Audio"
    #add more options for colormodes here, prob an else also,

#sets Visual Settings for when employee objects are created, handles button sinking and disabling
def setColorModewithButtons(color):
    global tempVisualSetting
    if(color == "dark"):
        #sets the selected button to sunken, every other button should be reset to normal state and flat
        darkModeButton.config(relief=SUNKEN, state = DISABLED)
        lightModeButton.config(relief=FLAT, state = NORMAL)
        tempVisualSetting = "dark"
    elif(color == "light"):
        lightModeButton.config(relief=SUNKEN, state = DISABLED)
        darkModeButton.config(relief=FLAT, state = NORMAL)
        tempVisualSetting = "light"
    #add more options for colormodes here

def updateSettings():
    audioSetting = tempAudioSetting
    visualSetting = tempVisualSetting
    tempVisualSetting = None
    tempAudioSetting = None
    makeAdminFrame()
    print("updateSettings()")