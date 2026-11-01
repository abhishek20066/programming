from format_checker import is_valid_pin, find_mobile


valid_contacts = []
rejected_contacts = []

with open("contacts.txt", "r") as file:
    contacts = file.readlines()


for contact in contacts:
    contact = contact.strip()

    name, mobile, pin = contact.split(",")

    reasons = []

    if find_mobile(mobile) != mobile:
        reasons.append("Invalid mobile")

    if not is_valid_pin(pin):
        reasons.append("Invalid PIN")

    if len(reasons) == 0:
        valid_contacts.append(contact)
    else:
        rejected_contacts.append(
            contact + " - " + ", ".join(reasons)
        )


with open("valid_contacts.txt", "w") as file:
    for contact in valid_contacts:
        file.write(contact + "\n")


with open("rejected_contacts.txt", "w") as file:
    for contact in rejected_contacts:
        file.write(contact + "\n")


print("Valid contacts:", len(valid_contacts))
print("Rejected contacts:", len(rejected_contacts))
print("Files created successfully")