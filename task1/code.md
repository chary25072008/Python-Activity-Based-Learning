1. University Scholarship Allocation
1. Problem Statement
Design a system that evaluates applicants using aggregate marks, minimum subject marks, attendance, and
family-income criteria. It ranks eligible students and resolves ties using attendance.
Assumptions / Rules
Eligibility rules used in this example: aggregate marks ‡ 80, attendance ‡ 75%, minimum subject marks ‡ 60, and
annual family income £ n2,50,000. Rank by aggregate marks (highest first), then attendance (highest first).
2. Algorithm<br>
1. Start.
2. Read the number of students.
3. For each student, read name, aggregate marks, attendance, minimum subject marks, and family income.
4. Check all four eligibility conditions.
5. If every condition is satisfied, add the student to the eligible list; otherwise mark the student as not eligible.
6. Sort eligible students by aggregate marks and then attendance, both in descending order.
7. Display eligible students with ranks and list students who are not eligible.
8. Stop.
   Mermaid Flowchart Code
3. flowchart TD
    N0(["START"])<br>
    N1["Input number of students and each student's details"]<br>
    N0 --> N1<br>
    N2{"All eligibility conditions satisfied?"}<br>
    N1 --> N2<br>
    N3["Yes fi Add student to eligible list; No fi Mark not eligible"]<br>
    N2 -->|Yes / No as applicable| N3<br>
    N4["Repeat until all students are processed"]<br>
    N3 --> N4<br>
    N5["Sort eligible students by marks, then attendance"]<br>
    N4 --> N5<br>
    N6["Display ranked eligible list and ineligible students"]<br>
    N5 --> N6<br>
    N7(["STOP"])<br>
    N6 --> N7<br>
5. Pseudocode
START<br>
INPUT number_of_students<br>
eligible = empty list<br>
ineligible = empty list<br>
FOR each student<br>
    INPUT name, aggregate, attendance, subject_min, income<br>
    IF aggregate >= 80 AND attendance >= 75<br>
       AND subject_min >= 60 AND income <= 250000<br>
        ADD (name, aggregate, attendance) TO eligible<br>
    ELSE<br>
        ADD name TO ineligible<br>
    END IF<br>
END FOR<br>
SORT eligible by aggregate descending,<br>
     then attendance descending<br>
DISPLAY eligible students with ranks<br>
DISPLAY ineligible students<br>
STOP<br>
7. Sample Input<br>
Enter number of students: 3
Student 1: Ravi, marks 90, attendance 85,
subject marks 70, income 200000
Student 2: Priya, marks 85, attendance 90,
subject marks 65, income 150000
Student 3: Kumar, marks 70, attendance 80,
subject marks 65, income 100000
8. Sample Output<br>
Eligible Scholarship Students
1 Ravi 90.0 85.0
2 Priya 85.0 90.0
Not eligible: ['Kumar']
9. Conclusion
The program checks scholarship eligibility using all specified conditions and ranks eligible students by aggregate
marks, using attendance to break ties
