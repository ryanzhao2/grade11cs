"""
from tkinter import *
from tkinter.font import Font
from tkinter.messagebox import *


# import tkinter.messagebox as tk


def acceptTerms():
    # get the Checkbutton value from the GUI
    checkval = acceptVar.get()
    # configure the widgets based on the value from Checkbutton

    if checkval == "accept":
        signatureEntry.configure(state="normal")
        acceptButton.configure(state="normal")
    else:
        signatureEntry.configure(state="disabled")
        acceptButton.configure(state="disabled")

    root.update()


def acceptMessage():
    name = signatureVar.get()

    if askquestion(f'Thank you {name}', "You have accepted the terms and conditions.\nContinue?") == "yes":

        signatureVar.set("")
        signatureEntry.configure(state="disabled")
        acceptVar.set("")
        acceptButton.configure(state="disabled")


    else:
        pass

    root.update()


def cancelMessage():
    if askquestion("Goodbye", "You have canceled.\nContinue?") == "yes":
        pass
    else:
        pass


# MAIN
root = Tk()
mainframe = Frame(root)

timesFontSmall = Font(family="Times New Roman", size=20)
timesFontLarge = Font(family="Times New Roman", size=30)

# Create the widgets
titleLabel = Label(mainframe, text="Terms of Agreement", font=timesFontLarge)
conditions = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam tristique quam ut lectus interdum, vitae elementum velit mattis. Proin elit odio, porta at ex id, scelerisque rutrum dui. Vestibulum blandit lectus massa, nec rutrum felis ullamcorper eget. Maecenas molestie odio tellus. Aliquam rutrum euismod metus vitae fringilla. Suspendisse lobortis tellus ac felis porta, sit amet interdum nisi commodo. Donec eros arcu, accumsan sit amet varius a, sollicitudin at massa. Pellentesque vitae imperdiet tortor, vel scelerisque odio. Donec vel ante facilisis, tristique felis non, malesuada urna. Sed faucibus tempus dolor quis condimentum. Suspendisse blandit mattis nulla sit amet imperdiet. Pellentesque dapibus efficitur ullamcorper. Aenean maximus ipsum nec tellus viverra, quis tempor ligula maximus.\n\nUt ac elit sit amet tortor efficitur aliquam. Morbi felis dui, vestibulum sit amet nulla sit amet, elementum consequat lorem. Nulla semper massa nec massa eleifend, non luctus mi auctor. Aliquam suscipit arcu vel viverra convallis. Mauris turpis odio, finibus sed mi sed, lobortis eleifend dui. Morbi dignissim facilisis augue at hendrerit. Nullam tempus volutpat est, ut aliquam neque iaculis quis. Quisque et nisl sed orci fringilla condimentum finibus id nulla.\n\nUt rutrum malesuada eleifend. Praesent nunc lorem, vulputate vulputate purus vel, aliquam aliquet metus. Duis pharetra venenatis turpis dictum laoreet. Phasellus ut nulla a libero fermentum mollis. Proin maximus bibendum turpis ut cursus. Duis id consequat magna, eget elementum nunc. Integer molestie nulla justo, nec venenatis ipsum eleifend a.\n\nMaecenas enim justo, lobortis ut efficitur et, mollis vitae nisi. In ac erat elementum, pulvinar quam vitae, sagittis leo. In placerat commodo arcu a lobortis. Sed aliquam aliquam urna a blandit. Sed venenatis, lorem sit amet pharetra ornare, arcu nisl venenatis ex, eget euismod elit justo sit amet purus. In ullamcorper mauris non mattis molestie. In dapibus ultrices dolor, ut bibendum magna bibendum non. Nunc risus sapien, iaculis nec neque in, venenatis aliquet leo. Nam porta maximus lectus, sit amet interdum purus convallis quis. Proin ultricies, ipsum eu auctor varius, leo erat vehicula elit, at suscipit ex erat sit amet nisi. Fusce at tristique dolor. Morbi fringilla, lacus a lobortis placerat, felis nisl porta elit, ut laoreet odio enim gravida quam. Quisque rhoncus porttitor fringilla. Donec sit amet tempor ex.\n\nFusce auctor augue id orci facilisis, sed molestie metus laoreet. Donec consectetur finibus libero id imperdiet. Nullam efficitur mauris sit amet gravida vulputate. Sed tristique mi in purus fermentum, sed volutpat lorem pellentesque. Duis id lacus in ligula aliquet porta. Aliquam quis pellentesque elit, quis commodo urna. Donec malesuada ut lorem sed tempor. Mauris at ipsum nunc."
conditionsText = Text(mainframe, bg="#eeeeee", bd=10)
conditionsText.insert(END, conditions)

acceptVar = StringVar()
acceptCheck = Checkbutton(mainframe, text="I accept the Terms & Conditions", variable=acceptVar, onvalue="accept",
                          offvalue="", font=timesFontSmall, command=acceptTerms)

signatureVar = StringVar()
signatureEntry = Entry(mainframe, textvariable=signatureVar, state=DISABLED, font=timesFontSmall)

acceptButton = Button(mainframe, text="Accept", state=DISABLED, command=acceptMessage)
cancelButton = Button(mainframe, text="Cancel", command=cancelMessage)

# GRID the widgets
mainframe.grid(padx=80, pady=80)
titleLabel.grid(row=0, column=1, columnspan=2, sticky=W)
conditionsText.grid(row=1, column=1, columnspan=2)
acceptCheck.grid(row=2, column=1, columnspan=2, sticky=E, pady=(50, 5))
signatureEntry.grid(row=3, column=2, columnspan=2, sticky=EW, pady=(0, 50))

cancelButton.grid(row=4, column=1, ipady=10, padx=10, sticky=EW)
acceptButton.grid(row=4, column=2, ipady=10, padx=10, sticky=EW)

root.mainloop()

"""
'''
Created May 2018
Author: aaronquesnelle
'''
"""
from tkinter import *


def calculateOrder():
    total = 0
    Wash = WashVar.get()
    Vacuum = VacuumVar.get()
    Pet = PetVar.get()
    Fabric = FabricVar.get()
    Car = carTypeVar.get()
    total += Wash
    total += Vacuum
    total += Pet
    total += Fabric
    total *= Car
    priceVar.set(f'${total:.2f}')

# MAIN   
root = Tk()
root.title("Q Detailing")
mainframe = Frame(root)

# CREATE THE WIDGETS
titleLabel = Label(mainframe, text="Service List", font=("Arial", 20))

carTypeFrame = LabelFrame(mainframe, text="Car Type?")
carTypeVar = DoubleVar()
carTypeVar.set(1)
sedanRadio = Radiobutton(carTypeFrame, text="Sedan", variable=carTypeVar, value=1)
suvRadio = Radiobutton(carTypeFrame, text="SUV", variable=carTypeVar, value=1.2)
vanRadio = Radiobutton(carTypeFrame, text="7 seats/Van", variable=carTypeVar, value=1.4)

calculateButton = Button(mainframe, text="calculate", command=calculateOrder, relief=RAISED)

priceVar = StringVar()
priceLabel = Label(mainframe, textvariable=priceVar)

WashVar = IntVar()
VacuumVar = IntVar()
PetVar = IntVar()
FabricVar = IntVar()
serviceListFrame = LabelFrame(mainframe, text="Service List, choose any number")
Wash = Checkbutton(serviceListFrame, text="Basic Exterior Wash", variable=WashVar, onvalue=28, offvalue=0)
Vacuum = Checkbutton(serviceListFrame, text="Interior Vacuum and dashboard cleaning", variable=VacuumVar, onvalue=40, offvalue=0)
Pet = Checkbutton(serviceListFrame, text="Pet Hair Removal", variable=PetVar, onvalue=45, offvalue=0)
Fabric = Checkbutton(serviceListFrame, text="Fabric Protection", variable=FabricVar, onvalue=20, offvalue=0)


# display the widgets to the user. Working on a 4row*2column layout
mainframe.grid(padx=30, pady=30)
titleLabel.grid(row=1, column=1, columnspan=3, pady=20, sticky=E)

carTypeFrame.grid(row=2, column=1, ipadx=55, pady=30, sticky=W)
sedanRadio.grid(row=1, column=1)
suvRadio.grid(row=1, column=2)
vanRadio.grid(row=1, column=3)

calculateButton.grid(row=2, column=2, ipadx=50, ipady=10, padx=20, pady=30, columnspan=2, sticky=NW)

priceLabel.grid(row=3, column=2)

serviceListFrame.grid(row=3, column=1, ipadx=40, sticky=W)
Wash.grid(row=1, column=1,sticky=W)
Vacuum.grid(row=2, column=1,sticky=W)
Pet.grid(row=3, column=1,sticky=W)
Fabric.grid(row=4, column=1,sticky=W)



root.mainloop()
"""

