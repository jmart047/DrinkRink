#!/usr/bin/python3
from tkinter import *

from tkinter import messagebox

import sqlite3

conn = sqlite3.connect('DrinkRink1.db')
c = conn.cursor()
top = Tk()
top.title("welcome")
top.configure(background="#a1dbcd")
photo = PhotoImage(file="dr_logo2.png")
w = Label(top, image=photo)
w.pack()
def go():
    #main screen
    t1=Toplevel(top)
    t1.title("main screen")
    t1.geometry("200x200")
    def test():
        #function for first button
        t2=Toplevel(t1)
        t2.title("get ingredients")
        label1= Label(t2,text="enter ing")
        e1= Entry(t2, bd = 5)
        def getIng():
            ing= e1.get()
            result =c.execute("SELECT ININID FROM Ingredients WHERE INDESC = ?", (ing,))
            resultrow = c.fetchone()
            if resultrow is not None:
                for row in resultrow:
                    newresult = row
        
                    dresult = c.execute("SELECT DTDRID FROM Detail WHERE INGID = ?", (newresult,))
                    dresult= c.fetchall()
                    t3=Toplevel(t2)
                    t3.title("get ingredients")
                    mess= Message(t3, text=dresult)
                    mess.pack()
                    leave=Button(t3, text="Go Back", command=t3.destroy)
                    leave.pack()
            else:
                t4=Toplevel(t2)
                errlabel=Label(terr,text="Not an Ingredient")
                    
                    
                goback = Button(terr, text="Go Back", command=terr.destroy)
                errlabel.pack()
                goback.pack()
            
   
        
        button1= Button(t2, text="Enter", command= getIng)
        label1.pack()
        e1.pack()
        button1.pack()
        button = Button(t2, text="Dismiss", command=t2.destroy)
        button.pack()
    
    def test2():
        #function for second button
        t5=Toplevel(t1)
        t5.title("MyBar")
        label1= Label(t5,text="enter ing")
        label2= Label(t5,text="enter ing")
        label3= Label(t5,text="enter ing")
        e1= Entry(t5, bd = 5)
        e2= Entry(t5, bd = 5)
        e3= Entry(t5, bd = 5)
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
##            final = c.execute("SELECT DTDRID FROM Detail WHERE INGID = ?",(result1,))
##            finalresult = print(c.fetchall())
            finalresult= result1 + result2 + result3
            t6=Toplevel(t5)
            messa = Message(t6, text= finalresult)
            messa.pack()
            leave=Button(t6, text="Go Back", command=t6.destroy)
            leave.pack()
        button1= Button(t5, text="Enter", command= getAns)
        button2= Button(t5, text="Go Back", command= t5.destroy)
        label1.pack()
        e1.pack()
        label2.pack()
        e2.pack()
        label3.pack()
        e3.pack()
        button1.pack()
        button2.pack()

    def drinklist():
        #function for third button
        t7=Toplevel(t1)
        t7.title("Drink List")
        mylist=list()
        a = c.execute("SELECT DRDESC FROM Drinks ")
        resultset = c.fetchall()
        for result in resultset:
            mylist.extend(result)
             
        msg = Message(t7, text=mylist)
        msg.pack()
        button = Button(t7, text="Dismiss", command=t7.destroy)
        button.pack()
        
    one = Button(t1, text = "Enter Ingredients", command = test)
    two = Button(t1, text = "MyBar", command=test2)
    three = Button(t1, text = "Full Drink List", command=drinklist)
    four = Button(t1, text = "Leave", command= t1.destroy)
    one.place(x=75,y=10)
    two.place(x=75,y=60)
    three.place(x=75,y=110)
    four.place(x=75,y=160)
    
    
   
    

        
start= Button(top, text="Enter Drinkrink",command=go)
start.place(x=200,y=200)
start.pack
end= Button(top, text="Leave Drinkrink",command=top.destroy)
end.place(x=350, y=200)
top.mainloop()

