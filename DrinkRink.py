#!usr/bin/env python3



import sqlite3

conn = sqlite3.connect('DrinkRinkRealVersion.sqlite')
c = conn.cursor()


def checkIngredient():
    usrIngredient = input("\nEnter your ingredient\n\n")
    
    results = c.execute("SELECT DRDESC FROM Drinks WHERE DRDESC = ? ", (usrIngredient,))

    resultrow = c.fetchone()

    if resultrow is not None:
        print(resultrow)
    else:
        print("Sorry, there are no drinks with that ingredient")

checkIngredient()    


