"""Simple in-memory expense tracker for beginners."""

expenses = []

def add_expense():
    title = input("Expense title: ").strip()
    amount = float(input("Amount: "))
    category = input("Category: ").strip() or "Other"
    expenses.append({"title": title, "amount": amount, "category": category})
    print("Expense added.")

def show_expenses():
    if not expenses:
        print("No expenses yet.")
        return

    total = 0
    print("\n--- Expenses ---")
    for index, item in enumerate(expenses, start=1):
        total += item["amount"]
        print(f'{index}. {item["title"]} | {item["category"]} | ₹{item["amount"]:.2f}')

    print(f"Total: ₹{total:.2f}")

def category_summary():
    summary = {}
    for item in expenses:
        category = item["category"]
        summary[category] = summary.get(category, 0) + item["amount"]

    print("\n--- Category Summary ---")
    for category, amount in summary.items():
        print(f"{category}: ₹{amount:.2f}")

while True:
    print("\n1. Add expense")
    print("2. Show expenses")
    print("3. Category summary")
    print("4. Exit")

    choice = input("Choose: ").strip()

    if choice == "1":
        add_expense()
    elif choice == "2":
        show_expenses()
    elif choice == "3":
        category_summary()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")
