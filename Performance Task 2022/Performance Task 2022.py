from tkinter import *
from tkinter.font import Font
from PIL import Image, ImageTk

#SETTING UP FRAMES
root = Tk()
root.config(bg="#c2e8dc")
mainframe = Frame(root, bg="#c2e8dc")
topframe = Frame(root, bg="#c2e8dc")

#FONTS
main_font = Font(family="Constantia", size=20)
medium_font = Font(family="Constantia", size=15)
small_font = Font(family="Constantia", size=12)

#global big_list
big_list = []

#global large_details_list
large_details_list = []

#global name_list
name_list = []

#GLOBAL VARIABLES FOR DISPLAYING PRICE OF PROGRAMS
price = 0
PriceVar = IntVar()
price_label = Label(mainframe, text=f'Price: ${PriceVar.get():.2f}', font=main_font, bg="#c2e8dc")

#GLOBAL FOR PREVENTING DUPLICATE PRICE GRIDDING
number_of_guests = f'Number of Guests: {1+len(large_details_list)}/10'
registered_label = Label(topframe, text=number_of_guests, font=medium_font, bg="#c2e8dc")

#FUNCTIONS FOR HIDING WIDGETS DETERMINED BY THE OPTION MENU
def forget_register():
    first_name_entry.grid_forget()
    last_name_entry.grid_forget()
    age_var_scale.grid_forget()
    MaleRadio.grid_forget()
    FemaleRadio.grid_forget()
    register_button.grid_forget()
    first_name_label.grid_forget()
    last_name_label.grid_forget()
    programs_label_frame.grid_forget()
    phone_label.grid_forget()
    phone_entry.grid_forget()
    email_label.grid_forget()
    email_entry.grid_forget()
    room_label.grid_forget()
    room_entry.grid_forget()
    medical_label.grid_forget()
    medical_entry.grid_forget()
    price_label.grid_forget()

def forget_guests():
    guests_label.grid_forget()
    guests_listbox.grid_forget()
    guest_details_button.grid_forget()
    guest_details_label.grid_forget()
    guest_delete_button.grid_forget()

def forget_programs():
    programs_listbox.grid_forget()
    program_label.grid_forget()
    program_details_button.grid_forget()
    program_details_label.grid_forget()

def forget_homepage():
    logo_canvas.grid_forget()

#FUNCTION FOR GRIDDING AND HIDING WIDGETS WHEN THE OPTION MENU IS SELECTED TO SOMETHING
def changescreen(self):
    selection = OptionVar.get()
    if selection == "Homepage":
        logo_canvas.grid_forget()
        logo_canvas.grid(row=2, column=1, columnspan=3)
        forget_register()
        forget_guests()
        forget_programs()

    elif selection == "Register Guests":
        first_name_label.grid(row=2, column=2)
        last_name_label.grid(row=2, column=4, padx=40)
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
        MaleRadio.grid(row=2, column=1, sticky=W, padx=20)
        FemaleRadio.grid(row=3, column=1, sticky=W, padx=20)
        programs_label_frame.grid(row=5, column=2, sticky=W)
        PaddleCheck.grid(row=1, column=1, sticky=W)
        ScubaCheck.grid(row=2, column=1, sticky=W)
        ConcertCheck.grid(row=3, column=1, sticky=W)
        WhaleCheck.grid(row=4, column=1, sticky=W)
        GolfingCheck.grid(row=5, column=1, sticky=W)
        KayakingCheck.grid(row=6, column=1, sticky=W)
        MovieCheck.grid(row=7, column=1, sticky=W)
        price_label.grid(row=5, column=3, padx=20, sticky=W)
        forget_guests()
        forget_programs()
        forget_homepage()

    elif selection == "View Programs":
        programs_listbox.grid(row=3, column=1, sticky=W, padx=150)
        program_label.grid(row=2, column=1)
        program_details_button.grid(row=4, column=3, sticky=NW, padx=133, pady=30)
        program_details_label.grid(row=4, column=2, sticky=E)
        forget_guests()
        forget_register()
        forget_homepage()

    elif selection == "View Guests":
        guests_listbox.grid(row=3, column=1, sticky=W, padx=150)
        guests_label.grid(row=2, column=1)
        guest_details_button.grid(row=4, column=3, sticky=N, padx=127, pady=30)
        guest_details_label.grid(row=4, column=2, sticky=E)
        guest_delete_button.grid(row=4, column=3, sticky=S)
        forget_programs()
        forget_register()
        forget_homepage()

