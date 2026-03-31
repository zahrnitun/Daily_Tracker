import sqlite3
connection = sqlite3.connect("expenses.db")
cursor = connection.cursor()
cursor.execute('''
               CREATE TABLE IF NOT EXISTS expenses_table(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               date TEXT,
               amount INTEGER,
               description TEXT)''')
connection.commit()
connection.close()
#Step 4:Creating Main Menu
while True:
    print("\n Expense Tracker Menu")
    print("1. Add New Expense")
    print("2. View Total Expenses")
    print("3. Exit")

    choice = input("Choose an option (1/2/3):")

    if choice == '1':
        print("---Daily Expense Tracker---")
        date = input("Enter the date e.g.,15-March:")
        amount = input("Enter the amount e.g.,4000:")
        description = input("What did you use it for?:")
        connection = sqlite3.connect("expenses.db")
        cursor = connection.cursor()
        cursor.execute('''
                       INSERT INTO expenses_table (date, amount, description)
                       VALUES (?, ?, ?)''',
                       (date,int(amount),description))
        connection.commit()
        connection.close()
        print("n\---Expense securely saved to Database!---")


    elif choice == '2':
        print("---Your Expense History---")
        total_expense = 0
        connection = sqlite3.connect("expenses.db")
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM expenses_table")
        records = cursor.fetchall()
        
        for row in records:
             print(f"Date: {row[1]} | Amount:{row[2]} | Description:{row[3]}")
             total_expense = total_expense + row[2]
        connection.close()
        print("------------------------------------------------------------------")
        print("Total Spent:",total_expense,"Kyats")
    elif choice == '3':
        print("Exiting the program. Goodbye!")
        break

    else:
            print("Invalid choice.Please try again.")
            

