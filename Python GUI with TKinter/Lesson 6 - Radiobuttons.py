from tkinter import *
from tkinter.font import Font


def updatePlan():
    choice = planChoiceVar.get()
    if choice == 1:
        infoVar.set(planInformationList[0])
        infoLabel.grid(row=3, column=2, padx=10, sticky=S)
    if choice == 2:
        infoVar.set(planInformationList[1])
        infoLabel.grid(row=3, column=2, padx=10, sticky=S)
    if choice == 3:
        infoVar.set(planInformationList[3])
        infoLabel.grid(row=3, column=2, padx=10, sticky=S)
    if choice == 4:
        infoVar.set(planInformationList[2])
        infoLabel.grid(row=3, column=2, padx=10, sticky=S)

root = Tk()
root.config(bg="#1DB954")
mainframe = Frame(root, bg="#1DB954")

traffoFontSmall = Font(family="Moonbeam", size=20)
traffoFontLarge = Font(family="Moonbeam", size=35)

planInformationList = ['INDIVIDUAL\n$9.99 CAD/mnth\n1 account', \
                       'DUO\n$12.99 CAD/mnth\n2 accounts', \
                       'FAMILY\n$14.99 CAD/mnth\n6 accounts', \
                       'STUDENT\n$4.99 CAD/mnth\n1 account']

planChoiceVar = IntVar()
individualRadio = Radiobutton(mainframe, text="individiual", variable=planChoiceVar, value=1, font=traffoFontSmall, command=updatePlan, highlightcolor="#1DB954", fg="#ffffff", bg="#1DB954")
duoRadio = Radiobutton(mainframe, text="duo", variable=planChoiceVar, value=2, font=traffoFontSmall, command=updatePlan, highlightcolor="#1DB954", fg="#ffffff", bg="#1DB954")
familyRadio = Radiobutton(mainframe, text="student", variable=planChoiceVar, value=3, font=traffoFontSmall, command=updatePlan, highlightcolor="#1DB954", fg="#ffffff", bg="#1DB954")
studentRadio = Radiobutton(mainframe, text="family", variable=planChoiceVar, value=4, font=traffoFontSmall, command=updatePlan, highlightcolor="#1DB954", fg="#ffffff", bg="#1DB954")


planChoiceVar.set(0)

infoVar = StringVar()
infoVar.set(planInformationList[0])
infoLabel = Label(mainframe, textvariable=infoVar, font=traffoFontLarge, highlightcolor="#1DB954", bg="#1DB954")

# GRID WIDGETS
mainframe.grid(padx=50, pady=50)

individualRadio.grid(row=1, column=1, padx=10)
duoRadio.grid(row=1, column=2, padx=10)
familyRadio.grid(row=1, column=3, padx=10)
studentRadio.grid(row=1, column=4, padx=10)



root.mainloop()
