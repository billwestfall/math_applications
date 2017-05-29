from tkinter import *

master = Tk()

def callback():
    print("click me")

b = Button(master, text="OK", command=callback)
b.pack()

mainloop()
