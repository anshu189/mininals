'''
Author: Anshu Saini
GitHub: https://github.com/anshu189
Mail: anshusaini189381@gmail.com
Requirements: tkinter, time (pip install tkinter)
Program: Clock

'''

from tkinter import *
from tkinter.ttk import *
from time import strftime

root = Tk()
root.title("Clock")
root.wm_minsize(440, 90)
root.resizable(width=0, height=0)

def time():
    string = strftime("%H:%M:%S:%p")
    label.config(text=string)
    label.after(1000, time)

label = Label(root, font=("ds-digital", 80), background = "black", foreground = "cyan")
label.pack(anchor="center")
time()

mainloop()
