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
    t=Toplevel()
    label1= Label(t,text="enter ing")
    e1= Entry(t, bd = 5)
    def getIng():
        ing= e1.get()
        result =c.execute("SELECT ININID FROM Ingredients WHERE INDESC = ?", (ing,))
        resultrow = c.fetchone()
##        if resultrow is not None:
##            print(resultrow)
##        else:
##            print("Sorry, thats not an ingredient")
   
        for row in resultrow:
            newresult = row
        
            dresult = c.execute("SELECT DTDRID FROM Detail WHERE INGID = ?", (newresult,))
            dresult= c.fetchall()
            t2=Toplevel(t)
            mess= Message(t2, text=dresult)
            mess.pack()
        
    button1= Button(t, text="Enter", command= getIng)
    label1.pack()
    e1.pack()
    button1.pack()
    button = Button(t, text="Dismiss", command=top.destroy)
    button.pack()
def drinklist():
    a = c.execute("SELECT DRDESC FROM Drinks ")
    b = c.fetchall()
    top = Toplevel()
    msg = Message(top, text=b)
    msg.pack()
    button = Button(top, text="Dismiss", command=top.destroy)
    button.pack()

   

B = Button(top, text = "Enter Ingredients", command = test)
C = Button(top, text = "MyBar", command=test)
D = Button(top, text = "Full Drink List", command=drinklist)       
B.place(x = 100,y = 50)
C.place(x = 100,y = 100)
D.place(x = 100,y = 150)
top.mainloop()
