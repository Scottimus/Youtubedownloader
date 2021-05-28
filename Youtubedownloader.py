"""
This is a tool to download the highest resolution stream from a youtube URL the user pastes into the blank field.
"""
#import Libraries tkinter for the GUI and pytube for the youtube download funtionality
import tkinter
from pytube import YouTube

#create the parameters of the popup interface that the user then can interact with
root = tkinter.Tk()
root.geometry("500x230")#can change the dimensions of the GUI here
root.resizable(0,0)
root.title("YouTube Downloader")#title of GUI box

tkinter.Label(root, text = "YouTube Downloader", font ="arial 20 bold").pack()#header title

link = tkinter.StringVar()

tkinter.Label(root, text ="Paste Link Here: ", font ="arial 16 bold").place(x= 160, y = 60)#the main funtion of the program
link_enter = tkinter.Entry(root, width = 70, textvariable = link).place(x = 32, y = 90)

def Download():#the download funtion for this tool to work
    url = YouTube(str(link.get()))
    video = url.streams.get_highest_resolution()#pytube has other .get funtions such as audio only or lower resolutions
    video.download()#download command (Will download to directory where program is run)
    tkinter.Label(root, text = "Downloaded", font = "arial 16").place(x = 180, y = 200)#once download is finished text saying "downloaded" will pop up

tkinter.Button(root, text = "Download", font = "arial 16 bold", bg = "grey", padx = 2, command = Download).place(x = 180, y = 150)#button that links to download function

root.mainloop()