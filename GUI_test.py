#!/usr/bin/python3
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
        if resultrow is not None:
            for row in resultrow:
                newresult = row
        
                dresult = c.execute("SELECT DTDRID FROM Detail WHERE INGID = ?", (newresult,))
                dresult= c.fetchall()
                t2=Toplevel(t)
                mess= Message(t2, text=dresult)
                mess.pack()
        else:
            terr=Toplevel(t)
            errlabel=Label(terr,text="Not an Ingredient")
            
            
            goback = Button(terr, text="Go Back", command=terr.destroy)
            errlabel.pack()
            goback.pack()
            
   
        
    button1= Button(t, text="Enter", command= getIng)
    label1.pack()
    e1.pack()
    button1.pack()
    button = Button(t, text="Dismiss", command=t.destroy)
    button.pack()
def test2():
    t=Toplevel()
    label1= Label(t,text="enter ing")
    label2= Label(t,text="enter ing")
    label3= Label(t,text="enter ing")
    e1= Entry(t, bd = 5)
    e2= Entry(t, bd = 5)
    e3= Entry(t, bd = 5)
    def getAns():
        ing1= e1.get()
        ing2= e2.get()
        ing3= e3.get()
        res1 =c.execute("SELECT ININID FROM Ingredients WHERE INDESC = ?", (ing1,))
        result1 = c.fetchone()

        res2 =c.execute("SELECT ININID FROM Ingredients WHERE INDESC = ?", (ing2,))
        result2 = c.fetchone()
        res3 =c.execute("SELECT ININID FROM Ingredients WHERE INDESC = ?", (ing3,))
        result3 = c.fetchone()
##        final = c.execute("SELECT DTDRID FROM Detail WHERE INGID = ? OR ? OR ing3",(ing1,ing2,ing3,))
##        finalresult = c.fetchall()
        finalresult= result1 + result2 + result3
        
        t2=Toplevel(t)
        messa = Message(t2, text= finalresult)
        messa.pack()
    button1= Button(t, text="Enter", command= getAns)
    label1.pack()
    e1.pack()
    label2.pack()
    e2.pack()
    label3.pack()
    e3.pack()
    button1.pack()
def drinklist():
    a = c.execute("SELECT DRDESC FROM Drinks ")
    b = c.fetchall()
    top = Toplevel()
    msg = Message(top, text=b)
    msg.pack()
    button = Button(top, text="Dismiss", command=top.destroy)
    button.pack()

   

B = Button(top, text = "Enter Ingredients", command = test)
C = Button(top, text = "MyBar", command=test2)
D = Button(top, text = "Full Drink List", command=drinklist)       
B.place(x = 100,y = 50)
C.place(x = 100,y = 100)
D.place(x = 100,y = 150)
top.mainloop()
