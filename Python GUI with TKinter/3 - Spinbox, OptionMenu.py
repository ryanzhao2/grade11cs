from tkinter import *
import random


def changeFontColour():
    colours = colourOptionVar.get()


# MAIN
# HOlding frames
#########
root = Tk()
mainframe = Frame(root)

# Widgets
#########
colourWordVar = StringVar()
colourWordVar.set("black")
colourWordLabel = Label(mainframe, font=("Arial", 50), fg="#000000", textvariable=colourWordVar)

colours = ['black', 'grey', 'blue', 'red', 'orange', 'pink', 'green']
colourOptionVar = StringVar()
colourOptionVar.set('black')
colourOption = OptionMenu(mainframe, colourOptionVar, *colours)

colourButton = Button(mainframe, text="change", command=changeFontColour)

# GRID THE WIDGETS
###########
root.minsize(width=450, height=200)
root.maxsize(width=450, height=200)
mainframe.grid(padx=50, pady=50)

colourOption.grid(row=1, column=1, padx=40, ipadx=12)
colourButton.grid(row=2, column=1, padx=40, ipadx=20)
colourWordLabel.grid(row=1, column=2, rowspan=2)

root.mainloop()