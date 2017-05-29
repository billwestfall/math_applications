from tkinter import *

master = Tk()

def callback():
    print("There have been no clicks yet")

b = Button(master, text="click me", command=callback)
b.pack()

mainloop()
