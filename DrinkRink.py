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
def start():
    #main screen
    mainScreen=Toplevel(top)
    mainScreen.title("Main Screen")
    mainScreen.geometry("200x200")
    def getDrink():
        #user inputs ingredient, returns all drinks with that ingredient.
        inputScreen=Toplevel(mainScreen)
        inputScreen.title("Ingredients")
        enterIng= Label(inputScreen,text="enter ingredient")
        entry1= Entry(inputScreen, bd = 5)
        def getIng():
            #using user input to get data from sqlite database
            ing= entry1.get()
            result =c.execute("SELECT ININID FROM Ingredients WHERE INDESC = ?", (ing,))
            resultrow = c.fetchone()
            if resultrow is not None:
                for row in resultrow:
                    newresult = row
        
                    searchresult = c.execute("SELECT DTDRID FROM Detail WHERE INGID = ?", (newresult,))
                    fetchresult= c.fetchall()
                    answerScreen=Toplevel(inputScreen)
                    answerScreen.title("Drinks")
                    mess= Message(answerScreen, text=fetchresult)
                    mess.pack()
                    leave=Button(answerScreen, text="Go Back", command=answerScreen.destroy)
                    leave.pack()
            else:
                errorScreen=Toplevel(inputScreen)
                errlabel=Label(errorScreen,text="Not an Ingredient")
                    
                    
                goback = Button(errorScreen, text="Go Back", command=errorScreen.destroy)
                errlabel.pack()
                goback.pack()
            
   
        
        getAnswer= Button(inputScreen, text="Enter", command= getIng)
        enterIng.pack()
        entry1.pack()
        getAnswer.pack()
        goBack = Button(inputScreen, text="Dismiss", command=inputScreen.destroy)
        goBack.pack()
    
    def myBar():
        #user inputs multiple ingredients, returns the IDs. Work on returning drinks using multiple Ingredients
        barScreen=Toplevel(mainScreen)
        barScreen.title("MyBar")
        enterIng1= Label(barScreen,text="enter ingredient")
        enterIng2= Label(barScreen,text="enter ingredient")
        enterIng3= Label(barScreen,text="enter ingredient")
        entry1= Entry(barScreen, bd = 5)
        entry2= Entry(barScreen, bd = 5)
        entry3= Entry(barScreen, bd = 5)
        def getmyBar():
            #search database for Ingredient IDs
            ing1= entry1.get()
            ing2= entry2.get()
            ing3= entry3.get()
            res1 =c.execute("SELECT ININID FROM Ingredients WHERE INDESC = ?", (ing1,))
            result1 = c.fetchone()
            res2 =c.execute("SELECT ININID FROM Ingredients WHERE INDESC = ?", (ing2,))
            result2 = c.fetchone()
            res3 =c.execute("SELECT ININID FROM Ingredients WHERE INDESC = ?", (ing3,))
            result3 = c.fetchone()
##            final = c.execute("SELECT DTDRID FROM Detail WHERE INGID = ?",(result1,))
##            finalresult = print(c.fetchall())
            finalresult= result1 + result2 + result3
            answerScreen=Toplevel(barScreen)
            messa = Message(answerScreen, text= finalresult)
            messa.pack()
            leave=Button(answerScreen, text="Go Back", command=answerScreen.destroy)
            leave.pack()
        getAnswer= Button(barScreen, text="Enter", command= getmyBar)
        goBack= Button(barScreen, text="Go Back", command= barScreen.destroy)
        enterIng1.pack()
        entry1.pack()
        enterIng2.pack()
        entry2.pack()
        enterIng3.pack()
        entry3.pack()
        getAnswer.pack()
        goBack.pack()

    def drinklist():
        #returns a list of all the drinks in database
        dlScreen=Toplevel(mainScreen)
        dlScreen.title("Drink List")
        mylist=list()
        showAll = c.execute("SELECT DRDESC FROM Drinks ")
        resultset = c.fetchall()
        for result in resultset:
            mylist.extend(result)
             
        msg = Message(dlScreen, text=mylist)
        msg.pack()
        button = Button(dlScreen, text="Dismiss", command=dlScreen.destroy)
        button.pack()
    #main screen buttons    
    one = Button(mainScreen, text = "Enter Ingredients", command = getDrink)
    two = Button(mainScreen, text = "MyBar", command=myBar)
    three = Button(mainScreen, text = "Full Drink List", command=drinklist)
    four = Button(mainScreen, text = "Leave", command= mainScreen.destroy)
    one.place(x=75,y=10)
    two.place(x=75,y=60)
    three.place(x=75,y=110)
    four.place(x=75,y=160)
    
    
   
    

#start screen buttons       
start= Button(top, text="Enter Drinkrink",command=start)
start.place(x=200,y=200)
start.pack
end= Button(top, text="Leave Drinkrink",command=top.destroy)
end.place(x=350, y=200)
top.mainloop()

