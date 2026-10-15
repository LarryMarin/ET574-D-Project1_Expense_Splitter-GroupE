import data

#add_expense function
#ask user for their name (make sure it is a valid name and not a number)
#ask the user to put a description of their expense (make sure it is a valid String and not numbers)
#to validate we can use try-except
#ask the user to input an amount

def add_expense():
    
    name = input("Enter your name: ").strip()

    while not name.replace(" ","").isalpha():
        print("Invalid input. Please enter your name using letters.")
        name = input("Enter your name: ").strip()

    description = input("Expense description: ").strip()

    while not description.replace(" ","").isalnum():
        print("Invalid input. Please enter a description of your expense using letters, numbers and spaces.")
        description = input("Expense description: ").strip()

    while True:
        try:
            expense = float(input("Amount: "))

            if expense <= 0:
                print("Invalid amount. Please enter an amount greater than 0.")
            else:
                break

        except ValueError:
            print("Invalid amount. Please enter in dollars and cents.")

    data.user_names.append(name)
    data.expense_descriptions.append(description)
    data.expense_costs.append(expense)

    print(f"Your ${expense:.2f} {description} has been added successfully {name}!".title())


#view_all_expenses function
#prints out all current expenses in the list formatted correctly
def view_all_expenses():
    if not data.expense_costs:
        print("No current expenses. Please add an expense.")
        return
    for index in range(len(data.expense_costs)):
        print(f"Expense {index + 1}: ")
        print(f"Name: {data.user_names[index].capitalize()}")
        print(f"Expense Description: {data.expense_descriptions[index].capitalize()}")
        print(f"Expense Amount: ${data.expense_costs[index]:.2f}", end = '\n\n')

#split_summary function:
#we ask the user to input the amount of people they want to split all the expenses in the list 
#it will print the total expenses, number of expenses, average expenses, highest expense, lowest expense, and equal share per person

def split_summary():
    if not data.expense_costs:
        print("No current expenses. Please add an expense.")
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

    allExpenses = data.expense_costs
    
    print(f"Total Expenses = ${sum(allExpenses):.2f}")
    print(f"Number of Expenses = {len(allExpenses)}")
    print(f"Average Expense = ${sum(allExpenses)/len(allExpenses):.2f}")
    print(f"Highest Expense = ${max(allExpenses):.2f}")
    print(f"Lowest Expense = ${min(allExpenses):.2f}")
    print(f"Equal Share Per Person = ${sum(allExpenses)/numToSplit:.2f}")
