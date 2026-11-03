1. Python Source Code
plans = [
    ("Plan A", 199, 2, 28),
    ("Plan B", 299, 3, 28),
    ("Plan C", 399, 5, 56)
]
usage = float(input("Enter data usage in GB: "))
validity = int(input("Enter required validity: "))
budget = float(input("Enter budget: "))
best = None
best_cost = float("inf")
for name, price, data, days in plans:
    if days >= validity:
        extra = max(0, usage - data)
        total = price + extra * 50
        if total <= budget and total < best_cost:
            best = name
            best_cost = total
if best is not None:
    print("Best Plan:", best)
    print("Total Cost: Rs.", round(best_cost, 2))
else:
    print("No eligible plan available")
