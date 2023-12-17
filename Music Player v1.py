from tkinter import *
from tkinter import filedialog
import pygame.mixer as mixer
import os

mixer.init()

#below is the setup of the pause, play, load, stop and resume functions

def play_song(song_name: StringVar, songs_list: Listbox, status: StringVar):
    song_name.set(songs_list.get(ACTIVE))

    mixer.music.load(songs_list.get(ACTIVE))
    mixer.music.play()

    status.set("Now Playing")

def stop_song(status: StringVar):
    mixer.music.stop()
    status.set("Playback Ended")

def load(listbox):
    os.chdir(filedialog.askdirectory(title='Choose songs folder'))

    tracks = os.listdir() #the os module is looking into the current directory (of my machine) for the lists of files and then assigns each to the variable "tracks"

    for track in tracks:
        listbox.insert (END, track) #it adds each of the songs 1 after the other in separate boxes (icon/box to click on basically)

def pause_song(status: StringVar):
    mixer.music.pause()
    status.set("Paused")

def resume_song(status: StringVar):
    mixer.music.unpause()
    status.set("Resumed")

#there is only 1 StringVar being used by all the functions

# Creating the master GUI

root = Tk()
root.geometry('700x220') #specify the size of the GUI window
root.title('Kallfic Music Player')
root.resizable(0, 0) #stops the user from being able to resize the window

song_frame = LabelFrame(root, text= 'Current Song', bg='LightBlue', width=400, height=80)
song_frame.place(x=0, y=0)

button_frame = LabelFrame(root, text='Buttons that control the music', bg='Turquoise', width=400, height=120)
button_frame.place(y=80)

listbox_frame = LabelFrame(root, text='Playlist', bg='RoyalBlue') #the size and colour of the box that displays all the song in the playlist
listbox_frame.place(x=400, y=0, height=200, width=300)

current_song = StringVar(root, value='<Not Selected>') #it's dynamic, it will show whatever song is being played once it happens, even while it is paused, stopped etc

current_status = StringVar(root, value='<Not Available>') #it's dynamic as in it can change depending on whether the song is playing paused etc

#now I am working on the contents of the playlist box

playlist = Listbox(listbox_frame, font=('Helvetica', 11), selectbackground='Gold') #this sets the font of the elements within the playlist box as well as the font size. Background colour being gold too

scroll_bar = Scrollbar(listbox_frame, orient=VERTICAL) #creates a vertical scroll bar
scroll_bar.pack(side=RIGHT, fill=BOTH) #places the scroll bar on the right side of the playlist box but still within it

playlist.config(yscrollcommand=scroll_bar.set) #this tells the playlist listbox to use the scroll bar. The ".set" part is used to tell the scroll bar to change depending on the size of the playlist

scroll_bar.config(command=playlist.yview) #allows the scroll bar to change the y-axis of the playlists list box

playlist.pack(fill=BOTH, padx=5, pady=5) #the pack command places the playlist listbox into the parent widget (the music window itself) + BOTH then instructs the listbox to fill both sides vert and horizontally

Label(song_frame, text='Currently Playing', bg='LightBlue', font=("Times", 10, 'bold')).place(x=5, y=20)

song_lbl = Label(song_frame, textvariable=current_song, bg='Goldenrod', font=("Times", 12), width=25) #it will highlight the song that is currently playing within the current song box not the playlist
song_lbl.place(x=150, y=20) #dictates where the highlighted box thing is gonna be placed (aka over the name of the file (the song) being played

#below is the placement of the buttons for controlling the player

pause_btn = Button(button_frame, text='Pause', bg='Aqua', font=("Georgia", 13), width=7,
                   command=lambda: pause_song(current_status))
pause_btn.place(x=15, y=10)

stop_btn = Button(button_frame, text='Stop', bg='Aqua', font=("Georgia", 13), width=7,
                  command=lambda: stop_song(current_status))
stop_btn.place(x=105, y=10)

play_btn = Button(button_frame, text='Play', bg='Aqua', font=("Georgia", 13), width=7,
                  command=lambda: play_song(current_song, playlist, current_status))
play_btn.place(x=195, y=10)

resume_btn = Button(button_frame, text='Resume', bg='Aqua', font=("Georgia", 13), width=7,
                    command=lambda: resume_song(current_status))
resume_btn.place(x=285, y=10)

load_btn = Button(button_frame, text='Load Directory', bg='Aqua', font=("Georgia", 13), width=35,
                  command=lambda: load(playlist))
load_btn.place(x=10, y=55)

Label(root, textvariable=current_status, bg='SteelBlue', font=('Times', 9), justify=LEFT).pack(side=BOTTOM, fill=X) #this just creates a label on the bottom part of the root window that extends all across the bottom. The label itself is whatever the current status of the song is (playing, paused etc). The justify part refers to the labels alligment with the text of the label

root.update()
root.mainloop()