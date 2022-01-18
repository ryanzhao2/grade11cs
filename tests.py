'''
Created May 6, 2018
For ICS3U

@author: aaronquesnelle
'''

from tkinter import *
import random


def drawText(event):
    x = event.x
    y = event.y

    cv.delete(ALL)

    cv.create_text(x, y, font=("Courier, 18"), text=(f'(X: {x}, Y: {y})'))


# MAIN
# Holding frames
#########
root = Tk()
mainframe = Frame(root)

# Widgets
#########

cv = Canvas(mainframe, width=500, height=500, bg="#eeeeee")
cv.bind("<Button-1>", drawText)

instructionLabel = Label(mainframe, text="CLICK", font=("Courier", 30))

# GRID THE WIDGETS
###########
root.minsize(width=450, height=200)
mainframe.grid(row=1, column=1, padx=50, pady=50)

instructionLabel.grid(row=1, column=1, sticky=W)
cv.grid(row=2, column=1, columnspan=2)

root.mainloop()
