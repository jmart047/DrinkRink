# !/usr/bin/python3
from tkinter import *

from tkinter import messagebox

import sqlite3

conn = sqlite3.connect('DrinkRink1.db')
c = conn.cursor()

top = Tk()
top.geometry("300x300")
top.title("DrinkRink")
def test():
    L1 = Label(top, text = "Ingredient:")
    L1.grid( row=1, column=5)
    E1 = Entry(top, bd = 5)
    E1.grid(row = 9, column =5)
def drinklist():
    a = c.execute("SELECT * FROM Drinks ")
    b = c.fetchall()
    print(b)
    top = Toplevel()

   

B = Button(top, text = "Enter Ingredients", command = test)
C = Button(top, text = "MyBar", command=test)
D = Button(top, text = "Full Drink List", command=drinklist)       
B.place(x = 100,y = 50)
C.place(x = 100,y = 100)
D.place(x = 100,y = 150)
top.mainloop()
