"""input helpers that keep asking until the user types something valid."""

def get_int_in_range(prompt: str, low: int, high: int) -> int:
    """Keep asking until user give a whole number b/w high and low."""
    while True:
        try:
            num = int(input(prompt))
        except ValueError:
            print("That's not a whole number.")
            continue

        if low<= num <= high:
            return num
        
        print(f"Please enter a number from {low} to {high}.")

def get_positive_float(prompt: str) -> float:
    """Keep asking until the user gives the number greater than 0"""

    while True:
        try:
            num = float(input(prompt))

        except ValueError:
            print("Please enter a valid number.")
            continue

        if num > 0:
            return round(num, 2)

        print("Amount must be greater than 0.")

def get_text(prompt: str) -> str:
    """Keep asking until the user enters a noo empty text"""

    while True:
        text = input(prompt).strip()

        if text:
            return text
        print("This can't be empty.")