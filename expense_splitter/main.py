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


    
