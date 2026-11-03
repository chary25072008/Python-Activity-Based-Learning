6. Python Source Code
n = int(input("Enter number of students: "))
eligible = []
ineligible = []
for i in range(n):
    print("\\nStudent", i + 1)
    name = input("Enter name: ")
    marks = float(input("Enter aggregate marks: "))
    attendance = float(input("Enter attendance (%): "))
    subject = float(input("Enter minimum subject marks: "))
    income = float(input("Enter annual family income: "))
    if (marks >= 80 and attendance >= 75
            and subject >= 60 and income <= 250000):
        eligible.append((name, marks, attendance))
    else:
        ineligible.append(name)
eligible.sort(key=lambda x: (x[1], x[2]), reverse=True)
print("\\nEligible Scholarship Students")
if eligible:
    for rank, student in enumerate(eligible, 1):
        print(rank, student[0], student[1], student[2])
else:
    print("No eligible students")
print("Not eligible:", ineligible)
