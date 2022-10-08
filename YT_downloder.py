# youtube downloader by PyRedouane (tkinter,bytube)

import tkinter as tk
from pytube import YouTube as yt

root = tk.Tk()
root.title("Youtube downloader by RD1")
root.geometry("650x350")
root.configure(bg="grey")
root.resizable(False, False)

tk.Label(root, text="============= YouTube Downloader =============",
         font="arial 25 bold", fg="cyan", bg="grey").pack()

tk.Label(root, text="Download & convert videos from Youtube",
         font="arial 15 bold", bg="grey", fg="white").place(x=128, y=35)

tk.Label(root, text="copy and paste link here :",
         font="arial 13 bold", bg="grey", fg="cyan").place(x=215, y=100)

link = tk.StringVar()

link_entry = tk.Entry(root, width=65, textvariable=link).place(x=115, y=130)


def high_quality():
    get_link = yt(str(link.get()))
    vd = get_link.streams.get_highest_resolution()
    vd.download()


def low_quality():
    get_link = yt(str(link.get()))
    vd = get_link.streams.get_lowest_resolution()
    vd.download()


def audio_only():
    get_link = yt(str(link.get()))
    vd = get_link.streams.get_audio_only()
    vd.download()


high_quality_button = tk.Button(text="high quality", bg="#138D75",
                                fg="white", width=19, height=4,
                                font="arial 10 bold", command=high_quality).place(x=45, y=170)

low_quality_button = tk.Button(text="low quality", bg="#F39C12",
                               fg="white", width=19, height=4,
                               font="arial 10 bold", command=low_quality).place(x=245, y=170)

only_audio_button = tk.Button(text="audio", bg="#CB4335",
                              fg="white", width=19, height=4,
                              font="arial 10 bold", command=audio_only).place(x=445, y=170)

tk.mainloop()
