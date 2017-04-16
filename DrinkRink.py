#!usr/bin/env python3

import sqlite3
import sys

conn = sqlite3.connect('DrinkRink.sqlite')
c = conn.cursor()


def listDrinks():
    """This function displays all of the drinks in the database"""
    
    query = c.execute("SELECT DRDESC FROM Drinks")

    resultset = c.fetchall()
    for result in resultset:
        result = ' '.join(result)
        print(result)

def listIngredients():
    """This function displays all of the ingredients the user can search for"""

    query = c.execute("SELECT INDESC FROM Ingredients")

    resultset = c.fetchall()
    for result in resultset:
        result = ' '.join(result)
        print(result)
            
def checkIngredient():
    """This function checks the database for the drinks that contain the ingredient the user entered

    This function only checks for one ingredient
    """
    
    usrIngredient = input("\nEnter an ingredient that you would like to make a drink with: \n\n")


    query = c.execute("SELECT DRDESC FROM Drinks WHERE DRDRID IN"
                      "(SELECT DTDRID FROM Detail WHERE INGID "
                      "=(SELECT INGID FROM Ingredients WHERE INDESC LIKE ?))", (usrIngredient,))
    

    resultset = c.fetchall()

    for result in resultset:
        if resultset is not None:
            result = ' '.join(result)
            print(result)
        else:
            print("Sorry, there are no drinks with that ingredient")

def checkMultipleIngredients():
    """This function displays all of the drinks that contain all of the ingredients the user entered.

    This function is able to check for multiple ingredients.
    """

    ingredients = []
    numberOfIngredients = int(input('Enter how many ingredients you would like to search for: '))
    for i in range(0, numberOfIngredients):
        x = input('Enter your ingredient: ')
        ingredients.append(x)
    print(ingredients)

    query = c.execute("SELECT DRDESC FROM Drinks WHERE DRDRID IN"
                      "(SELECT DTDRID FROM Detail WHERE INGID "
                      "=(SELECT INGID FROM Ingredients WHERE INDESC LIKE))", (ingredients,))

def main():

    print("Welcome to DrinkRink!\n\n")
    while (True):
        
        usrInput = eval(input("\nPress 1 to list all of the drinks in the database.\n"
        "Press 2 to display all of the ingredients in the database.\n"
        "Press 3 to enter one ingredient and display all of the drinks with that ingredient.\n"
        "Press 4 to enter multiple ingredients and display all of the drinks that contain all of the ingredients you entered.\n"
        "Press 5 to exit the DrinkRink.\n\n"))

        if usrInput == 1:
            print("\n")
            listDrinks()
        elif usrInput == 2:
            print("\n")
            listIngredients()
        elif usrInput == 3:
            print("\n")
            checkIngredient()
        elif usrInput == 4:
            print("\n")
            checkMultipleIngredients()
        elif usrInput == 5:
            sys.exit()
        else:
            print("\n You entered an invalid number!!!\n")
    
if __name__ == "__main__":
    main()
