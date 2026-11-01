import random

used_numbers = []

def new_bill_number():
    number = random.randint(1000, 9999)

    while number in used_numbers:
        number = random.randint(1000, 9999)

    used_numbers.append(number)

    return "HW-" + str(number)