from tkinter import *


def calculatePayment():
    peryear = dollarVar.get()
    total = dollarVar.get()
    total -= (dollarVar.get() * taxVar.get())
    total -= (dollarVar.get() * rrspVar.get())
    total -= (dollarVar.get() * unionVar.get())
    total -= (dollarVar.get() * healthVar.get())
    yearVar.set(f'${total:.2f}/net year')
    if freqVar.get() == "52 - weekly":
        total = total/52

    if freqVar.get() == "24 - bimonthly":
        total = total/24

    if freqVar.get() == "12 - monthly":
        total = total/12
    paymentVar.set(f'${total:.2f}/pmt')


# MAIN
root = Tk()
mainframe = Frame(root)

# Create widgets

titleLabel = Label(mainframe, text="Salary Calculator", font=("Arial", 50))

dollarVar = IntVar()
dollarVar.set(45000)
dollarScale = Scale(mainframe, from_=100000, to=20000, orient=VERTICAL, width=50, length=300, resolution=5000,
                    variable=dollarVar)

frequencies = ["52 - weekly", "24 - bimonthly", "12 - monthly"]
freqVar = StringVar()
freqSpinbox = Spinbox(mainframe, textvariable=freqVar, values=frequencies)

deductFrame = LabelFrame(mainframe, text="Deductions")
taxVar = DoubleVar()
taxCheck = Checkbutton(deductFrame, text="Tax", variable=taxVar, onvalue=0.35, offvalue=0)
rrspVar = DoubleVar()
rrspCheck = Checkbutton(deductFrame, text="RRSP", variable=rrspVar, onvalue=0.13, offvalue=0)
unionVar = DoubleVar()
unionCheck = Checkbutton(deductFrame, text="Union Dues", variable=unionVar, onvalue=0.01, offvalue=0)
healthVar = DoubleVar()
healthCheck = Checkbutton(deductFrame, text="Health Plan", variable=healthVar, onvalue=0.025, offvalue=0)