#FUNCTION FOR CLEARING ALL WIDGETS
def clear_entry():
    global price
    first_nameVar.set("")
    last_nameVar.set("")
    PhoneVar.set("")
    EmailVar.set("")
    RoomVar.set("")
    MedicalVar.set("")
    AgeVar.set(0)
    GenderVar.set(0)
    PaddleVar.set(0)
    ScubaVar.set(0)
    ConcertVar.set(0)
    WhaleVar.set(0)
    GolfingVar.set(0)
    KayakingVar.set(0)
    MovieVar.set(0)
    price = 0
    clear_price()
    display_price()

#FUNCTION FOR CLEARING PRICE LABEL
def clear_price():
    global price_label
    price_label.grid_forget()

#FUNCTION FOR DETERMINING IF GENDER IS MALE OR FEMALE
def get_gender(gname):
    gender = ""
    if gname == 1:
        gender = 'Male'
    if gname == 2:
        gender = 'Female'
    return gender

#FUNCTION FOR REGISTERING GUESTS DETAILS IN LIST WITHOUT CURLY BRACKETS
def register_names():
    global name_list
    first = first_nameVar.get().upper()
    last = last_nameVar.get().upper()
    name_list.append(f'Name: {first} {last}')
    GuestsVar.set(name_list)

#FUNCTION FOR GETTING INFORMATION WHEN REGISTERING GUESTS AND ALSO DISPLAYING SPOTS LEFT IN RESORT
def register_details():
    global registered_label
    global number_of_guests
    registered_label.grid_forget()
    number_of_guests = f'Number of Guests: {1+len(large_details_list)}/10'
    registered_label = Label(topframe, text=number_of_guests, font=medium_font, bg="#c2e8dc")
    registered_label.grid(row=1, column=3, sticky=W)
    gender = get_gender(GenderVar.get())
    mini_list = []
    register_names()
    mini_list.append(AgeVar.get())
    mini_list.append(gender)
    mini_list.append(PhoneVar.get())
    mini_list.append(EmailVar.get())
    mini_list.append(RoomVar.get())
    mini_list.append(MedicalVar.get())
    if PaddleVar.get() == 1:
        mini_list.append("Stand Up Paddle Boarding")
    if ScubaVar.get() == 2:
        mini_list.append("Scuba Diving")
    if ConcertVar.get() == 3:
        mini_list.append("Concert")
    if WhaleVar.get() == 4:
        mini_list.append("Whale Watching")
    if GolfingVar.get() == 5:
        mini_list.append("Golfing")
    if KayakingVar.get() == 6:
        mini_list.append("Kayaking")
    if MovieVar.get() == 7:
        mini_list.append("Movie Under the Stars")
    clear_entry()
    if len(large_details_list) < 9:
        large_details_list.append(mini_list)
    else:
        large_details_list.append(mini_list)
        register_button.configure(state=DISABLED)

#FUNCTION FOR DISPLAYING EXTRA DETAILS FOR EACH REGISTRATION
def guest_details():
    if(guests_listbox.curselection() == ()):
        return
    selection = guests_listbox.curselection()[0]
    first = large_details_list[selection][0]
    second = large_details_list[selection][1]
    third = large_details_list[selection][2]
    fourth = large_details_list[selection][3]
    fifth = large_details_list[selection][4]
    sixth = large_details_list[selection][5]
    six_to_eight = large_details_list[selection][6:9]
    last = large_details_list[selection][9:]
    format_data = (f'Age: {first}\nGender: {second}\nPhone: {third}\nEmail: {fourth}\nRoom: {fifth}\nMedical: {sixth}\nPrograms: {six_to_eight}\n{last}')
    guest_details_var.set(format_data)

