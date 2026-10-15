#we have to use import so we can access the contents inside those files
#ex. data.expense_list
import data
import tracker

# Student A - Main Menu and Program Flow
# Expense Splitter Project

from tracker import add_expense, view_all_expenses, split_summary


def main():
    print("Welcome to Expense Splitter!")

    while True:
        print("\n1. Add Expense")
        print("2. View All Expenses")
        print("3. View Split Summary")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_all_expenses()
        elif choice == "3":
            split_summary()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")


main()


#can use a while loop for the menu
#while the user input is not exit (0) the while loop will start/continue
#the user will enter a number
#depending on the number chosen we will do that task 
#can use an if statement to check what number the user inputed so we can do that task
#if 1: call add expense function
#elif 2: call all expenses function
#elif 3: call split summary function
#elif 0: exit the loop

#can also make sure the user enters a valid input or if the input is out of range
#try-except helps with this

#maybe when they press 3 we can clear the list after it is done running?

    
