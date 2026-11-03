6. Python Source Code
n = int(input("Enter number of months: "))
bills = []
for i in range(n):
    units = float(input("Enter units consumed: "))
    if units <= 100:
        energy = units * 2
    elif units <= 200:
        energy = 100 * 2 + (units - 100) * 3
    else:
        energy = 100 * 2 + 100 * 3 + (units - 200) * 5
    bill = energy + 50 + energy * 0.05
    if units < 100:
        bill -= 20
    bills.append(bill)
    print("Month", i + 1, "Bill: Rs.", round(bill, 2))
    if i > 0 and bills[i - 1] > 0:
        increase = (bills[i] - bills[i - 1]) / bills[i - 1] * 100
        if increase > 50:
            print("Unusual increase detected")
        else:
            print("Normal increase")
