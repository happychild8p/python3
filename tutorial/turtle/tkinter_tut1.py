#!/usr/bin/python3

from tkinter import *

window = Tk()
l1 = Label(window, text = 'ID')
l2 = Label(window, text = 'Password')
l1.grid(row=0, column=0)
l2.grid(row=1, column=0)
e1 = Entry(window)
e2 = Entry(window)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
b1 = Button(window, text="Enter")
b2 = Button(window, text="Cancel")
b1.grid(row=2, column=0)
b2.grid(row=2, column=1)
window.mainloop()
