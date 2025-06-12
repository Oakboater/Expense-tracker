import csv
import os
from datetime import datetime

filename = 'DataExpense.csv'

# Ensure the file exists with headers
if not os.path.exists(filename):
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['ID', 'Expense', 'Description', 'Cost', 'Date'])

def generate_id():
    try:
        with open(filename, 'r') as f:
            reader = csv.reader(f)
            rows = list(reader)
            if len(rows) > 1:
                return int(rows[-1][0]) + 1
            else:
                return 1
    except:
        return 1

def add_expense():
    Addexpense = input("What expense would you like to add? ")
    Adddescription = input("Description for expense: ")
    try:
        Addcost = float(input("Cost (e.g. 43.23): "))
    except ValueError:
        print("Invalid cost. Please enter a number.")
        return

    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    new_id = generate_id()

    with open(filename, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([new_id, Addexpense, Adddescription, Addcost, date])

    print("Expense added!")

def menu():
    while True:
        print("\n--- Expense Tracker ---")
        print("1. Add an expense")
        print("2. Update expense")
        print("3. Delete expense")
        print("4. View all expenses")
        print("5. Summary of all expenses")
        print("6. Summary of a specific month")
        print("7. Set goals")
        print("0. Exit")

        try:
            choice = int(input("Enter your choice (0-7): "))
        except ValueError:
            print("Invalid input. Please enter a number between 0 and 7.")
            continue

        if choice == 0:
            print("Exiting. Bye!")
            break
        elif choice == 1:
            add_expense()
        elif choice == 2:
            print("Please enter ID")
            try:
                enterid = int(input("Enter id eg. 3"))
            except ValueError:
                print("Enter Correct ")
menu()
