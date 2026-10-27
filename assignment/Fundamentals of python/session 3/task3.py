price = float(input("enter food item price :"))
quantity = int(input("enter quantity : "))

total_bill = price * quantity

print(f"your total bill is ₹ {total_bill: .2f}")