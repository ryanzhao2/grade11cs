"""
from tkinter import *
from tkinter.font import Font
import random


def get_names(filename):
    global all_names

    all_names = []

    fileIn = open(filename, encoding='utf-8', errors='replace')

    for line in fileIn:
        all_names.append(line.strip())

    return all_names


def generate_names():
    random_list = []
    for i in range(10):
        random_list.append(random.choice(get_names("random_names.txt")))
    name_var.set(random_list)



# MAIN
global all_names
get_names("random_names.txt")

root = Tk()
root.config(bg="#293d3d")
mainframe = Frame(root, bg="#293d3d")

sunday_font = Font(family="Sunday", size=20)

title = Label(mainframe, text="Random Names", bg="#293d3d", fg="#ffffff", font=sunday_font)

# create the Listbox widget
initial_list=[]
name_var = StringVar()
for i in range(10):
    initial_list.append(random.choice(get_names("random_names.txt")))
name_var.set(initial_list)
name_listbox = Listbox(mainframe, listvariable=name_var, selectmode=SINGLE, font=sunday_font)



random_button = Button(mainframe, text="Randomize", highlightbackground="#669999", font=sunday_font,
                       command=generate_names)

# Grid the widgets
mainframe.grid(padx=100, pady=100)
title.grid(row=0, column=1, pady=10)
name_listbox.grid(row=1, column=1, pady=20)
random_button.grid(row=2, column=1, sticky=EW, ipady=10)

root.mainloop()
"""

from tkinter import *
from tkinter.font import Font


def load_images():
    global image_list
    rey_photo = PhotoImage(file="rey.png")
    bb8_photo = PhotoImage(file="bb8.png")
    c3po_photo = PhotoImage(file="c3po.png")
    finn_photo = PhotoImage(file="finn.png")
    poe_photo = PhotoImage(file="poe.png")

    image_list = [rey_photo, bb8_photo, c3po_photo, finn_photo, poe_photo]


def change_image():
    global image_list
    if images_listbox.curselection == 0:
        print(image_list[0])
    if images_listbox.curselection == 1:
        print(image_list[1])
    if images_listbox.curselection == 2:
        print(image_list[2])
    if images_listbox.curselection == 3:
        print(image_list[3])
    if images_listbox.curselection == 4:
        print(image_list[4])


# MAIN
# Holding frames
#########

root = Tk()
mainframe = Frame(root)

starwars_fontsmall = Font(family="Star Jedi", size=15)
starwars_font = Font(family="Star Jedi", size=30)

global image_list
load_images()
image_names = ['Rey', 'BB-8', 'C-3Po', 'Finn', 'Poe']

# Widgets
#########
title = Label(mainframe, text="star wars", font=starwars_font)

images_var = StringVar(value=image_names)
images_listbox = Listbox(mainframe, listvariable=images_var, selectmode=SINGLE, font=starwars_fontsmall)



current_image_label = Label(mainframe)

update_button = Button(mainframe, text="SEE", command=change_image)

# GRID THE WIDGETS
###########

mainframe.grid(padx=50, pady=50)
title.grid(row=1, column=1, sticky=W, padx=20, pady=5)
images_listbox.grid(row=2, column=1, padx=10)
current_image_label.grid(row=2, column=2, sticky=W, padx=10, pady=10)
update_button.grid(row=3, column=1, ipady=20, ipadx=40, padx=10, pady=10, sticky=E)


root.mainloop()

"""
from tkinter import *
from tkinter.font import Font


def generate_spotify_list(filename):
    global spotify_music_list
    spotify_music_list = []

    fileIn = open(filename, encoding='utf-8', errors='replace')
    fileIn.readline()
    fileIn.readline()

    for line in fileIn:
        line = line.strip().split(",")

        song = []
        song.append(int(line[0]))
        song.append(line[1].strip().replace('"', ''))
        song.append(line[2].strip().replace('"', ''))
        song.append(int(line[3]))

        spotify_music_list.append(song)
    return spotify_music_list

def format_music():
    global spotify_music_list
    format_list = []
    for i in range(len(spotify_music_list)):
        mini_list = []
        a = spotify_music_list[i][1]
        b = spotify_music_list[i][2]
        mini_list.append(f'{a:<30}')
        mini_list.append('by')
        mini_list.append(f'{b}')

        format_list.append(mini_list)
    return format_list





def see_song_details():
    global spotify_music_list
    selection = music_listbox.curselection()[0]
    first = spotify_music_list[selection][0]
    second = spotify_music_list[selection][1]
    third = spotify_music_list[selection][2]
    fourth = spotify_music_list[selection][3]
    format_data = (f'chart # {first}\n{second} by {third}\n#streams {fourth}')
    info_var.set(format_data)
# MAIN

global spotify_music_list
spotify_music_list = generate_spotify_list("spotifyJan172020.csv")

# Holding frames
#########

root = Tk()
mainframe = Frame(root)

monofurFont = Font(family="monofur", size=20)
monofurFontMedium = Font(family="monofur", size=30)
monofurFontLarge = Font(family="monofur", size=40)

# Widgets
#########
title = Label(mainframe, text="music", font=monofurFontLarge)


music_list = format_music()
musicVar = StringVar()
musicVar.set(music_list)
music_listbox = Listbox(mainframe, selectmode=SINGLE, listvariable=musicVar, width=80, font=monofurFont)



info_var = StringVar()
info_var.set("")
info_label = Label(mainframe, textvariable=info_var, justify=LEFT, fg="#dd0054", font=monofurFontMedium)

seemore_button = Button(mainframe, text="see more", font=monofurFontLarge, command=see_song_details)

# GRID THE WIDGETS
###########

mainframe.grid(padx=50, pady=50)
title.grid(row=1, column=1, sticky=W, padx=20, pady=5)
music_listbox.grid(row=2, column=1, columnspan=2, padx=10)
info_label.grid(row=3, column=1, sticky=W, padx=10, pady=10)
seemore_button.grid(row=3, column=2, ipady=20, ipadx=40, padx=10, pady=10, sticky=E)

root.mainloop()
"""