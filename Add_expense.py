import csv

def add_expense():
    date = input("Enter date (YYYY-MM-DD): ")
    category = input("Enter category: ")
    amount = input("Enter amount: ")
    type_ = input("Enter type (Income/Expense): ")

    with open("expenses.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount, type_])

    print("Expense saved successfully!")