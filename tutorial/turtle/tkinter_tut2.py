#!/usr/bin/python3
from tkinter import *

def farToCel():
    e2.delete(0,END)
    temperature = float(e1.get())
    mytemp = (temperature-32)*5/9
    e2.insert(END, str(mytemp))
    
window = Tk()

l1 = Label(window, text="Fahrenheit")
l2 = Label(window, text="Celcius")
l1.grid(row=0, column=0)
l2.grid(row=1, column=0)

e1 = Entry(window)
e2 = Entry(window)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
b1 = Button(window, text="Fahrenheit -> Celsius", command=farToCel)
b2 = Button(window, text="Celsius -> Fahrenheit")
b1.grid(row=2, column=0)
b2.grid(row=2, column=1)
window.mainloop()
