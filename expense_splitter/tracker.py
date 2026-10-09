import data

#add_expense function
#ask user for their name (make sure it is a valid name and not a number)
#ask the user to put a description of their expense (make sure it is a valid String and not numbers)
#to validate we can use try-except
#ask the user to input an amount

#all of this will be appended to a list in data.py
#we may need to use 2D list for all of this. in a 2D list we can store multiple lists inside. look at list2examples folder for 2D list examples

#view_all_expenses function
#prints out all current expenses in the list formatted correctly
def view_all_expenses():
    if data.expense_list == []:
        print("The list is empty. Please fill the list first.")
        return
    counter = 1
    for expense in data.expense_list:
        print(f"Expense {counter}: ")
        print(f"Name: {expense[0]}")
        print(f"Expense Description: {expense[1]}")
        print(f"Expense Amount: ${expense[2]:.2f}", end = '\n\n')
        counter+=1

#split_summary function:
#we ask the user to input the amount of people they want to split all the expenses in the list 
#it will print the total expenses, number of expenses, average expenses, highest expense, lowest expense, and equal share per person

def split_summary():
    if data.expense_list == []:
        print("The list is empty. Please fill the list first.")
        return
    while True:
        try:
            numToSplit = int(input("Please enter the amount of people you want to split the expenses with: "))
            if numToSplit > 0:
                break
            else:
                print("The number cannot be 0 or a negative number please try again.")
        except ValueError:
            print("Invalid Input.")

    allExpenses = []
    for expense in data.expense_list:
        allExpenses.append(expense[2])
    
    print(f"Total Expenses = ${sum(allExpenses):.2f}")
    print(f"Number of Expenses = {len(allExpenses)}")
    print(f"Average Expense = ${sum(allExpenses)/len(allExpenses):.2f}")
    print(f"Highest Expense = ${max(allExpenses):.2f}")
    print(f"Lowest Expense = ${min(allExpenses):.2f}")
    print(f"Equal Share Per Person = ${sum(allExpenses)/numToSplit:.2f}")
