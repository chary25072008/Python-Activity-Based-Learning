1. Python Source Code
n = int(input("Enter number of passengers: "))
for i in range(n):
    print("\\nPassenger", i + 1)
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    distance = float(input("Enter distance: "))
    travel_class = input("Enter class (sleeper/ac): ").lower()
    if travel_class == "ac":
        multiplier = 2
    elif travel_class == "sleeper":
        multiplier = 1
    else:
        print("Invalid class")
        continue
    fare = distance * 2 * multiplier
    if age < 5:
        fare = 0
    elif age <= 12:
        fare *= 0.50
    elif age >= 60:
        fare *= 0.80
    if fare > 0:
        fare += 30
    cancel = input("Cancel ticket? (yes/no): ").lower()
    if cancel == "yes":
        fare *= 0.10
        print("Cancellation penalty:", round(fare, 2))
    else:
        print("Ticket fare:", round(fare, 2))
    print("Passenger:", name)
