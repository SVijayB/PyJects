from pytube import YouTube
from tkinter import *


class SecondWindow:
    def __init__(self, downloadWindow, youtubeEntry, folderName, choice):
        self.downloadWindow = downloadWindow
        self.downloadWindow.state("zoomed")
        self.downloadWindow.grid_rowconfigure(0, weight=0)
        self.downloadWindow.grid_columnconfigure(0, weight=1)
        self.youtubeEntry = youtubeEntry
        self.folderName = folderName
        self.choice = choice

        self.yt = YouTube(self.youtubeEntry)

        if self.choice == "1":
            self.stream = self.yt.streams.first()

        if self.choice == "2":
            self.stream = self.yt.streams.filter(only_audio=True).first()

        self.downloadFile()

        self.loading = Label(
            self.downloadWindow,
            text="Download Completed\nThanks For Using YouTube Extractor",
            font=("Small Fonts", 40),
        )
        self.loading.grid(pady=(100, 0))
        downloadWindow.protocol("WM_DELETE_WINDOW", self.closing)
        downloadWindow.mainloop()

    def downloadFile(self):
        print(
            "\nYour File Is Being Downloaded...\nWe will notify you once Download is completed."
        )
        print("Thanks For Using YouTube Extractor")
        self.stream.download(self.folderName)

    def closing(self):
        sys.exit(0)
