i = 1

while i <= 4:
    space = 1
    while space <= 4 - i:
        print(" ", end="")
        space += 1

    star = 1
    while star <= 2 * i - 1:
        print("*", end="")
        star += 1

    print()
    i += 1