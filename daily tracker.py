#Step 1:Getting data from the user
# print("--- Daily Expense Tracker ---")
#Get user input and store them in variables
date = input("Enter the date (e.g.,15-Mar):")
amount = input("Enter the amount(e.g.,5000):")
description = input("What did you use it on?:")
#Display the entered data to confirm
print("\n--- Record Saved---")
print("Date:",date)
print("Amount:",amount)
print("Description:",description)
#Step 2:Saving data to a file automatically
#Using 'with' is the best practice because it automically closes the file for us
with open("expenses.txt","a") as file:
    # Write the data separated by a pipe '|' , and add '\n' to go to new line
    file.write(date + " | " + amount + " | " + description + "\n")
print("---Data Successfully saved to expenses.txt! ---")