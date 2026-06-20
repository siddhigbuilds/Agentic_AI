expenses = []

while True:
    print("\n===== Expense Tracker =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expenses")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        amount = float(input("Enter amount: ₹"))
        category = input("Enter category: ")

        expense = {
            "amount": amount,
            "category": category
        }

        expenses.append(expense)

        print("Expense added successfully!")

    elif choice == "2":
        if len(expenses) == 0:
            print("No expenses found.")
        else:
            print("\nExpenses:")
            for i, expense in enumerate(expenses, start=1):
                print(f"{i}. Amount: ₹{expense['amount']}, Category: {expense['category']}")



    elif choice == "3":
        total = 0

        for expense in expenses:
            total += expense["amount"]

        print(f"Total Expenses: ₹{total}")

    elif choice == "4":
        print("Thank you for using Expense Tracker!")
        
        break

    else:
        print("Invalid choice. Please try again.")