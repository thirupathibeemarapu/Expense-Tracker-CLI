import csv

def view_expense():
    try:
        with open("expenses.csv", "r") as file:
            reader = csv.reader(file)

            print("\n--- All Expenses ---")
            for row in reader:
                print(row[0], "|", row[1], "|", row[2], "|", row[3])

    except FileNotFoundError:
        print("No expenses recorded yet.")