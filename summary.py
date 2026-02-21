import csv

def monthly_summary():

    income = 0
    expense = 0

    try:
        with open("expenses.csv", "r") as file:

            reader = csv.reader(file)

            for row in reader:
                amount = float(row[2])

                if row[3].strip().lower() == "income":
                    income += amount
                elif row[3].strip().lower() == "expense":
                    expense += amount

        print("\n--- Monthly Summary ---")
        print("Total Income:", income)
        print("Total Expense:", expense)
        print("Balance:", income - expense)

    except FileNotFoundError:
        print("No data available.")