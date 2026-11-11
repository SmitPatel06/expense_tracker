from helpers import get_int_in_range, get_positive_float, get_text
from storage import saving_expeneses, load_expenses
from expense import (
    add_expense,
    delete_expense,
    show_expenses,
    show_totals
)

def main() -> None:
    expenses = load_expenses()
    print(f"Loaded {len(expenses)} expenses.")

    while True:
        print("\n ----- Expense Tracker -----")
        print("1. Add Expense")
        print("2. View all expenses")
        print("3. Total by category")
        print("4. Delete expense")
        print("5. Quit")

        choice = get_int_in_range("Choose from 1-5: ", 1, 5)

        if choice == "1":
            amount = get_positive_float("Amount: ")
            category = get_text("Category (food, transport, ...): ")
            note = input("Note (Optional): ")
            e = add_expense(expenses, amount, category, note)
            saving_expeneses(expenses)
            print(f"Added {e['amount']:.2f} to {e['category']}.")

        elif choice == "2":
            show_expenses(expenses)

        elif choice == "3":
            show_totals(expenses)

        elif choice == "4":
            if not expenses:
                print("There are no expenses yet.")
                continue
            show_expenses(expenses)
            num = get_int_in_range("Please choose a number to delete: ", 1, len(expenses))
            removed = delete_expense(expenses, num)
            saving_expeneses(expenses)
            print(f"Deleted {removed['amount']:.2f} ({removed['category']}).")

        elif choice == "5":
            print("Byeee!!!")
            break

if __name__ == "__main__":
    main()