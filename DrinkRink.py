#!usr/bin/env python3



import sqlite3

conn = sqlite3.connect('DrinkRink1.db')
c = conn.cursor()


def checkIngredient():
    usrIngredient = input("\nEnter your ingredient\n\n")
    
    results = c.execute("SELECT ININID FROM Ingredients WHERE INDESC = ?", (usrIngredient,))

    resultrow = c.fetchone()

    if resultrow is not None:
        print(resultrow)
    else:
        print("Sorry, thats not an ingredient")
    dresult = c.execute("SELECT DTDRID FROM Detail WHERE INGID = ?", (resultrow,))

    dresult= c.fetchone()

    if dresult is not None:
        print(dresult)
    else:
        print("Sorry, there are no drinks with that ingredient")

checkIngredient()   
