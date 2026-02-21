from Add_expense import add_expense
from view_expense import view_expense
from summary import monthly_summary
from total import total_amount

while True:
    
    print("==== Expense Tracker ====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Monthly Summary")
    print("4. Exit")
    print("5. Total Amount")

    choice = input("Enter choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expense()

    elif choice == "3":
        monthly_summary()

    elif choice == "4":
        print("Exiting program...")
        break

    elif choice == "5":
        total_amount()

    else:
        print("Invalid choice")