#FUNCTION FOR DELETING GUEST ENTRIES
def guest_delete():
    global registered_label
    global number_of_guests
    if(guests_listbox.curselection() == ()):
        return
    selection = guests_listbox.curselection()[0]
    guests_listbox.delete(selection)
    guest_details_var.set('')
    name_list.pop(selection)
    large_details_list.pop(selection)
    registered_label.grid_forget()
    number_of_guests = f'Number of Guests: {len(large_details_list)}/10'
    registered_label = Label(topframe, text=number_of_guests, font=medium_font, bg="#c2e8dc")
    registered_label.grid(row=1, column=3, sticky=W)
    register_button.configure(state=NORMAL)

#FUNCTION FOR DISPLAYING EXTRA DETAILS FOR THE PROGRAMS
def program_details():
    if(programs_listbox.curselection() == ()):
        return
    day1 = 'Monday, January 7th'
    day2 = 'Tuesday, January 8th'
    day3 = 'Wednesday, January 9th'
    day4 = 'Thursday, January 10th'
    day5 = 'Friday, January 11th'
    day6 = 'Saturday, January 12th'
    day7 = 'Sunday, January 13th'
    morning = '10:00 AM'
    noon = '12:00 AM'
    afternoon = '2:00 PM'
    early_evening = '4:00 PM'
    evening = '6:00 PM'
    nighttime = '10:00 PM'
    beach_location1 = 'Far right side of the beach'
    beach_location2 = 'Far left side of the beach'
    beach_location3 = 'General beach area'
    golf = 'Golf course beside main building'
    main = 'Main Building'
    dock = 'At the dock'

    selection = programs_listbox.curselection()[0]
    if selection == 0:
        program_details_var.set(f'Day: {day1}\nTime: {morning}\nLocation: {beach_location1}')
    elif selection == 1:
        program_details_var.set(f'Day: {day2}\nTime: {noon}\nLocation: {beach_location2}')
    elif selection == 2:
        program_details_var.set(f'Day: {day3}\nTime: {evening}\nLocation: {main}')
    elif selection == 3:
        program_details_var.set(f'Day: {day4}\nTime: {early_evening}\nLocation: {dock}')
    elif selection == 4:
        program_details_var.set(f'Day: {day5}\nTime: {afternoon}\nLocation: {golf}')
    elif selection == 5:
        program_details_var.set(f'Day: {day6}\nTime: {noon}\nLocation: {beach_location1}')
    elif selection == 6:
        program_details_var.set(f'Day: {day7}\nTime: {nighttime}\nLocation: {beach_location3}')

#DISPLAY PRICE
def display_price():
    global price_label
    PriceVar.set(price)
    price_label = Label(mainframe, text=f'Price: ${PriceVar.get():.2f}', font=main_font, bg="#c2e8dc")
    price_label.grid(row=5, column=3, padx=20, sticky=W)

#EACH FUNCTION IS ASSIGNED TO A DIFFERENT PROGRAM AS A COMMAND, IT CLEARS THE PREVIOUS GRID BEFORE IT DISPLAYS A NEW ONE
def paddle_price():
    global price
    price_label.grid_forget()
    if PaddleVar.get() == 1:
        price += 35
    else:
        price -= 35
    display_price()

def scuba_price():
    price_label.grid_forget()
    global price
    if ScubaVar.get() == 2:
        price += 65
    else:
        price -= 65
    display_price()

def concert_price():
    price_label.grid_forget()
    global price
    if ConcertVar.get() == 3:
        price += 79
    else:
        price -= 79
    display_price()

def whale_price():
    price_label.grid_forget()
    global price
    if WhaleVar.get() == 4:
        price += 29
    else:
        price -= 29
    display_price()

def golfing_price():
    price_label.grid_forget()
    global price
    if GolfingVar.get() == 5:
        price += 25
    else:
        price -= 25
    display_price()

def kayaking_price():
    price_label.grid_forget()
    global price
    if KayakingVar.get() == 6:
        price += 28
    else:
        price -= 28
    display_price()

def movie_price():
    price_label.grid_forget()
    global price
    if MovieVar.get() == 7:
        price += 24
    else:
        price -=24
    display_price()

#SETTING UP ALL WIDGETS INCLUDING THEIR FONT, COLORS, SIZE, ETC
title = Label(topframe, text="Blossom Springs", font=("Segoe Script", 35), bg="#c2e8dc")

