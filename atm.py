import getpass

# Connecting to database
import sqlite3
from sqlite3.dbapi2 import OperationalError, connect
# Creating a connection to the database
db = sqlite3.connect("Bank_Database.db")
# Creating the cursor object
cur = db.cursor()

def check_balance(user_info):
    try:
        query = cur.execute(f"SELECT * FROM AccountInfo WHERE AccountNumber = '{user_info[0]}' and CardNumber = '{user_info[1]}'")
        content = query.fetchall()
    except sqlite3.OperationalError:
        print("You have no money in your account.")
        cur.execute("INSERT INTO AccountInfo(AccountNumber, CardNumber, Amount) values(?,?,?)", (int(user_info[0]), int(user_info[1]), 0))
        db.commit()
    else:
        print(f"You have N {content[0][2]} in your account.")
        start(user_info)

def deposit(user_info):
    print("Please enter the amount you would like to deposit.")
    valid = False
    while not valid:
        try:
            user_input = int(input(": "))
            valid = True
        except:
            print("Incorrect input")
    
    query = cur.execute(f"SELECT Amount FROM AccountInfo WHERE AccountNumber = '{user_info[0]}'")
    content = query.fetchall()

    cur.execute(f"UPDATE AccountInfo SET Amount = {int(content[0][0]) + user_input} WHERE AccountNumber = {user_info[0]}")

    db.commit()
    print("Successful!")
    start(user_info)

def withdraw(user_info):
    query = cur.execute(f"SELECT * FROM AccountInfo WHERE AccountNumber = '{user_info[0]}'")
    content = query.fetchall()

    # Check if amount is more than 100
    if int(content[0][2]) <= 100:
        print("Sorry you do not have enough to deposit, you need to have N100 in your account at all times.")
        start(user_info)
    
    print("Please enter the amount you would like to withdraw.")
    valid = False
    while not valid:
        user_input = int(input(": "))
        if (int(content[0][2]) - user_input) < 100:
            print("You do not have enough money in your account the make that withdrawal.")
            valid = False
        else:
            valid = True
            newAmount = int(content[0][2]) - user_input
            cur.execute(f"UPDATE AccountInfo SET Amount = {newAmount} WHERE AccountNumber = {user_info[0]}")
            db.commit()
            print("Successful!")
            start(user_info)

def start(user_info):
    #
    print("Enter 1 to check balance.")
    print("Enter 2 to deposit.")
    print("Enter 3 to withdraw.")

    user_input = int(input(": "))

    valid = False
    while not valid:
        if user_input not in (1, 2, 3):
            print("Incorrect input")
            user_input = input(": ")
        else:
            valid = True
    
    if user_input == 1:
        check_balance(user_info)
    elif user_input == 2:
        deposit(user_info)
    elif user_input == 3:
        withdraw(user_info)

# Validation
valid = False
while not valid:
    # Client Validation
    # Input last four digits of card number
    CardNo = input("Card NO: ")

    pin = getpass.getpass("Pin: ")

    if len(CardNo) == 16 and len(pin) == 4:
        valid = True
    else:
        print("Error: Incorrect Input.")
        valid = False

    # Database Validation
    if valid:
        try:
            # Database Validation
            query = cur.execute(f"SELECT * FROM Customers Where CardNumber = '{CardNo}' "
                                f"and Pin = '{pin}'")
            content = query.fetchall()
        except sqlite3.OperationalError:
            valid = False
            print("Error: That Account does not exist.")
        else:
            # Storing Information
            user_info = [content[0][0], CardNo, pin, content[0][3], content[0][4], content[0][5]]
            # Welcome message
            print(f"Welcome {user_info[3]}.")
            start(user_info)
