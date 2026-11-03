2. Progressive Electricity Billing
1. Problem Statement
Calculate household electricity bills using multiple consumption slabs, fixed charges, surcharges, and rebates.
Compare bills across months and identify unusual increases.
Assumptions / Rules
Example tariff: first 100 units at n2/unit; next 100 units at n3/unit; units above 200 at n5/unit. Fixed charge n50;
surcharge 5% of energy charge; rebate n20 when consumption is below 100 units. An increase greater than 50%
over the previous bill is unusual.
2. Algorithm
1. Start.
2. Read the number of months.
3. For each month, read units consumed.
4. Calculate energy charges using the applicable slabs.
5. Add fixed charge and 5% surcharge; subtract n20 rebate if units are below 100.
6. Store and display the bill.
7. From the second month onward, compare the bill with the previous month's bill.
8. If the increase is greater than 50%, report an unusual increase.
9. Stop.
   Mermaid Flowchart Code
flowchart TD
    N0(["START"])<br>
    N1["Input number of months and monthly units"]<br>
    N0 --> N1<br>
    N2["Calculate slab-wise energy charge"]<br>
    N1 --> N2<br>
    N3["Add fixed charge and surcharge; apply rebate if eligible"]<br>
    N2 --> N3<br>
    N4["Calculate and store the monthly bill"]<br>
    N3 --> N4<br>
    N5{"Is this not the first month?"}<br>
    N4 --> N5<br>
    N6["If yes, compare with previous bill and flag increase > 50%"]<br>
    N5 -->|Yes / No as applicable| N6<br>
    N7["Display bill; repeat for remaining months"]<br>
    N6 --> N7<br>
    N8(["STOP"])<br>
    N7 --> N8<br>
5. Pseudocode
START<br>
INPUT number_of_months<br>
bills = empty list<br>
FOR each month<br>
    INPUT units<br>
    IF units <= 100<br>
        energy = units * 2<br>
    ELSE IF units <= 200<br>
        energy = 100 * 2 + (units - 100) * 3<br>
    ELSE<br>
        energy = 100 * 2 + 100 * 3 + (units - 200) * 5<br>
    END IF<br>
    bill = energy + 50 + energy * 0.05<br>
    IF units < 100<br>
        bill = bill - 20<br>
    END IF<br>
    ADD bill TO bills<br>
    DISPLAY bill<br>
    IF this is not the first month<br>
        increase_percent = (current - previous) / previous * 100<br>
        IF increase_percent > 50<br>
            DISPLAY "Unusual increase"<br>
        END IF<br>
    END IF<br>
END FOR<br>
STOP<br>
7. Sample Input<br>
Enter number of months: 3
Enter units consumed: 80
Enter units consumed: 150
Enter units consumed: 250
8. Sample Output<br>
Month 1 Bill: Rs. 238.0
Month 2 Bill: Rs. 523.0
Unusual increase detected
Month 3 Bill: Rs. 1039.5
Unusual increase detected
9. Conclusion
The program calculates monthly electricity bills using progressive slabs and additional charges. It also compares bills
and detects unusually large increases.
