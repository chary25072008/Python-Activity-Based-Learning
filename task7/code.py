n = int(input("Enter number of products: "))
subtotal = 0
for i in range(n):
    print("\\nProduct", i + 1)
    name = input("Enter product name: ")
    category = input("Enter category: ").lower()
    price = float(input("Enter price: "))
    quantity = int(input("Enter quantity: "))
    amount = price * quantity
    if category == "electronics":
        discount = amount * 0.10
    elif category == "clothing":
        discount = amount * 0.15
    else:
        discount = amount * 0.05
    net = amount - discount
    subtotal += net
    print("Product:", name)
    print("Amount:", amount)
    print("Discount:", discount)
    print("Net Amount:", net)
extra = subtotal * 0.05 if subtotal > 5000 else 0
taxable = subtotal - extra
gst = taxable * 0.05
final = taxable + gst
print("\\nShopping Invoice")
print("Subtotal:", subtotal)
print("Extra Discount:", extra)
print("GST:", gst)
print("Final Bill:", round(final, 2))
