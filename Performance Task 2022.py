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
        guests_label.grid_forget()
        program_label.grid_forget()
        programs_label_frame.grid_forget()
        phone_label.grid_forget()
        phone_entry.grid_forget()
        email_label.grid_forget()
        email_entry.grid_forget()
        room_label.grid_forget()
        room_entry.grid_forget()
        medical_label.grid_forget()
        medical_entry.grid_forget()

    elif selection == "Register Guests":
        first_name_label.grid(row=2, column=2)
        last_name_label.grid(row=2, column=4, padx=20)
        first_name_entry.grid(row=2, column=3)
        last_name_entry.grid(row=2, column=5)
        phone_label.grid(row=3, column=2, pady=40)
        phone_entry.grid(row=3, column=3)
        email_label.grid(row=3, column=4)
        email_entry.grid(row=3, column=5)
        room_label.grid(row=4, column=2)
        room_entry.grid(row=4, column=3)
        medical_label.grid(row=4, column=4)
        medical_entry.grid(row=4, column=5)
        register_button.grid(row=5, column=5)
        age_var_scale.grid(row=4, column=1, pady=20)
        MaleRadio.grid(row=2, column=1, sticky=W)
        FemaleRadio.grid(row=3, column=1, sticky=W)
        programs_label_frame.grid(row=5, column=2, sticky=W)
        PaddleCheck.grid(row=1, column=1, sticky=W)
        ScubaCheck.grid(row=2, column=1, sticky=W)
        ConcertCheck.grid(row=3, column=1, sticky=W)
        WhaleCheck.grid(row=4, column=1, sticky=W)
        GolfingCheck.grid(row=5, column=1, sticky=W)
        KayakingCheck.grid(row=6, column=1, sticky=W)
        MovieCheck.grid(row=7, column=1, sticky=W)
        guests_listbox.grid_forget()
        programs_listbox.grid_forget()
        guests_label.grid_forget()
        program_label.grid_forget()


    elif selection == "View Programs":
        programs_listbox.grid(row=3, column=1)
        program_label.grid(row=2, column=2)
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
        guests_label.grid_forget()
        programs_label_frame.grid_forget()
        phone_label.grid_forget()
        phone_entry.grid_forget()
        email_label.grid_forget()
        email_entry.grid_forget()
        room_label.grid_forget()
        room_entry.grid_forget()
        medical_label.grid_forget()
        medical_entry.grid_forget()

    elif selection == "View Guests":
        guests_listbox.grid(row=3, column=1)
        guests_label.grid(row=2, column=2)
        first_name_entry.grid_forget()
        last_name_entry.grid_forget()
        programs_listbox.grid_forget()
        age_var_scale.grid_forget()
        MaleRadio.grid_forget()
        FemaleRadio.grid_forget()
        register_button.grid_forget()
        first_name_label.grid_forget()
        last_name_label.grid_forget()
        program_label.grid_forget()
        programs_label_frame.grid_forget()
        phone_label.grid_forget()
        phone_entry.grid_forget()
        email_label.grid_forget()
        email_entry.grid_forget()
        room_label.grid_forget()
        room_entry.grid_forget()
        medical_label.grid_forget()
        medical_entry.grid_forget()


root = Tk()
mainframe = Frame(root)
topframe= Frame(root)
middleframe = Frame(root)
bottomframe = Frame(root)

main_font = Font(family="Constantia", size=20)
medium_font = Font(family="Constantia", size=15)
small_font = Font(family="Constantia", size=12)

title = Label(topframe, text="Blossom Springs", font=("main_font", 30))

Options = ['Homepage', 'Register Guests', 'View Programs', 'View Guests']
OptionVar = StringVar()
OptionVar.set('Homepage')
Option = OptionMenu(topframe, OptionVar, *Options, command=changescreen)

