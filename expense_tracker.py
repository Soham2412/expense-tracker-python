import csv

FILENAME = "expenses.csv"

def add_expense(date, category, amount):
    with open(FILENAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount])

def view_expenses():
    total = 0
    try:
        with open(FILENAME, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)
                total += float(row[2])
    except FileNotFoundError:
        print("No expenses found.")
    print("Total Expense:", total)

while True:
    print("\n1. Add Expense\n2. View Expenses\n3. Exit")
    choice = input("Choose: ")

    if choice == "1":
        date = input("Date: ")
        category = input("Category: ")
        amount = input("Amount: ")
        add_expense(date, category, amount)
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        break
