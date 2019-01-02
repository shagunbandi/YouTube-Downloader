from tkinter import *
from tkinter.ttk import *
import youtube_dl
import tkinter as tk

from helper import up_down
from audio import download_audio
from video import download_video


def download():
	url = url_txt.get()

	print("url: " + url)
	print("av_val: " + str(av_val))
	print("plst_val: " + str(plst_val))

	if av_val:
		download_audio(url, plst_val)
		av_switch(True)
	else:
		download_video(url, plst_val)
		plst_switch(True)


def plst_switch(reset=False):

	global plst_val

	if reset:
		plst_val = False
	
	if plst_val:
		plst_btn["text"] = "No"
		plst_val = False
	else:
		plst_btn["text"] = "Yes"
		plst_val = True


def av_switch(reset=False):
	global av_val

	if reset:
		av_val = False

	if av_val:
		av_btn["text"] = "Video"
		av_val = False
	else:
		av_btn["text"] = "Audio"
		av_val = True


win = tk.Tk()

win.title("Youtube Downloader")
win.geometry('500x200')


# URL Label
url_lbl = Label(win, text ="Enter the URL here")
url_lbl.grid(column = 0, row = 0)

# URL Value
url_txt = Entry(win, width=30)
url_txt.grid(column = 1, row = 0, columnspan=1)

# Playlist Label
plst_lbl = Label(win, text ="Download the full Playlist?")
plst_lbl.grid(column = 0, row = 1)

# Plst Button
plst_val = True
plst_btn = Button(win, text="Yes", command = plst_switch)
plst_btn.grid(column = 1, row = 1)

# AV Label
av_lbl = Label(win, text ="Audio or Video?")
av_lbl.grid(column = 0, row = 2)

# AV Button
av_val = True
av_btn = Button(win, text="Audio", command = av_switch)
av_btn.grid(column = 1, row = 2)

# Download Button
btn = Button(win, text="Download", command = download, width=30)
btn.grid(column = 0, row = 4, columnspan=2)

win.mainloop()