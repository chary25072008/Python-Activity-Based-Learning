6. Python Source Code
name = input("Enter patient name: ")
age = int(input("Enter patient age: "))
insurance = input("Valid insurance? (yes/no): ").lower()
consultation = 500
diagnostic = 1000
treatment = 3000
total = consultation + diagnostic + treatment
if insurance == "yes":
    discount = total * 0.20
    category = "Insured Patient"
elif age >= 60:
    discount = total * 0.10
    category = "Senior Citizen"
else:
    discount = 0
    category = "Normal Patient"
final_bill = total - discount
print("\\nHospital Bill")
print("Patient:", name)
print("Category:", category)
print("Total:", total)
print("Discount:", discount)
print("Final Bill:", final_bill)
