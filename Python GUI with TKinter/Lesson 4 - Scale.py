"""
from tkinter import *
import random



def changeTemp(self):
    temp = tempVar.get()
    speed = speedVar.get()
    windchill = 13.12 + 0.6215 * temp - 11.37 * (speed ** 0.16) + 0.3965 * temp * (speed ** 0.16)
    feelLikeVar.set(f'Feels like {windchill:.1f}\u00B0C')

# MAIN
#########
root = Tk()
mainframe = Frame(root)

# Widgets
#########

titleLabel = Label(mainframe, text="Wind Chill Calculator", font=("Arial 10"))

tempLabel = Label(mainframe, text="temp")

tempVar = IntVar()
tempScale = Scale(mainframe, from_=30, to=-20, variable=tempVar, orient=VERTICAL)
tempScale.bind("<ButtonRelease-1>", changeTemp)

windLabel = Label(mainframe, text="wind")

speedVar = IntVar()
speedScale = Scale(mainframe, from_=40, to=0, variable=speedVar, orient=VERTICAL)
speedScale.bind("<ButtonRelease-1>", changeTemp)

feelLikeVar = StringVar()
feelLikeVar.set("Feels like:")
feelLikeLabel = Label(mainframe, font=("Arial 16"), textvariable=feelLikeVar)

# GRID THE WIDGETS
###########
root.minsize(width=450, height=200)
mainframe.grid(row=1, column=1, padx=30, pady=40)

titleLabel.grid(row=0, column=0, padx=20, sticky=W)

tempLabel.grid(row=2, column=0, padx=10, sticky=NW)
tempScale.grid(row=1, column=0, pady=20, sticky=W)

windLabel.grid(row=2, column=0, padx=50, sticky=NW)
speedScale.grid(row=1, column=0, padx=40, pady=20, sticky=W)

feelLikeLabel.grid(row=1, column=0, padx=100)


root.mainloop()
"""
from tkinter import *
import random


def changeDayNight(self):
    dayNight = dayNightVar.get()
    if dayNight == 2:
        wordVar.set("OFF")
        wordLabel.config(bg='Dark Blue')
        root.config(bg='Dark Blue')
        mainframe.config(bg='Dark Blue')
        dayNightScale.config(activebackground='Dark Blue', highlightbackground='Dark Blue', highlightcolor='Dark Blue', troughcolor='Dark Blue', bg='Dark Blue', background='Dark Blue')
        dayNight = dayNightVar.get()
    if dayNight == 1:
        wordVar.set("ON")
        wordLabel.config(bg='Yellow')
        root.config(bg='Yellow')
        mainframe.config(bg='Yellow')
        dayNightScale.config(activebackground='Grey', highlightbackground='Yellow', highlightcolor='Yellow', troughcolor='Yellow', bg='Yellow', background='Grey')
        dayNight = dayNightVar.get()






# MAIN
# HOlding frames
#########
root = Tk()
mainframe = Frame(root)

# Widgets
#########

dayNightVar = IntVar()
dayNightVar.set(1)
dayNightScale = Scale(mainframe, variable=dayNightVar, width=50, length=100, from_=2, to=1, showvalue=False,
                      orient=HORIZONTAL, command=changeDayNight)

wordVar = StringVar()
wordVar.set("ON")
wordLabel = Label(mainframe, textvariable=wordVar, font=("Arial", 40))

wordLabel.config(bg='Yellow')
root.config(bg='Yellow')
mainframe.config(bg='Yellow')
dayNightScale.config(activebackground='Grey', highlightbackground='Yellow', highlightcolor='Yellow',
                     troughcolor='Yellow', bg='Yellow', background='Grey')


# GRID THE WIDGETS
###########
root.minsize(width=300, height=200)
mainframe.grid(row=1, column=1, padx=100, pady=100)

wordLabel.grid(row=1, column=1)
dayNightScale.grid(row=2, column=1)

root.mainloop()

