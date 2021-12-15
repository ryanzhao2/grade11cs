from tkinter import *
import random


def change_size(value):
    size = sizeVar.get()

    wordLabel.config(font=(f'Helvetica {size}'))

    wordVar.set(f'hello {size} pt')


# MAIN
# Holding frames
#########
root = Tk()
mainframe = Frame(root)

# Widgets
#########
wordVar = StringVar()
wordVar.set("hello!")
wordLabel = Label(mainframe, font=("Helvetica 15"), textvariable=wordVar)

sizeVar = IntVar()
sizeScale = Scale(mainframe, \
                  from_=8, to=100, \
                  variable=sizeVar, \
                  orient=VERTICAL, \
                  width=50, length=200, \
                  # showvalue = False, \
                  troughcolor="#fe3254", \
                  # label="pt", \
                  #command=change_size
                  )

# depending on the event you want to cause the change
sizeScale.bind("<ButtonRelease-1>", change_size)

# GRID THE WIDGETS
###########
mainframe.grid(padx=50, pady=50)

wordLabel.grid(row=1, column=2, padx=20, pady=30, sticky=E + W)

sizeScale.grid(row=1, column=1, padx=50, sticky=N)

root.mainloop()

