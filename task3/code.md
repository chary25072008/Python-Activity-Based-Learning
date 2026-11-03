3. Hospital Billing and Patient Classification
1. Problem Statement
Process consultation, diagnostic, and treatment charges, apply concessions, validate billing constraints, and classify
patients according to a supplied payment policy.
Assumptions / Rules
Example charges: consultation n500, diagnostics n1,000, treatment n3,000. A valid insurance card gives 20%
discount. Otherwise, patients aged 60 or above receive 10%. Only the highest applicable discount is applied.
2. Algorithm
 1. Start.
 2. Read patient name, age, and insurance status.
 3. Set consultation, diagnostic, and treatment charges.
 4. Calculate the total bill.
 5. If insurance is valid, apply 20% discount; otherwise, if age is at least 60, apply 10%; otherwise, no discount.
 6. Calculate final bill and classify the patient.
 7. Display the bill.
 8. Stop
4. Mermaid Flowchart Code
flowchart TD
    N0(["START"])<br>
    N1["Input patient name, age, and insurance status"]<br>
    N0 --> N1<br>
    N2["Add consultation, diagnostic, and treatment charges"]<br>
    N1 --> N2<br>
    N3{"Is insurance valid?"}<br>
    N2 --> N3<br>
    N4["Yes fi Apply 20% discount; No fi Check age"]<br>
    N3 -->|Yes / No as applicable| N4<br>
    N5{"Is age 60 or above?"}<br>
    N4 --> N5<br>
    N6["Yes fi Apply 10%; No fi No discount"]<br>
      N5 -->|Yes / No as applicable| N6<br>
    N7["Calculate final bill and display patient category"]<br>
    N6 --> N7<br>
    N8(["STOP"])<br>
    N7 --> N8<br>
5. Pseudocode
START<br>
INPUT name, age, insurance_status<br>
consultation = 500<br>
diagnostic = 1000<br>
treatment = 3000<br>
total = consultation + diagnostic + treatment<br>
IF insurance_status is "yes"<br>
    discount = total * 0.20<br>
    category = "Insured Patient"<br>
ELSE IF age >= 60<br>
    discount = total * 0.10<br>
    category = "Senior Citizen"<br>
ELSE<br>
    discount = 0<br>
    category = "Normal Patient"<br>
END IF<br>
final_bill = total - discount<br>
DISPLAY name, category, total, discount, final_bill<br>
STOP<br>
7. Sample Input<br>
Enter patient name: Ravi
Enter patient age: 65
Valid insurance? (yes/no): no
8. Sample Output<br>
Hospital Bill
Patient: Ravi
Category: Senior Citizen
Total: 4500
Discount: 450.0
Final Bill: 4050.0
9. Conclusion
The program calculates hospital charges, applies the correct concession based on insurance or age, and displays the
patient's final payable amount