#Option Menu is gridded to root so it displays top left
Options = ['Homepage', 'Register Guests', 'View Programs', 'View Guests']
OptionVar = StringVar()
OptionVar.set('Homepage')
Option = OptionMenu(root, OptionVar, *Options, command=changescreen)
Option.config(bg="#c2e8dc", highlightbackground="#c2e8dc", activebackground="#437b99")

first_name_label = Label(mainframe, text="First Name", font=medium_font, bg="#c2e8dc")
last_name_label = Label(mainframe, text="Last Name", font=medium_font, bg="#c2e8dc")
phone_label = Label(mainframe, text="Phone", font=medium_font, bg="#c2e8dc")
email_label = Label(mainframe, text="Email", font=medium_font, bg="#c2e8dc")
room_label = Label(mainframe, text="Room Number", font=medium_font, bg="#c2e8dc")
medical_label = Label(mainframe, text="Medical", font=medium_font, bg="#c2e8dc")

registered_label = Label(topframe, text="Number of Guests: 0/10", font=medium_font, bg="#c2e8dc")

programs_label_frame = LabelFrame(mainframe, text="Programs", font=medium_font, width=40, bg="#c2e8dc")

first_nameVar = StringVar()
first_name_entry = Entry(mainframe, width=15, font=main_font, textvariable=first_nameVar, bg="#c2e8dc")

last_nameVar = StringVar()
last_name_entry = Entry(mainframe, width=15, font=main_font, textvariable=last_nameVar, bg="#c2e8dc")

GenderVar = IntVar()
MaleRadio = Radiobutton(mainframe, text="Male", variable=GenderVar, value=1, font=small_font, bg="#c2e8dc", activebackground="#c2e8dc")
FemaleRadio = Radiobutton(mainframe, text="Female", variable=GenderVar, value=2, font=small_font, bg="#c2e8dc", activebackground="#c2e8dc")

PhoneVar = StringVar()
phone_entry = Entry(mainframe, width=15, font=main_font, textvariable=PhoneVar, bg="#c2e8dc")

EmailVar = StringVar()
email_entry = Entry(mainframe, width=15, font=main_font, textvariable=EmailVar, bg="#c2e8dc")

RoomVar = StringVar()
room_entry = Entry(mainframe, width=15, font=main_font, textvariable=RoomVar, bg="#c2e8dc")

MedicalVar = StringVar()
medical_entry = Entry(mainframe, width=15, font=main_font, textvariable=MedicalVar, bg="#c2e8dc")

guest_details_button = Button(root, text="See Details", font=medium_font, width=10, height=2, command=guest_details, bg="#c2e8dc", activebackground="#437b99")

guest_delete_button = Button(root, text="Delete", font=medium_font, width=10, height=1, command=guest_delete, bg="#c2e8dc", activebackground="#437b99")

program_details_button = Button(root, text="See Details", font=medium_font, width=10, height=2, command=program_details, bg="#c2e8dc", activebackground="#437b99")

AgeVar = IntVar()
age_var_scale = Scale(mainframe, from_=150, to=0, label='Age', variable=AgeVar, length=100, orient=VERTICAL, bg="#c2e8dc", activebackground="#c2e8dc", highlightbackground="#c2e8dc")

PaddleVar = IntVar()
PaddleCheck = Checkbutton(programs_label_frame, text="Stand Up Paddle Boarding", onvalue=1, offvalue = 0, command=paddle_price, variable = PaddleVar, font=small_font, bg="#c2e8dc", activebackground="#c2e8dc")

ScubaVar = IntVar()
ScubaCheck = Checkbutton(programs_label_frame, text="Scuba Diving", onvalue=2, offvalue = 0, command=scuba_price, variable = ScubaVar, font=small_font, bg="#c2e8dc", activebackground="#c2e8dc")

ConcertVar = IntVar()
ConcertCheck = Checkbutton(programs_label_frame, text="Concert", onvalue=3, offvalue = 0, command=concert_price, variable = ConcertVar, font=small_font, bg="#c2e8dc", activebackground="#c2e8dc")

WhaleVar = IntVar()
WhaleCheck = Checkbutton(programs_label_frame, text="Whale Watching", onvalue=4, offvalue = 0, command=whale_price, variable = WhaleVar, font=small_font, bg="#c2e8dc", activebackground="#c2e8dc")

