#!/usr/bin/python3

##trying to get ammount of ingredients, and return a list with those ingredients
from tkinter import *

from tkinter import messagebox

import sqlite3

conn = sqlite3.connect('DrinkRink1.db')
c = conn.cursor()
t1 = Tk()


#main screen

t1.title("main screen")
t1.geometry("200x200")
def test():
    #function for first button
    t2=Toplevel(t1)
    t2.title("amm")
    label1= Label(t2,text="How many ingredients?")
    amm= Entry(t2)
    myList=list()
    def getList(x):
        myList.append(x)
        
        
        
    def getIng(x):
        result =c.execute("SELECT ININID FROM Ingredients WHERE INDESC = ?", (x,))
        resultrow = c.fetchone()
        if resultrow is not None:
            for row in resultrow:
                newresult = row

                dresult = c.execute("SELECT DTDRID FROM Detail WHERE INGID = ?", (newresult,))
                dresult= c.fetchall()
                print(dresult)
    def loop():
        t3=Toplevel(t2)
        t3.title("amm2")
        ammount=amm.get()
        num=int(ammount)
        
        for i in range(1,num+1):
            label=Label(t3,text="Enter Ingredients")
            label.pack()
            enter=Entry(t3)
            enter.pack()
            ing=enter.get()
            
            
            getIt=Button(t3,text="Get it",command= getList(ing))
            getIt.pack()
        returnIt=Button(t3,text="return",command=print(myList))
        returnIt.pack()
        
    button1= Button(t2, text="Enter", command= loop)
    label1.pack()
    amm.pack()
    button1.pack()
    button = Button(t2, text="Dismiss", command=t2.destroy)
    button.pack()


    

    

one = Button(t1, text = "Enter Ingredients", command = test)
one.pack()
t1.mainloop()
