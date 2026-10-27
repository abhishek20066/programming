import math

bill = 1000
discount = bill * 10 / 100
final_bill = math.floor(bill - discount)

print(final_bill)