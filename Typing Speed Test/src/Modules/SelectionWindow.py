from tkinter import *
from Modules.Words import words


class SelectionWindow:
    def __init__(self, root):
        self.root = root
        self.root.grid_rowconfigure(0, weight=2)
        self.root.grid_columnconfigure(0, weight=1)
        self.root.configure(bg="black")

        self.heading = Label(
            self.root,
            text="TYPING SPEED TEST",
            fg="green",
            bg="black",
            font=("Castellar", 70),
        )
        self.heading.grid(pady=(0, 10))

        self.choice = Label(
            self.root,
            text="SELECT TYPING MODE",
            bg="black",
            fg="white",
            font=("Algerian", 40),
        )
        self.choice.grid(pady=(0, 100))

        Choices = [(" WARMUP ", 1), (" EASY ", 2), (" HARD ", 3)]
        self.choiceVar = StringVar()
        self.choiceVar.set(1)

        for text, mode in Choices:
            self.type = Radiobutton(
                self.root,
                text=text,
                font=("Northwest old", 15),
                fg="#FF6347",
                bg="black",
                variable=self.choiceVar,
                value=mode,
            )
            self.type.grid(pady=(0, 30))

        self.Start = Button(
            self.root,
            text="Start",
            width=10,
            command=self.launch,
            fg="white",
            bg="black",
            font=("Bell MT", 15),
        )
        self.Start.grid(pady=(30, 70))

    def launch(self):
        self.root.withdraw()
        words(self.choiceVar.get())
