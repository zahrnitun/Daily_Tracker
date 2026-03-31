#Step 3:Reading data and calculating the total
print("---Your Expense History---")
total_expense = 0
#Open the file in read mode
with open("expenses.txt","r")
#Read line by line
for line in file:
    #Check if the line has our pipe symbol to avoid empty line errors
    if "|" in line:
        #Print the line without extra spaces (strip)
        print(line.strip())
        #Data Processing: Split the line into parts
        parts = line.split("|")
        #The amount is the second item (index 1)
        amount_str = parts[1]
        #Convert string to integer and add to the running total
        total_expense = total_expense + int(amount_str)
print("-------------------------")
print("Total Spent:",total_expense,"Kyats")
