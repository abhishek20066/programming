import re


# Task 1: Check Indian PIN Code
def is_valid_pin(text):
    pattern = r"^[1-9][0-9]{5}$"
    return re.match(pattern, text) is not None


print("PIN Code Checking:")

print(is_valid_pin("380015"))
print(is_valid_pin("110001"))
print(is_valid_pin("056001"))
print(is_valid_pin("38001"))
print(is_valid_pin("3800155"))
print(is_valid_pin("38O015"))


# Task 2: Find Mobile Number
def find_mobile(text):
    pattern = r"(?<![0-9])(?:\+91)?[6-9][0-9]{9}(?![0-9])"

    match = re.search(pattern, text)

    if match:
        return match.group()

    return None


print("\nMobile Number Checking:")

print(find_mobile("Call 9000012345 after 6 pm"))
print(find_mobile("Reach me on +919000012345"))
print(find_mobile("Flat 5000012345"))
print(find_mobile("Ring 900001234"))

# Task 3: Count PIN Codes

def count_pins():
    with open("addresses.txt", "r") as file:
        text = file.read()

    pins = re.findall(r"\b[1-9][0-9]{5}\b", text)

    pin_count = {}

    for pin in pins:
        if pin in pin_count:
            pin_count[pin] += 1
        else:
            pin_count[pin] = 1

    for pin, count in pin_count.items():
        print(pin, ":", count)


print("\nPIN Code Count:")
count_pins()

