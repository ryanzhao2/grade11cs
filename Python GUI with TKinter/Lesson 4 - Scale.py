from tkinter import *
import random


def changeTemp(self):
    feel = tempVar.get()
    feelLikeLabel.config(font=(f'Helvetica {feel}'))
    feelLikeVar.set(f'Feels like {feel} pt')


# MAIN
#########
root = Tk()
mainframe = Frame(root)

# Widgets
#########

titleLabel = Label(mainframe, text="Wind Chill Calculator", font=("Arial 18"))

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
feelLikeLabel = Label(mainframe, font=("Arial 30"), textvariable=feelLikeVar)

# GRID THE WIDGETS
###########
root.minsize(width=450, height=200)
mainframe.grid(row=1, column=1, padx=30, pady=40)

root.mainloop()