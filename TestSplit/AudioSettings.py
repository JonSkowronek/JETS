from tkinter import *
from TimeClockV104Split import *

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