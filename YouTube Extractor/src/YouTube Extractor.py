from tkinter import *
from Modules.SelectionWindow import SelectionWindow

if __name__ == "__main__":
    window = Tk()
    window.state("zoomed")
    data = open("../assets/version.txt", "r").read()
    print("YouTube Extractor | " + data)
    window.title("YouTube Extractor | " + data)
    window.iconbitmap("../assets/images/Icon.ico")
    app = SelectionWindow(window)
    window.mainloop()
