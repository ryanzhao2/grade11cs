from tkinter import *
from tkinter.font import Font


def generate_spotify_list(filename):
    global spotify_music_list
    spotify_music_list = []

    fileIn = open(filename, encoding='utf-8', errors = 'replace')
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
        
    
        

def format_music():
    global spotify_music_list


    


def see_song_details():
    global spotify_music_list
    
    



#MAIN

global spotify_music_list
spotify_music_list = generate_spotify_list("spotifyJan172020.csv")

#Holding frames
#########

root = Tk()
mainframe = Frame(root)

monofurFont = Font(family="monofur", size=20)
monofurFontMedium = Font(family="monofur", size=30)
monofurFontLarge = Font(family="monofur", size=40)


#Widgets
#########
title = Label(mainframe, text="music", font=monofurFontLarge)

music_list = format_music()

music_listbox = Listbox(mainframe, selectmode=SINGLE, width=80, font=monofurFont)


info_var = StringVar()
info_var.set("")
info_label = Label(mainframe, textvariable=info_var, justify=LEFT, fg="#dd0054", font=monofurFontMedium)

seemore_button = Button(mainframe, text="see more", font=monofurFontLarge, command = see_song_details)
    
#GRID THE WIDGETS
###########

mainframe.grid(padx=50, pady=50)
title.grid(row=1, column=1, sticky=W, padx = 20, pady=5)
music_listbox.grid(row=2, column=1, columnspan=2, padx=10)
info_label.grid(row=3, column=1, sticky=W, padx=10, pady=10)
seemore_button.grid(row=3, column=2, ipady=20, ipadx=40, padx=10, pady=10, sticky=E)

