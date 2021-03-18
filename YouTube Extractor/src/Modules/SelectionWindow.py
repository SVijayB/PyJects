from tkinter import *
from tkinter import filedialog
from tkinter import ttk
import re
from Modules.SecondWindow import SecondWindow


class SelectionWindow:
    def __init__(self, root):
        self.root = root
        self.root.grid_rowconfigure(0, weight=2)
        self.root.grid_columnconfigure(0, weight=1)
        self.root.configure(bg="black")

        self.heading = Label(
            self.root,
            text="YOUTUBE EXTRACTOR",
            fg="green",
            bg="black",
            font=("Castellar", 70),
        )
        self.heading.grid(pady=(0, 10))

        self.link = Label(
            self.root,
            text="Paste the YouTube Link Below",
            fg="white",
            bg="black",
            font=("Algerian", 30),
        )
        self.link.grid(pady=(0, 20))

        self.entryvar = StringVar()
        self.entry = Entry(
            self.root,
            width=70,
            textvariable=self.entryvar,
            fg="green",
            bg="white",
            font=("Agency Fb", 25),
        )
        self.entry.grid(pady=(0, 15), ipady=2)

        self.error = Label(
            self.root, text="", font=("freestyle script", 25), bg="black", fg="white"
        )
        self.error.grid(pady=(0, 8))

        self.location = StringVar()

        self.save = Label(
            self.root,
            text="Select The Location You Want To Save In",
            fg="white",
            bg="black",
            font=("Algerian", 30),
        )
        self.save.grid()

        self.directory = Button(
            self.root,
            text="Location",
            fg="white",
            bg="black",
            font=("Bell MT", 15),
            command=self.openDirectory,
        )
        self.directory.grid(pady=(10, 3))

        self.fileLocation = Label(self.root, text="", bg="black")
        self.fileLocation.grid()

        self.choice = Label(
            self.root,
            text="Choose The Download Type",
            bg="black",
            fg="white",
            font=("Algerian", 30),
        )
        self.choice.grid()

        downloadChoices = [(" Video MP4 ", 1), (" Audio MP3 ", 2)]
        self.choiceVar = StringVar()
        self.choiceVar.set(1)

        for text, mode in downloadChoices:
            self.type = Radiobutton(
                self.root,
                text=text,
                font=("Northwest", 15),
                fg="#FF6347",
                bg="black",
                variable=self.choiceVar,
                value=mode,
            )
            self.type.grid()

        self.download = Button(
            self.root,
            text="Download",
            width=10,
            command=self.checkYoutubeLink,
            fg="white",
            bg="black",
            font=("Bell MT", 15),
        )
        self.download.grid(pady=(30, 5))

    def checkYoutubeLink(self):
        self.matchYoutubeLink = re.match(
            "^https://www.youtube.com/.*", self.entryvar.get()
        )

        if not self.matchYoutubeLink:
            self.error.config(text="Invalid YouTube Link", fg="red")
        elif len(self.FolderName) < 1:
            self.fileLocation.config(
                text="Please Select A Location To Save The File",
                fg="red",
                bg="black",
                font=("Freestyle script", 25),
            )
        elif self.matchYoutubeLink and len(self.FolderName) > 1:
            self.downloadWindow()

    def downloadWindow(self):
        self.new_window = Toplevel(self.root)
        self.root.withdraw()
        self.app = SecondWindow(
            self.new_window, self.entryvar.get(), self.location, self.choiceVar.get()
        )

    def openDirectory(self):
        self.FolderName = filedialog.askdirectory()
        if len(self.FolderName) > 1:
            self.fileLocation.config(
                text=self.FolderName,
                fg="green",
                bg="black",
                font=("Freestyle script", 25),
            )
            self.location = self.FolderName
            return True
        else:
            self.fileLocation.config(
                text="Please Choose The Folder",
                fg="red",
                bg="black",
                font=("Freestyle script", 25),
            )
            return False
        return False
