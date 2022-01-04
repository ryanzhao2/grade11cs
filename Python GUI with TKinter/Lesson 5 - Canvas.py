"""
'''
Created May 6, 2018
Updated May 2019
For ICS3U

@author: aaronquesnelle
'''

from tkinter import *
import random


def showPoint(event):
    x = event.x
    y = event.y

    currentPointVar.set(f'X = {x}, Y = {y}')


def drawSquare(event):
    x = event.x
    y = event.y
    d = random.randint(10, 100)

    c = random.choice(["#7F2626", "#FF4C4C", "#FF9999", "#7F4C4C", "#CC3D3D"])
    cv.create_rectangle(10, 400, 10 + 50, 400 + 50, fill=c, outline=c)
    cv.create_rectangle(100, 250, 200, 300, fill=c, outline=c)
    cv.create_rectangle(400, 50, 400 + 200, 50 + 200, fill=c, outline=c)
    cv.create_rectangle(x, y, x+100, y+100, fill = c, outline = c)

def clear():
    cv.delete(ALL)
# MAIN
# Holding frames
#########
root = Tk()
mainframe = Frame(root)

# Widgets
#########

cv = Canvas(mainframe, width=500, height=500, bg="#bfc3c9")
cv.bind("<Button-1>", drawSquare)
cv.bind("<Motion>", showPoint)

instructionLabel = Label(mainframe, text="CLICK!", font=("Courier", 30))

currentPointVar = StringVar()
currentPointVar.set(f'X = 0, Y = 0')
currentPointLabel = Label(mainframe, textvariable=currentPointVar)

clearButton = Button(mainframe, text="Clear", command=clear)

# GRID THE WIDGETS
###########
root.minsize(width=450, height=200)
mainframe.grid(row=1, column=1, padx=50, pady=50)

instructionLabel.grid(row=1, column=1, sticky=W)
cv.grid(row=2, column=1, columnspan=2)
currentPointLabel.grid(row=3, column=2, sticky=E)
clearButton.grid(row=1, column=2, ipadx=60)

root.mainloop()
"""
'''
Created May 6, 2018
For ICS3U

@author: aaronquesnelle
'''
"""
from tkinter import *
import random
from PIL import Image, ImageTk


def addImage(event):
    global weather, weatherPictures

    # get the mouse click location (x, y)
    x = event.x
    y = event.y
    # get the Option Menu selection
    menu_option = weatherOptionVar.get()
    # find the index of the selection in the weather list
    index = weather.index(menu_option)
    # use the index to find the correct PhotoImage in the weatherPictures list
    photoToUse = weatherPictures[index]
    # The function create_image below will add an image to the canvas
    cv.create_image(x, y, image=photoToUse)


def clearScreen():
    cv.delete(ALL)


# MAIN
# Holding frames
#########
root = Tk()
mainframe = Frame(root)

# Widgets
#########

cv = Canvas(mainframe, width=500, height=500, bg="#a8b1bf")
cv.bind("<Button-1>", addImage)

instructionLabel = Label(mainframe, text="CLICK!", font=("Courier", 30))

sunImage = Image.open("sun.png").resize((200, 200))
sunPhoto = ImageTk.PhotoImage(sunImage)
cloudImage = Image.open("clouds.png").resize((200, 200))
cloudPhoto = ImageTk.PhotoImage(cloudImage)
rainImage = Image.open("rain.png").resize((200, 200))
rainPhoto = ImageTk.PhotoImage(rainImage)
cloudyImage = Image.open("cloudy.png").resize((200, 200))
cloudyPhoto = ImageTk.PhotoImage(cloudyImage)

global weatherPictures
weatherPictures = [sunPhoto, cloudyPhoto, cloudPhoto, rainPhoto]

global weather
weather = ["Sun", "Sun/Clouds", "Cloudy", "Rain"]
weatherOptionVar = StringVar()
weatherOptionVar.set("Sun")
weatherOption = OptionMenu(mainframe, weatherOptionVar, *weather)
weatherOption.config(width=20)

clearButton = Button(mainframe, text="CLEAR", command=clearScreen)

# GRID THE WIDGETS
###########
root.minsize(width=450, height=200)
mainframe.grid(row=1, column=1, padx=50, pady=50)

clearButton.grid(row=1, column=2, rowspan=2, ipady=20, ipadx=30, sticky=E)
instructionLabel.grid(row=1, column=1, sticky=W)
weatherOption.grid(row=2, column=1, ipady=10, sticky=W)

cv.grid(row=3, column=1, columnspan=2, pady=10)

root.mainloop()
"""