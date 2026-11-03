6. Python Source Code
import math
participants = int(input("Enter number of participants: "))
fee = float(input("Enter registration fee: "))
sponsorship = float(input("Enter sponsorship amount: "))
venue = 5000
equipment = 3000
catering = 10000
transport = 2000
certificates = 1000
expenses = venue + equipment + catering + transport + certificates
registration_income = participants * fee
total_income = registration_income + sponsorship
if total_income >= expenses:
    shortfall = 0
    print("Event is financially covered")
else:
    shortfall = expenses - total_income
    print("Financial shortfall:", shortfall)
required_amount = expenses - sponsorship
if required_amount <= 0:
    break_even = 0
elif fee > 0:
    break_even = math.ceil(required_amount / fee)
else:
    break_even = "Not possible with zero registration fee"
print("\\nCampus Event Financial Report")
print("Total Expenses:", expenses)
print("Registration Income:", registration_income)
print("Sponsorship:", sponsorship)
print("Total Income:", total_income)
print("Shortfall:", shortfall)
print("Break-even Registrations:", break_even