GolfingVar = IntVar()
GolfingCheck = Checkbutton(programs_label_frame, text="Golfing", onvalue=5, offvalue = 0, command=golfing_price, variable = GolfingVar, font=small_font, bg="#c2e8dc", activebackground="#c2e8dc")

KayakingVar = IntVar()
KayakingCheck = Checkbutton(programs_label_frame, text="Kayaking", onvalue=6, offvalue = 0, command=kayaking_price, variable = KayakingVar, font=small_font, bg="#c2e8dc", activebackground="#c2e8dc")

MovieVar = IntVar()
MovieCheck = Checkbutton(programs_label_frame, text="Movie Under the Stars", onvalue=7, offvalue = 0, command=movie_price, variable = MovieVar, font=small_font, bg="#c2e8dc", activebackground="#c2e8dc")

register_button = Button(mainframe, text="Register", command=register_details, width=20, height=5, state=NORMAL, bg="#c2e8dc", activebackground="#437b99")

program_label = Label(mainframe, text="Programs", font=medium_font, bg="#c2e8dc")

guests_label = Label(mainframe, text="Guests", font=medium_font, bg="#c2e8dc")

#DETAILS LABEL USES ANCHOR SO TEXT IS ALWAYS ON THE RIGHT AND WIDTH SO THE LABEL BOX IS ALWAYS THE SAME WIDTH
guest_details_var = StringVar()
guest_details_label = Label(root, textvariable=guest_details_var, justify=LEFT, font=("Constantia", 13), anchor=W, width=50, height=8, bg="#c2e8dc")

program_details_var = StringVar()
program_details_label = Label(root, textvariable=program_details_var, justify=LEFT, font=medium_font, anchor=W, width=41, bg="#c2e8dc")

#PROGRAM LIST FOR ALL THE PROGRAMS IN THE RESORT
all_programs = ["Stand Up Paddle Boarding", "Scuba Diving", "Concert", "Whale Watching"\
    ,"Golfing", "Kayaking", "Movie Under the Stars"]
ProgramsVar = StringVar()
ProgramsVar.set(all_programs)
programs_listbox = Listbox(mainframe, selectmode=SINGLE, listvariable=ProgramsVar, width=50, font=main_font, height=10, bg="#c2e8dc")

GuestsVar = StringVar()
guests_listbox = Listbox(mainframe, selectmode=SINGLE, listvariable=GuestsVar, width=50, font=main_font, height=10, bg="#c2e8dc")

flowerImage = Image.open("flower.png").resize((500, 250))
flowerPhoto = ImageTk.PhotoImage(flowerImage)

#CREATING LOGO WITH LINES AND CANVAS
logo_canvas = Canvas(mainframe, width=1000, height=700, bg="#f2b6c1", highlightthickness=3, highlightbackground='#cfd7f8')
logo_canvas.create_line(0, 0, 120, 120, fill='#e1dff8', width=3)
logo_canvas.create_line(1000, 0, 120, 120, fill='#e1dff8', width=3)
logo_canvas.create_line(0, 594, 120, 120, fill='#e1dff8', width=3)
logo_canvas.create_line(1000, 0, 870, 470, fill='#e1dff8', width=3)
#FOR MAC
#logo_canvas.create_line(1030, 620, 870, 470, fill='#e1dff8', width=3)
#logo_canvas.create_line(0, 595, 870, 470, fill='#e1dff8', width=3)
#FOR WINDOWS
logo_canvas.create_line(0, 570, 870, 470, fill='#e1dff8', width=3)
logo_canvas.create_line(1030, 594, 870, 470, fill='#e1dff8', width=3)
logo_canvas.create_image(498, 298, image=flowerPhoto)

#GRIDDING PERMANENT WIDGETS
#root.geometry("1000x800")
root.minsize(width=1000, height=750)
root.maxsize(width=1000, height=750)
mainframe.grid(row=2, column=1, columnspan=3)
topframe.grid(row=1, column=1, columnspan=3)
logo_canvas.grid(row=2, column=1, columnspan=3)
title.grid(row=1, column=2, sticky=N, padx=150, pady=40)
Option.grid(row=1, column=1, sticky=NW)
registered_label.grid(row=1, column=3, sticky=W)

root.mainloop()