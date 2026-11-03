1. Python Source Code
name = input("Enter employee name: ")
basic = float(input("Enter basic salary: "))
hours = float(input("Enter overtime hours: "))
hra = basic * 0.20
da = basic * 0.10
overtime = hours * 100
incentive = 1000
gross = basic + hra + da + overtime + incentive
pf = basic * 0.12
tax = gross * 0.05
deduction = pf + tax
net = gross - deduction
print("\\nEmployee Salary Statement")
print("Name:", name)
print("Basic Salary:", basic)
print("HRA:", hra)
print("DA:", da)
print("Overtime:", overtime)
print("Incentive:", incentive)
print("Gross Salary:", gross)
print("Total Deduction:", deduction)
print("Net Salary:", net)
