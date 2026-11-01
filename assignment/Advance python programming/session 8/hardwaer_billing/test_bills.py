from hardware_shop.bill_numbers import new_bill_number

bills = []

for i in range(20):
    bills.append(new_bill_number())

for bill in bills:
    print(bill)

if len(bills) == len(set(bills)):
    print("Duplicates: 0")