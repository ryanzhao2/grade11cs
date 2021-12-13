from tkinter import *
import random

def changeStyle():
    #style = styleOptionVar.get()
    style = styleSpinVar.get()

    if style == "normal":
        wordLabel.config(font=("Century Gothic", "40", "normal"))
        #wordLabel.config(font=("Helvetica 40"))
        wordVar.set("normal")

    elif style == "underline":
        wordLabel.config(font=("Century Gothic", "40", "underline"))
        #wordLabel.config(font=("Helvetica 40 underline"))
        wordVar.set("underline")


    elif style == "bold":
        wordLabel.config(font=("Century Gothic", "40", "bold"))
        #wordLabel.config(font=("Helvetica 40 bold"))
        wordVar.set("bold")

    elif style == "italic":
        wordLabel.config(font=("Century Gothic", "40", "italic"))
        #wordLabel.config(font=("Helvetica 40 italic"))
        wordVar.set("italic")





#MAIN
#HOlding frames
#########
root = Tk()
mainframe = Frame(root)

#Widgets
#########
wordVar = StringVar()
wordVar.set("normal")
wordLabel = Label(mainframe, font=("Century Gothic", "40", "normal"), textvariable=wordVar)
#wordLabel = Label(mainframe, font=("Helvetica 40 underline"), textvariable=wordVar)

styles = ['normal', 'underline', 'italic', 'bold']
styleOptionVar = StringVar()
styleOptionVar.set('normal')
styleOption = OptionMenu(mainframe, styleOptionVar, *styles)


styles = ['normal', 'underline', 'italic', 'bold']
styleSpinVar = StringVar()
styleSpinVar.set('normal')
styleSpinbox = Spinbox(mainframe, textvariable = styleSpinVar, values=styles)

styleButton = Button(mainframe, text="change", command=changeStyle)


#GRID THE WIDGETS
###########
mainframe.grid(padx = 50, pady = 50)


styleOption.grid(row=1, column=1, padx=20, pady=10, sticky=E+W)
styleSpinbox.grid(row=2, column=1, padx=20, pady=10, sticky=E+W)

styleButton.grid(row=3, column=1, padx=20, pady=10, ipady=10, sticky=E+W)

wordLabel.grid(row=1, column=2, padx = 20, rowspan=2)


root.mainloop()
