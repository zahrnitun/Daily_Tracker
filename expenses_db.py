import sqlite3
#Step 1: Connect to the database (It will create 'expenses.db' automically if it doesn't exist)
connection = sqlite3.connect("expenses.db")
#Step 2: Create a cursor (A tool to excute SQL commands)
cursor = connection.cursor()
#Step 3: Write SQL to create a table named 'expenses_table'
cursor.execute('''
            CREATE TABLE ILF NOT EXISTS expenses_table(
               id  INTEGER PRIMARY KEY AUTOINCREMENT,
                date TEXT,
               amount INTEGER,
               description TEXT)''')
#Step 4:Save the changes and close the connection
connection.commit()
connection.close()

print("--- Datebase and Table created successffully!---")


