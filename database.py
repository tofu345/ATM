import sqlite3
import random
from datetime import datetime, time

# Creating a connection to the database
db = sqlite3.connect("Bank_Database.db")

# Creating the cursor object
cur = db.cursor()

# Creating random numbers for the account number
random_accountNo = (random.randint(1000000000000000, 99999999999999999))  # Method for getting random numbers
random_cardNo = (random.randint(100000000000000, 9999999999999999))  # Method for getting random numbers

# Getting the current date and storing it in a variable
now = datetime.now()
formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')

# Creating a table to store user info
# cur.execute("CREATE TABLE Customers(AccountNumber TEXT PRIMARY KEY NOT NULL,"
#             "CardNumber TEXT NOT NULL, Pin INTEGER NOT NULL,"
#             "FirstName TEXT NOT NULL, MiddleName TEXT NOT NULL, LastName TEXT NOT NULL)")

# Creating a table to store account info
# cur.execute("CREATE TABLE AccountInfo(AccountNumber TEXT PRIMARY KEY NOT NULL, "
#             "CardNumber TEXT NOT NULL, Amount TEXT NOT NULL)"
# )

# Creating a user
# cur.execute("INSERT INTO Customers (AccountNumber, CardNumber, Pin, FirstName, MiddleName, LastName) VALUES(?,?,?,?,?,?)", (random_accountNo, random_cardNo, 2345, "FirstName", "middleName", "LastName"))

db.commit()