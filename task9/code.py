1. Python Source Code
rates = {"USD": 85, "EUR": 95, "GBP": 110}
budget = float(input("Enter travel budget in INR: "))
n = int(input("Enter number of expenses: "))
expenses = []
total = 0
for i in range(n):
    print("\\nExpense", i + 1)
    category = input("Enter category: ")
    currency = input("Enter currency (USD/EUR/GBP): ").upper()
    amount = float(input("Enter amount: "))
    if currency in rates:
        converted = amount * rates[currency]
        total += converted
        expenses.append((category, converted))
        print("Converted amount:", converted)
    else:
        print("Invalid currency")
if expenses:
    largest = max(expenses, key=lambda x: x[1])
    print("\\nTravel Budget Report")
    print("Total Expenses:", total)
    print("Largest Category:", largest[0])
    print("Largest Expense:", largest[1])
    if total > budget:
        print("Budget Exceeded")
    else:
        print("Within Budget")
else:
    print("No valid expenses entered")
