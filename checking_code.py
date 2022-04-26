import tkinter
from tkinter import *
import messagebox
import requests
from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled
from pytube import YouTube

screen = tkinter.Tk()
title = screen.title("Download Video Transcript")

canvas = Canvas(screen, width=500, height=500)
canvas.pack()

lable1 = Label(screen, text="Download Video Subtitles")
canvas.create_window(250, 50, window=lable1)

video_id_field = Entry(screen, width=50)
lable2 = Label(screen, text="Enter Video ID")

canvas.create_window(250, 170, window=video_id_field)
canvas.create_window(250, 150, window=lable2)
# video_id_2 = video_id_field.get()


def video_subtitles():
    try:
        video_id = video_id_field.get()
        srt = YouTubeTranscriptApi.get_transcript(video_id)
        subtitles_file2 = open('srt_file_checking_code.txt', 'w')
        for text in srt:
            # subtitles_file2.write("%s\n" % text['text'])
            subtitles_file2.write(f"{text.get('text')}\n")
        messagebox.showinfo("Alert Message", "Video Transcript Downloaded")
    except TranscriptsDisabled:
        messagebox.showerror("Error Message", "Subtitles are unavailable")
    except:
        messagebox.showwarning("Error Message", "Please Enter Video ID ")


B = tkinter.Button(screen, text="Get Subtitles", command=video_subtitles, width=30, bg='brown', fg='white')
canvas.create_window(250, 250, window=B)
screen.mainloop()