first_name_label = Label(mainframe, text="First Name", font=medium_font)
last_name_label = Label(mainframe, text="Last Name", font=medium_font)
phone_label = Label(mainframe, text="Phone", font=medium_font)
email_label = Label(mainframe, text="Email", font=medium_font)
room_label = Label(mainframe, text="Room Number", font=medium_font)
medical_label = Label(mainframe, text="Medical", font=medium_font)

programs_label_frame = LabelFrame(mainframe, text="Programs", font=medium_font, width=40)

first_nameVar = StringVar()
first_name_entry = Entry(mainframe, width=15, text="", font=main_font, textvariable=first_nameVar)

last_nameVar = StringVar()
last_name_entry = Entry(mainframe, width=15, text="", font=main_font, textvariable=last_nameVar)

PhoneVar = StringVar()
phone_entry = Entry(mainframe, width=15, text="", font=main_font, textvariable=PhoneVar)

EmailVar = StringVar()
email_entry = Entry(mainframe, width=15, text="", font=main_font, textvariable=EmailVar)

RoomVar = StringVar()
room_entry = Entry(mainframe, width=15, text="", font=main_font, textvariable=RoomVar)

MedicalVar = StringVar()
medical_entry = Entry(mainframe, width=15, text="", font=main_font, textvariable=MedicalVar)

PaddleVar = IntVar()
PaddleCheck = Checkbutton(programs_label_frame, text="Stand Up Paddle Boarding", onvalue=1, offvalue = 0, variable = PaddleVar, font=medium_font)

ScubaVar = IntVar()
ScubaCheck = Checkbutton(programs_label_frame, text="Scuba Diving", onvalue=2, offvalue = 0, variable = ScubaVar, font=medium_font)

ConcertVar = IntVar()
ConcertCheck = Checkbutton(programs_label_frame, text="Concert", onvalue=3, offvalue = 0, variable = ConcertVar, font=medium_font)

WhaleVar = IntVar()
WhaleCheck = Checkbutton(programs_label_frame, text="Whale Watching", onvalue=4, offvalue = 0, variable = WhaleVar, font=medium_font)

GolfingVar = IntVar()
GolfingCheck = Checkbutton(programs_label_frame, text="Golfing", onvalue=5, offvalue = 0, variable = GolfingVar, font=medium_font)

KayakingVar = IntVar()
KayakingCheck = Checkbutton(programs_label_frame, text="Kayaking", onvalue=6, offvalue = 0, variable = KayakingVar, font=medium_font)

MovieVar = IntVar()
MovieCheck = Checkbutton(programs_label_frame, text="Movie Under the Stars", onvalue=7, offvalue = 0, variable = MovieVar, font=medium_font)

register_button = Button(mainframe, text="Register", command="", width=20, height=5)

AgeVar = IntVar()
age_var_scale = Scale(mainframe, from_=200, to=0, label='Age', variable=AgeVar, orient=VERTICAL)
#age_var_scale.bind("<ButtonRelease-1>")

GenderVar = IntVar()
MaleRadio = Radiobutton(mainframe, text="Male", variable=GenderVar, value=1, font=small_font, command="")


FemaleRadio = Radiobutton(mainframe, text="Female", variable=GenderVar, value=2, font=small_font, command="")

program_label = Label(topframe, text="Programs", font=medium_font)

guests_label = Label(topframe, text="Guests", font=medium_font)

ProgramsVar = StringVar()
programs_listbox = Listbox(mainframe, selectmode=SINGLE, listvariable=ProgramsVar, width=60, font=main_font, height=15)

GuestsVar = StringVar()
guests_listbox = Listbox(mainframe, selectmode=SINGLE, listvariable=GuestsVar, width=60, font=main_font, height=15, )

#GRIDDING
root.geometry("1000x750")
root.minsize(width=1000, height=750)
root.maxsize(width=1000, height=750)
mainframe.grid(row=2, column=1)
topframe.grid(row=1, column=1)

title.grid(row=1, column=2, sticky=N, padx=250, pady=100)
Option.grid(row=1, column=1, sticky=N)



root.mainloop()