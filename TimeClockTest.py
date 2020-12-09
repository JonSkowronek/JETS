from tkinter import *
import tkinter as tk
import random

print("Current Method:")
for i in range(10):
    idNumber = random.randint(0,9)   
    for i in range(5):
        idNumber *= 10
        idNumber += random.randint(0,9)
    print(idNumber)

print("New method:")
for i in range(10):        
    print(random.randint(0,99999))

firstWindow = Tk()
firstWindow.title("Admin Login Window")
firstWindow.geometry("300x150")

secondWindow = Tk()

firstButton = Button(firstWindow, text = "First Button")
firstButton.pack()

def secondwindow():
    print("SecondWindow")

firstWindow.mainloop()