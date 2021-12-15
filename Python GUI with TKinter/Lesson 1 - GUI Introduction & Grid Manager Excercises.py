'''
Created April 2018
Aaron Quesnelle

for ICS3U

'''
from tkinter import *


def generateNameBox():
    n = inputStringVar.get()

    s = ""
    s += "+" + "-" * len(n) + "+\n"
    s += "|" + n + "|\n"
    s += "+" + "-" * len(n) + "+\n"

    nameStringVar.set(s)


# MAIN
# Generate holding structures for GUI
#############
root = Tk()

mainframe = Frame(root)

# Create the widgets and associated Vars
#############
nameStringVar = StringVar()
nameLabel = Label(mainframe, text="", font=("Courier", 30), textvariable=nameStringVar)

instructionLabel = Label(mainframe, text="Enter your name", font=("Courier", 11))

greetingButton = Button(mainframe, text="FORMAT", command=generateNameBox)

clearButton = Button(mainframe, text="Clear", command=generateNameBox)

inputStringVar = StringVar()
inputEntry = Entry(mainframe, width=15, textvariable=inputStringVar)



# Grid the widgets
#############
root.minsize(width=250, height=400)
root.maxsize(width=500, height=400)
mainframe.grid(padx=50, pady=50)

instructionLabel.grid(row=1, column=1, sticky=W)
inputEntry.grid(row=2, column=1, sticky=W)
greetingButton.grid(row=3, column=1, ipadx=33, pady=5, sticky=W)
clearButton.grid(row=4, column=1, ipadx=33, pady=5, sticky=W)

nameLabel.grid(row=5, column=1, sticky=W)

root.mainloop()