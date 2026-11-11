"""Core logic: adding, deleting, listing and totalling expenses."""

from datetime import date


def add_expense(expenses: list[dict], amount: float, category: str, note: str) -> dict:
    """Create an expense, add it to the list and return it."""
    expense = {
        "amount" : amount,
        "category" : category.strip().lower(),
        "note" : note.strip(),
        "date" : date.today().isoformat(),
    }
    expenses.append(expense)
    return expense

def delete_expense(expenses: list[dict], number: int) -> dict:
    """Remove the expense at position number (starting from 1) and return it"""
    return expenses.pop(number-1)

def total_by_category(expenses: list[dict]) -> dict[str, float]:
    """Return the total of all the expenses."""
    totals = {}
    for e in expenses:
        cat = e["category"]
        totals[cat] = totals.get(cat, 0) + e["amount"]
    return totals

def grand_total(expenses: list[dict]) -> float:
    total = 0
    for e in expenses:
        total += e["amount"]
    return total

def show_expenses(expenses: list[dict]) -> None:
    """Print all the expenses."""

    if not expenses:
        print("There are no expenses.")
        return
    
    print(f"\n{'#':<4}{'date':<12}{'category' :<14}{'amount' :>10} Note")
    
    print("-" * 56)

    for i, e in enumerate(expenses, start=1):
        print(f"{i:<4}{e['date']:<12}{e['category'].title():<14}{e['amount']:>10.2f} {e['note']}")
    
    print("-" * 56)

    print(f"{'Total':<30}{grand_total(expenses):>10.2f}")

def show_totals(expenses: list[dict]) -> None:
    """Prints total per category, highest first."""

    totals = total_by_category(expenses)

    if not totals:
        print("No expenses yet.")
        return

    print(f"\n{'Category':<14}{'Total':>10}")
    print("-" * 24)

    for cat, amount in sorted(totals.items(), key=lambda x: x[1], reverse=True):
        print(f"{cat.title():<14}{amount:>10.2f}")