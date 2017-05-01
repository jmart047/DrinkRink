#!usr/bin/env python3
# DrinkRink
# Nicco Narbutas

from tkinter import *
from tkinter import messagebox


import sqlite3
import sys

top = Tk()
top.title("welcome")
top.configure(background = "#a1dbcd")
photo = PhotoImage(file = "dr_logo2.gif")
w = Label(top, image = photo)
w.pack()


conn = sqlite3.connect('DrinkRink.sqlite')   #connects SQLite database to program
c = conn.cursor()



def listDrinks():
    """This function displays all of the drinks in the database"""
    
    query = c.execute("SELECT DRDESC FROM Drinks ORDER BY 1")

    resultset = c.fetchall()
    for result in resultset:    #prints results of SQL query one row at a time
        result = ' '.join(result)
        print(result)

def listIngredients():
    """This function displays all of the ingredients the user can search for"""

    query = c.execute("SELECT INDESC FROM Ingredients ORDER BY 1")

    resultset = c.fetchall()
    for result in resultset:    #prints results of SQL query one row at a time
        result = ' '.join(result)
        print(result)
            
def checkIngredient():
    """This function checks the database for the drinks that contain the ingredient the user entered

    This function only checks for one ingredient
    """
    
    usrIngredient = input("\nEnter an ingredient that you "
                          "would like to make a drink with: \n\n")    #prompts the user to enter an ingredient

    query = c.execute("SELECT DRDESC FROM Drinks WHERE DRDRID IN "
                      "(SELECT DTDRID FROM Detail WHERE INGID "
                      "=(SELECT INGID FROM Ingredients WHERE INDESC LIKE ?))", (usrIngredient,))
    
    resultset = c.fetchall()

    if not resultset:
        print("Sorry, the drink you entered does not match any drinks in our database.")  #if there are no results of the SQL query, this is printed
    else:
        for result in resultset:       #prints results one row at a time
            result = ' '.join(result)
            print("\n\t", result)

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
    length = (len(ingredients))

    query = c.execute("SELECT DRDESC FROM Drinks WHERE DRDRID IN"
                      "(SELECT DTDRID FROM Detail WHERE INGID "
                      "=(SELECT INGID FROM Ingredients WHERE INDESC LIKE ?))", (ingredients[0:length],))

    resultset = c.fetchall()

    for result in resultset:  #prints results one row at a time
        if resultset is not None:
            result = ' '.join(result)
            print(result)
        else:
            print("Sorry, the ingredient you entered does not match any drinks in our database.")
    

def displayDrinkRecipe():
    """This function displays the recipe of the drink the user enters"""

    usrDrink = input("Enter the drink you would like the recipe for: \n") #prompts the user to enter a drink
    query = c.execute("SELECT Ingredients.INDESC, Detail.QTY "
                      "FROM Detail INNER JOIN Ingredients ON Detail.INGID=Ingredients.INGID "
                      "WHERE DTDRID=(SELECT DRDRID FROM Drinks WHERE DRDESC LIKE ?)", (usrDrink,))

    resultset = c.fetchall()

    for result in resultset:  #prints results one row at a time
        if resultset is not None:
            result = ' '.join(result)
            print("\n\t", result)
        else:
            print("Sorry, the drink you entered does not match any drinks in our database.")


def mainScreenWindow():
    mainScreen = Toplevel(top)
    mainScreen.title("Main Screen")
    mainScreen.geometry("200x200")
    one = Button(mainScreen, text = "Enter Ingredients", command = checkIngredient)
    one.place(x = 75, y = 10)

def main():

    mainScreenWindow()
    
##    print("Welcome to DrinkRink!\n\n")
##    while (True):  #displays the following message while the program is running
##        
##        usrInput = input("\nPress 1 to list all of the drinks in the database.\n"
##        "Press 2 to display all of the ingredients in the database.\n"
##        "Press 3 to enter one ingredient and display all of the drinks with that ingredient.\n"
##        "Press 4 to enter multiple ingredients and display all of the drinks that contain all of the ingredients you entered.\n"
##        "Press 5 to display the recipe of a particular drink.\n"
##        "Press 6 to exit DrinkRink.\n\n")
##
##        if usrInput == "1":
##            print("\n")
##            listDrinks()
##        elif usrInput == "2":
##            print("\n")
##            listIngredients()
##        elif usrInput == "3":
##            print("\n")
##            checkIngredient()            #   <------------- buttons
##        elif usrInput == "4":
##            print("\n")
##            checkMultipleIngredients()
##        elif usrInput == "5":
##            print("\n")
##            displayDrinkRecipe()
##        elif usrInput == "6":
##            sys.exit()
##        else:
##            print("\n\tYou entered an invalid number!!!\n")
    
if __name__ == "__main__":
    main()
