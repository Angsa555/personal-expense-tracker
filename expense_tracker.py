import json
from pathlib import Path
from datetime import datetime

DATA_FILE = Path("expenses.json")


def load_expenses():
    if not DATA_FILE.exists():
        return []

    try:
        return json.loads(DATA_FILE.read_text())
    except json.JSONDecodeError:
        return []


def save_expenses(expenses):
    DATA_FILE.write_text(
        json.dumps(expenses, indent=2),
        encoding="utf-8"
    )


def add_expense(expenses):
    category = input("Category: ").strip()
    amount = float(input("Amount: "))
    note = input("Note: ").strip()

    expense = {
        "date": datetime.now().strftime("%Y-%m-%d"),
        "category": category,
        "amount": amount,
        "note": note
    }

    expenses.append(expense)
    save_expenses(expenses)
    print("Expense added successfully.")


def show_expenses(expenses):
    if not expenses:
        print("No expenses recorded.")
        return

    total = 0

    print("\nExpense History")
    print("-" * 50)

    for expense in expenses:
        print(
            f"{expense['date']} | "
            f"{expense['category']} | "
            f"{expense['amount']:.2f} | "
            f"{expense['note']}"
        )
        total += expense["amount"]

    print("-" * 50)
    print(f"Total: {total:.2f}")


def main():
    expenses = load_expenses()

    while True:
        print("\nPersonal Expense Tracker")
        print("1. Add expense")
        print("2. Show expenses")
        print("3. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            show_expenses(expenses)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()
