1. Python Source Code
name = input("Enter product name: ")
quantity = int(input("Enter production quantity: "))
material = float(input("Enter material cost: "))
labour = float(input("Enter labour cost: "))
machine = float(input("Enter machine cost: "))
if quantity <= 0:
    print("Quantity must be greater than zero")
else:
    wastage = material * 0.05
    total = material + labour + machine + wastage
    cost_per_unit = total / quantity
    selling_price = total * 1.20
    profit = selling_price - total
    target = total * 0.20
    print("\\nManufacturing Report")
    print("Product:", name)
    print("Wastage Cost:", wastage)
    print("Total Cost:", total)
    print("Cost Per Unit:", cost_per_unit)
    print("Selling Price:", selling_price)
    print("Profit:", profit)
    if profit >= target:
        print("Profit Target Achieved")
    else:
        print("Profit Target Not Achieved")
