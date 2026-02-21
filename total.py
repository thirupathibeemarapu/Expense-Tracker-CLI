import csv

def total_amount():
    total = 0

    try:
        with open("expenses.csv", "r") as file:
            reader = csv.reader(file)

            for row in reader:
                total += float(row[2])

        print("Total Transaction Amount:", total)

    except FileNotFoundError:
        print("No data found.")