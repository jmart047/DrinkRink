#!usr/bin/env python3
# DrinkRink
# Nicco Narbutas


import sqlite3
import sys
import unittest

conn = sqlite3.connect('DrinkRink1.db')   #connects SQLite database to program
c = conn.cursor()

def checkIngredient(usrIngredient):
    """This function checks the database for the drinks that contain the ingredient the user entered
    This function only checks for one ingredient
    """
    
    

    query = c.execute("SELECT DRDESC FROM Drinks WHERE DRDRID IN "
                      "(SELECT DTDRID FROM Detail WHERE INGID "
                      "=(SELECT INGID FROM Ingredients WHERE INDESC LIKE ?))", (usrIngredient,))
    
    resultset = c.fetchall()

    if not resultset:
        print("Sorry, there are no drinks with that ingredient.")  #if there are no results of the SQL query, this is printed
    else:
        for result in resultset:       #prints results one row at a time
            result = ' '.join(result)
            print("\n\t", result)


class CheckIngTest(unittest.TestCase):
    def testCheck(self):
        result = checkIngredient("Vodka")
        print(result)
    def testCheckCap(self):
        result = checkIngredient("vodka")
        print(result)
if __name__ == '__main__':
    unittest.main()
