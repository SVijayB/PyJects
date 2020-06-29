from tkinter import *
import random

time = 61
score = 0
wordpos = 0	

def testwindow(wordslist):
    window = Tk()
    data = open("../assets/version.txt" , "r").read()
    window.title("Typing-Speed-Test | " + data)
    window.iconbitmap("../assets/images/Icon.ico")
    window.config(bg = "black")
    window.state("zoomed")

    colours = ["Red","Green","Pink","Yellow","Orange","White","Purple","Brown"]
    words = wordslist

    current_word = StringVar(window)
    entry_field = Entry(window, textvariable=current_word, width= 30, font = "Algerian 30",
        bg = "black", insertbackground = "red", fg='white')
    entry_field.focus()

    board = Label(window,text="Press enter \nto start",width=600,height=400,
            font="Algerian 70",fg = "green",bg = "black")
    board.pack()

    question = Label(window,font = "Algerian 60",bg = "black")
    question.place(x=450,y=200)

    time_up_message = Label(window)

    score_label = Label(window,text = "Words : 0", font = "Agency 25",fg = "green", bg = "black")

    time_label = Label(window)
        
    def time_decrement():
        global time
        if time>0:
            time = time - 1
            time_label.config(text = "Time Left : " + str(time),font = "Agency 25", 
                bg = "black", fg = "orange")
            time_label.place(x = 2, y = 2)
            window.after(1000,time_decrement)
        else:
            entry_field.place_forget()
            score_label.place_forget()
            time_label.place_forget()
            time_up_message.config(text = "Time's Up", font = "Algerian 80", bg = "black", 
                fg = "red", width = 600, height = 600)
            time_up_message.pack()
            window.after(2500,result)

    def final_score(score):
        return score
        
    def result():
        speed = Label(window,text = "Speed : " + str(score) + "wpm", 
            width = 200, height = 100, fg = "green", font = "Algerian 80",bg = "black")
        speed.pack()
        time_up_message.forget()
        score_label.forget()

    class test():
        def start(event):
            try:
                board.pack_forget()
                global time
                if (time == 61):
                    time_decrement()
                colour = random.randint(0,9)
                global wordpos
                wordpos = wordpos + 1
                question.config(text = str(words[wordpos]),fg = colours[colour])
                entry_field.place(x=350,y=400)
                score_label.place(x=1200,y=2)
            
                def correct(event):
                    global score
                    if (current_word.get() == (words[wordpos]).lower()):
                        entry_field.delete(0,END)
                        score = score + 1
                        score_label.config(text = "Words : " + str(score))
                        final_score(score)
                        test.start(event)
                    else:
                        entry_field.delete(0,END)
                        test.start(event)
                window.bind("<Return>",correct)
            except:
                pass
        window.bind("<Return>",start)

    def closing(): 
        sys.exit(0)

    window.protocol("WM_DELETE_WINDOW",closing)
    window.mainloop()