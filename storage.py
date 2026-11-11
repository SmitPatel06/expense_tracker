"""Saving and loading expenses from a JSON file."""

import json

FILE = "expenses.json"

def saving_expeneses(expenses: list[dict]) -> None:
    """Save all expenses to the JSON file."""

    with open(FILE, "w") as f:
        json.dump(expenses, f, indent=2)

def load_expenses() -> list[dict]:
    """Load expenses, or start empty if the file is broken or missing."""

    try:
        with open(FILE, "r") as f:
            return json.load(f)

    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("Warning: Expenses file is corrupted, start fresh.")
        return []

