 ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# Jai Sanga,11.16.2021,Added code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFile = "ToDoList.txt"   # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = "" # A Capture the user option selection


# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
objFile = open("ToDoList.txt", "r")
for row in objfile:
    1stRow = row.split(",")
    dicrow = {"Item": 1stRow[0], "Value": 1stRow[1].strip()}
    1stTable.append(dicRow)
objfile.close()

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks
    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        objfile = open("ToDoList.txt", "r")
        for row in Objfile:
            i, v = row.split(",")
            dicrow = {'Item': i, "Value": v}
            1stTable.append(dicRow)
            print(1stTable)
        objfile.close

    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        while (True):
            strItem = input('Item: ')
            strValue = input('Value: ')
            lstTable.append({"Item": strItem, "Value": strValue})
            strChoice = input("Exit? ('y/n'): ")
            if strChoice.lower() == 'y':
                break

    # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):
        while (True):
            strItem = input('Item to Remove: ')
            for row in lstTable:
                if row['Item'].lower() == strItem.lower():
                    lstTable.remove(row)
                    print("row removed")
                    print(lstTable, "<< List with Dictionary objects")
                else:
                    print('row not found')
                    print(lstTable)
            strChoice = input("Exit? ('y/n') : ")
            if strChoice.lower() == "y":
                break

    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif (strChoice.strip() == '4'):
        objFile = open('ToDoList.txt', 'w')
        for row in lstTable:
            objFile.write(str(row['Item'] + ',' + str(row['Value'] + '\n')))
        objFile.close()
        print('Saved to File!')

    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        print('Exiting Program')
        break  # and Exit the program