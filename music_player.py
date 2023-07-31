import pygame
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from mutagen.mp3 import MP3

root = tk.Tk()
root.title("Carva!")
root.configure(bg='red')
root.geometry('1000x10000')

def select_file():
    file_path = filedialog.askopenfilename(filetypes=[('Audio Files', '*.mp3')])
    return file_path

def audio_duration(length):
    hours = length // 3600  # calculate in hours
    length %= 3600
    mins = length // 60  # calculate in minutes
    length %= 60
    seconds = length  # calculate in seconds
    return hours, mins, seconds

def play_music():
    file_name = select_file()
    if file_name:
        try:
            pygame.mixer.init()
            pygame.mixer.music.load(file_name)
            pygame.mixer.music.play()
            audio = MP3(file_name)
            length = int(audio.info.length)
            hours, mins, seconds = audio_duration(length)
            print('Total Duration: {}:{}:{}'.format(hours, mins, seconds))

            update_time(hours, mins, seconds)  # Update the time on the GUI

        except pygame.error as e:
            print("Error:", e)

def update_time(hours, mins, seconds):
    time_label.config(text='Total Duration: {}:{}:{}'.format(hours, mins, seconds))
    root.after(1000, lambda: update_time(hours, mins, seconds))  # Update the time every 1 second

def music_end_callback():
    # This function will be called when the music finishes playing
    pygame.mixer.music.stop()
    pygame.mixer.music.set_endevent(pygame.USEREVENT)
    pygame.mixer.quit()

def rewindMusic():
    pygame.mixer.music.rewind()

def pause_unpause():
    if pygame.mixer.music.get_busy():
        pygame.mixer.music.pause()
    else:
        pygame.mixer.music.unpause()

# GUI components

label = tk.Label(root, text="Carva", bg='red', font=('Blackadder ITC', 200))
label.pack(pady=50)

photo1 = tk.PhotoImage(file='image_path')
photoimage1 = photo1.subsample(60, 65)
btn1 = tk.Button(root, text='Music', image=photoimage1, bd='5', fg='blue', height=40, width=50, relief=tk.FLAT, command=play_music)
btn1.place(x=490, y=550)
btn1.bind("<KeyPress>", select_file)

btn2 = tk.Button(root, text='Quit!', command=root.destroy, fg='black', relief=tk.SUNKEN)
btn2.place(y=2, x=1240)
btn2.configure(bg="red")

btn3 = tk.Button(root, text='rewind', bd='5', fg='blue', height=2, width=7, relief=tk.FLAT, command=rewindMusic)
btn3.place(x=900, y=552)

photo4 = tk.PhotoImage(file='image_path')
photoimage4 = photo4.subsample(3, 4)
btn4 = tk.Button(root, text='stop music', image=photoimage4, bd='5', fg='blue', relief=tk.FLAT, command=music_end_callback)
btn4.place(x=1150, y=552)

photo5 = tk.PhotoImage(file='image_path')
photoimage5 = photo5.subsample(20, 20)
btn5 = tk.Button(root, text='pause', image=photoimage5, bd='5', relief=tk.FLAT, command=pause_unpause)
btn5.place(x=90, y=550)

# Time label
time_label = tk.Label(root, text='', bg='red', fg='white', font=('Helvetica', 16))
time_label.place(x=490, y=610)

# Bind the event to the music_end_callback function
pygame.mixer.init()
pygame.mixer.music.set_endevent(pygame.USEREVENT)

root.mainloop()
