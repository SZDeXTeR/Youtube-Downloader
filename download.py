from tkinter import *
from tkinter import filedialog
from pytube import YouTube
import webbrowser

import shutil

def dxtr_yt():
    webbrowser.open_new_tab("https://www.youtube.com/channel/UCPviajcbiDUYAn5ADwzp8dg")

#Functions
def select_path():
    #allows user to select a path from the explorer
    path = filedialog.askdirectory()
    path_label.config(text=path)

def download_file():
    #get user path
    get_link = link_field.get()
    #get selected path
    user_path = path_label.cget("text")
    screen.title('Downloading...')
    #Download Video
    mp4_video = YouTube(get_link).streams.get_highest_resolution().download()
    #move file to selected directory
    shutil.move(mp4_video, user_path)
    screen.title('Download Complete! Download Another File... (By DeXTeR)')

screen = Tk()
title = screen.title('Youtube Download By DeXTeR')
canvas = Canvas(screen, width=500, height=500)
canvas.pack()

#image logo
logo_img = PhotoImage(file='yt.png')
#resize
logo_img = logo_img.subsample(2, 2)
canvas.create_image(250, 80, image=logo_img)

#link field
link_field = Entry(screen, width=40, font=('Arial', 15) )
link_label = Label(screen, text="Enter Download Link: ", font=('Arial', 15))

#Select Path for saving the file
path_label = Label(screen, text="Select Path For Download\nBy DeXTeR", font=('Arial', 15))
select_btn =  Button(screen, text="Select Path", bg='red', padx='22', pady='5',font=('Arial', 15), fg='#fff', command=select_path)

#DeXTeR YT Link
dexter_yt =  Button(screen, text="DeXTeR's Channel", bg='red', padx='22', pady='5',font=('Arial', 15), fg='#fff', command=dxtr_yt)

#Add to window
canvas.create_window(250, 280, window=path_label)
canvas.create_window(250, 330, window=select_btn)
canvas.create_window(250, 460, window=dexter_yt)

#Add widgets to window 
canvas.create_window(250, 170, window=link_label)
canvas.create_window(250, 220, window=link_field)

#Download btns
download_btn = Button(screen, text="Download File",bg='green', padx='22', pady='5',font=('Arial', 15), fg='#fff', command=download_file)
#add to canvas
canvas.create_window(250, 390, window=download_btn)

screen.mainloop()