paymentVar = StringVar()
paymentLabel = Label(mainframe, textvariable=paymentVar, font=("Arial, 30"))

yearVar = StringVar()
yearLabel = Label(mainframe, textvariable=yearVar, font=("Arial, 15"))

calculateButton = Button(mainframe, text="each paycheck?", command=calculatePayment)

# Grid widgets
mainframe.grid(padx=50, pady=50)

titleLabel.grid(row=0, column=1, columnspan=2, pady=20, sticky=E)
dollarScale.grid(row=1, column=1, rowspan=5)
freqSpinbox.grid(row=1, column=2, padx=30, sticky=E + W)

deductFrame.grid(row=2, column=2, padx=30, ipadx=50, sticky=N)
taxCheck.grid(sticky=W)
rrspCheck.grid(sticky=W)
unionCheck.grid(sticky=W)
healthCheck.grid(sticky=W)

calculateButton.grid(row=3, column=2, ipady=15, pady=10, padx=30, sticky=E + W)

paymentLabel.grid(row=4, column=2)
yearLabel.grid(row=5, column=2)

##titleLabel.grid()
##dollarScale.grid()
##freqSpinbox.grid()
##
##deductFrame.grid()
##taxCheck.grid()
##rrspCheck.grid()
##unionCheck.grid()
##healthCheck.grid()
##
##
##calculateButton.grid()
##
##paymentLabel.grid()
##yearLabel.grid()


root.mainloop()


