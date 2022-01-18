from tkinter import *
from tkinter.font import Font


def changescreen(selection):
    selection = OptionVar.get()
    if selection == "Homepage":
        first_name_entry.grid_forget()
        last_name_entry.grid_forget()
        guests_listbox.grid_forget()
        programs_listbox.grid_forget()
        age_var_scale.grid_forget()
        MaleRadio.grid_forget()
        FemaleRadio.grid_forget()
        register_button.grid_forget()
        first_name_label.grid_forget()
        last_name_label.grid_forget()

    elif selection == "Register Guests":
        first_name_entry.grid(row=2, column=2)
        last_name_entry.grid(row=2, column=4)
        register_button.grid(row=5, column=5)
        age_var_scale.grid(row=4, column=1, pady=20)
        MaleRadio.grid(row=3, column=1)
        FemaleRadio.grid(row=3, column=2)
        first_name_label.grid(row=2, column=1, pady=30)
        last_name_label.grid(row=2, column=3, sticky=W, pady=10)
        guests_listbox.grid_forget()
        programs_listbox.grid_forget()


    elif selection == "View Programs":
        programs_listbox.grid(row=3, column=1)
        first_name_entry.grid_forget()
        last_name_entry.grid_forget()
        guests_listbox.grid_forget()
        age_var_scale.grid(row=2, column=4)
        age_var_scale.grid_forget()
        MaleRadio.grid_forget()
        FemaleRadio.grid_forget()
        register_button.grid_forget()
        first_name_label.grid_forget()
        last_name_label.grid_forget()

    elif selection == "View Guests":
        guests_listbox.grid(row=3, column=1)
        first_name_entry.grid_forget()
        last_name_entry.grid_forget()
        programs_listbox.grid_forget()
        age_var_scale.grid_forget()
        MaleRadio.grid_forget()
        FemaleRadio.grid_forget()
        register_button.grid_forget()
        first_name_label.grid_forget()
        last_name_label.grid_forget()

root = Tk()
mainframe = Frame(root)

main_font = Font(family="Constantia", size=20)
medium_font = Font(family="Constantia", size=15)
small_font = Font(family="Constantia", size=12)

title = Label(mainframe, text="Blossom Springs", font=("main_font", 30))

Options = ['Homepage', 'Register Guests', 'View Programs', 'View Guests']
OptionVar = StringVar()
OptionVar.set('Homepage')
Option = OptionMenu(mainframe, OptionVar, *Options, command=changescreen)

first_name_label = Label(mainframe, text="First Name", font=medium_font)
last_name_label = Label(mainframe, text="Last Name", font=medium_font)


first_nameVar = StringVar()
first_name_entry = Entry(mainframe, width=10, text="", font=main_font, textvariable=first_nameVar)

last_nameVar = StringVar()
last_name_entry = Entry(mainframe, width=10, text="", font=main_font, textvariable=last_nameVar)

ProgramsVar = StringVar()
programs_listbox = Listbox(mainframe, selectmode=SINGLE, listvariable=ProgramsVar, width=30, font=main_font, height=5)

GuestsVar = StringVar()
guests_listbox = Listbox(mainframe, selectmode=SINGLE, listvariable=GuestsVar, width=30, font=main_font, height=5)

register_button = Button(mainframe, text="Register", command="", width=20, height=5)

AgeVar = IntVar()
age_var_scale = Scale(mainframe, from_=200, to=0, label='Age', variable=AgeVar, orient=VERTICAL)
#age_var_scale.bind("<ButtonRelease-1>")

GenderVar = IntVar()
MaleRadio = Radiobutton(mainframe, text="Male", variable=GenderVar, value=1, font=small_font, command="")


FemaleRadio = Radiobutton(mainframe, text="Female", variable=GenderVar, value=2, font=small_font, command="")

#GRIDDING

mainframe.grid(padx=300, pady=300)
title.grid(row=1, column=2, sticky=N, padx=20, pady=20)
Option.grid(row=1, column=1, sticky=W)



root.mainloop()