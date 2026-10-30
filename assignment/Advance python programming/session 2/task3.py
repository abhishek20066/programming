file = open("orders.txt", "w")

file.write("Pizza\n")
file.write("Burger\n")
file.write("Pasta\n")
file.write("Dosa\n")
file.write("Sandwich\n")

file.close()

file = open("orders.txt", "r")

while True:
    line = file.readline()

    if not line:
        break

    print("Order:", line.strip())
    print("File position:", file.tell())

file.close()