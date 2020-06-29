from tkinter import *
from Modules.SelectionWindow import SelectionWindow

if __name__ == "__main__":
    window = Tk()
    data = open("../assets/version.txt" , "r").read()
    window.state("zoomed")
    window.title("Typing-Speed-Test | " + data)
    window.iconbitmap("../assets/images/Icon.ico")
    app = SelectionWindow(window)
    window.mainloop()