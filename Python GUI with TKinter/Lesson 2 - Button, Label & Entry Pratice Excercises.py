"""
from tkinter import *
import random

def generateRandomNumbers():
    num1Var.set(random.randint(0, 59))
    num2Var.set(random.randint(0, 59))
    num3Var.set(random.randint(0, 59))



#MAIN
#HOlding frames
#########
root = Tk()
mainframe = Frame(root)

#Widgets
#########

num1Var = StringVar()
num1Label = Label(mainframe, text="", font=("Arial", 50), textvariable=num1Var)

num2Var = StringVar()
num2Label = Label(mainframe, text="", font=("Arial", 50), textvariable=num2Var)

num3Var = StringVar()
num3Label = Label(mainframe, text="", font=("Arial", 50), textvariable=num3Var)

randomButton = Button(mainframe, text="NEW COMBO", command=generateRandomNumbers)

#GRID THE WIDGETS
###########

mainframe.grid(padx=100, pady=100)
num1Label.grid(row=1, column=1)
num2Label.grid(row=1, column=2)
num3Label.grid(row=1, column=3)
randomButton.grid(row=2, column=1, columnspan=3, padx=70, pady=70)

root.mainloop()
"""
"""
from tkinter import *
import random


def calculateGPA():
    total = 0
    num1 = int(num1Var.get())
    num2 = int(num2Var.get())
    num3 = int(num3Var.get())
    num3 = int(num4Var.get())
    #calcavg =

# MAIN
# HOlding frames
#########
root = Tk()
mainframe = Frame(root)

# Widgets
#########

instructionLabel = Label(mainframe, text="Enter your 4 course grades")

num1Var = StringVar()
num1Entry = Entry(mainframe, width=5, text="", font=("Arial", 20), textvariable=num1Var)

num2Var = StringVar()
num2Entry = Entry(mainframe, width=5, text="", font=("Arial", 20), textvariable=num2Var)

num3Var = StringVar()
num3Entry = Entry(mainframe, width=5, text="", font=("Arial", 20), textvariable=num3Var)

num4Var = StringVar()
num4Entry = Entry(mainframe, width=5, text="", font=("Arial", 20), textvariable=num4Var)

gpaButton = Button(mainframe, text="FIND GPA", command=calculateGPA)

# GRID THE WIDGETS
###########

mainframe.grid(padx=100, pady=100)
instructionLabel.grid(row=1, column=1, columnspan=3)
num1Entry.grid(row=2, column=1)
num2Entry.grid(row=2, column=2)
num3Entry.grid(row=2, column=3)
num4Entry.grid(row=2, column=4)

gpaButton.grid(row=3, column=1, columnspan=4, ipadx=80, pady=30)

root.mainloop()
"""